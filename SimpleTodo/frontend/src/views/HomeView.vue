<script setup lang="ts">
import { onMounted } from 'vue'
import { useTaskStore } from '../stores/taskStore'
import TaskSummary from '../components/TaskSummary.vue'
import QuickAddTask from '../components/QuickAddTask.vue'

const taskStore = useTaskStore()

onMounted(async () => {
  await taskStore.fetchTasks()
  await taskStore.fetchStats()
})
</script>

<template>
  <div class="home-view">
    <section class="hero">
      <h1>SimpleTodo</h1>
      <p>Your personal task management assistant</p>
    </section>

    <TaskSummary />

    <section class="quick-add">
      <h2>Quick Add</h2>
      <QuickAddTask />
    </section>

    <section class="recent-tasks">
      <h2>Recent Tasks</h2>
      <ul v-if="taskStore.tasks.length > 0">
        <li v-for="task in taskStore.tasks.slice(0, 5)" :key="task.id">
          <router-link :to="`/tasks/${task.id}`">{{ task.title }}</router-link>
          <span class="priority">{{ task.priority }}</span>
        </li>
      </ul>
      <p v-else>No tasks yet. Start by adding one!</p>
    </section>

    <section class="navigation">
      <router-link to="/tasks">View All Tasks</router-link>
      <router-link to="/stats">View Statistics</router-link>
      <router-link to="/settings">Settings</router-link>
    </section>
  </div>
</template>

<style scoped>
.home-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.hero {
  text-align: center;
  padding: 40px 0;
}

.hero h1 {
  font-size: 48px;
  margin-bottom: 10px;
}

.hero p {
  color: #666;
}

.quick-add, .recent-tasks {
  margin-top: 30px;
}

.recent-tasks ul {
  list-style: none;
  padding: 0;
}

.recent-tasks li {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.navigation {
  display: flex;
  gap: 20px;
  margin-top: 40px;
  justify-content: center;
}

.navigation a {
  padding: 10px 20px;
  background: #f5f5f5;
  border-radius: 8px;
}
</style>