from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
from langchain.prompts import load_prompt
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
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
validate = load_prompt("data/validate.json")
qna = load_prompt("data/qna.json")
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
    info.pop("summary")

    if not payload.summary:
        payload.summary = scraper.fetch(payload.title, payload.ep_title)  
    
    # TODO only scrape if not already in DB
    db.add(payload.summary, info)
    texts = db.search(payload.question, {'title': payload.title})

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

    validateContext = validate.format(
        title=payload.title,
        ep_title=payload.ep_title,
        season_num=payload.season_num,
        ep_num=payload.ep_num
    )
    
    qnaqs = qna.format(
        question = payload.question,
        answer = answer
    )

    # llm_chain = LLMChain(prompt= validateContext, llm=llm)

    # prerefined = llm_chain.run(qnaqs)
    # refined = llm_chain.run("You just spoiled in your answer")
    refined = llm([
        SystemMessage(content=validateContext),
        HumanMessage(content=qnaqs)
    ])
    # refined = llm([
    #     HumanMessage(content="You just spoiled in your answer {prerefined}")
    # ])


    return {"answer": answer.content, "refined": refined.content}