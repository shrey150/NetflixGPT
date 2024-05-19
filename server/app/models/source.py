from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType
import enum

class PageInfo(BaseModel):
    '''Used internally for scraping services.'''
    title: str
    summary: str

class SourceType(enum.IntEnum):
    FANDOM = 0
    WIKIPEDIA = 1
    OTHER = 2

class SourceBase(SQLModel):
    '''Maps from titles to URLs for their sources.'''
    url: str = Field(max_length=255, nullable=False)
    type: SourceType = Field(sa_column=Column(ChoiceType(SourceType, impl=Integer()), nullable=False))  # Fandom, Wikipedia, other

class Source(SourceBase, table=True):
    '''Represents the `sources` table.'''
    __tablename__ = "sources"
    id: Optional[int] = Field(default=None, primary_key=True)