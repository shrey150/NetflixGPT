from pydantic import BaseModel

class TitleInfo(BaseModel):
    title: str
    ep_title: str
    season_num: int
    ep_num: int
    summary: str

class TitleQuestion(TitleInfo):
    question: str