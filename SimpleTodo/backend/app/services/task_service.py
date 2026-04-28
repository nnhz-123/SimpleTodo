"""Service layer for task operations."""

from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from app.models.task import TaskModel
from app.schemas.task import TaskCreate, TaskUpdate, PriorityEnum, CategoryEnum


class TaskService:
    """Service class for task business logic."""

    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_data: TaskCreate, user_id: Optional[int] = None) -> TaskModel:
        """Create a new task."""
        # TODO: Implementation
        task = TaskModel(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority.value,
            category=task_data.category.value,
            due_date=task_data.due_date,
            tags=','.join(task_data.tags) if task_data.tags else ''
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task_by_id(self, task_id: int) -> Optional[TaskModel]:
        """Get a task by ID."""
        return self.db.query(TaskModel).filter(TaskModel.id == task_id).first()

    def get_tasks(
        self,
        page: int = 1,
        page_size: int = 20,
        completed: Optional[bool] = None,
        priority: Optional[PriorityEnum] = None,
        category: Optional[CategoryEnum] = None,
        search: Optional[str] = None
    ) -> List[TaskModel]:
        """Get tasks with filtering and pagination."""
        query = self.db.query(TaskModel)

        if completed is not None:
            query = query.filter(TaskModel.completed == completed)

        if priority:
            query = query.filter(TaskModel.priority == priority.value)

        if category:
            query = query.filter(TaskModel.category == category.value)

        if search:
            query = query.filter(
                or_(
                    TaskModel.title.ilike(f'%{search}%'),
                    TaskModel.description.ilike(f'%{search}%')
                )
            )

        offset = (page - 1) * page_size
        return query.offset(offset).limit(page_size).all()

    def update_task(self, task_id: int, task_data: TaskUpdate) -> Optional[TaskModel]:
        """Update an existing task."""
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        update_data = task_data.dict(exclude_unset=True)

        if 'completed' in update_data and update_data['completed']:
            update_data['completed_at'] = datetime.utcnow()

        for key, value in update_data.items():
            setattr(task, key, value)

        task.updated_at = datetime.utcnow()
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.db.delete(task)
        self.db.commit()
        return True

    def get_stats(self) -> dict:
        """Get task statistics."""
        total = self.db.query(TaskModel).count()
        completed = self.db.query(TaskModel).filter(TaskModel.completed == True).count()
        pending = total - completed

        overdue = self.db.query(TaskModel).filter(
            and_(
                TaskModel.completed == False,
                TaskModel.due_date < datetime.utcnow()
            )
        ).count()

        # Count by priority
        by_priority = {}
        for p in PriorityEnum:
            count = self.db.query(TaskModel).filter(TaskModel.priority == p.value).count()
            by_priority[p.value] = count

        # Count by category
        by_category = {}
        for c in CategoryEnum:
            count = self.db.query(TaskModel).filter(TaskModel.category == c.value).count()
            by_category[c.value] = count

        return {
            'total_tasks': total,
            'completed_tasks': completed,
            'pending_tasks': pending,
            'overdue_tasks': overdue,
            'by_priority': by_priority,
            'by_category': by_category
        }

    def bulk_complete(self, task_ids: List[int]) -> int:
        """Mark multiple tasks as completed."""
        count = self.db.query(TaskModel).filter(TaskModel.id.in_(task_ids)).update(
            {'completed': True, 'completed_at': datetime.utcnow()},
            synchronize_session=False
        )
        self.db.commit()
        return count

    def bulk_delete(self, task_ids: List[int]) -> int:
        """Delete multiple tasks."""
        count = self.db.query(TaskModel).filter(TaskModel.id.in_(task_ids)).delete(
            synchronize_session=False
        )
        self.db.commit()
        return count