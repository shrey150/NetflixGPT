from typing import Union
from pydantic import BaseModel

class TitleInfo(BaseModel):
    title: str
    ep_title: str
    season_num: int
    ep_num: int
    summary: Union[str, None]

class PageInfo(BaseModel):
    title: str
    summary: str

class TitleQuestion(TitleInfo):
    question: str

class TitleAnswer(BaseModel):
    answer: str