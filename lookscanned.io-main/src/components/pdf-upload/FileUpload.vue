<template>
  <!-- A real <input> inside a <label> opens the native picker in every browser, including Safari -->
  <label v-if="compact" class="compact-button">
    <input
      ref="input"
      class="visually-hidden"
      type="file"
      :accept="ACCEPT"
      :multiple="multiple"
      @change="onChange"
    />
    <n-icon :component="ArrowSync16Regular" />
    <span>{{ multiple ? t('upload.addMore') : t('upload.replace') }}</span>
  </label>

  <label v-else class="dropzone" :class="{ dragging: pageDragging }">
    <input
      ref="input"
      class="visually-hidden"
      type="file"
      :accept="ACCEPT"
      :multiple="multiple"
      @change="onChange"
    />
    <n-icon class="upload-icon" :component="CloudArrowUp24Regular" />
    <span class="title">{{ multiple ? t('upload.dropTitleMany') : t('upload.dropTitle') }}</span>
    <span class="or">{{ t('upload.or') }}</span>
    <span class="choose">{{ multiple ? t('upload.chooseMany') : t('upload.choose') }}</span>
    <span class="hint">{{ t('settings.supportedHint') }}</span>
    <span class="privacy">
      <n-icon :component="LockClosed16Regular" />
      {{ t('upload.privacy') }}
    </span>
  </label>

  <Teleport to="body">
    <div v-if="pageDragging" class="page-drop-overlay">
      <div class="page-drop-box">
        <n-icon class="upload-icon" :component="CloudArrowUp24Regular" />
        <span>{{ multiple ? t('upload.dropOverlayMany') : t('upload.dropOverlay') }}</span>
      </div>
    </div>
  </Teleport>
</template>

<script lang="ts" setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { NIcon, useMessage } from 'naive-ui'
import { ArrowSync16Regular, CloudArrowUp24Regular, LockClosed16Regular } from '@vicons/fluent'
import { useI18n } from 'vue-i18n'
import { isSupportedSourceFile } from '@/utils/document-source/normalize-to-pdf'

const ACCEPT = [
  'application/pdf',
  'image/*',
  '.pdf',
  '.jpg',
  '.jpeg',
  '.png',
  '.webp',
  '.gif',
  '.svg',
  '.bmp',
  '.txt',
  '.md',
  '.html',
  '.htm',
  '.docx',
  '.xlsx',
  '.xls',
  '.csv'
].join(',')

const { t } = useI18n()
const message = useMessage()

const props = defineProps<{
  multiple?: boolean
  compact?: boolean
}>()

const emit = defineEmits<{
  (e: 'update:file', file: File): void
  (e: 'update:files', files: File[]): void
}>()

const input = ref<HTMLInputElement>()
const pageDragging = ref(false)
let dragDepth = 0

function emitFiles(files: File[]) {
  const accepted = files.filter(isSupportedSourceFile)
  const rejected = files.filter((file) => !isSupportedSourceFile(file))
  if (rejected.length) {
    message.error(t('upload.unsupported', { name: rejected.map((file) => file.name).join(', ') }), {
      duration: 6000
    })
  }
  if (!accepted.length) return
  if (props.multiple) emit('update:files', accepted)
  else emit('update:file', accepted[0])
}

function onChange() {
  const files = Array.from(input.value?.files ?? [])
  // Clear the value so choosing the same file again still fires "change"
  if (input.value) input.value.value = ''
  if (files.length) emitFiles(files)
}

function hasFiles(event: DragEvent) {
  return Array.from(event.dataTransfer?.types ?? []).includes('Files')
}

// The whole page is a drop target: a file dropped anywhere is picked up
// instead of the browser navigating away to open it.
function onDragEnter(event: DragEvent) {
  if (!hasFiles(event)) return
  event.preventDefault()
  dragDepth += 1
  pageDragging.value = true
}

function onDragOver(event: DragEvent) {
  if (!hasFiles(event)) return
  event.preventDefault()
  if (event.dataTransfer) event.dataTransfer.dropEffect = 'copy'
}

function onDragLeave(event: DragEvent) {
  if (!hasFiles(event)) return
  dragDepth = Math.max(0, dragDepth - 1)
  if (dragDepth === 0) pageDragging.value = false
}

function onDrop(event: DragEvent) {
  if (!hasFiles(event)) return
  event.preventDefault()
  dragDepth = 0
  pageDragging.value = false
  const list = event.dataTransfer?.files
  if (list?.length) emitFiles(Array.from(list))
}

onMounted(() => {
  window.addEventListener('dragenter', onDragEnter)
  window.addEventListener('dragover', onDragOver)
  window.addEventListener('dragleave', onDragLeave)
  window.addEventListener('drop', onDrop)
})

onBeforeUnmount(() => {
  window.removeEventListener('dragenter', onDragEnter)
  window.removeEventListener('dragover', onDragOver)
  window.removeEventListener('dragleave', onDragLeave)
  window.removeEventListener('drop', onDrop)
})
</script>

<style scoped>
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.dropzone {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 28px 18px 22px;
  border: 2px dashed #8fd14f;
  border-radius: 12px;
  background: rgba(143, 209, 79, 0.06);
  color: #f4f4f5;
  text-align: center;
  cursor: pointer;
  transition:
    background 0.15s,
    border-color 0.15s;
}

.dropzone:hover,
.dropzone.dragging {
  background: rgba(143, 209, 79, 0.14);
}

.dropzone:focus-within {
  outline: 2px solid #8fd14f;
  outline-offset: 3px;
}

.upload-icon {
  font-size: 44px;
  color: #8fd14f;
}

.title {
  font-size: 16px;
  font-weight: 600;
}

.or {
  font-size: 12px;
  color: #8e8e99;
}

.choose {
  display: inline-flex;
  align-items: center;
  min-height: 40px;
  padding: 0 20px;
  border-radius: 999px;
  background: #8fd14f;
  color: #10200a;
  font-weight: 700;
}

.hint {
  margin-top: 6px;
  font-size: 12px;
  line-height: 1.4;
  color: #a1a1aa;
}

.privacy {
  font-size: 12px;
  line-height: 1.5;
  color: #8e8e99;
}

.privacy .n-icon {
  margin-right: 4px;
  vertical-align: -2px;
}

.compact-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 34px;
  padding: 0 14px;
  border: 1px solid #3f3f46;
  border-radius: 999px;
  color: #f4f4f5;
  font-size: 13px;
  cursor: pointer;
}

.compact-button:hover {
  border-color: #8fd14f;
}

.compact-button:focus-within {
  outline: 2px solid #8fd14f;
  outline-offset: 2px;
}

.page-drop-overlay {
  position: fixed;
  inset: 0;
  z-index: 3000;
  display: grid;
  place-items: center;
  padding: 16px;
  background: rgba(11, 11, 15, 0.82);
  pointer-events: none;
}

.page-drop-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  width: min(520px, 100%);
  padding: 56px 24px;
  border: 3px dashed #8fd14f;
  border-radius: 20px;
  color: #f4f4f5;
  font-size: 20px;
  font-weight: 600;
  text-align: center;
}

.page-drop-box .upload-icon {
  font-size: 64px;
}
</style>
