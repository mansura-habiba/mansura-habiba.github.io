<script setup lang="ts">
defineProps<{
  fromLabel?: string
  toLabel?: string
  title?: string
}>()
</script>

<template>
  <aside class="blog-block cross-industry" aria-label="Cross-industry comparison">
    <p v-if="title" class="cross-industry-title">{{ title }}</p>
    <div class="cross-industry-grid">
      <div class="cross-industry-cell cross-industry-from">
        <p class="cross-industry-label">{{ fromLabel || 'In other industries' }}</p>
        <div class="cross-industry-body">
          <slot name="from" />
        </div>
      </div>
      <div class="cross-industry-arrow" aria-hidden="true">→</div>
      <div class="cross-industry-cell cross-industry-to">
        <p class="cross-industry-label">{{ toLabel || 'In security architecture' }}</p>
        <div class="cross-industry-body">
          <slot name="to" />
        </div>
      </div>
    </div>
  </aside>
</template>
