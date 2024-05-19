from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from starlette.config import Config
from starlette.responses import RedirectResponse
import os
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
import re
import tldextract

from .models import TitleBase, QuestionRequest, MetadataRequest
from .scraper import Scraper
from .__db import Database
from . import utils
from ..config import settings

import json
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_db_and_tables()
    yield

####################
# TODO use lifespan events to create these top-level objects
llm = ChatOpenAI(model="gpt-4o")
scraper = Scraper()
db = Database()
prompttemplate = open(settings.PROMPT_REG_TXT_PATH, "r", encoding="utf-8").read()
prompt = PromptTemplate(
    input_variables= ["title","ep_title","season_num","ep_num","summary","chat_history","question"],
    template = prompttemplate
)
####################

app = FastAPI(lifespan=lifespan)
#prompt = load_prompt("data/prompt.json")

memory = ConversationBufferMemory(memory_key="chat_history")

@app.post("/titles/{title_id}/episodes/{episode_id}/questions")
async def ask_question(title_id: str, episode_id: str, question_req: QuestionRequest) -> TitleAnswer:
    question_req = question_req

    summary = payload.summary
    if not payload.summary:
        if not db.has(info):
            print(payload)
            summary = scraper.fetch(payload)  
            print('summary', summary)
            db.add(summary, info)

        texts = db.search(payload.question, {'title': payload.title})
        summary = '\n'.join(texts)
        print('Context:', texts)

    context = prompt.format(
        title=payload.title,
        ep_title=payload.ep_title,
        season_num=payload.season_num,
        ep_num=payload.ep_num,
        summary=summary,
        question = "{question}",
        chat_history = "{chat_history}"
    )

    llm_chain = LLMChain(
        prompt = PromptTemplate(input_variables=["chat_history", "question"], template = context),
        llm = llm,
        verbose = True,
        memory = memory
    )

    answer = llm_chain.predict(question=payload.question)
    similar_texts = db.search(answer, {'title': payload.title })
    db_all = db.get_all()
    db_dict = db.dict_get_all()
    #Get the episode number from similar_texts
    episode_number = []
    for text in similar_texts:
        for e in db_all:
            content = e[1]
            
            if content == text:
                metadata = e[2]
                ep_num = utils.abs_ep_num(db_dict, payload.title, metadata['season_num'], metadata['ep_num'])
                print(metadata)
                print("pogpogpogpogpogpogpogpogpo", ep_num)
                episode_number.append(ep_num)
    
    print("episode_number ", episode_number)
    counter = 0
    for ep in episode_number:
        ep_num = utils.abs_ep_num(db_dict, payload.title, payload.season_num, payload.ep_num)
        if ep > ep_num:
            counter += 1
    if counter > 5:
        return {"answer": "I'm sorry, this information cannot be revealed"}
    return {"answer": answer}

# GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID') or None
# GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or None
# data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID}
# config = Config(environ=data)

@app.post("/metadata")
async def parse_metadata(payload: MetadataRequest):

    site_info = tldextract.parse(payload.url)

    match site_info.domain:
        case "netflix":
            data = payload.data
            result = []
            season_num = 1
            for season in data["video"]["seasons"]:
                episode_num = 1
                for episode in season["episodes"]:
                    result.append(TitleBase(
                        title=data["video"]["title"],
                        season_num=season_num,
                        ep_num=episode_num,
                        ep_title=episode["title"]))
                    episode_num += 1
                season_num += 1
            return result

