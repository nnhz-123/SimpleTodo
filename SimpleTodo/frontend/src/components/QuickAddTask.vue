<script setup lang="ts">
import { ref } from 'vue'
import { useTaskStore } from '../stores/taskStore'

const taskStore = useTaskStore()

const title = ref('')
const priority = ref('medium')

async function handleSubmit() {
  if (!title.value.trim()) return

  await taskStore.createTask({
    title: title.value,
    priority: priority.value
  })

  title.value = ''
}
</script>

<template>
  <form @submit.prevent="handleSubmit" class="quick-add">
    <input
      v-model="title"
      type="text"
      placeholder="What needs to be done?"
      required
    />

    <select v-model="priority">
      <option value="low">Low</option>
      <option value="medium">Medium</option>
      <option value="high">High</option>
    </select>

    <button type="submit">Add</button>
  </form>
</template>

<style scoped>
.quick-add {
  display: flex;
  gap: 10px;
}

.quick-add input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.quick-add select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.quick-add button {
  padding: 10px 20px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>