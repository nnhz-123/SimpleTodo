import { describe, it, expect } from 'vitest'
import {
  formatDate,
  formatPriority,
  getCategoryColor,
  truncateText
} from '../src/utils/formatters'

describe('formatDate', () => {
  it('formats date correctly', () => {
    const date = new Date('2026-04-28T10:00:00Z')
    expect(formatDate(date)).toContain('2026')
  })

  it('handles null date', () => {
    expect(formatDate(null)).toBe('')
  })
})

describe('formatPriority', () => {
  it('returns correct label for priority', () => {
    expect(formatPriority('high')).toBe('High')
    expect(formatPriority('urgent')).toBe('Urgent')
  })
})

describe('getCategoryColor', () => {
  it('returns correct color for category', () => {
    expect(getCategoryColor('work')).toBe('#2196F3')
    expect(getCategoryColor('personal')).toBe('#4CAF50')
  })
})

describe('truncateText', () => {
  it('truncates long text', () => {
    const text = 'This is a very long text that needs to be truncated'
    expect(truncateText(text, 20).length).toBeLessThanOrEqual(23)
  })

  it('keeps short text unchanged', () => {
    const text = 'Short text'
    expect(truncateText(text, 20)).toBe(text)
  })
})