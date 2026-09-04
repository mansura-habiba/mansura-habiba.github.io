<script setup lang="ts">
defineProps<{
  studio?: string
  tagline?: string
}>()
</script>

<template>
  <div class="topic-studio">
    <header v-if="studio || tagline" class="topic-studio-header">
      <div class="topic-studio-brand">
        <h1 v-if="studio" class="topic-studio-title">{{ studio }}</h1>
        <p v-if="tagline" class="topic-studio-tagline">{{ tagline }}</p>
      </div>
    </header>

    <div class="topic-studio-body">
      <slot />
    </div>
  </div>
</template>
