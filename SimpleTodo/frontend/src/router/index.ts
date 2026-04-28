import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomeView.vue'),
    meta: { title: 'SimpleTodo - Home' }
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: () => import('../views/TasksView.vue'),
    meta: { title: 'SimpleTodo - Tasks' }
  },
  {
    path: '/tasks/:id',
    name: 'TaskDetail',
    component: () => import('../views/TaskDetailView.vue'),
    meta: { title: 'SimpleTodo - Task Detail' }
  },
  {
    path: '/stats',
    name: 'Stats',
    component: () => import('../views/StatsView.vue'),
    meta: { title: 'SimpleTodo - Statistics' }
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('../views/SettingsView.vue'),
    meta: { title: 'SimpleTodo - Settings' }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFoundView.vue'),
    meta: { title: 'SimpleTodo - 404' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard for title
router.beforeEach((to, _from, next) => {
  document.title = to.meta.title as string || 'SimpleTodo'
  next()
})

export default router