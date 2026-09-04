<script setup lang="ts">
import { computed } from 'vue'
import { data as posts } from '../posts.data'

const props = defineProps<{
  limit?: number
  category?: string
}>()

const visible = computed(() => {
  let list = props.category
    ? posts.filter((p) => p.categories.includes(props.category!))
    : posts
  if (props.limit) list = list.slice(0, props.limit)
  return list
})
</script>

<template>
  <ol v-if="visible.length" class="post-list">
    <li v-for="p in visible" :key="p.url" class="post-list-item">
      <p class="post-meta">
        <time :datetime="p.dateISO">{{ p.date }}</time>
        <template v-if="p.categories.length">
          &nbsp;·&nbsp; {{ p.categories.join(', ') }}
        </template>
      </p>
      <h3>
        <a :href="p.url">{{ p.title }}</a>
      </h3>
      <p v-if="p.subtitle" class="post-excerpt">{{ p.subtitle }}</p>
      <p v-else-if="p.excerpt" class="post-excerpt">{{ p.excerpt }}</p>
    </li>
  </ol>
  <p v-else style="color: var(--vp-c-text-2);">
    <template v-if="category">
      No published pages in this topic yet.
    </template>
    <template v-else>
      No posts yet. New writing will appear here — in the meantime,
      <a href="https://mansurahabiba.medium.com/" target="_blank" rel="noopener">previous essays are on Medium</a>.
    </template>
  </p>
</template>
