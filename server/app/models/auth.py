from pydantic import BaseModel

class AuthRequest(BaseModel):
    auth_token: str