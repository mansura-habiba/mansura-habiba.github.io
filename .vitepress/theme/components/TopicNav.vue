<script setup lang="ts">
defineProps<{
  title?: string
}>()
</script>

<template>
  <nav class="topic-nav" aria-label="Topic navigation">
    <p v-if="title" class="topic-nav-title">{{ title }}</p>
    <ul class="topic-nav-list">
      <slot />
    </ul>
  </nav>
</template>
