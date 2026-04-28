"""Pytest configuration and fixtures."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base
from app.models.task import TaskModel


# Test database engine
TEST_DATABASE_URL = "sqlite:///./test_simpletodo.db"
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture
def db_session():
    """Create a test database session."""
    Base.metadata.create_all(bind=test_engine)
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def sample_task(db_session):
    """Create a sample task for testing."""
    task = TaskModel(
        title="Sample Task",
        description="This is a sample task for testing",
        priority="medium",
        category="general",
        completed=False
    )
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    return task


@pytest.fixture
def multiple_tasks(db_session):
    """Create multiple sample tasks."""
    tasks = []
    for i in range(5):
        task = TaskModel(
            title=f"Task {i+1}",
            description=f"Description for task {i+1}",
            priority="high" if i % 2 == 0 else "low",
            category="work" if i % 3 == 0 else "personal",
            completed=i % 4 == 0
        )
        db_session.add(task)
        tasks.append(task)
    db_session.commit()
    return tasks