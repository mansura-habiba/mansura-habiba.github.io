<script setup lang="ts">
defineProps<{
  title?: string
  readTime?: string
}>()
</script>

<template>
  <aside class="blog-block tldr-card" aria-label="TL;DR">
    <div class="tldr-card-head">
      <span class="tldr-card-eyebrow">{{ title || 'TL;DR' }}</span>
      <span v-if="readTime" class="tldr-card-meta">{{ readTime }}</span>
    </div>
    <div class="tldr-card-body">
      <slot />
    </div>
  </aside>
</template>
