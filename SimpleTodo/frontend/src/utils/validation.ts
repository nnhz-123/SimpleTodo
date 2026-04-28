/**
 * Validation utilities for task input.
 */

export interface ValidationResult {
  valid: boolean
  errors: string[]
}

export function validateTaskTitle(title: string): ValidationResult {
  const errors: string[] = []

  if (!title || title.trim().length === 0) {
    errors.push('Title is required')
  }

  if (title.length > 200) {
    errors.push('Title must be less than 200 characters')
  }

  return {
    valid: errors.length === 0,
    errors
  }
}

export function validateTaskDescription(description: string): ValidationResult {
  const errors: string[] = []

  if (description && description.length > 1000) {
    errors.push('Description must be less than 1000 characters')
  }

  return {
    valid: errors.length === 0,
    errors
  }
}

export function validateDueDate(dueDate: string | null): ValidationResult {
  const errors: string[] = []

  if (dueDate) {
    const date = new Date(dueDate)
    if (isNaN(date.getTime())) {
      errors.push('Invalid due date format')
    }
  }

  return {
    valid: errors.length === 0,
    errors
  }
}

export function validateTaskInput(input: {
  title: string
  description?: string
  due_date?: string | null
}): ValidationResult {
  const titleResult = validateTaskTitle(input.title)
  const descriptionResult = validateTaskDescription(input.description || '')
  const dueDateResult = validateDueDate(input.due_date || null)

  const allErrors = [
    ...titleResult.errors,
    ...descriptionResult.errors,
    ...dueDateResult.errors
  ]

  return {
    valid: allErrors.length === 0,
    errors: allErrors
  }
}

export function isValidPriority(priority: string): boolean {
  return ['low', 'medium', 'high', 'urgent'].includes(priority)
}

export function isValidCategory(category: string): boolean {
  return ['work', 'personal', 'study', 'health', 'finance', 'general'].includes(category)
}