from typing import Union, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime

class TitleBase(SQLModel):
    '''Represents a TV show or movie.'''
    name: str
    num_seasons: int

class TitleInfo(TitleBase, table=True):
    '''Represents the `titles` table.'''
    __tablename__ = "titles"
    id: Optional[int] = Field(default=None, primary_key=True)

class SummaryBase(SQLModel):
    '''Represents a plot summary from a given source for an episode.'''
    text: str
    source: str             # Fandom, Wikipedia, other
    last_indexed: datetime

class SummaryInfo(SummaryBase, table=True):
    '''Represents the `summaries` table.'''
    __tablename__ = "summaries"
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="titles.id")
    ep_id: Optional[int] = Field(default=None, foreign_key="episodes.id")

class EpisodeBase(SQLModel):
    '''Represents the metadata for an episode.'''
    synopsis: str           # 1-2 sentence summary for networks / Netflix
    season_num: int
    ep_num: int
    # air_date: datetime

class EpisodeInfo(EpisodeBase, table=True):
    '''Represents the `episodes` table.'''
    __tablename__ = "episodes"
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="titles.id")

class SourceBase(SQLModel):
    '''Maps from titles to URLs for their sources.'''
    url: str
    source: str     # Fandom, Wikipedia, other

class SourceInfo(SourceBase, table=True):
    '''Represents the `sources` table.'''
    __tablename__ = "sources"
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="titles.id")


class PageInfo(BaseModel):
    '''Used internally for scraping services.'''
    title: str
    summary: str

class TitleQuestion(TitleInfo):
    question: str

class TitleAnswer(BaseModel):
    answer: str

class SourcePayload(BaseModel):
    source: str
    data: dict = Body(...)