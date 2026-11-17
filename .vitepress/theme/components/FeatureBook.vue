<script setup lang="ts">
const books = [
  {
    title: 'Accountable Knowledge Architecture for Enterprise AI',
    meta: 'Leanpub · 2026',
    blurb:
      'A practical architecture for accountable enterprise AI, connecting evidence, knowledge, decisions, and autonomous agents across distributed systems.',
    href: 'https://leanpub.com/accountable-knowledge-architecture-for-ai',
    cover: '/books/accountable-knowledge-architecture-cover.png',
    cta: 'Get the book →',
  },
  {
    title: 'Recent Trends in Modelling the Continuous Time Series using Deep Learning',
    meta: 'Springer · 2026',
    blurb:
      'A research monograph on neural ODEs and continuous-time models for time-series data, including data with informative missingness.',
    href: 'https://link.springer.com/book/9783032180216',
    cover: 'https://media.springernature.com/w158/springer-static/cover/book/978-3-032-18021-6.jpg',
    cta: 'Springer page →',
  },
  {
    title: 'Emergence of Agentic AI',
    meta: 'Leanpub · 2025',
    blurb:
      'A practical framework for designing, securing, and operating agentic AI systems — the runtime layer most teams discover only after the demo ships.',
    href: 'https://leanpub.com/emergence-agentic-ai',
    cover: 'https://d2sofvawe08yqg.cloudfront.net/emergence-agentic-ai/s_hero?1746930297&1746930297',
    cta: 'Get the book →',
  },
]
</script>

<template>
  <section class="feature-books" aria-label="Latest books">
    <div class="section-header">
      <h2>Latest books</h2>
      <a class="see-all" href="/book">All books →</a>
    </div>
    <div class="feature-book-grid">
      <article v-for="book in books" :key="book.href" class="feature-book">
        <a class="feature-book-cover" :href="book.href" target="_blank" rel="noopener">
          <img :src="book.cover" :alt="`${book.title} — book cover`" loading="lazy" />
        </a>
        <h3>{{ book.title }}</h3>
        <p class="feature-meta">{{ book.meta }}</p>
        <p class="feature-book-blurb">{{ book.blurb }}</p>
        <a class="btn btn-primary" :href="book.href" target="_blank" rel="noopener">{{ book.cta }}</a>
      </article>
    </div>
  </section>
</template>
