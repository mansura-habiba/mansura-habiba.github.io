<script setup lang="ts">
defineProps<{
  title?: string
}>()
</script>

<template>
  <aside class="topic-notes" aria-label="Key notes">
    <p v-if="title" class="topic-notes-title">{{ title }}</p>
    <div class="topic-notes-body">
      <slot />
    </div>
  </aside>
</template>
