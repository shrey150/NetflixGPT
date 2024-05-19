from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    answer: str