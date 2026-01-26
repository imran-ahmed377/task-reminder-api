from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    """Base Task model with common fields"""
    title: str
    description: Optional[str] = None
    due_date: Optional[str] = None  # Format: YYYY-MM-DD


class TaskCreate(TaskBase):
    """Model for creating a new task"""
    pass


class TaskUpdate(BaseModel):
    """Model for updating a task"""
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskResponse(TaskBase):
    """Model for task response"""
    id: int
    is_completed: bool = False
    created_at: datetime

    class Config:
        from_attributes = True
