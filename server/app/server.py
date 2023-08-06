from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
from langchain.prompts import load_prompt
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain import PromptTemplate, LLMChain
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import pywikibot

from app.models import TitleQuestion, TitleAnswer, SourcePayload
from app.scraper import Scraper
from app.db import Database

from dotenv import load_dotenv
from constants import *

import json

load_dotenv(DOTENV_PATH)

app = FastAPI()
llm = ChatOpenAI(model="gpt-3.5-turbo")
scraper = Scraper()
db = Database()
#prompt = load_prompt("data/prompt.json")
prompttemplate = open(PROMPT_REG_TXT_PATH,"r").read()
prompt = PromptTemplate(
    input_variables= ["title","ep_title","season_num","ep_num","summary","chat_history","question"],
    template = prompttemplate
)
memory = ConversationBufferMemory(memory_key="chat_history")
#qna = load_prompt(PROMPT_QNA_JSON_PATH)
@app.get("/get_all")
async def get_all():
    data = db.get_all()
    return {"data": data}

# debugging
class ScrapePayload(BaseModel):
    sub: str
    site: str
    search_term: str

@app.get("/scrape/fetch_plot")
async def fetch_plot(payload: ScrapePayload):
    scraper._fetch_plot(pywikibot.Site(payload.sub, payload.site), f'\"{payload.search_term}\"')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(payload: TitleQuestion) -> TitleAnswer:
    # generate dict representing TitleInfo
    info = payload.dict()
    info.pop("question")
    info.pop("summary")

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
    return {"answer": answer}
    print('Answer:', answer)

    # similar_texts = db.search(answer, {'title': payload.title })

    # validateQ = "Did your bum ass spoil anything "
    # Take whatever response it gives you 
    # return { "answer": llm_chain.predict(question = validateQ) }

    
    # answer = llm([
    #     SystemMessage(content=context),
    #     HumanMessage(content=payload.question),
    # ])
    # return {"answer": answer.content, "refined": refined.content}

@app.post("/info")
async def parse(payload: SourcePayload):
    info = json.loads(payload)
    print(info['vidio']['seasons'])

