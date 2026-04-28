"""SimpleTodo Backend API Entry Point."""

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI(title="SimpleTodo API", version="0.1.0")

# Task Model
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    priority: str = "medium"  # low, medium, high
    category: str = "general"  # work, personal, general
    completed: bool = False
    created_at: datetime = datetime.utcnow()

# In-memory storage (for demo)
tasks: list[Task] = []

@app.get("/api/tasks")
async def get_tasks():
    """Get all tasks."""
    return tasks

@app.post("/api/tasks")
async def create_task(task: Task):
    """Create a new task."""
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@app.put("/api/tasks/{id}")
async def update_task(id: int, task: Task):
    """Update a task."""
    # TODO: Implementation
    return {"message": "Task updated"}

@app.delete("/api/tasks/{id}")
async def delete_task(id: int):
    """Delete a task."""
    # TODO: Implementation
    return {"message": "Task deleted"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)