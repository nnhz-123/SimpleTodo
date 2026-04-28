import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

interface Task {
  id: number
  title: string
  description: string | null
  priority: string
  category: string
  completed: boolean
  created_at: string
}

export const useTaskStore = defineStore('tasks', () => {
  const tasks = ref<Task[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  async function fetchTasks() {
    loading.value = true
    error.value = null
    try {
      const response = await axios.get<Task[]>('/api/tasks')
      tasks.value = response.data
    } catch (e) {
      error.value = 'Failed to fetch tasks'
    } finally {
      loading.value = false
    }
  }

  async function createTask(task: Partial<Task>) {
    try {
      const response = await axios.post<Task>('/api/tasks', task)
      tasks.value.push(response.data)
    } catch (e) {
      error.value = 'Failed to create task'
    }
  }

  async function updateTask(id: number, task: Partial<Task>) {
    try {
      await axios.put(`/api/tasks/${id}`, task)
      const index = tasks.value.findIndex(t => t.id === id)
      if (index !== -1) {
        tasks.value[index] = { ...tasks.value[index], ...task }
      }
    } catch (e) {
      error.value = 'Failed to update task'
    }
  }

  async function deleteTask(id: number) {
    try {
      await axios.delete(`/api/tasks/${id}`)
      tasks.value = tasks.value.filter(t => t.id !== id)
    } catch (e) {
      error.value = 'Failed to delete task'
    }
  }

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    createTask,
    updateTask,
    deleteTask
  }
})