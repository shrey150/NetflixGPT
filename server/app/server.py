from contextlib import asynccontextmanager
from typing import Optional
from fastapi import BackgroundTasks, FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
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

from .database import create_db_and_tables, async_get_db

from .models.episode import Episode, EpisodeCreate
from .models.netflix import NetflixPayload
from .models.netflix import Episode as NetflixEpisode
from .models.title import Title, TitleBase, TitleCreate
from .models.conversation import Conversation
from .models.message import Message
from .models.user import User
from .models.metadata import MetadataRequest

from .scraper import Scraper
from . import utils
from config import settings
from .crud import crud_episode, crud_title

import json
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

####################
# TODO use lifespan events to create these top-level objects
llm = ChatOpenAI(model="gpt-4o")
# scraper = Scraper()
# db = Database()
prompttemplate = open(settings.PROMPT_REG_TXT_PATH, "r", encoding="utf-8").read()
prompt = PromptTemplate(
    input_variables= ["title","ep_title","season_num","ep_num","summary","chat_history","question"],
    template = prompttemplate
)
####################

app = FastAPI(lifespan=lifespan)
#prompt = load_prompt("data/prompt.json")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "https://www.netflix.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory = ConversationBufferMemory(memory_key="chat_history")

# @app.post("/titles/{title_id}/episodes/{episode_id}/questions")
# async def ask_question(title_id: str, episode_id: str, question_req: QuestionRequest) -> TitleAnswer:
    
#     question = question_req.question

#     summary = payload.summary
#     if not payload.summary:
#         if not db.has(info):
#             print(payload)
#             summary = scraper.fetch(payload)  
#             print('summary', summary)
#             db.add(summary, info)

#         texts = db.search(payload.question, {'title': payload.title})
#         summary = '\n'.join(texts)
#         print('Context:', texts)

#     context = prompt.format(
#         title=payload.title,
#         ep_title=payload.ep_title,
#         season_num=payload.season_num,
#         ep_num=payload.ep_num,
#         summary=summary,
#         question = "{question}",
#         chat_history = "{chat_history}"
#     )

#     llm_chain = LLMChain(
#         prompt = PromptTemplate(input_variables=["chat_history", "question"], template = context),
#         llm = llm,
#         verbose = True,
#         memory = memory
#     )

#     answer = llm_chain.predict(question=payload.question)
#     similar_texts = db.search(answer, {'title': payload.title })
#     db_all = db.get_all()
#     db_dict = db.dict_get_all()
#     #Get the episode number from similar_texts
#     episode_number = []
#     for text in similar_texts:
#         for e in db_all:
#             content = e[1]
            
#             if content == text:
#                 metadata = e[2]
#                 ep_num = utils.abs_ep_num(db_dict, payload.title, metadata['season_num'], metadata['ep_num'])
#                 print(metadata)
#                 print("pogpogpogpogpogpogpogpogpo", ep_num)
#                 episode_number.append(ep_num)
    
#     print("episode_number ", episode_number)
#     counter = 0
#     for ep in episode_number:
#         ep_num = utils.abs_ep_num(db_dict, payload.title, payload.season_num, payload.ep_num)
#         if ep > ep_num:
#             counter += 1
#     if counter > 5:
#         return {"answer": "I'm sorry, this information cannot be revealed"}
#     return {"answer": answer}

# GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID') or None
# GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or None
# data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID}
# config = Config(environ=data)

def get_title_by_name(name: str) -> Title:
    print("[TODO] get_title_by_name not implemented, sending dummy data")
    dummy_title = Title(
        id=69,
        title="Dummy Title",
        ep_title="Dummy Episode Title",
        season_num=1,
        ep_num=1,
        summary="This is a dummy summary for the dummy title."
    )
    return dummy_title

def get_episode_by_name(name: str, db: AsyncSession) -> NetflixEpisode:
    # TODO implement
    print("[TODO] get_episode_by_name not implemented, sending dummy data")

    episode = crud_episode.exists(db, name=name)
    return episode

def find_netflix_episode(data: NetflixPayload) -> (NetflixEpisode, int, int):
    for season_num, season in enumerate(data.video.seasons):
        for ep_num, episode in enumerate(season.episodes):
            if episode.episodeId == data.video.currentEpisode:
                # convert from zero-indexing to 1-indexing
                return (episode, season_num+1, ep_num+1)

    raise HTTPException(status_code=400, detail="Episode metadata not found in Netflix payload")

async def ensure_all_episodes_in_db(data: NetflixPayload, db: AsyncSession, title_id: int):
    for season_num, season in enumerate(data.video.seasons):
        for ep_num, episode in enumerate(season.episodes):
            episode_name = episode.title
            if not await crud_episode.exists(db, name=episode_name):
                await crud_episode.create(db, object=EpisodeCreate(
                    name=episode_name,
                    synopsis=episode.synopsis,
                    title_id=title_id,
                    # account for zero-indexing -> 1-indexing
                    season_num=season_num+1,
                    ep_num=ep_num+1,
                ))

                # TODO call scraping background task here

@app.post("/metadata")
async def parse_metadata(
    payload: MetadataRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(async_get_db)
):
    site_info = tldextract.extract(payload.url)

    match site_info.domain:
        case "netflix":
            try:
                data = NetflixPayload(**payload.data)
            except ValidationError as e:
                print(e)
                raise HTTPException(status_code=400, detail="Malformed Netflix metadata") from e

            title_name = data.video.title
            num_seasons = len(data.video.seasons)

            if not await crud_title.exists(db, name=title_name):
                await crud_title.create(db, object=TitleCreate(
                    name=title_name,
                    num_seasons=num_seasons,
                ))

            title = await crud_title.get(db, name=title_name)

            netflix_episode, season_num, ep_num = find_netflix_episode(data)
            title_name = netflix_episode.title

            if not await crud_episode.exists(db, name=title_name):
                await crud_episode.create(db, object=EpisodeCreate(
                    name=netflix_episode.title,
                    synopsis=netflix_episode.synopsis,
                    season_num=season_num,
                    ep_num=ep_num,
                    title_id=title["id"])
                )

            episode = await crud_episode.get(db, name=title_name)
            background_tasks.add_task(ensure_all_episodes_in_db, data, db, title["id"])

            # include title & episode objects in final response
            res = {
                "episode_id": episode["id"],
                "episode_name": episode["name"],
                "title_name": title["name"],
                "title_id": title["id"],
                **title,
                **episode,
            }

            # account for key collisions
            res.pop("id")
            res.pop("name")

            return res
      
        case _:
            raise HTTPException(status_code=400, detail="Unsupported streaming provider")
