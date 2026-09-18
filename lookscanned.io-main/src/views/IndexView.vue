<template>
  <div class="landing">
    <section class="hero">
      <div class="copy">
        <div class="scanner">
          <ScannerSvg />
        </div>
        <h1>{{ t('base.landing.headline') }}</h1>
        <p class="subhead">{{ t('base.landing.subhead') }}</p>
        <RouterLink class="cta" to="/scan">{{ t('base.landing.cta') }}</RouterLink>
        <p class="note">{{ t('base.landing.note') }}</p>
      </div>
    </section>

    <ul class="points">
      <li>{{ t('base.landing.points.formats') }}</li>
      <li>{{ t('base.landing.points.local') }}</li>
      <li>{{ t('base.landing.points.free') }}</li>
      <li>{{ t('base.landing.points.preview') }}</li>
    </ul>

    <section class="steps">
      <h2>{{ t('base.landing.stepsTitle') }}</h2>
      <ol>
        <li>
          <span>01</span>
          <h3>{{ t('base.landing.step1Title') }}</h3>
          <p>{{ t('base.landing.step1Body') }}</p>
        </li>
        <li>
          <span>02</span>
          <h3>{{ t('base.landing.step2Title') }}</h3>
          <p>{{ t('base.landing.step2Body') }}</p>
        </li>
        <li>
          <span>03</span>
          <h3>{{ t('base.landing.step3Title') }}</h3>
          <p>{{ t('base.landing.step3Body') }}</p>
        </li>
      </ol>
    </section>

    <section class="features">
      <h2>{{ t('base.landing.featuresTitle') }}</h2>
      <TheFeatures />
    </section>

    <footer class="footer">{{ t('base.landing.footer') }}</footer>
  </div>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useHead } from '@unhead/vue'
import { useI18n } from 'vue-i18n'
import ScannerSvg from '@/components/Misc/ScannerSvg.vue'
import TheFeatures from '@/components/Features/TheFeatures.vue'

const { t } = useI18n()

useHead({
  title: t('base.title'),
  meta: [{ name: 'description', content: t('base.description') }]
})
</script>

<style scoped>
.landing {
  color: #f4f4f5;
}

.hero {
  min-height: calc(100vh - 92px);
  display: grid;
  place-items: center;
  padding: 48px 20px 32px;
  text-align: center;
}

.copy {
  max-width: 720px;
}

.scanner {
  width: min(180px, 42vw);
  margin: 0 auto 18px;
}

h1 {
  margin: 0 0 12px;
  font-size: clamp(32px, 6vw, 56px);
  letter-spacing: -0.04em;
  font-weight: 700;
}

.subhead {
  margin: 0 auto 24px;
  max-width: 640px;
  color: #c4c4cc;
  font-size: 16px;
  line-height: 1.6;
}

.cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
  padding: 0 22px;
  border-radius: 999px;
  background: #8fd14f;
  color: #10200a;
  text-decoration: none;
  font-weight: 700;
}

.note {
  margin: 14px 0 0;
  color: #8e8e99;
  font-size: 13px;
}

.points {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  list-style: none;
  margin: 0;
  padding: 22px 24px;
  border-top: 1px solid #22232a;
  border-bottom: 1px solid #22232a;
  color: #c9c9d1;
  font-size: 14px;
}

.points li::before {
  content: '';
  display: inline-block;
  width: 7px;
  height: 7px;
  margin-right: 8px;
  border-radius: 50%;
  background: #8fd14f;
}

.steps,
.features {
  max-width: 1100px;
  margin: 0 auto;
  padding: 72px 24px;
}

h2 {
  margin: 0 0 28px;
  font-size: 28px;
  letter-spacing: -0.03em;
}

.steps ol {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.steps span {
  display: block;
  color: #8fd14f;
  font-weight: 700;
  margin-bottom: 8px;
}

.steps h3,
.steps p {
  margin: 0;
}

.steps p,
.footer {
  color: #b8b8c2;
  line-height: 1.55;
}

.footer {
  padding: 0 24px 64px;
  text-align: center;
}

@media (max-width: 800px) {
  .points,
  .steps ol {
    grid-template-columns: 1fr;
  }
}
</style>
