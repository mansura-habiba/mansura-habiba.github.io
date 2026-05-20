<script setup lang="ts">
defineProps<{
  beforeLabel?: string
  afterLabel?: string
  title?: string
}>()
</script>

<template>
  <aside class="blog-block before-after" aria-label="Before and after comparison">
    <p v-if="title" class="before-after-title">{{ title }}</p>
    <div class="before-after-grid">
      <div class="before-after-pane before-pane">
        <p class="before-after-label">{{ beforeLabel || 'Before' }}</p>
        <div class="before-after-body">
          <slot name="before" />
        </div>
      </div>
      <div class="before-after-pane after-pane">
        <p class="before-after-label">{{ afterLabel || 'After' }}</p>
        <div class="before-after-body">
          <slot name="after" />
        </div>
      </div>
    </div>
  </aside>
</template>
