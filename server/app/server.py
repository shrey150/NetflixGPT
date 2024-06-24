from contextlib import asynccontextmanager
from datetime import timedelta
from typing import Optional
from celery import chain, group
from fastapi import BackgroundTasks, FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import ValidationError
from starlette.config import Config
from starlette.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
import os
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
import requests
import tldextract
from logging import Logger

from .providers.netflix import resolve_netflix
from .providers.crunchyroll import resolve_crunchyroll

from .database import create_db_and_tables, async_get_db

from .models.question import QuestionRequest, QuestionResponse
from .models.episode import Episode, EpisodeCreate
from .models.netflix import NetflixPayload
from .models.netflix import Episode as NetflixEpisode

from .models.crunchyroll import CrunchyPayload
from .models.crunchyroll import EpisodeData as CrunchyrollEpisode


from .models.title import Title, TitleBase, TitleCreate
from .models.conversation import Conversation
from .models.message import Message
from .models.user import User, UserBase, UserCreate
from .models.auth import AuthRequest
from .models.metadata import MetadataRequest
from .tasks import find_fandom_sub, summarize_episode_fandom, scrape_episode_fandom, process_episode

from .scraper import Scraper
from . import utils
from config import settings
from .crud import crud_episode, crud_title, crud_user
from .auth import verify_google_token, create_access_token, get_current_user, TokenData, Token

import spacy
import json

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

from .vecstore import vecstore


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


# TODO use lifespan events to create these top-level objects
llm = ChatOpenAI(model="gpt-4o", api_key=settings.OPENAI_API_KEY)
prompttemplate = open(settings.PROMPT_REG_TXT_PATH, "r", encoding="utf-8").read()
prompt = PromptTemplate(
    input_variables=[
        "title",
        "ep_title",
        "season_num",
        "ep_num",
        "summary",
        "chat_history",
        "question",
    ],
    template=prompttemplate,
)

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "https://www.netflix.com",
    "https://www.crunchyroll.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(
    question_req: QuestionRequest,
    db: AsyncSession = Depends(async_get_db)
) -> QuestionResponse:
    print(f"Question: {question_req.question}")

    title = await crud_title.get(db, id=question_req.title_id)
    episode = await crud_episode.get(db, id=question_req.episode_id)

    print(f"Title: {title}")
    print(f"Episode: {episode}")

    retriever = vecstore.as_retriever(
        search_type="similarity",
        filter={
            "title_id": question_req.title_id,
            # TODO filter by <= abs_ep_num
        },
    )

    docs = retriever.invoke(question_req.question)
    docs_content = "\n".join(doc.page_content for doc in docs)

    print(f"Retrieved {len(docs)} documents")
    print(f"Docs content: {docs_content}")

    question = question_req.question
    context = prompt.format(
        title_name=title["name"],
        ep_name=episode["name"],
        season_num=episode["season_num"],
        ep_num=episode["ep_num"],
        title_synopsis=title["synopsis"],
        episode_synopsis=episode["synopsis"],
        question=question,
        summary_chunks=docs_content,
    )

    answer = llm.invoke(context)
    return QuestionResponse(
        answer=answer.content,
    )


def find_netflix_episode(data: NetflixPayload) -> (NetflixEpisode, int, int):
    for season_num, season in enumerate(data.video.seasons):
        for ep_num, episode in enumerate(season.episodes):
            if episode.episodeId == data.video.currentEpisode:
                # convert from zero-indexing to 1-indexing
                return (episode, season_num+1, ep_num+1)

    raise HTTPException(status_code=400, detail="Episode metadata not found in Netflix payload")

async def ensure_all_episodes_in_db(data: NetflixPayload, db: AsyncSession, title_id: int):
    parallel_scraper_tasks = []
    
    print(f'Ensuring all episodes exist for title id {title_id}')
    title = await crud_title.get(db, id=title_id)

    for season_num, season in enumerate(data.video.seasons):
        for ep_num, netflix_episode in enumerate(season.episodes):
            episode_name = netflix_episode.title
            if not await crud_episode.exists(db, name=episode_name, title_id=title_id):
                print(f'Discovered episode {episode_name}')
                episode = await crud_episode.create(db, object=EpisodeCreate(
                    name=episode_name,
                    synopsis=netflix_episode.synopsis,
                    title_id=title_id,
                    # account for zero-indexing -> 1-indexing
                    season_num=season_num+1,
                    ep_num=ep_num+1,
                ))

            episode = await crud_episode.get(db, name=episode_name, title_id=title_id)
            parallel_scraper_tasks.append(process_episode(title, episode))

    # execute all tasks in parallel
    chain(
        find_fandom_sub.s(title),
        group(parallel_scraper_tasks),
    ).delay()

@app.post("/metadata")
async def parse_metadata(
    payload: MetadataRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(async_get_db),
    #current_user: TokenData = Depends(get_current_user)
):
    site_info = tldextract.extract(payload.url)

    match site_info.domain:
        case "netflix":
            return await resolve_netflix(payload, background_tasks, db)

        case "crunchyroll":
            return await resolve_crunchyroll(payload, background_tasks, db)

        case _:
            raise HTTPException(status_code=400, detail="Unsupported streaming provider")

@app.post("/signin")
async def signin(payload: AuthRequest):
    response = requests.get(
        url=f'https://{settings.REACT_APP_AUTH0_DOMAIN}/userinfo',
        headers={'Authorization': f'Bearer {payload.auth_token}'},
        timeout=5
    )
    response.raise_for_status()
    data = response.json()
    print(data)

    # crud_user.create(db, object=UserCreate(
    #     id=data['sub'],
    #     email=data['email']
    # ))


