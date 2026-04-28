# SimpleTodo - 待办事项管理应用

> 一个简单的全栈待办事项管理应用，用于演示 AI Agent 协作开发流程。

## 项目简介

SimpleTodo 是一个个人待办事项管理应用，包含：
- **Frontend**: Vue 3 + TypeScript + Vite
- **Backend**: Python FastAPI + SQLite
- **Features**: 任务创建、编辑、删除、分类、优先级设置

## 技术栈

| 层 | 技术 |
|---|------|
| Frontend | Vue 3, TypeScript, Vite, Pinia |
| Backend | Python 3.11, FastAPI, SQLAlchemy |
| Database | SQLite |

## 开发方式

本项目使用 **Claude Code Agent** 进行协作开发：
- 使用 CLAUDE.md 文件定义项目规范
- Agent 辅助代码编写、测试、文档生成
- 采用 TDD（测试驱动开发）方法论

## 项目结构

```
SimpleTodo/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── stores/
│   │   └── main.ts
│   ├── package.json
│   └── vite.config.ts
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   └── main.py
│   ├── requirements.txt
│   └── pyproject.toml
├── CLAUDE.md
├── README.md
└── .gitignore
```

## 快速开始

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 开发日志

- 2026-04-28: 项目初始化，使用 Claude Code Agent 创建骨架
- 使用 Agent 辅助：架构设计、代码生成、文档编写

## License

MIT License