/**
 * Storage utilities for local data persistence.
 */

const STORAGE_KEY_PREFIX = 'simpletodo_'

export function setItem<T>(key: string, value: T): void {
  const fullKey = STORAGE_KEY_PREFIX + key
  try {
    localStorage.setItem(fullKey, JSON.stringify(value))
  } catch (e) {
    console.error('Failed to save to localStorage:', e)
  }
}

export function getItem<T>(key: string, defaultValue: T): T {
  const fullKey = STORAGE_KEY_PREFIX + key
  try {
    const item = localStorage.getItem(fullKey)
    if (item === null) return defaultValue
    return JSON.parse(item) as T
  } catch (e) {
    console.error('Failed to read from localStorage:', e)
    return defaultValue
  }
}

export function removeItem(key: string): void {
  const fullKey = STORAGE_KEY_PREFIX + key
  try {
    localStorage.removeItem(fullKey)
  } catch (e) {
    console.error('Failed to remove from localStorage:', e)
  }
}

export function clearAll(): void {
  try {
    const keysToRemove = Object.keys(localStorage)
      .filter(key => key.startsWith(STORAGE_KEY_PREFIX))
    keysToRemove.forEach(key => localStorage.removeItem(key))
  } catch (e) {
    console.error('Failed to clear localStorage:', e)
  }
}

export function getSettings(): Record<string, any> {
  return getItem('settings', {
    theme: 'light',
    notifications: true,
    defaultPriority: 'medium',
    defaultCategory: 'general'
  })
}

export function saveSettings(settings: Record<string, any>): void {
  setItem('settings', settings)
}