<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useTaskStore } from '../stores/taskStore'

const router = useRouter()
const taskStore = useTaskStore()

const title = ref('')
const description = ref('')
const priority = ref('medium')
const category = ref('general')
const dueDate = ref('')
const tags = ref('')

const priorities = ['low', 'medium', 'high', 'urgent']
const categories = ['work', 'personal', 'study', 'health', 'finance', 'general']

async function handleSubmit() {
  if (!title.value.trim()) return

  await taskStore.createTask({
    title: title.value,
    description: description.value,
    priority: priority.value,
    category: category.value,
    due_date: dueDate.value || null,
    tags: tags.value.split(',').map(t => t.trim()).filter(t => t)
  })

  router.push('/tasks')
}
</script>

<template>
  <div class="task-form-page">
    <h1>Create New Task</h1>

    <form @submit.prevent="handleSubmit" class="task-form">
      <div class="form-group">
        <label>Title *</label>
        <input v-model="title" type="text" required placeholder="Task title" />
      </div>

      <div class="form-group">
        <label>Description</label>
        <textarea v-model="description" placeholder="Task description" rows="3" />
      </div>

      <div class="form-row">
        <div class="form-group">
          <label>Priority</label>
          <select v-model="priority">
            <option v-for="p in priorities" :key="p" :value="p">{{ p }}</option>
          </select>
        </div>

        <div class="form-group">
          <label>Category</label>
          <select v-model="category">
            <option v-for="c in categories" :key="c" :value="c">{{ c }}</option>
          </select>
        </div>
      </div>

      <div class="form-group">
        <label>Due Date</label>
        <input v-model="dueDate" type="date" />
      </div>

      <div class="form-group">
        <label>Tags (comma-separated)</label>
        <input v-model="tags" type="text" placeholder="urgent, review, bug" />
      </div>

      <div class="form-actions">
        <router-link to="/tasks" class="btn-cancel">Cancel</router-link>
        <button type="submit" class="btn-submit">Create Task</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.task-form-page {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.task-form {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #eee;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.btn-cancel {
  padding: 10px 20px;
  background: #f5f5f5;
  border-radius: 4px;
  text-decoration: none;
}

.btn-submit {
  padding: 10px 20px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>