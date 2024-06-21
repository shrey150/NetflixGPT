from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy_utils import ChoiceType
import enum

class TitleBase(SQLModel):
    '''Represents a TV show or movie.'''
    name: str = Field(max_length=255, nullable=False)
    num_seasons: int = Field(nullable=False)
    synopsis: str # The high-level, one-line summary for an episode usually provided for TV networks. This is NOT the full summary.
    keywords: dict = Field(default={}, sa_column=Column(JSON))

class Title(TitleBase, table=True):
    '''Represents the `titles` table.'''
    __tablename__ = "titles"
    id: Optional[int] = Field(default=None, primary_key=True)

class TitleCreate(TitleBase):
    pass