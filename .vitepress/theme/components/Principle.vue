<script setup lang="ts">
defineProps<{
  number: number | string
  title: string
}>()
</script>

<template>
  <article class="principle-chip">
    <span class="principle-number">{{ String(number).padStart(2, '0') }}</span>
    <div class="principle-body">
      <h4 class="principle-title">{{ title }}</h4>
      <div class="principle-text">
        <slot />
      </div>
    </div>
  </article>
</template>
