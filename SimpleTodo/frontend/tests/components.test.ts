import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import TaskList from '../src/components/TaskList.vue'

describe('TaskList', () => {
  it('renders empty state when no tasks', () => {
    const wrapper = mount(TaskList, {
      global: {
        mocks: {
          taskStore: {
            tasks: [],
            loading: false,
            error: null
          }
        }
      }
    })
    expect(wrapper.find('.empty').exists()).toBe(true)
  })

  it('renders loading state', () => {
    const wrapper = mount(TaskList, {
      global: {
        mocks: {
          taskStore: {
            tasks: [],
            loading: true,
            error: null
          }
        }
      }
    })
    expect(wrapper.find('.loading').exists()).toBe(true)
  })

  it('renders task items', () => {
    // TODO: Implement with mock tasks
  })
})