<script setup lang="ts">
import { withBase } from 'vitepress'
</script>

<template>
  <section class="home-hero">
    <div class="home-hero-photo">
      <img :src="withBase('/images/mansura.png')" alt="Mansura Habiba" />
    </div>
    <div class="home-hero-text">
      <p class="home-hero-tagline">Principal Platform Architect — AI · HPC · Cloud</p>
      <h1>Hi, I'm Mansura.</h1>
      <p>
        I architect and operate AI and high-performance computing platforms at
        <strong>IBM</strong>. My work sits at the seam where deep-learning
        research meets the boring-but-load-bearing realities of enterprise
        infrastructure — security, scalability, and the chain-of-custody people
        only remember after something goes wrong.
      </p>
      <p>
        I write about agentic AI security, hybrid cloud, and the architectural
        decisions that decide whether an AI system survives contact with
        production.
      </p>
      <div class="home-hero-actions">
        <a class="btn btn-primary" href="/blog/">Read the blog</a>
        <a class="btn btn-ghost" href="/cv.html">View full CV</a>
      </div>
    </div>
  </section>
</template>
