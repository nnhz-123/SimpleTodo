# SimpleTodo Architecture

## Overview

SimpleTodo is a full-stack web application for personal task management.

## Technology Stack

### Frontend

- **Framework**: Vue 3 with Composition API
- **Language**: TypeScript
- **Build Tool**: Vite
- **State Management**: Pinia
- **HTTP Client**: Axios
- **Testing**: Vitest

### Backend

- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Database**: SQLite (via SQLAlchemy)
- **Validation**: Pydantic
- **Testing**: pytest + pytest-asyncio

## Project Structure

```
SimpleTodo/
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable Vue components
│   │   ├── views/          # Page-level views
│   │   ├── stores/         # Pinia state stores
│   │   ├── router/         # Vue Router configuration
│   │   ├── utils/          # Utility functions
│   │   ├── types/          # TypeScript type definitions
│   │   └── styles/         # Global CSS styles
│   └── tests/              # Frontend tests
├── backend/
│   ├── app/
│   │   ├── api/            # API route handlers
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic services
│   │   ├── utils/          # Utility functions
│   │   └── db/             # Database configuration
│   └── tests/              # Backend tests
└── docs/                   # Documentation
```

## Data Flow

```
User Action → Vue Component → Pinia Store → Axios → FastAPI → Service → Database
                    ↓
              State Update → Component Re-render
```

## Key Components

### Frontend Components

| Component | Purpose |
|-----------|---------|
| TaskList | Display list of tasks |
| TaskItem | Single task row |
| TaskForm | Create/edit task form |
| TaskFilterPanel | Filter controls |
| TaskSummary | Statistics overview |
| QuickAddTask | Quick task creation |

### Backend Services

| Service | Purpose |
|---------|---------|
| TaskService | CRUD operations, filtering, statistics |
| Database | Connection management, session handling |

## API Design

- RESTful endpoints
- JSON request/response
- Pagination support
- Filtering capabilities
- Bulk operations

## Database Schema

### tasks table

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| title | VARCHAR(200) | Task title |
| description | VARCHAR(1000) | Task description |
| priority | VARCHAR(20) | Priority level |
| category | VARCHAR(50) | Category |
| completed | BOOLEAN | Completion status |
| due_date | DATETIME | Due date |
| tags | VARCHAR | Comma-separated tags |
| created_at | DATETIME | Creation timestamp |
| updated_at | DATETIME | Update timestamp |
| completed_at | DATETIME | Completion timestamp |

## Development Workflow

1. Plan feature using Claude Code Agent
2. Write tests first (TDD)
3. Implement functionality
4. Review code with Agent
5. Commit with detailed message