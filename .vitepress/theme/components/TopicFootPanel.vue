<script setup lang="ts">
defineProps<{
  title: string
}>()
</script>

<template>
  <section class="topic-foot-panel">
    <h3 class="topic-foot-panel-title">{{ title }}</h3>
    <div class="topic-foot-panel-body">
      <slot />
    </div>
  </section>
</template>
