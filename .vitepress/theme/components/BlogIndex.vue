<script setup lang="ts">
import { computed, ref } from 'vue'
import { data as posts } from '../posts.data'
import { THEMES } from '../post-themes'

const active = ref<string | null>(null)

const filters = computed(() =>
  THEMES.map((t) => ({
    label: t.label,
    count: posts.filter((p) => p.themes.includes(t.label)).length,
  })).filter((f) => f.count > 0),
)

const filtered = computed(() =>
  active.value ? posts.filter((p) => p.themes.includes(active.value!)) : posts,
)

const featured = computed(() => (active.value ? null : filtered.value[0] ?? null))

const groups = computed(() => {
  const rest = featured.value ? filtered.value.slice(1) : filtered.value
  const byMonth = new Map<string, typeof rest>()
  for (const p of rest) {
    const month = new Date(p.dateISO).toLocaleDateString('en-US', { year: 'numeric', month: 'long' })
    if (!byMonth.has(month)) byMonth.set(month, [])
    byMonth.get(month)!.push(p)
  }
  return [...byMonth.entries()]
})

function day(iso: string) {
  return new Date(iso).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}
</script>

<template>
  <div class="blog-index">
    <div class="blog-filters" role="group" aria-label="Filter posts by theme">
      <button
        type="button"
        class="blog-filter"
        :aria-pressed="active === null"
        @click="active = null"
      >All <span>{{ posts.length }}</span></button>
      <button
        v-for="f in filters"
        :key="f.label"
        type="button"
        class="blog-filter"
        :aria-pressed="active === f.label"
        @click="active = f.label"
      >{{ f.label }} <span>{{ f.count }}</span></button>
    </div>

    <a v-if="featured" :href="featured.url" class="blog-featured">
      <p class="blog-featured-eyebrow">Latest · {{ featured.date }}</p>
      <h2>{{ featured.title }}</h2>
      <p v-if="featured.subtitle" class="blog-featured-sub">{{ featured.subtitle }}</p>
      <p class="blog-themes">
        <span v-for="t in featured.themes" :key="t" class="blog-theme">{{ t }}</span>
      </p>
    </a>

    <section v-for="[month, items] in groups" :key="month" class="blog-month">
      <h2 class="blog-month-title">{{ month }}</h2>
      <ol class="blog-rows">
        <li v-for="p in items" :key="p.url" class="blog-row">
          <time :datetime="p.dateISO" class="blog-row-date">{{ day(p.dateISO) }}</time>
          <div>
            <h3><a :href="p.url">{{ p.title }}</a></h3>
            <p v-if="p.subtitle" class="blog-row-sub">{{ p.subtitle }}</p>
            <p class="blog-themes">
              <span v-for="t in p.themes" :key="t" class="blog-theme">{{ t }}</span>
            </p>
          </div>
        </li>
      </ol>
    </section>
  </div>
</template>
