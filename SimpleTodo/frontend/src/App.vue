<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useTaskStore } from './stores/taskStore'
import TaskList from './components/TaskList.vue'
import TaskForm from './components/TaskForm.vue'

const taskStore = useTaskStore()
const showForm = ref(false)

onMounted(async () => {
  await taskStore.fetchTasks()
})
</script>

<template>
  <div class="app">
    <header>
      <h1>SimpleTodo</h1>
      <button @click="showForm = !showForm">
        {{ showForm ? 'Close' : 'Add Task' }}
      </button>
    </header>

    <TaskForm v-if="showForm" @submit="showForm = false" />
    <TaskList />
  </div>
</template>

<style>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

h1 {
  font-size: 24px;
}

button {
  padding: 8px 16px;
  cursor: pointer;
}
</style>