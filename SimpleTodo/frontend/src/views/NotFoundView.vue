<script setup lang="ts">
</script>

<template>
  <div class="not-found">
    <h1>404</h1>
    <p>Page not found</p>
    <router-link to="/">Go back home</router-link>
  </div>
</template>

<style scoped>
.not-found {
  text-align: center;
  padding: 50px;
}

.not-found h1 {
  font-size: 72px;
  color: #f44336;
}

.not-found a {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background: #2196F3;
  color: white;
  border-radius: 8px;
}
</style>