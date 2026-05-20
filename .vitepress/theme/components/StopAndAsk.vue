<script setup lang="ts">
defineProps<{
  question?: string
}>()
</script>

<template>
  <aside class="blog-block stop-and-ask" aria-label="Reflection prompt">
    <p class="stop-and-ask-label">Stop and ask</p>
    <p v-if="question" class="stop-and-ask-question">{{ question }}</p>
    <div v-else class="stop-and-ask-question">
      <slot />
    </div>
  </aside>
</template>
