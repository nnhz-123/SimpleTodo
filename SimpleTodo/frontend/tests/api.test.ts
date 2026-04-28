import { describe, it, expect } from 'vitest'
import axios from 'axios'
import MockAdapter from 'axios-mock-adapter'

describe('API Integration', () => {
  it('fetches tasks from API', async () => {
    const mock = new MockAdapter(axios)
    mock.onGet('/api/tasks').reply(200, [
      { id: 1, title: 'Task 1', completed: false },
      { id: 2, title: 'Task 2', completed: true }
    ])

    const response = await axios.get('/api/tasks')
    expect(response.status).toBe(200)
    expect(response.data.length).toBe(2)
    mock.restore()
  })

  it('creates a task via API', async () => {
    const mock = new MockAdapter(axios)
    mock.onPost('/api/tasks').reply(200, { id: 3, title: 'New Task' })

    const response = await axios.post('/api/tasks', { title: 'New Task' })
    expect(response.status).toBe(200)
    expect(response.data.id).toBe(3)
    mock.restore()
  })

  it('handles API errors', async () => {
    const mock = new MockAdapter(axios)
    mock.onGet('/api/tasks').reply(500)

    try {
      await axios.get('/api/tasks')
    } catch (error: any) {
      expect(error.response.status).toBe(500)
    }
    mock.restore()
  })
})