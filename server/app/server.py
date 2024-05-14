import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2AuthorizationCodeBearer
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.cors import SessionMiddleware
# from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.responses import RedirectResponse
from dotenv import load_dotenv
import os

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
import re

from app.models import TitleQuestion, TitleAnswer, SourcePayload, TitleInfo
from app.scraper import Scraper
from app.db import Database
from app import utils

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

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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
    print('Answer:', answer)

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID') or None
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or None
data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID}
config = Config(environ=data)
# oauth = OAuth(config)
# app.add_middleware(SessionMiddleware, secret_key=GOOGLE_CLIENT_SECRET)

# oauth.register(
#     name='google',
#     server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
#     client_kwargs={
#         'scope': 'openid email profile'
#     }
# )

# @app.get('/login')
# async def login(request: Request):
#     redirect_uri = request.url_for('auth')
#     print(redirect_uri)
#     return await oauth.google.authorize_redirect(request, redirect_uri)

# @app.get('/token')
# async def auth(request: Request):
#     try:
#         token = await oauth.google.authorize_access_token(request)
#     except OAuthError as error:
#         raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
#                             detail ='Could not validate credentials',
#                             headers={'WWW_Authenticate': 'Bearer'},)
#     user = await oauth.google.parse_id_token(request, token)
    

# @app.get('/')
# def public(request: Request):
#     user = request.session.get('user')
#     if user:
#         name = user.get('name')
#         return HTMLResponse(f'<p>Hello {name}!</p><a href=/logout>Logout</a>')
#     return HTMLResponse('<a>href=/login>Login</a>')

# @app.route('/logout')
# async def logout(request: Request):
#     request.session.pop('user', None)
#     return RedirectResponse(url='/')


@app.post("/info")
async def parse(payload: SourcePayload):
    #Return would simply be a list of titleinfo objects
    print(payload, payload.source, payload.data)
    data = payload.data
    result = []
    season_num = 1
    for season in data["video"]["seasons"]:
        episode_num = 1
        for episode in season["episodes"]:
            result.append(TitleInfo(
                title=data["video"]["title"],
                season_num=season_num,
                ep_num=episode_num,
                ep_title=episode["title"]))
            episode_num += 1
        season_num += 1
    return result

