<script setup lang="ts">
defineProps<{
  title: string
  href: string
  lines?: string[]
  tags?: string[]
}>()
</script>

<template>
  <article class="open-source-card">
    <h3 class="open-source-card-title">
      <a :href="href" target="_blank" rel="noopener">{{ title }}</a>
    </h3>
    <div class="open-source-card-body">
      <p
        v-for="(line, index) in lines"
        :key="index"
        class="open-source-card-line"
      >
        {{ line }}
      </p>
      <slot />
    </div>
    <ul v-if="tags?.length" class="open-source-tags" aria-label="Tags">
      <li v-for="tag in tags" :key="tag" class="open-source-tag">{{ tag }}</li>
    </ul>
  </article>
</template>
