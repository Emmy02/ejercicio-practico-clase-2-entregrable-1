from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True)
    titulo      = Column(String, nullable=False)
    contenido   = Column(String, nullable=True)
    deadline    = Column(DateTime, nullable=False)
    completada  = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    author_id   = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Author", back_populates="tasks")