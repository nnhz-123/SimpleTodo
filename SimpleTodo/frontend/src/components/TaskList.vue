<script setup lang="ts">
import { useTaskStore } from '../stores/taskStore'

const taskStore = useTaskStore()
</script>

<template>
  <div class="task-list">
    <div v-if="taskStore.loading" class="loading">Loading...</div>
    <div v-if="taskStore.error" class="error">{{ taskStore.error }}</div>

    <ul v-if="!taskStore.loading">
      <li v-for="task in taskStore.tasks" :key="task.id" class="task-item">
        <span :class="{ completed: task.completed }">{{ task.title }}</span>
        <span class="priority">{{ task.priority }}</span>
        <button @click="taskStore.deleteTask(task.id)">Delete</button>
      </li>
    </ul>

    <div v-if="taskStore.tasks.length === 0 && !taskStore.loading" class="empty">
      No tasks yet. Add one!
    </div>
  </div>
</template>

<style scoped>
.task-list {
  margin-top: 20px;
}

.task-item {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.completed {
  text-decoration: line-through;
  color: #999;
}

.priority {
  font-size: 12px;
  padding: 2px 6px;
  border-radius: 4px;
}

.loading, .error, .empty {
  text-align: center;
  padding: 20px;
}

.error {
  color: red;
}
</style>