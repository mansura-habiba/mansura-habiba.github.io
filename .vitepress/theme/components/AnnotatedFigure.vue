<script setup lang="ts">
defineProps<{
  caption?: string
  notice?: string
  number?: number | string
}>()
</script>

<template>
  <figure class="blog-block annotated-figure">
    <div class="annotated-figure-body">
      <slot />
    </div>
    <figcaption v-if="caption || notice" class="annotated-figure-caption">
      <p v-if="caption" class="annotated-figure-title">
        <span v-if="number" class="annotated-figure-number">Figure {{ number }}.</span>
        {{ caption }}
      </p>
      <p v-if="notice" class="annotated-figure-notice">
        <span class="annotated-figure-notice-label">What to notice:</span>
        {{ notice }}
      </p>
    </figcaption>
  </figure>
</template>
