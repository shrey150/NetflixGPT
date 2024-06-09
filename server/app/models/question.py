from pydantic import BaseModel

class QuestionRequest(BaseModel):
    title_id: int
    episode_id: int
    question: str

class QuestionResponse(BaseModel):
    answer: str