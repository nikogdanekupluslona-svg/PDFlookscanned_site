<template>
  <n-card>
    <div
      class="dropzone"
      :class="{ dragging }"
      @dragenter.prevent="dragging = true"
      @dragover.prevent="dragging = true"
      @dragleave.prevent="dragging = false"
      @drop.prevent="onDrop"
      @click="onClick"
    >
      <n-button text>
        <template #icon>
          <n-icon>
            <FolderOpen16Regular />
          </n-icon>
        </template>
        <n-text>
          {{ multiple ? t('actions.addFiles') : t('settings.pdfSelectLabel') }}
        </n-text>
      </n-button>
      <p class="hint">{{ t('settings.supportedHint') }}</p>
    </div>
  </n-card>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { NButton, NIcon, NText, NCard } from 'naive-ui'
import { FolderOpen16Regular } from '@vicons/fluent'
import { fileOpen } from 'browser-fs-access'
import { useI18n } from 'vue-i18n'
import { isSupportedSourceFile } from '@/utils/document-source/normalize-to-pdf'

const { t } = useI18n()
const dragging = ref(false)

const props = defineProps<{
  multiple?: boolean
}>()

const emit = defineEmits<{
  (e: 'update:file', file: File): void
  (e: 'update:files', files: File[]): void
}>()

const pickerOptions = {
  description: 'Documents',
  mimeTypes: [
    'application/pdf',
    'image/*',
    'text/plain',
    'text/markdown',
    'text/html',
    'text/csv',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.ms-excel'
  ],
  extensions: [
    '.pdf',
    '.jpg',
    '.jpeg',
    '.png',
    '.webp',
    '.gif',
    '.svg',
    '.txt',
    '.md',
    '.html',
    '.htm',
    '.docx',
    '.xlsx',
    '.xls',
    '.csv'
  ]
}

function emitFiles(files: File[]) {
  const accepted = files.filter(isSupportedSourceFile)
  if (!accepted.length) return
  if (props.multiple) emit('update:files', accepted)
  else emit('update:file', accepted[0])
}

async function onClick() {
  const result = await fileOpen({
    ...pickerOptions,
    multiple: Boolean(props.multiple)
  })
  const files = Array.isArray(result) ? result : [result]
  emitFiles(files)
}

function onDrop(event: DragEvent) {
  dragging.value = false
  const list = event.dataTransfer?.files
  if (!list?.length) return
  emitFiles(Array.from(list))
}
</script>

<style scoped>
.dropzone {
  cursor: pointer;
  border-radius: 8px;
  padding: 8px 4px;
}

.dropzone.dragging {
  outline: 1px dashed var(--n-color-target);
}

.hint {
  margin: 6px 0 0;
  font-size: 12px;
  opacity: 0.7;
  line-height: 1.4;
}
</style>
