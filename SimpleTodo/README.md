# SimpleTodo - 待办事项管理应用

> 一个完整的全栈待办事项管理应用，演示 AI Agent 协作开发流程。

## 项目简介

SimpleTodo 是一个个人待办事项管理应用，包含：

- **Frontend**: Vue 3 + TypeScript + Vite + Pinia
- **Backend**: Python 3.11 + FastAPI + SQLAlchemy + SQLite
- **Features**: 任务创建、编辑、删除、分类、优先级、截止日期、标签、统计分析

## 技术栈

| 层 | 技术 |
|---|------|
| Frontend Framework | Vue 3 (Composition API) |
| Frontend Language | TypeScript |
| Frontend Build | Vite |
| State Management | Pinia |
| HTTP Client | Axios |
| Frontend Testing | Vitest |
| Backend Framework | FastAPI |
| Backend Language | Python 3.11+ |
| Database ORM | SQLAlchemy |
| Database | SQLite |
| Validation | Pydantic |
| Backend Testing | pytest + pytest-asyncio |

## 项目结构

```
SimpleTodo/
├── frontend/
│   ├── src/
│   │   ├── components/        # 可复用组件 (8个)
│   │   │   ├── TaskList.vue
│   │   │   ├── TaskItem.vue
│   │   │   ├── TaskForm.vue
│   │   │   ├── TaskFilterPanel.vue
│   │   │   ├── TaskSummary.vue
│   │   │   ├── QuickAddTask.vue
│   │   │   ├── CastCell.vue
│   │   │   └── CastGrid.vue
│   │   ├── views/             # 页面视图 (7个)
│   │   │   ├── HomeView.vue
│   │   │   ├── TasksView.vue
│   │   │   ├── CreateTaskView.vue
│   │   │   ├── TaskDetailView.vue
│   │   │   ├── StatsView.vue
│   │   │   ├── SettingsView.vue
│   │   │   └── NotFoundView.vue
│   │   ├── stores/            # Pinia 状态管理
│   │   ├── router/            # Vue Router 配置
│   │   ├── utils/             # 工具函数
│   │   ├── types/             # TypeScript 类型定义
│   │   └── styles/            # 全局样式
│   ├── tests/                 # 前端测试 (4个)
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
├── backend/
│   ├── app/
│   │   ├── api/               # API 路由
│   │   ├── models/            # SQLAlchemy 模型
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # 业务逻辑层
│   │   ├── utils/             # 工具函数
│   │   ├── db/                # 数据库配置
│   │   └── main.py            # 应用入口
│   ├── tests/                 # 后端测试 (3个)
│   ├── requirements.txt
│   └── pyproject.toml
├── docs/
│   ├── api/                   # API 文档
│   ├── architecture/          # 架构文档
│   └── development-log.md     # 开发日志
├── scripts/
│   ├── start-dev.sh           # 开发启动脚本
│   ├── run-tests.sh           # 测试脚本
│   └── build.sh               # 构建脚本
├── CLAUDE.md                  # Agent 协作规范
├── README.md
└── .gitignore
```

## 功能特性

### 任务管理
- 创建任务（标题、描述、优先级、分类、截止日期、标签）
- 编辑任务
- 删除任务
- 批量操作（批量完成、批量删除）

### 筛选与搜索
- 按状态筛选（已完成/待处理）
- 按优先级筛选
- 按分类筛选
- 关键词搜索
- 截止日期范围筛选

### 统计分析
- 总任务数
- 已完成数
- 待处理数
- 逾期任务数
- 按优先级分布
- 按分类分布

### 用户设置
- 主题切换（亮色/暗色/自动）
- 通知开关
- 默认优先级设置
- 默认分类设置
- 日期格式设置

## 快速开始

### 前端

```bash
cd frontend
npm install
npm run dev
```

访问 http://localhost:3000

### 后端

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

访问 http://localhost:8000

### 同时启动

```bash
./scripts/start-dev.sh
```

## API 端点

| 方法 | 端点 | 说明 |
|------|------|------|
| GET | /api/tasks | 获取任务列表 |
| POST | /api/tasks | 创建任务 |
| PUT | /api/tasks/{id} | 更新任务 |
| DELETE | /api/tasks/{id} | 删除任务 |
| POST | /api/tasks/bulk/complete | 批量完成 |
| POST | /api/tasks/bulk/delete | 批量删除 |
| GET | /api/stats | 获取统计 |
| GET | /health | 健康检查 |

详细 API 文档见 [docs/api/endpoints.md](docs/api/endpoints.md)

## 测试

```bash
# 运行所有测试
./scripts/run-tests.sh

# 仅后端测试
cd backend && pytest tests/ -v --cov=app

# 仅前端测试
cd frontend && npm run test
```

## 开发方式

本项目使用 **Claude Code Agent** 进行协作开发：

- 使用 CLAUDE.md 定义项目规范和开发流程
- Agent 辅助架构设计、代码生成、测试编写
- 采用 TDD（测试驱动开发）方法论
- Agent 创建 API 文档和架构文档

详见 [docs/development-log.md](docs/development-log.md)

## 统计

| 指标 | 数值 |
|------|------|
| 后端文件 | 15+ |
| 前端文件 | 25+ |
| 测试文件 | 7 |
| 文档文件 | 4 |
| 总代码行数 | ~2500+ |

## License

MIT License