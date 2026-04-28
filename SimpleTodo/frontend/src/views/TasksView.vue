<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useTaskStore } from '../stores/taskStore'
import TaskItem from '../components/TaskItem.vue'
import TaskFilterPanel from '../components/TaskFilterPanel.vue'

const taskStore = useTaskStore()

const showFilters = ref(false)
const selectedTasks = ref<number[]>([])

onMounted(async () => {
  await taskStore.fetchTasks()
  await taskStore.fetchStats()
})

function toggleSelection(taskId: number) {
  const index = selectedTasks.value.indexOf(taskId)
  if (index === -1) {
    selectedTasks.value.push(taskId)
  } else {
    selectedTasks.value.splice(index, 1)
  }
}

async function bulkComplete() {
  await taskStore.bulkComplete(selectedTasks.value)
  selectedTasks.value = []
}

async function bulkDelete() {
  await taskStore.bulkDelete(selectedTasks.value)
  selectedTasks.value = []
}
</script>

<template>
  <div class="tasks-view">
    <header class="tasks-header">
      <h1>My Tasks</h1>
      <div class="header-actions">
        <button @click="showFilters = !showFilters">
          {{ showFilters ? 'Hide Filters' : 'Show Filters' }}
        </button>
        <router-link to="/tasks/new" class="btn-primary">Add Task</router-link>
      </div>
    </header>

    <TaskFilterPanel v-if="showFilters" />

    <div v-if="selectedTasks.length > 0" class="bulk-actions">
      <span>{{ selectedTasks.length }} selected</span>
      <button @click="bulkComplete">Complete All</button>
      <button @click="bulkDelete">Delete All</button>
    </div>

    <div v-if="taskStore.loading" class="loading">Loading tasks...</div>

    <div v-else-if="taskStore.tasks.length === 0" class="empty-state">
      <p>No tasks yet. Create your first task!</p>
      <router-link to="/tasks/new">Add Task</router-link>
    </div>

    <ul v-else class="task-list">
      <TaskItem
        v-for="task in taskStore.filteredTasks"
        :key="task.id"
        :task="task"
        :selected="selectedTasks.includes(task.id)"
        @toggle-select="toggleSelection(task.id)"
      />
    </ul>

    <div v-if="taskStore.error" class="error">{{ taskStore.error }}</div>
  </div>
</template>

<style scoped>
.tasks-view {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.tasks-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.header-actions {
  display: flex;
  gap: 10px;
}

.bulk-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  background: #e3f2fd;
  border-radius: 8px;
  margin-bottom: 20px;
}

.task-list {
  list-style: none;
  padding: 0;
}

.empty-state {
  text-align: center;
  padding: 40px;
}

.btn-primary {
  background: #4CAF50;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  text-decoration: none;
}

.loading, .error {
  text-align: center;
  padding: 20px;
}
</style>