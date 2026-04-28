<script setup lang="ts">
import { computed } from 'vue'
import type { Task } from '../types'

const props = defineProps<{
  task: Task
  selected: boolean
}>()

const emit = defineEmits<{
  toggleSelect: []
  toggleComplete: []
  delete: []
}>()

const isOverdue = computed(() => {
  if (props.task.completed || !props.task.due_date) return false
  return new Date(props.task.due_date) < new Date()
})

const priorityClass = computed(() => {
  return `priority-${props.task.priority}`
})
</script>

<template>
  <li class="task-item" :class="{ completed: task.completed, overdue: isOverdue }">
    <input
      type="checkbox"
      :checked="selected"
      @change="emit('toggleSelect')"
      class="select-checkbox"
    />

    <div class="task-content">
      <div class="task-header">
        <input
          type="checkbox"
          :checked="task.completed"
          @change="emit('toggleComplete')"
          class="complete-checkbox"
        />
        <router-link :to="`/tasks/${task.id}`" class="task-title">
          {{ task.title }}
        </router-link>
        <span :class="['priority-badge', priorityClass]">{{ task.priority }}</span>
      </div>

      <p v-if="task.description" class="task-description">{{ task.description }}</p>

      <div class="task-meta">
        <span class="category">{{ task.category }}</span>
        <span v-if="task.due_date" class="due-date">
          Due: {{ new Date(task.due_date).toLocaleDateString() }}
        </span>
        <div v-if="task.tags.length > 0" class="tags">
          <span v-for="tag in task.tags" :key="tag.id" class="tag">{{ tag.name }}</span>
        </div>
      </div>
    </div>

    <button @click="emit('delete')" class="delete-btn">Delete</button>
  </li>
</template>

<style scoped>
.task-item {
  display: flex;
  align-items: flex-start;
  padding: 15px;
  border-bottom: 1px solid #eee;
  background: #fff;
}

.task-item.completed {
  background: #f5f5f5;
}

.task-item.overdue {
  border-left: 3px solid #f44336;
}

.select-checkbox {
  margin-right: 10px;
}

.task-content {
  flex-grow: 1;
}

.task-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.task-title {
  font-weight: 500;
  text-decoration: none;
  color: #333;
}

.task-item.completed .task-title {
  color: #999;
  text-decoration: line-through;
}

.priority-badge {
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.priority-low { background: #e8f5e9; color: #2e7d32; }
.priority-medium { background: #fff3e0; color: #ef6c00; }
.priority-high { background: #ffebee; color: #c62828; }
.priority-urgent { background: #f44336; color: white; }

.task-description {
  color: #666;
  margin-top: 5px;
  font-size: 14px;
}

.task-meta {
  display: flex;
  gap: 10px;
  margin-top: 10px;
  font-size: 12px;
  color: #888;
}

.tags {
  display: flex;
  gap: 5px;
}

.tag {
  background: #e3f2fd;
  padding: 2px 6px;
  border-radius: 4px;
}

.delete-btn {
  background: transparent;
  color: #f44336;
  border: none;
  cursor: pointer;
}
</style>