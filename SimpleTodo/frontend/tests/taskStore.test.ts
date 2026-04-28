import { describe, it, expect, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useTaskStore } from '../stores/taskStore'

describe('TaskStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('initializes with empty tasks', () => {
    const store = useTaskStore()
    expect(store.tasks).toEqual([])
    expect(store.loading).toBe(false)
    expect(store.error).toBeNull()
  })

  it('sets filters correctly', () => {
    const store = useTaskStore()
    store.setFilters({ priority: 'high', category: 'work' })
    expect(store.filters.priority).toBe('high')
  })

  it('clears filters', () => {
    const store = useTaskStore()
    store.setFilters({ priority: 'high' })
    store.clearFilters()
    expect(store.filters.priority).toBeUndefined()
  })

  it('computes filtered tasks', () => {
    const store = useTaskStore()
    // TODO: Add mock tasks and test filtering
    expect(store.filteredTasks).toEqual([])
  })
})