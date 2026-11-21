<script setup lang="ts">
import { withBase } from 'vitepress'
</script>

<template>
  <section class="home-hero">
    <div class="home-hero-photo">
      <img :src="withBase('/images/mansura.png')" alt="Mansura Habiba" />
    </div>
    <div class="home-hero-text">
      <p class="home-hero-tagline">Principal Architect — Enterprise AI Platforms · Agentic Infrastructure · HPC</p>
      <h1>Hi, I'm Mansura.</h1>
      <p>
        I architect multi-tenant enterprise AI capabilities at <strong>IBM Software</strong>, including
        governed agent tool access, cross-product execution, and model routing. Previously, I led
        architecture for a large enterprise HPC compute estate supporting financial services.
      </p>
      <p>
        I write about the decisions that make AI systems deployable, governable, resilient,
        and accountable in production.
      </p>
      <div class="home-hero-actions">
        <a class="btn btn-primary" href="/cv.html">Professional CV</a>
        <a class="btn btn-ghost" href="/blog/">Read the blog</a>
      </div>
    </div>
  </section>
</template>
