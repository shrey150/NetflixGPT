from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType
import enum

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