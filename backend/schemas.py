from datetime import datetime
from pydantic import BaseModel


class EntryCreate(BaseModel):
    title: str | None = None
    content: str


class EntryOut(BaseModel):
    id: int
    title: str | None
    content: str
    summary: str | None
    mood: str | None
    created_at: datetime

class EntryUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    summary: str | None = None
    mood: str | None = None


    class Config:
        from_attributes = True
