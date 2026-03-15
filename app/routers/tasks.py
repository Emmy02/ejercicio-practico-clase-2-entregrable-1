from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services import task_service
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return task_service.get_all(db)

@router.get("/caducadas", response_model=List[TaskResponse])
def list_expired_tasks(db: Session = Depends(get_db)):
    return task_service.get_expired(db)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create(db, data)

@router.put("/{task_id}/completar", response_model=TaskResponse)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.complete(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    if not task_service.delete(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")