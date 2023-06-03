from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import load_prompt
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

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

@app.get("/ask")
async def ask(payload: TitleQuestion):
    # generate dict representing TitleInfo
    info = payload.dict()
    info.pop("question")
    
    db.has(info)

    scraper.fetch_wikipedia(payload.title, payload.ep_title)
    texts = db.search(payload.question)

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