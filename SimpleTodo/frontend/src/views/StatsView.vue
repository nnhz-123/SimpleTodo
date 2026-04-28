<script setup lang="ts">
import { computed } from 'vue'
import { useTaskStore } from '../stores/taskStore'

const taskStore = useTaskStore()

const stats = computed(() => taskStore.stats)

const priorityLabels = {
  low: 'Low',
  medium: 'Medium',
  high: 'High',
  urgent: 'Urgent'
}

const categoryLabels = {
  work: 'Work',
  personal: 'Personal',
  study: 'Study',
  health: 'Health',
  finance: 'Finance',
  general: 'General'
}
</script>

<template>
  <div class="stats-view">
    <h1>Task Statistics</h1>

    <div v-if="stats" class="stats-grid">
      <div class="stat-card">
        <h3>Total Tasks</h3>
        <p class="stat-value">{{ stats.total_tasks }}</p>
      </div>

      <div class="stat-card">
        <h3>Completed</h3>
        <p class="stat-value completed">{{ stats.completed_tasks }}</p>
      </div>

      <div class="stat-card">
        <h3>Pending</h3>
        <p class="stat-value pending">{{ stats.pending_tasks }}</p>
      </div>

      <div class="stat-card">
        <h3>Overdue</h3>
        <p class="stat-value overdue">{{ stats.overdue_tasks }}</p>
      </div>

      <div class="stat-section">
        <h2>By Priority</h2>
        <div class="bar-chart">
          <div v-for="(count, priority) in stats.by_priority" :key="priority" class="bar">
            <span class="label">{{ priorityLabels[priority] }}</span>
            <div class="bar-fill" :style="{ width: `${(count / stats.total_tasks) * 100}%` }"></div>
            <span class="count">{{ count }}</span>
          </div>
        </div>
      </div>

      <div class="stat-section">
        <h2>By Category</h2>
        <div class="bar-chart">
          <div v-for="(count, category) in stats.by_category" :key="category" class="bar">
            <span class="label">{{ categoryLabels[category] }}</span>
            <div class="bar-fill category" :style="{ width: `${(count / stats.total_tasks) * 100}%` }"></div>
            <span class="count">{{ count }}</span>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="loading">Loading statistics...</div>
  </div>
</template>

<style scoped>
.stats-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.stat-card {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.stat-value {
  font-size: 32px;
  font-weight: bold;
}

.stat-value.completed { color: #4CAF50; }
.stat-value.pending { color: #2196F3; }
.stat-value.overdue { color: #f44336; }

.stat-section {
  grid-column: span 2;
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #eee;
}

.bar-chart .bar {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.bar .label {
  width: 80px;
}

.bar-fill {
  height: 20px;
  background: #2196F3;
  border-radius: 4px;
}

.bar-fill.category {
  background: #4CAF50;
}

.bar .count {
  width: 40px;
  text-align: right;
}
</style>