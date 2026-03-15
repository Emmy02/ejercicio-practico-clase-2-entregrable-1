from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Este modelo no es requerido en el ejercicio, pero quise ver como funcionaba la relación entre tablas.
class Author(Base):
    __tablename__ = "authors"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    email       = Column(String, unique=True, nullable=False)
    created_at  = Column(DateTime, default=datetime.utcnow)

    todos = relationship("Todo", back_populates="author")