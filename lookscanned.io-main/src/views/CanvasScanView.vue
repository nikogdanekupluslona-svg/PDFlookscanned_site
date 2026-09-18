<template>
  <ScanWorkspace
    :page-title="t('base.scanTitle')"
    :default-config="defaultConfig"
    :create-scanner="createScanner"
  />
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n'
import ScanWorkspace from '@/components/scan/ScanWorkspace.vue'
import type { ScanConfig } from '@/utils/scan-renderer'
import { defaultConfig, CanvasScanner } from '@/utils/scan-renderer/canvas-scan'

const { t } = useI18n()

function createScanner(config: ScanConfig) {
  return new CanvasScanner(config)
}
</script>
