from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Este modelo no es requerido en el ejercicio, pero quise ver como funcionaba la relación entre tablas.
class Author(Base):
    __tablename__ = "authors"

    id          = Column(Integer, primary_key=True, index=True)
    nombre        = Column(String, nullable=False)
    correo       = Column(String, unique=True, nullable=False)
    fecha_creacion  = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="author")