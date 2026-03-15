from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import List

class AuthorCreate(BaseModel):
    nombre: str = Field(..., min_length=3)
    correo: EmailStr

class TaskSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    completada: bool

class AuthorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    correo: str
    tasks: List[TaskSummary] = []

AuthorResponse.model_rebuild()