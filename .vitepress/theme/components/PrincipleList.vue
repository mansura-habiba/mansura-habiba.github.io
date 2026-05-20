<script setup lang="ts">
defineProps<{
  title?: string
}>()
</script>

<template>
  <section class="blog-block principle-list" aria-label="Principles">
    <h3 v-if="title" class="principle-list-title">{{ title }}</h3>
    <div class="principle-list-grid">
      <slot />
    </div>
  </section>
</template>
