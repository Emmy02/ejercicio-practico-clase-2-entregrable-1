from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.models.author import Author
from app.schemas.author import AuthorCreate

def get_all(db: Session):
    return db.query(Author).all()

def get_by_id(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def create(db: Session, data: AuthorCreate):
    existing = db.query(Author).filter(Author.email == data.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")
    author = Author(**data.model_dump())
    db.add(author)
    db.commit()
    db.refresh(author)

    return author

def delete(db: Session, author_id: int):
    author = get_by_id(db, author_id)
    if not author:
        return False
    db.delete(author)
    db.commit()
    return True