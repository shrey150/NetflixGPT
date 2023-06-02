from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import load_prompt
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from scraper import Scraper
import uvicorn

from dotenv import load_dotenv

from server.src.db import Database
load_dotenv("../../.env")

app = FastAPI()
llm = ChatOpenAI(model="gpt-3.5-turbo")
scraper = Scraper()
db = Database()
prompt = load_prompt("../../data/template.json")

class TitleInfo(BaseModel):
    title: str
    ep_title: str
    season_num: int
    ep_num: int
    summary: str

class TitleQuestion(TitleInfo):
    question: str

@app.get("/ask")
async def ask(payload: TitleQuestion):
    # generate dict representing TitleInfo
    info = payload.dict()
    info.pop("question")
    
    db.has(info)

    #scraper.fetch_wikipedia(payload.title, payload.ep_title)
    #texts = db.search(payload.question)

    context = prompt.format(
        title=payload.title,
        ep_title=payload.ep_title,
        season_num=payload.season_num,
        ep_num=payload.ep_num,
        summary=payload.summary,
    )

    answer = llm([
        SystemMessage(content=context),
        HumanMessage(content=payload.question),
    ])

    return {"answer": answer.content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)