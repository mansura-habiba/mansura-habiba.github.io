<script setup lang="ts">
defineProps<{
  eyebrow?: string
  title: string
}>()
</script>

<template>
  <div class="blog-block part-divider" role="separator">
    <p v-if="eyebrow" class="part-divider-eyebrow">{{ eyebrow }}</p>
    <h2 class="part-divider-title">{{ title }}</h2>
    <div class="part-divider-rule" aria-hidden="true"></div>
  </div>
</template>
