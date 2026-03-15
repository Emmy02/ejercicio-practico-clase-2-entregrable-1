from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    titulo: str = Field(min_length=1, description="Título de la tarea")
    contenido: str = Field(min_length=1, description="Contenido de la tarea")
    deadline: datetime = Field(description="Fecha de vencimiento")
    author_id: int

class TaskUpdate(BaseModel):
    completada: bool = Field(description="Estado de completado")

class AuthorSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    contenido: str
    deadline: datetime
    completada: bool
    fecha_creacion: datetime
    author_id: int
    author: AuthorSummary