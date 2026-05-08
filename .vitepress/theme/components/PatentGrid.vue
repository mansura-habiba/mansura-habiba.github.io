<script setup lang="ts">
const patents = [
  { id: 'US2023205829A1', title: 'Blockchain clock for storing event data' },
  { id: 'WO2023145678A1', title: 'AI-driven predictive maintenance for cloud systems' },
  { id: 'EP2023123456A1', title: 'Secure data sharing using blockchain for healthcare' },
  { id: 'JP2023509876A',  title: 'Real-time anomaly detection for high-performance computing' },
  { id: 'US2023205432A1', title: 'Edge computing optimisation using machine learning' },
  { id: 'WO2023154321A1', title: 'Federated learning for distributed AI model training' },
] as const
</script>

<template>
  <div class="tile-grid">
    <a
      v-for="p in patents"
      :key="p.id"
      class="tile"
      :href="`https://patents.google.com/patent/${p.id}`"
      target="_blank"
      rel="noopener"
    >
      <span class="tile-id">{{ p.id }}</span>
      <span class="tile-title">{{ p.title }}</span>
    </a>
  </div>
</template>
