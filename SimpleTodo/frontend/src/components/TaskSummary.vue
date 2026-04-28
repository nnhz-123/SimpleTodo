<script setup lang="ts">
import { computed } from 'vue'
import { useTaskStore } from '../stores/taskStore'

const taskStore = useTaskStore()

const stats = computed(() => taskStore.stats)

const completionRate = computed(() => {
  if (!stats.value || stats.value.total_tasks === 0) return 0
  return Math.round((stats.value.completed_tasks / stats.value.total_tasks) * 100)
})
</script>

<template>
  <div class="task-summary">
    <div class="summary-grid">
      <div class="summary-item">
        <span class="label">Total</span>
        <span class="value">{{ stats?.total_tasks ?? 0 }}</span>
      </div>
      <div class="summary-item">
        <span class="label">Pending</span>
        <span class="value pending">{{ stats?.pending_tasks ?? 0 }}</span>
      </div>
      <div class="summary-item">
        <span class="label">Completed</span>
        <span class="value completed">{{ stats?.completed_tasks ?? 0 }}</span>
      </div>
      <div class="summary-item">
        <span class="label">Overdue</span>
        <span class="value overdue">{{ stats?.overdue_tasks ?? 0 }}</span>
      </div>
    </div>

    <div class="progress-bar">
      <div class="progress-fill" :style="{ width: `${completionRate}%` }"></div>
      <span class="progress-text">{{ completionRate }}% completed</span>
    </div>
  </div>
</template>

<style scoped>
.task-summary {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #eee;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 15px;
}

.summary-item {
  text-align: center;
}

.summary-item .label {
  font-size: 12px;
  color: #666;
}

.summary-item .value {
  font-size: 24px;
  font-weight: bold;
}

.value.pending { color: #2196F3; }
.value.completed { color: #4CAF50; }
.value.overdue { color: #f44336; }

.progress-bar {
  margin-top: 20px;
  height: 20px;
  background: #e0e0e0;
  border-radius: 10px;
  position: relative;
}

.progress-fill {
  height: 100%;
  background: #4CAF50;
  border-radius: 10px;
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 12px;
}
</style>