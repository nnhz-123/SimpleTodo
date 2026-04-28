# SimpleTodo API Documentation

## Base URL

```
http://localhost:8000/api
```

## Endpoints

### Tasks

#### GET /tasks

Get all tasks with optional filtering and pagination.

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | int | 1 | Page number |
| page_size | int | 20 | Items per page |
| completed | bool | - | Filter by completion status |
| priority | string | - | Filter by priority (low, medium, high, urgent) |
| category | string | - | Filter by category |
| search | string | - | Search in title and description |

**Response:**

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Task title",
      "description": "Task description",
      "priority": "medium",
      "category": "work",
      "completed": false,
      "due_date": "2026-04-30T10:00:00Z",
      "tags": ["urgent", "review"],
      "created_at": "2026-04-28T08:00:00Z",
      "updated_at": null,
      "completed_at": null
    }
  ],
  "total": 50,
  "page": 1,
  "page_size": 20,
  "has_next": true
}
```

#### POST /tasks

Create a new task.

**Request Body:**

```json
{
  "title": "New task title",
  "description": "Optional description",
  "priority": "high",
  "category": "work",
  "due_date": "2026-04-30T10:00:00Z",
  "tags": ["urgent"]
}
```

**Response:** Task object with id and timestamps.

#### PUT /tasks/{id}

Update an existing task.

**Request Body:** Partial task object with fields to update.

#### DELETE /tasks/{id}

Delete a task.

#### POST /tasks/bulk/complete

Mark multiple tasks as completed.

**Request Body:**

```json
{
  "task_ids": [1, 2, 3]
}
```

#### POST /tasks/bulk/delete

Delete multiple tasks.

### Statistics

#### GET /stats

Get task statistics.

**Response:**

```json
{
  "total_tasks": 50,
  "completed_tasks": 20,
  "pending_tasks": 30,
  "overdue_tasks": 5,
  "by_priority": {
    "low": 10,
    "medium": 25,
    "high": 10,
    "urgent": 5
  },
  "by_category": {
    "work": 20,
    "personal": 15,
    "general": 15
  }
}
```

### Health

#### GET /health

Health check endpoint.

**Response:**

```json
{
  "status": "ok"
}
```

## Error Responses

All errors follow this format:

```json
{
  "error": "VALIDATION_ERROR",
  "message": "Title is required",
  "details": {
    "field": "title"
  }
}
```

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| VALIDATION_ERROR | 422 | Invalid request data |
| NOT_FOUND | 404 | Resource not found |
| INTERNAL_ERROR | 500 | Server error |