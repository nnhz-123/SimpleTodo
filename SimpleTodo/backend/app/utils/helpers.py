"""Utility functions for the backend."""

from datetime import datetime, timedelta
from typing import Optional
import re


def format_datetime(dt: datetime) -> str:
    """Format datetime to ISO string."""
    return dt.isoformat() if dt else None


def parse_datetime(dt_str: str) -> Optional[datetime]:
    """Parse ISO datetime string."""
    try:
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except (ValueError, AttributeError):
        return None


def is_overdue(due_date: Optional[datetime], completed: bool) -> bool:
    """Check if a task is overdue."""
    if completed or not due_date:
        return False
    return due_date < datetime.utcnow()


def get_priority_weight(priority: str) -> int:
    """Get numeric weight for priority sorting."""
    weights = {
        'urgent': 4,
        'high': 3,
        'medium': 2,
        'low': 1
    }
    return weights.get(priority.lower(), 0)


def calculate_time_remaining(due_date: datetime) -> dict:
    """Calculate time remaining until due date."""
    now = datetime.utcnow()
    if due_date < now:
        return {
            'overdue': True,
            'days_overdue': (now - due_date).days,
            'hours_overdue': (now - due_date).seconds // 3600
        }

    delta = due_date - now
    return {
        'overdue': False,
        'days_remaining': delta.days,
        'hours_remaining': delta.seconds // 3600,
        'total_seconds': delta.total_seconds()
    }


def sanitize_input(text: str) -> str:
    """Sanitize user input text."""
    # Remove potentially harmful characters
    text = re.sub(r'[<>\"\'&]', '', text)
    # Trim whitespace
    text = text.strip()
    return text


def generate_task_summary(tasks: list) -> str:
    """Generate a summary of tasks."""
    if not tasks:
        return "No tasks found."

    completed = sum(1 for t in tasks if t.get('completed'))
    pending = len(tasks) - completed
    overdue = sum(1 for t in tasks if is_overdue(
        parse_datetime(t.get('due_date')),
        t.get('completed')
    ))

    return f"Total: {len(tasks)}, Completed: {completed}, Pending: {pending}, Overdue: {overdue}"


class PaginationHelper:
    """Helper class for pagination calculations."""

    @staticmethod
    def calculate_offset(page: int, page_size: int) -> int:
        return (page - 1) * page_size

    @staticmethod
    def calculate_total_pages(total: int, page_size: int) -> int:
        return (total + page_size - 1) // page_size

    @staticmethod
    def has_next_page(page: int, total_pages: int) -> bool:
        return page < total_pages

    @staticmethod
    def has_prev_page(page: int) -> bool:
        return page > 1