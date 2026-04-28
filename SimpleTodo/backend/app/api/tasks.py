"""API routes for tasks."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"
    category: str = "general"

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    category: str
    completed: bool
    created_at: datetime

@router.get("/", response_model=List[TaskResponse])
async def list_tasks():
    """List all tasks."""
    # TODO: Implement database query
    return []

@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    """Create a new task."""
    # TODO: Implement database insert
    return TaskResponse(
        id=1,
        title=task.title,
        description=task.description,
        priority=task.priority,
        category=task.category,
        completed=False,
        created_at=datetime.utcnow()
    )