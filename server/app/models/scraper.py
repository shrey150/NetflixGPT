from pydantic import BaseModel
from ..ner import search_rules_generator

class FandomSubPayload(BaseModel):
    sub: str
    source_id: int
    title_id: int

class FandomScraperPayload(FandomSubPayload):
    raw_text: str
    url: str
    ep_id: int

class FandomSummaryPayload(FandomScraperPayload):
    text: str