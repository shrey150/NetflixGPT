from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType

class SummaryBase(SQLModel):
    '''Represents a plot summary from a given source for an episode.'''
    raw_text: str   # The raw HTML scraped for generating summary text
    url: str        # The specific page where the data came from
    text: str       # The summarized text (using LLMs or extraction)
    title_id: Optional[int] = Field(default=None, foreign_key="titles.id")
    source_id: Optional[int] = Field(default=None, foreign_key="sources.id")
    ep_id: Optional[int] = Field(default=None, foreign_key="episodes.id")
    last_indexed: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    reliability_score: float   # NER reliability score, 0-1
    is_primary: bool

class Summary(SummaryBase, table=True):
    '''Represents the `summaries` table.'''
    __tablename__ = "summaries"
    id: Optional[int] = Field(default=None, primary_key=True)

class SummaryCreate(SummaryBase):
    pass
