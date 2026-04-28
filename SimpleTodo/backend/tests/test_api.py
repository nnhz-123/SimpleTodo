"""API endpoint tests."""

import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


class TestHealthEndpoint:
    """Tests for health check endpoint."""

    def test_health_check_returns_ok(self):
        """Test health check returns 200."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"


class TestTaskEndpoints:
    """Tests for task API endpoints."""

    def test_get_tasks_empty(self):
        """Test getting tasks when empty."""
        response = client.get("/api/tasks")
        assert response.status_code == 200
        assert response.json() == []

    def test_create_task(self):
        """Test creating a new task."""
        task_data = {
            "title": "New Task",
            "description": "Task description",
            "priority": "high",
            "category": "work"
        }
        response = client.post("/api/tasks", json=task_data)
        assert response.status_code == 200
        assert response.json()["title"] == "New Task"

    def test_create_task_validation_error(self):
        """Test creating task with invalid data."""
        task_data = {"title": ""}  # Empty title should fail
        response = client.post("/api/tasks", json=task_data)
        assert response.status_code == 422

    def test_update_task(self):
        """Test updating a task."""
        # TODO: Implementation
        pass

    def test_delete_task(self):
        """Test deleting a task."""
        # TODO: Implementation
        pass

    def test_get_stats(self):
        """Test getting task statistics."""
        response = client.get("/api/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_tasks" in data
        assert "completed_tasks" in data


class TestTaskBulkOperations:
    """Tests for bulk operations."""

    def test_bulk_complete(self):
        """Test bulk completing tasks."""
        # TODO: Implementation
        pass

    def test_bulk_delete(self):
        """Test bulk deleting tasks."""
        # TODO: Implementation
        pass