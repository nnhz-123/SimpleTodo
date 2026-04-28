/**
 * Formatting utilities for task display.
 */

export function formatDate(date: Date | string | null): string {
  if (!date) return ''
  const d = new Date(date)
  return d.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

export function formatDateTime(date: Date | string | null): string {
  if (!date) return ''
  const d = new Date(date)
  return d.toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

export function formatPriority(priority: string): string {
  const labels: Record<string, string> = {
    low: 'Low',
    medium: 'Medium',
    high: 'High',
    urgent: 'Urgent'
  }
  return labels[priority] || priority
}

export function formatCategory(category: string): string {
  const labels: Record<string, string> = {
    work: 'Work',
    personal: 'Personal',
    study: 'Study',
    health: 'Health',
    finance: 'Finance',
    general: 'General'
  }
  return labels[category] || category
}

export function getCategoryColor(category: string): string {
  const colors: Record<string, string> = {
    work: '#2196F3',
    personal: '#4CAF50',
    study: '#9C27B0',
    health: '#E91E63',
    finance: '#FF9800',
    general: '#607D8B'
  }
  return colors[category] || '#607D8B'
}

export function getPriorityColor(priority: string): string {
  const colors: Record<string, string> = {
    low: '#4CAF50',
    medium: '#FF9800',
    high: '#f44336',
    urgent: '#D32F2F'
  }
  return colors[priority] || '#FF9800'
}

export function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text
  return text.substring(0, maxLength) + '...'
}

export function capitalizeFirst(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1)
}

export function pluralize(count: number, singular: string, plural?: string): string {
  return count === 1 ? singular : (plural || singular + 's')
}

export function formatRelativeTime(date: Date | string): string {
  const now = new Date()
  const then = new Date(date)
  const diffMs = now.getTime() - then.getTime()
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))

  if (diffDays === 0) return 'Today'
  if (diffDays === 1) return 'Yesterday'
  if (diffDays < 7) return `${diffDays} days ago`
  if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
  return formatDate(date)
}