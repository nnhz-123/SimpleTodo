<script setup lang="ts">
import { ref } from 'vue'
import { useTaskStore } from '../stores/taskStore'

const emit = defineEmits<{
  submit: []
}>()

const taskStore = useTaskStore()

const title = ref('')
const description = ref('')
const priority = ref('medium')
const category = ref('general')

async function handleSubmit() {
  if (!title.value.trim()) return

  await taskStore.createTask({
    title: title.value,
    description: description.value,
    priority: priority.value,
    category: category.value
  })

  title.value = ''
  description.value = ''
  emit('submit')
}
</script>

<template>
  <form @submit.prevent="handleSubmit" class="task-form">
    <input
      v-model="title"
      type="text"
      placeholder="Task title"
      required
    />

    <textarea
      v-model="description"
      placeholder="Description (optional)"
    />

    <select v-model="priority">
      <option value="low">Low</option>
      <option value="medium">Medium</option>
      <option value="high">High</option>
    </select>

    <select v-model="category">
      <option value="work">Work</option>
      <option value="personal">Personal</option>
      <option value="general">General</option>
    </select>

    <button type="submit">Create Task</button>
  </form>
</template>

<style scoped>
.task-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 20px;
}

input, textarea, select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

textarea {
  min-height: 60px;
}

button {
  padding: 10px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>