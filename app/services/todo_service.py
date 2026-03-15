from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.todo import Todo
from app.models.author import Author
from app.schemas.todo import TodoCreate, TodoUpdate

def get_all(db: Session):
    return db.query(Todo).all()

def get_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create(db: Session, data: TodoCreate):
    author = db.query(Author).filter(Author.id == data.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    todo = Todo(**data.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update(db: Session, todo_id: int, data: TodoUpdate):
    todo = get_by_id(db, todo_id)
    if not todo:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete(db: Session, todo_id: int):
    todo = get_by_id(db, todo_id)
    if not todo:
        return False
    db.delete(todo)
    db.commit()
    return True