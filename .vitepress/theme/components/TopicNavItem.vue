<script setup lang="ts">
defineProps<{
  label: string
  subtitle?: string
  href?: string
  active?: boolean
  color?: string
}>()
</script>

<template>
  <li class="topic-nav-item" :class="{ active }">
    <component
      :is="href ? 'a' : 'span'"
      :href="href"
      class="topic-nav-link"
      :aria-current="active ? 'page' : undefined"
    >
      <span
        v-if="color"
        class="topic-nav-dot"
        :style="{ background: color }"
        aria-hidden="true"
      />
      <span class="topic-nav-text">
        <span class="topic-nav-label">{{ label }}</span>
        <span v-if="subtitle" class="topic-nav-subtitle">{{ subtitle }}</span>
      </span>
    </component>
  </li>
</template>
