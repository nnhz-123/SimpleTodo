"""Pydantic schemas for request/response validation."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum


class PriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class CategoryEnum(str, Enum):
    WORK = "work"
    PERSONAL = "personal"
    STUDY = "study"
    HEALTH = "health"
    FINANCE = "finance"
    GENERAL = "general"


class TaskBase(BaseModel):
    """Base task schema."""
    title: str = Field(..., min_length=1, max_length=200, description="Task title")
    description: Optional[str] = Field(None, max_length=1000, description="Task description")
    priority: PriorityEnum = Field(default=PriorityEnum.MEDIUM, description="Task priority")
    category: CategoryEnum = Field(default=CategoryEnum.GENERAL, description="Task category")
    due_date: Optional[datetime] = Field(None, description="Due date for the task")
    tags: List[str] = Field(default_factory=list, description="Task tags")


class TaskCreate(TaskBase):
    """Schema for creating a new task."""
    pass


class TaskUpdate(BaseModel):
    """Schema for updating an existing task."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    priority: Optional[PriorityEnum] = None
    category: Optional[CategoryEnum] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None
    tags: Optional[List[str]] = None


class TaskResponse(TaskBase):
    """Schema for task response."""
    id: int
    completed: bool = False
    created_at: datetime
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class TaskListResponse(BaseModel):
    """Schema for task list response with pagination."""
    tasks: List[TaskResponse]
    total: int
    page: int
    page_size: int
    has_next: bool


class TaskStatsResponse(BaseModel):
    """Schema for task statistics."""
    total_tasks: int
    completed_tasks: int
    pending_tasks: int
    overdue_tasks: int
    by_priority: dict
    by_category: dict


class ErrorResponse(BaseModel):
    """Standard error response."""
    error: str
    message: str
    details: Optional[dict] = None