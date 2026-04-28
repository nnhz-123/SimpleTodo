import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export interface Tag {
  id: number
  name: string
  color: string
}

export interface User {
  id: number
  username: string
  email: string
  avatar?: string
}

export interface Task {
  id: number
  title: string
  description: string | null
  priority: 'low' | 'medium' | 'high' | 'urgent'
  category: 'work' | 'personal' | 'study' | 'health' | 'finance' | 'general'
  completed: boolean
  due_date: string | null
  tags: Tag[]
  created_at: string
  updated_at: string | null
  completed_at: string | null
  user?: User
}

export interface TaskStats {
  total_tasks: number
  completed_tasks: number
  pending_tasks: number
  overdue_tasks: number
  by_priority: Record<string, number>
  by_category: Record<string, number>
}

export interface TaskFilter {
  completed?: boolean
  priority?: string
  category?: string
  search?: string
  page?: number
  page_size?: number
}