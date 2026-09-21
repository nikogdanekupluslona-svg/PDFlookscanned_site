<template>
  <n-grid cols="1 m:2" x-gap="25px" y-gap="25px" responsive="screen">
    <n-grid-item>
      <p class="caption">{{ t('preview.original') }}</p>
      <n-card>
        <template #cover>
          <slot name="pdf" />
        </template>
      </n-card>
    </n-grid-item>
    <n-grid-item>
      <p class="caption">{{ t('preview.scanned') }}</p>
      <n-card>
        <template #cover>
          <slot name="scan" />
        </template>
      </n-card>
    </n-grid-item>
  </n-grid>
</template>

<script lang="ts" setup>
import { NGrid, NGridItem, NCard } from 'naive-ui'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<style scoped>
.caption {
  margin: 0 0 8px;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #a1a1aa;
}
</style>
