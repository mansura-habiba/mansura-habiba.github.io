<script setup lang="ts">
defineProps<{
  title: string
  subtitle?: string
  tip?: string
}>()
</script>

<template>
  <section class="topic-stage">
    <header class="topic-stage-header">
      <div class="topic-stage-titles">
        <h2 class="topic-stage-title">{{ title }}</h2>
        <p v-if="subtitle" class="topic-stage-subtitle">{{ subtitle }}</p>
      </div>
      <aside v-if="tip" class="topic-stage-tip">
        <span class="topic-stage-tip-label">Tip</span>
        {{ tip }}
      </aside>
    </header>

    <div class="topic-stage-diagram">
      <slot name="diagram" />
    </div>

    <div class="topic-stage-explanation">
      <slot />
    </div>
  </section>
</template>
