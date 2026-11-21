<script setup lang="ts">
import { withBase } from 'vitepress'
</script>

<template>
  <section class="home-hero">
    <div class="home-hero-photo">
      <img :src="withBase('/images/mansura.png')" alt="Mansura Habiba" />
    </div>
    <div class="home-hero-text">
      <p class="home-hero-tagline">Principal Architect — Large-scale x86 Compute · Enterprise AI · Security</p>
      <h1>Hi, I'm Mansura.</h1>
      <p>
        I develop and architect enterprise AI platform capabilities at <strong>IBM Software</strong>,
        including secure tool access, multi-tenant execution controls and cross-product model routing.
        Previously, I was technical architecture owner for a <strong>20,000+ x86-64 system</strong>
        enterprise compute estate in financial services.
      </p>
      <p>
        Security is central to both: identity, authorisation, isolation, resilience and auditability
        are foundational platform responsibilities, not features to add after deployment.
      </p>
      <div class="home-hero-actions">
        <a class="btn btn-primary" href="/cv.html">Professional CV</a>
        <a class="btn btn-ghost" href="/blog/">Read the blog</a>
      </div>
    </div>
  </section>
</template>
