from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.task import Task
from app.models.author import Author
from app.schemas.task import TaskCreate, TaskUpdate
from datetime import datetime

def get_all(db: Session):
    return db.query(Task).all()

def get_expired(db: Session):
    return db.query(Task).filter(Task.deadline < datetime.now()).all()

def get_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def create(db: Session, data: TaskCreate):
    author = db.query(Author).filter(Author.id == data.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    task = Task(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def complete(db: Session, task_id: int):
    task = get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completada = True
    db.commit()
    db.refresh(task)
    return task

def delete(db: Session, task_id: int):
    task = get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return True