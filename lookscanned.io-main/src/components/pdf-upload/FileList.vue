<template>
  <ul class="file-list">
    <li
      v-for="item in items"
      :key="item.id"
      :class="{ active: item.id === activeId, failed: item.status === 'failed' }"
    >
      <button
        type="button"
        class="select"
        :title="t('files.preview')"
        :disabled="item.status === 'failed'"
        @click="emit('select', item.id)"
      >
        <n-icon class="file-icon" :component="DocumentPdf24Regular" />
        <span class="details">
          <span class="name">{{ item.name }}</span>
          <span class="meta">
            {{ filesize(item.size) }}
            <template v-if="item.pages"> · {{ t('upload.pages', { n: item.pages }, item.pages) }}</template>
          </span>
          <span class="status" :class="item.status">
            <n-spin v-if="item.status === 'loading' || item.status === 'processing'" :size="10" />
            <n-icon v-else-if="item.status === 'done'" :component="CheckmarkCircle16Filled" />
            <n-icon v-else-if="item.status === 'failed'" :component="ErrorCircle16Filled" />
            {{ statusLabel(item) }}
          </span>
        </span>
      </button>
      <span class="row-actions">
        <button
          v-if="item.hasResult"
          type="button"
          class="icon-button"
          :title="t('files.downloadOne')"
          :aria-label="t('files.downloadOne')"
          @click="emit('download', item.id)"
        >
          <n-icon :component="ArrowDownload16Regular" />
        </button>
        <button
          type="button"
          class="icon-button"
          :title="t('files.remove')"
          :aria-label="t('files.remove')"
          :disabled="busy"
          @click="emit('remove', item.id)"
        >
          <n-icon :component="Dismiss16Regular" />
        </button>
      </span>
    </li>
  </ul>
  <p v-if="items.length > 1" class="list-hint">{{ t('files.hint') }}</p>
</template>

<script lang="ts" setup>
import { NIcon, NSpin } from 'naive-ui'
import {
  ArrowDownload16Regular,
  CheckmarkCircle16Filled,
  Dismiss16Regular,
  DocumentPdf24Regular,
  ErrorCircle16Filled
} from '@vicons/fluent'
import { filesize } from 'filesize'
import { useI18n } from 'vue-i18n'

export type FileStatus = 'loading' | 'ready' | 'processing' | 'done' | 'failed'

export interface FileListItem {
  id: string
  name: string
  size: number
  pages?: number
  status: FileStatus
  error?: string
  hasResult: boolean
}

const { t } = useI18n()

defineProps<{
  items: FileListItem[]
  activeId?: string
  busy?: boolean
}>()

const emit = defineEmits<{
  (e: 'select', id: string): void
  (e: 'remove', id: string): void
  (e: 'download', id: string): void
}>()

function statusLabel(item: FileListItem) {
  if (item.status === 'failed') return item.error ?? t('actions.failed')
  return t(`files.status.${item.status}`)
}
</script>

<style scoped>
.file-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.file-list li {
  display: flex;
  align-items: center;
  gap: 4px;
  border: 1px solid #27272a;
  border-radius: 10px;
  background: #18181b;
}

.file-list li.active {
  border-color: #8fd14f;
}

.select {
  display: flex;
  flex: 1;
  gap: 10px;
  align-items: flex-start;
  min-width: 0;
  padding: 10px 4px 10px 10px;
  border: 0;
  background: none;
  color: inherit;
  font: inherit;
  text-align: left;
  cursor: pointer;
}

.select:disabled {
  cursor: default;
}

.select:focus-visible,
.icon-button:focus-visible {
  outline: 2px solid #8fd14f;
  outline-offset: -2px;
  border-radius: 8px;
}

.file-icon {
  flex: none;
  font-size: 28px;
  color: #8fd14f;
}

.failed .file-icon {
  color: #71717a;
}

.details {
  display: flex;
  flex-direction: column;
  gap: 1px;
  min-width: 0;
}

.name {
  overflow: hidden;
  font-size: 14px;
  font-weight: 600;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.meta,
.status {
  font-size: 12px;
  color: #a1a1aa;
}

.status {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.status.ready,
.status.done {
  color: #8fd14f;
}

.status.failed {
  color: #f87171;
}

.row-actions {
  display: flex;
  flex: none;
  padding-right: 6px;
}

.icon-button {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border: 0;
  border-radius: 8px;
  background: none;
  color: #a1a1aa;
  font-size: 18px;
  cursor: pointer;
}

.icon-button:hover:not(:disabled) {
  background: #27272a;
  color: #f4f4f5;
}

.icon-button:disabled {
  cursor: default;
  opacity: 0.4;
}

.list-hint {
  margin: 8px 0 0;
  font-size: 12px;
  color: #8e8e99;
}
</style>
