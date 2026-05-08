<script setup lang="ts">
const books = [
  {
    title: 'Hybrid Cloud Infrastructure and Operations Explained',
    publisher: 'Packt Publishing · 2022',
    cover:
      'https://m.media-amazon.com/images/I/81l1weci4RL._SL1500,204,203,200_.jpg',
    description:
      "A practitioner's guide to modernising enterprise infrastructure with IBM Cloud and Red Hat — covering cloud architecture, migration patterns, and Day-2 operations.",
    primary: { label: 'Get the book', href: 'https://packt.link/a/9781803248318' },
    secondary: { label: 'Author interview', href: 'https://partnerships.packt.com/edit-post-6/' },
  },
  {
    title: 'Emergence of Agentic AI: Architecting the Next Generation of Intelligent Systems',
    publisher: 'Leanpub · 2025',
    cover: 'https://d2sofvawe08yqg.cloudfront.net/emergence-agentic-ai/s_hero?1746930297&1746930297',
    description:
      'A practical framework for designing, securing, and operating agentic AI systems — the runtime layer most teams discover only after the demo ships.',
    primary: { label: 'Get the book', href: 'https://leanpub.com/emergence-agentic-ai' },
  },
  {
    title: 'Recent Trends in Modelling the Continuous Time Series using Deep Learning',
    publisher: 'Springer · 2026',
    cover:
      'https://media.springernature.com/w158/springer-static/cover/book/978-3-032-18021-6.jpg',
    description:
      'A research monograph on neural ODEs and continuous-time models for time-series — including data with informative missingness.',
    primary: { label: 'Springer page', href: 'https://link.springer.com/book/9783032180216' },
  },
] as const
</script>

<template>
  <div class="card-grid">
    <article v-for="book in books" :key="book.title" class="card book-card">
      <div class="book-cover">
        <img :src="book.cover" :alt="`${book.title} — book cover`" loading="lazy" />
      </div>
      <div class="book-body">
        <p class="post-meta">{{ book.publisher }}</p>
        <h3>{{ book.title }}</h3>
        <p class="publisher">{{ book.description }}</p>
        <p>
          <a class="book-link" :href="book.primary.href" target="_blank" rel="noopener">
            {{ book.primary.label }} →
          </a>
          <template v-if="book.secondary">
            &nbsp;·&nbsp;
            <a class="book-link" :href="book.secondary.href" target="_blank" rel="noopener">
              {{ book.secondary.label }}
            </a>
          </template>
        </p>
      </div>
    </article>
  </div>
</template>
