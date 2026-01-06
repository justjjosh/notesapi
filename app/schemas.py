from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: str
class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class TagCreate(BaseModel):
    name: str

class TagResponse(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    tags: list[TagResponse] = []

    class Config:
        from_attributes = True
