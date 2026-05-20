<script setup lang="ts">
defineProps<{
  name: string
  symptom?: string
  cause?: string
  fix?: string
  severity?: 'low' | 'medium' | 'high'
}>()
</script>

<template>
  <aside
    class="blog-block failure-mode"
    :class="severity ? `failure-mode-${severity}` : ''"
    aria-label="Failure mode"
  >
    <header class="failure-mode-head">
      <span class="failure-mode-eyebrow">Failure mode</span>
      <h4 class="failure-mode-name">{{ name }}</h4>
    </header>
    <dl class="failure-mode-fields">
      <template v-if="symptom || $slots.symptom">
        <dt>Symptom</dt>
        <dd>
          <slot name="symptom">{{ symptom }}</slot>
        </dd>
      </template>
      <template v-if="cause || $slots.cause">
        <dt>Blameless cause</dt>
        <dd>
          <slot name="cause">{{ cause }}</slot>
        </dd>
      </template>
      <template v-if="fix || $slots.fix">
        <dt>What to do instead</dt>
        <dd>
          <slot name="fix">{{ fix }}</slot>
        </dd>
      </template>
    </dl>
  </aside>
</template>
