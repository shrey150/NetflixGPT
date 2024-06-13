from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType
import enum

class EpisodeBase(SQLModel):
    '''Represents the metadata for an episode.'''
    name: str
    synopsis: str # The high-level, one-line summary for an episode usually provided for TV networks. This is NOT the full summary.
    season_num: int = Field(nullable=False)
    ep_num: int = Field(nullable=False)

class Episode(EpisodeBase, table=True):
    '''Represents the `episodes` table.'''
    __tablename__ = "episodes"
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="titles.id")
    

class EpisodeCreate(EpisodeBase):
    title_id: int
