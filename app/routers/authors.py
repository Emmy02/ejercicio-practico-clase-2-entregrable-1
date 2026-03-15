from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.author import AuthorCreate, AuthorResponse
from app.services import author_service
from typing import List

# En test caso el prefix es "/authors" y los tags son ["authors"] esto nos ayuda a organizar la documentación de la API. 
router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/", response_model=List[AuthorResponse])
def list_authors(db: Session = Depends(get_db)):
    return author_service.get_all(db)

@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = author_service.get_by_id(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.post("/", response_model=AuthorResponse, status_code=201)
def create_author(data: AuthorCreate, db: Session = Depends(get_db)):
    return author_service.create(db, data)

@router.delete("/{author_id}", status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    if not author_service.delete(db, author_id):
        raise HTTPException(status_code=404, detail="Author not found")