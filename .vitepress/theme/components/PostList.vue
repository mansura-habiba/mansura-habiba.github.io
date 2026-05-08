<script setup lang="ts">
import { data as posts } from '../posts.data'

const props = defineProps<{ limit?: number }>()
const visible = props.limit ? posts.slice(0, props.limit) : posts
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
    No posts yet. New writing will appear here — in the meantime,
    <a href="https://mansurahabiba.medium.com/" target="_blank" rel="noopener">previous essays are on Medium</a>.
  </p>
</template>
