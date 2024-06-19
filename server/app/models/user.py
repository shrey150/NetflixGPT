from pydantic import EmailStr
from sqlmodel import SQLModel, Field, String
from typing import Optional

class UserBase(SQLModel):
    '''Represents a user.'''
    email: EmailStr = Field(sa_type=String())

class User(UserBase, table=True):
    '''Represents the `users` table.'''
    __tablename__ = "users"
    id: Optional[str] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    '''Represents a user.'''
    id: str