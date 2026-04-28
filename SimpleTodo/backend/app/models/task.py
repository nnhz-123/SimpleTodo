"""Task model for SQLAlchemy."""

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TaskModel(Base):
    """Task database model."""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(1000), nullable=True)
    priority = Column(String(20), default="medium")
    category = Column(String(50), default="general")
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)