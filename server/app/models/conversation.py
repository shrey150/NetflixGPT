from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType
import enum

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