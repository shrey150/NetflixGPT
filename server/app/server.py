from contextlib import asynccontextmanager
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
import re
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
from .models.user import User
from .models.metadata import MetadataRequest
from .tasks import find_fandom_sub, summarize_episode_fandom, scrape_episode_fandom

from .scraper import Scraper
from . import utils
from config import settings
from .crud import crud_episode, crud_title
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
    question_req: QuestionRequest, db: AsyncSession = Depends(async_get_db)
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


async def generate_keywords(titleID: int, db: AsyncSession = Depends(async_get_db)):
    # get title
    title = await crud_title.get(db, id=titleID)

    # get all synopses from episodes and title if exists
    episodes = await crud_episode.get_multi(db, title_id=titleID)
    all_synopses = title["synopsis"] if title["synopsis"] else ""
    for episode in episodes["data"]:
        all_synopses += " " + episode["synopsis"]

    # concatenate all the synopses and pass it to the NER model
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(all_synopses)

    # combine entities
    keywords = ", ".join(set([ent.text for ent in doc.ents]))

    # save the string of entities to keywords column in the title table
    await crud_title.update(
        db,
        id=titleID,
        object=TitleBase(
            name=title["name"],
            num_seasons=title["num_seasons"],
            synopsis=title["synopsis"],
            keywords=keywords,
        ),
    )

    return keywords  # for testing


@app.post("/metadata")
async def parse_metadata(
    payload: MetadataRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(async_get_db),
    current_user: TokenData = Depends(get_current_user)
):
    site_info = tldextract.extract(payload.url)

    match site_info.domain:
        case "netflix":
            return await resolve_netflix(payload, background_tasks, db)

        case "crunchyroll":
            return await resolve_crunchyroll(payload, background_tasks, db)

        case _:
            raise HTTPException(status_code=400, detail="Unsupported streaming provider")


@app.post("/signin", response_model=Token)
async def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    token_info = await verify_google_token(form_data.password)
    username = token_info['email']

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
