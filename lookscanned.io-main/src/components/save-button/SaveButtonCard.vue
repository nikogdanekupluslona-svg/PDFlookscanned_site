<template>
  <div class="save">
    <template v-if="pdf">
      <div class="result">
        <n-icon class="done-icon" :component="CheckmarkCircle24Filled" />
        <div class="result-text">
          <strong>{{ t('save.readyTitle') }}</strong>
          <span>{{ pdf.name }} · {{ filesize(pdf.size) }}</span>
        </div>
      </div>
      <button type="button" class="primary" @click="download">
        <n-icon :component="ArrowDownload24Regular" />
        {{ t('actions.downloadScannedPDF') }}
      </button>
      <p class="hint">{{ downloaded ? t('save.downloaded') : t('save.whereSaved') }}</p>
    </template>

    <template v-else>
      <button type="button" class="primary" :disabled="saving || disabled" @click="emit('generate')">
        <n-spin v-if="saving" :size="16" stroke="#10200a" />
        <n-icon v-else :component="DocumentPdf24Regular" />
        <span v-if="saving && totalPages">
          {{ t('save.progress', { current: finishedPages, total: totalPages }) }}
        </span>
        <span v-else-if="saving">{{ t('actions.generating') }}</span>
        <span v-else>{{ t('actions.generateScannedPDF') }}</span>
      </button>
      <div v-if="saving" class="bar"><div :style="{ width: (progress ?? 0) * 100 + '%' }" /></div>
      <p class="hint">{{ sample ? t('save.sampleHint') : t('save.generateHint') }}</p>
    </template>
  </div>
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue'
import { NIcon, NSpin } from 'naive-ui'
import {
  ArrowDownload24Regular,
  CheckmarkCircle24Filled,
  DocumentPdf24Regular
} from '@vicons/fluent'
import { filesize } from 'filesize'
import { useI18n } from 'vue-i18n'
import { downloadFile } from '@/utils/download-file'

const { t } = useI18n()

const props = defineProps<{
  progress?: number
  finishedPages?: number
  totalPages?: number
  saving?: boolean
  disabled?: boolean
  sample?: boolean
  pdf?: File
}>()

const emit = defineEmits<{
  (e: 'generate'): void
}>()

const downloaded = ref(false)
watch(
  () => props.pdf,
  () => (downloaded.value = false)
)

const download = () => {
  if (!props.pdf) return
  downloadFile(props.pdf, props.pdf.name)
  downloaded.value = true
}
</script>

<style scoped>
.save {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  max-width: 380px;
  min-height: 48px;
  padding: 0 16px;
  border: 0;
  border-radius: 999px;
  background: #8fd14f;
  color: #10200a;
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
}

.primary .n-icon {
  font-size: 20px;
}

.primary:hover:not(:disabled) {
  background: #a3e062;
}

.primary:focus-visible {
  outline: 2px solid #f4f4f5;
  outline-offset: 2px;
}

.primary:disabled {
  cursor: default;
  opacity: 0.75;
}

.bar {
  height: 4px;
  border-radius: 2px;
  background: #27272a;
  overflow: hidden;
}

.bar div {
  height: 100%;
  background: #8fd14f;
  transition: width 0.2s ease;
}

.result {
  display: flex;
  gap: 10px;
  align-items: center;
}

.done-icon {
  flex: none;
  font-size: 32px;
  color: #8fd14f;
}

.result-text {
  display: flex;
  flex-direction: column;
  min-width: 0;
  font-size: 12px;
  color: #a1a1aa;
  word-break: break-all;
}

.result-text strong {
  font-size: 14px;
  color: #f4f4f5;
}

.hint {
  margin: 0;
  font-size: 12px;
  line-height: 1.45;
  color: #a1a1aa;
}
</style>
