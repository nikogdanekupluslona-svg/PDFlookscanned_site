<template>
  <a class="feature-link" :href="CHROME_WEB_STORE_URL" target="_blank" rel="noopener noreferrer">
    <FeatureHolder :title="t('features.openSource.title')" :icon="LogoChrome">
      {{ t('features.openSource.description') }}
    </FeatureHolder>
  </a>
</template>

<script setup lang="ts">
import FeatureHolder from '@/components/Features/FeatureHolder.vue'
import { LogoChrome } from '@vicons/ionicons5'
import { useI18n } from 'vue-i18n'
import { CHROME_WEB_STORE_URL } from '@/constants'

const { t } = useI18n()
</script>

<style lang="scss" scoped>
.feature-link {
  text-decoration: none;
  color: inherit;
}
</style>
