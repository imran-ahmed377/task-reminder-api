from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from db_models import Task
from models import TaskCreate, TaskResponse, TaskUpdate
from typing import List
from auth_routes import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

# 1. Create a task - POST /tasks


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Create a new task"""
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# 2. Get all tasks - GET /tasks


@router.get("/", response_model=List[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Retrieve all tasks"""
    tasks = db.query(Task).all()
    return tasks

# 3. Get a single task - GET /tasks/{id}


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Retrieve a single task by ID"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

# 4. Update a task - PUT /tasks/{id}


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Update a task"""
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    # Update only provided fields
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

# 5. Mark task as completed - PATCH /tasks/{id}/complete


@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Mark a task as completed"""
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    db_task.is_completed = True
    db.commit()
    db.refresh(db_task)
    return db_task

# 6. Delete a task - DELETE /tasks/{id}


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Delete a task"""
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    task_id_to_delete = db_task.id
    db.delete(db_task)
    db.commit()
