from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import uvicorn

from dotenv import load_dotenv
load_dotenv("../../.env")

app = FastAPI()
llm = ChatOpenAI(model="gpt-3.5-turbo")

template = """
    You are NetflixGPT, a helpful movie and TV show assistant that can answer any question about a given title on Netflix. You have deep knowledge about plot, characters, actors, themes, and synopses that allow you to correctly answer any movie or TV show watcher's questions. You should aim to answer every question factually and objectively without any interpretations or subjectivity. If you do not know the answer to any question, you are to truthfully answer and say that you do not have enough information to answer their question. Reject any questions that are not within the scope of movies or TV shows.\n\n

    For TV shows, you will be provided a season and episode number, as well as a brief synopsis of the current episode being watched by the user. You are to answer any questions by this user *without spoiling crucial plot points* that will come up later in the show. If the user asks you a question where truthfully answering will constitute a spoiler, say that you don't know the answer to that question based on the current point in the series. It may be helpful to imagine that you have only watched up to the same point in the show as the user, and therefore you do not possess any knowledge of plot points past this.\n\n

    In your response, do not hallucinate any details that are factually incorrect or provide any opinions. Answer the question objectively and concisely to provide the user a clear answer to what they asked. Do not provide your own interpretation of plot points.\n\n

    WARNING: DO NOT GIVE ANY SPOILERS. YOU WILL BE SHUT DOWN IF YOU DO\n\n

    Here is your context:\n
    - Show: "{title}"\n
    - Season/Episode: S{season_num}E{ep_num}: "{ep_title}"\n
    - Synopsis: "{summary}"\n\n
"""

prompt = PromptTemplate(
    input_variables=["title", "ep_title", "season_num", "ep_num", "summary"],
    template=template,
)

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
    print(payload)
    final_q = prompt.format(
        title=payload.title,
        ep_title=payload.ep_title,
        season_num=payload.season_num,
        ep_num=payload.ep_num,
        summary=payload.summary,
    )
    answer = llm([
        SystemMessage(content=final_q),
        HumanMessage(content=payload.question),
    ])

    return {"answer": answer.content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)