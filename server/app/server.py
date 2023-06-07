from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
from langchain.prompts import load_prompt
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import pywikibot

from app.models import TitleQuestion
from app.scraper import Scraper
from app.db import Database

from dotenv import load_dotenv
load_dotenv('../.env')

app = FastAPI()
llm = ChatOpenAI(model="gpt-3.5-turbo")
scraper = Scraper()
db = Database()
prompt = load_prompt("data/prompt.json")

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
# debugging

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(payload: TitleQuestion):
    # generate dict representing TitleInfo
    info = payload.dict()
    info.pop("question")

    # TODO only scrape if not already in DB
    summary = scraper.fetch(payload.title, payload.ep_title)
    db.add(summary, info)

    texts = db.search(payload.question)

    print('Context:', texts)

    context = prompt.format(
        title=payload.title,
        ep_title=payload.ep_title,
        season_num=payload.season_num,
        ep_num=payload.ep_num,
        summary='\n'.join(texts)
    )

    answer = llm([
        SystemMessage(content=context),
        HumanMessage(content=payload.question),
    ])

    return {"answer": answer.content}