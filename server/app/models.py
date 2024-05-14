from typing import Union, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime

class TitleInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    num_seasons: int

class SummaryInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="title.id")
    ep_id: Optional[int] = Field(default=None, foreign_key="episode.id")
    text: str
    source: str
    last_indexed: datetime

class EpisodeInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="title.id")
    synopsis: str
    # air_date: datetime
    season_num: int
    ep_num: int

class PageInfo(BaseModel):
    title: str
    summary: str

class TitleQuestion(TitleInfo):
    question: str

class TitleAnswer(BaseModel):
    answer: str

class SourcePayload(BaseModel):
    source: str
    data: dict = Body(...)