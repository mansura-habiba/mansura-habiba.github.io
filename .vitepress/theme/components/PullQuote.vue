<script setup lang="ts">
defineProps<{
  attribution?: string
  align?: 'left' | 'right' | 'center'
}>()
</script>

<template>
  <figure
    class="blog-block pull-quote"
    :class="align ? `pull-quote-${align}` : 'pull-quote-center'"
  >
    <blockquote>
      <slot />
    </blockquote>
    <figcaption v-if="attribution">— {{ attribution }}</figcaption>
  </figure>
</template>
