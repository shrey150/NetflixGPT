from typing import Union
from pydantic import BaseModel

class TitleInfo(BaseModel):
    title: str
    ep_title: str
    season_num: int
    ep_num: int
    summary: Union[str, None]

class TitleQuestion(TitleInfo):
    question: str