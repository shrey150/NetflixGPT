from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Enum
from fastapi import Body
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType
import enum

class MetadataRequest(BaseModel):
    url: str
    data: dict = Body(...)