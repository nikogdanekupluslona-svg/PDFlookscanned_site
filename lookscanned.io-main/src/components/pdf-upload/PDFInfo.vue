<template>
  <div class="file-card">
    <n-icon class="file-icon" :component="DocumentPdf24Regular" />
    <div class="details">
      <n-ellipsis class="name" :line-clamp="2" :tooltip="false">{{ pdf.name }}</n-ellipsis>
      <span class="meta">
        {{ filesize(pdf.size) }}
        <template v-if="pages"> · {{ t('upload.pages', { n: pages }, pages) }}</template>
      </span>
      <span v-if="loading" class="status">
        <n-spin :size="12" /> {{ t('actions.converting') }}
      </span>
      <span v-else-if="!sample" class="status ok">
        <n-icon :component="CheckmarkCircle16Filled" /> {{ t('upload.ready') }}
      </span>
    </div>
  </div>
  <div class="actions"><slot /></div>
</template>

<script lang="ts" setup>
import { NIcon, NEllipsis, NSpin } from 'naive-ui'
import { CheckmarkCircle16Filled, DocumentPdf24Regular } from '@vicons/fluent'
import { filesize } from 'filesize'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

defineProps<{
  pdf: File
  pages?: number
  sample?: boolean
  loading?: boolean
}>()
</script>

<style scoped>
.file-card {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.file-icon {
  flex: none;
  font-size: 36px;
  color: #8fd14f;
}

.details {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}

.name {
  font-weight: 600;
  word-break: break-all;
}

.meta {
  font-size: 12px;
  color: #a1a1aa;
}

.status {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin-top: 2px;
  font-size: 12px;
  color: #a1a1aa;
}

.status.ok {
  color: #8fd14f;
}

.actions {
  margin-top: 12px;
}
</style>
