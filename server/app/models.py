from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType
import enum

class SourceType(enum.IntEnum):
    FANDOM = 0
    WIKIPEDIA = 1
    OTHER = 2

class TitleBase(SQLModel):
    '''Represents a TV show or movie.'''
    name: str = Field(max_length=255, nullable=False)
    num_seasons: int = Field(nullable=False)

class Title(TitleBase, table=True):
    '''Represents the `titles` table.'''
    __tablename__ = "titles"
    id: Optional[int] = Field(default=None, primary_key=True)

class SummaryBase(SQLModel):
    '''Represents a plot summary from a given source for an episode.'''
    raw_text: str # The raw HTML scraped for generating summary text.
    text: str
    source_id: Optional[int] = Field(default=None, foreign_key="sources.id")
    last_indexed: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class Summary(SummaryBase, table=True):
    '''Represents the `summaries` table.'''
    __tablename__ = "summaries"
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="titles.id")
    ep_id: Optional[int] = Field(default=None, foreign_key="episodes.id")

class EpisodeBase(SQLModel):
    '''Represents the metadata for an episode.'''
    synopsis: str # The high-level, one-line summary for an episode usually provided for TV networks. This is NOT the full summary.
    season_num: int = Field(nullable=False)
    ep_num: int = Field(nullable=False)

class Episode(EpisodeBase, table=True):
    '''Represents the `episodes` table.'''
    __tablename__ = "episodes"
    id: Optional[int] = Field(default=None, primary_key=True)
    title_id: Optional[int] = Field(default=None, foreign_key="titles.id")

class SourceBase(SQLModel):
    '''Maps from titles to URLs for their sources.'''
    url: str = Field(max_length=255, nullable=False)
    type: SourceType = Field(sa_column=Column(ChoiceType(SourceType, impl=Integer()), nullable=False))  # Fandom, Wikipedia, other

class Source(SourceBase, table=True):
    '''Represents the `sources` table.'''
    __tablename__ = "sources"
    id: Optional[int] = Field(default=None, primary_key=True)

class ConversationBase(SQLModel):
    '''Represents a conversation.'''
    user_id: int = Field(foreign_key="users.id", nullable=False)
    started_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, 
                                 description="TODO eventually use a DB trigger to update this automatically")

class Conversation(ConversationBase, table=True):
    '''Represents the `conversations` table.'''
    __tablename__ = "conversations"
    id: Optional[int] = Field(default=None, primary_key=True)

class MessageBase(SQLModel):
    '''Represents a message in a conversation.'''
    conversation_id: int = Field(foreign_key="conversations.id", nullable=False)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    content: str = Field(nullable=False)
    role: str # CHECK (role IN ('user', 'bot'))
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class Message(MessageBase, table=True):
    '''Represents the `messages` table.'''
    __tablename__ = "messages"
    id: Optional[int] = Field(default=None, primary_key=True)

class UserBase(SQLModel):
    '''Represents a user.'''
    email: EmailStr = Field(sa_type=String())

class User(UserBase, table=True):
    '''Represents the `users` table.'''
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)

class PageInfo(BaseModel):
    '''Used internally for scraping services.'''
    title: str
    summary: str

class TitleQuestion(TitleBase):
    question: str

class TitleAnswer(BaseModel):
    answer: str

class SourcePayload(BaseModel):
    source: str
    data: dict = Body(...)
    data: dict = Body(...)