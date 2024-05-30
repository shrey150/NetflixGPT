from pydantic import BaseModel

class FandomSubPayload(BaseModel):
    sub: str
    source_id: int
    title_id: int

class FandomScraperPayload(FandomSubPayload):
    raw_text: str
    url: str
    ep_id: int
