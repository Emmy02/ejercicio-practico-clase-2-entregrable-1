from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Este modelo es el que se requiere en el ejercicio. Con los siguientes atributos:
# id: Integer, primary_key=True, index=True
# title: String, nullable=False
# description: String, nullable=True
# completed: Boolean, default=False
# created_at: DateTime, default=datetime.utcnow
# author_id: Integer, ForeignKey("authors.id"), nullable=False
# author: relationship("Author", back_populates="todos")

class Todo(Base):
    __tablename__ = "todos"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed   = Column(Boolean, default=False)
    created_at  = Column(DateTime, default=datetime.utcnow)
    author_id   = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Author", back_populates="todos")