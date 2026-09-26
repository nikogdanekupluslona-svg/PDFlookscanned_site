<template>
  <header class="site-header">
    <div class="inner">
      <RouterLink class="brand" :to="localePath('/')">{{ t('base.title') }}</RouterLink>
      <nav class="nav" aria-label="Primary">
        <RouterLink :to="localePath('/')" :class="{ active: route.name === 'index' }">{{ t('base.nav.home') }}</RouterLink>
        <RouterLink :to="localePath('/scan')" :class="{ active: isScan }">{{ t('base.nav.scan') }}</RouterLink>
        <RouterLink :to="localePath('/scan/bulk')" :class="{ active: route.name === 'bulk' }">{{
          t('base.nav.bulk')
        }}</RouterLink>
        <a :href="localePath('/blog/')">{{ t('base.nav.guides') }}</a>
      </nav>
      <LanguageSwitcher class="lang" />
      <ChromeExtensionBadge class="badge" />
      <span class="row-break" aria-hidden="true" />
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import ChromeExtensionBadge from './ChromeExtensionBadge.vue'
import LanguageSwitcher from './LanguageSwitcher.vue'
import { useLanguage } from '@/composables/use-language'

const { t } = useI18n()
const route = useRoute()
const { localePath } = useLanguage()
const isScan = computed(() => route.name === 'scan' || route.name === 'scan-canvas' || route.name === 'scan-magica')
</script>

<style scoped>
.site-header {
  position: sticky;
  top: 0;
  z-index: 30;
  background: rgba(11, 11, 15, 0.92);
  border-bottom: 1px solid #22232a;
  backdrop-filter: blur(16px);
}

.inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 12px 18px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.brand {
  color: #f4f4f5;
  text-decoration: none;
  font-weight: 700;
  font-size: 15px;
  letter-spacing: -0.02em;
  white-space: nowrap;
}

.nav {
  display: flex;
  gap: 16px;
  flex: 1;
}

.nav a {
  color: #b8b8c2;
  text-decoration: none;
  font-size: 14px;
  white-space: nowrap;
}

.nav a.active,
.nav a:hover {
  color: #ffffff;
}

.row-break {
  display: none;
}

@media (max-width: 720px) {
  /* Row 1: brand + Chrome badge; row 2: navigation + language switcher */
  .inner {
    flex-wrap: wrap;
    padding: 10px 12px;
    gap: 10px;
  }

  .brand {
    flex: 1;
    font-size: 13px;
  }

  .badge {
    order: 2;
  }

  .row-break {
    display: block;
    order: 3;
    flex-basis: 100%;
    height: 0;
  }

  .nav {
    order: 4;
    min-width: 0;
    overflow-x: auto;
    scrollbar-width: none;
  }

  .lang {
    order: 5;
  }
}
</style>
