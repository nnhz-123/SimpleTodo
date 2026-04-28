<script setup lang="ts">
import { ref } from 'vue'

const settings = ref({
  theme: 'light',
  notifications: true,
  defaultPriority: 'medium',
  defaultCategory: 'general',
  dateFormat: 'MM/DD/YYYY',
  showCompleted: true
})

const themes = ['light', 'dark', 'auto']
const priorities = ['low', 'medium', 'high', 'urgent']
const categories = ['work', 'personal', 'study', 'health', 'finance', 'general']
const dateFormats = ['MM/DD/YYYY', 'DD/MM/YYYY', 'YYYY-MM-DD']

function saveSettings() {
  localStorage.setItem('simpletodo-settings', JSON.stringify(settings.value))
  alert('Settings saved!')
}

function resetSettings() {
  settings.value = {
    theme: 'light',
    notifications: true,
    defaultPriority: 'medium',
    defaultCategory: 'general',
    dateFormat: 'MM/DD/YYYY',
    showCompleted: true
  }
}
</script>

<template>
  <div class="settings-view">
    <h1>Settings</h1>

    <div class="settings-section">
      <h2>Appearance</h2>
      <div class="setting-item">
        <label>Theme</label>
        <select v-model="settings.theme">
          <option v-for="t in themes" :key="t" :value="t">{{ t }}</option>
        </select>
      </div>
    </div>

    <div class="settings-section">
      <h2>Notifications</h2>
      <div class="setting-item">
        <label>Enable notifications</label>
        <input v-model="settings.notifications" type="checkbox" />
      </div>
    </div>

    <div class="settings-section">
      <h2>Defaults</h2>
      <div class="setting-item">
        <label>Default Priority</label>
        <select v-model="settings.defaultPriority">
          <option v-for="p in priorities" :key="p" :value="p">{{ p }}</option>
        </select>
      </div>
      <div class="setting-item">
        <label>Default Category</label>
        <select v-model="settings.defaultCategory">
          <option v-for="c in categories" :key="c" :value="c">{{ c }}</option>
        </select>
      </div>
    </div>

    <div class="settings-section">
      <h2>Display</h2>
      <div class="setting-item">
        <label>Date Format</label>
        <select v-model="settings.dateFormat">
          <option v-for="f in dateFormats" :key="f" :value="f">{{ f }}</option>
        </select>
      </div>
      <div class="setting-item">
        <label>Show completed tasks</label>
        <input v-model="settings.showCompleted" type="checkbox" />
      </div>
    </div>

    <div class="settings-actions">
      <button @click="resetSettings" class="btn-reset">Reset</button>
      <button @click="saveSettings" class="btn-save">Save Settings</button>
    </div>
  </div>
</template>

<style scoped>
.settings-view {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.settings-section {
  background: #fff;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 15px;
  border: 1px solid #eee;
}

.settings-section h2 {
  margin-bottom: 10px;
  font-size: 16px;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
}

.setting-item select,
.setting-item input[type="checkbox"] {
  padding: 8px;
}

.settings-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.btn-reset {
  padding: 10px 20px;
  background: #f5f5f5;
  border: none;
  border-radius: 4px;
}

.btn-save {
  padding: 10px 20px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
}
</style>