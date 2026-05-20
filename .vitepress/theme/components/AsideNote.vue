<script setup lang="ts">
defineProps<{
  title?: string
  variant?: 'note' | 'anecdote' | 'caveat'
}>()
</script>

<template>
  <aside
    class="blog-block aside-note"
    :class="`aside-note-${variant || 'note'}`"
  >
    <p class="aside-note-label">
      {{ title || (variant === 'anecdote' ? 'Side note' : variant === 'caveat' ? 'Caveat' : 'Note') }}
    </p>
    <div class="aside-note-body">
      <slot />
    </div>
  </aside>
</template>
