# SimpleTodo - Agent 协作开发规范

> 本文件定义项目开发规范，供 Claude Code Agent 参考。

## 项目愿景

构建一个简单、实用的待办事项管理应用，演示 AI Agent 协作开发的完整流程。

## 技术约束

### Frontend (Vue 3 + TypeScript)

- 使用 Composition API
- 状态管理使用 Pinia
- 样式使用原生 CSS
- 文件命名：PascalCase.vue (组件), camelCase.ts (其他)

### Backend (Python FastAPI)

- 使用 Pydantic 进行数据验证
- 使用 SQLAlchemy ORM
- 遵循 RESTful API 设计
- Type hints 必须使用

## API 设计

### 端点列表

| 方法 | 端点 | 说明 |
|------|------|------|
| GET | /api/tasks | 获取所有任务 |
| POST | /api/tasks | 创建任务 |
| PUT | /api/tasks/{id} | 更新任务 |
| DELETE | /api/tasks/{id} | 删除任务 |

### 任务模型

```json
{
  "id": 1,
  "title": "任务标题",
  "description": "任务描述",
  "priority": "high",
  "category": "work",
  "completed": false,
  "created_at": "2026-04-28T10:00:00Z"
}
```

## 开发流程

1. **Plan First**: 使用 Agent 创建实施计划
2. **TDD**: 先写测试，再实现
3. **Code Review**: 使用 Agent 检查代码
4. **Commit**: 详细提交信息

## 编码规范

- 函数小于 50 行
- 文件小于 400 行
- 无硬编码值
- 有意义的命名

## 测试要求

- Frontend: Vitest
- Backend: pytest
- 覆盖率目标: 80%

## Agent 使用记录

本项目使用 Claude Code Agent 进行以下协作：
- 项目架构设计
- 代码骨架生成
- API 端点设计
- 文档编写辅助