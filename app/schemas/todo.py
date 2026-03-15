from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=5)
    description: Optional[str] = None
    author_id: int

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class AuthorSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

class TodoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    author: AuthorSummary