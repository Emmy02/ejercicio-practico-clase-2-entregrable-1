from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import List

class AuthorCreate(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr

class TodoSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    completed: bool

class AuthorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    todos: List[TodoSummary] = []

AuthorResponse.model_rebuild()