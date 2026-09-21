<template>
  <div class="save">
    <template v-if="output && !busy">
      <div class="result">
        <n-icon class="done-icon" :component="CheckmarkCircle24Filled" />
        <div class="result-text">
          <strong>{{ t('save.readyTitle', output.count) }}</strong>
          <span>{{ output.name }} · {{ filesize(output.size) }}</span>
        </div>
      </div>
      <button type="button" class="primary secondary" @click="emit('download')">
        <n-icon :component="ArrowDownload24Regular" />
        {{ t('save.downloadAgain') }}
      </button>
      <p class="hint">
        {{ t('save.whereSaved') }}
        <template v-if="output.count > 1"> {{ t('save.zipHint') }}</template>
      </p>
    </template>

    <template v-else>
      <button type="button" class="primary" :disabled="busy || !count" @click="emit('generate')">
        <n-spin v-if="busy" :size="16" stroke="#10200a" />
        <n-icon v-else :component="DocumentPdf24Regular" />
        <span v-if="busy">{{ progressText || t('actions.generating') }}</span>
        <span v-else>{{ t('save.create', { n: count }, Math.max(count, 1)) }}</span>
      </button>
      <div v-if="busy" class="bar"><div :style="{ width: (progress ?? 0) * 100 + '%' }" /></div>
      <p class="hint">{{ hint }}</p>
    </template>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import { NIcon, NSpin } from 'naive-ui'
import {
  ArrowDownload24Regular,
  CheckmarkCircle24Filled,
  DocumentPdf24Regular
} from '@vicons/fluent'
import { filesize } from 'filesize'
import { useI18n } from 'vue-i18n'

export interface SaveOutput {
  name: string
  size: number
  count: number
}

const { t } = useI18n()

const props = defineProps<{
  /** Files ready to be scanned */
  count: number
  loading?: boolean
  busy?: boolean
  progress?: number
  progressText?: string
  output?: SaveOutput
}>()

const emit = defineEmits<{
  (e: 'generate'): void
  (e: 'download'): void
}>()

const hint = computed(() => {
  if (props.busy) return t('save.busyHint')
  if (props.loading) return t('actions.converting')
  if (!props.count) return t('save.noFileHint')
  return t('save.autoHint', props.count)
})
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

.primary.secondary {
  border: 1px solid #8fd14f;
  background: transparent;
  color: #8fd14f;
}

.primary.secondary:hover {
  background: rgba(143, 209, 79, 0.12);
}

.primary:focus-visible {
  outline: 2px solid #f4f4f5;
  outline-offset: 2px;
}

.primary:disabled {
  cursor: default;
  opacity: 0.55;
}

.bar {
  max-width: 380px;
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
