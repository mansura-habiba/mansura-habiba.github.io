<script setup lang="ts">
defineProps<{
  title: string
  tagline?: string
  variant?: 'default' | 'fact'
}>()
</script>

<template>
  <article class="topic-note" :class="variant">
    <header class="topic-note-header">
      <h3 class="topic-note-title">{{ title }}</h3>
      <p v-if="tagline" class="topic-note-tagline">{{ tagline }}</p>
    </header>
    <div class="topic-note-body">
      <slot />
    </div>
  </article>
</template>
