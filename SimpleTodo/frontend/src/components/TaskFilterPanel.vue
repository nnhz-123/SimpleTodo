<script setup lang="ts">
import { ref, computed } from 'vue'
import { useTaskStore } from '../stores/taskStore'
import type { PriorityEnum, CategoryEnum } from '../types'

const taskStore = useTaskStore()

const filters = ref({
  completed: undefined as boolean | undefined,
  priority: undefined as PriorityEnum | undefined,
  category: undefined as CategoryEnum | undefined,
  search: '',
  dueDateRange: {
    start: '',
    end: ''
  }
})

const priorities = ['low', 'medium', 'high', 'urgent']
const categories = ['work', 'personal', 'study', 'health', 'finance', 'general']

const hasActiveFilters = computed(() => {
  return filters.value.completed !== undefined ||
    filters.value.priority !== undefined ||
    filters.value.category !== undefined ||
    filters.value.search !== ''
})

function applyFilters() {
  taskStore.setFilters(filters.value)
}

function clearFilters() {
  filters.value = {
    completed: undefined,
    priority: undefined,
    category: undefined,
    search: '',
    dueDateRange: { start: '', end: '' }
  }
  taskStore.clearFilters()
}
</script>

<template>
  <div class="filter-panel">
    <div class="filter-row">
      <div class="filter-group">
        <label>Status</label>
        <select v-model="filters.completed" @change="applyFilters">
          <option :value="undefined">All</option>
          <option :value="false">Pending</option>
          <option :value="true">Completed</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Priority</label>
        <select v-model="filters.priority" @change="applyFilters">
          <option :value="undefined">All</option>
          <option v-for="p in priorities" :key="p" :value="p">{{ p }}</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Category</label>
        <select v-model="filters.category" @change="applyFilters">
          <option :value="undefined">All</option>
          <option v-for="c in categories" :key="c" :value="c">{{ c }}</option>
        </select>
      </div>
    </div>

    <div class="filter-row">
      <div class="filter-group search">
        <label>Search</label>
        <input
          v-model="filters.search"
          type="text"
          placeholder="Search tasks..."
          @input="applyFilters"
        />
      </div>

      <button v-if="hasActiveFilters" @click="clearFilters" class="clear-btn">
        Clear Filters
      </button>
    </div>

    <div v-if="hasActiveFilters" class="active-filters">
      <span>Active filters:</span>
      <span v-if="filters.completed !== undefined">
        {{ filters.completed ? 'Completed' : 'Pending' }}
      </span>
      <span v-if="filters.priority">{{ filters.priority }}</span>
      <span v-if="filters.category">{{ filters.category }}</span>
      <span v-if="filters.search">"{{ filters.search }}"</span>
    </div>
  </div>
</template>

<style scoped>
.filter-panel {
  background: #f9f9f9;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.filter-row {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
}

.filter-group {
  display: flex;
  flex-direction: column;
}

.filter-group.search {
  flex-grow: 1;
}

label {
  font-size: 12px;
  color: #666;
  margin-bottom: 4px;
}

select, input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.clear-btn {
  background: #f44336;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  border: none;
}

.active-filters {
  display: flex;
  gap: 10px;
  font-size: 12px;
}

.active-filters span:not(:first-child) {
  background: #e3f2fd;
  padding: 2px 8px;
  border-radius: 4px;
}
</style>