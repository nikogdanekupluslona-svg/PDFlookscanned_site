<template>
  <MainContainer>
    <ol class="stepper">
      <li :class="{ done: items.length > 0 }">
        <span class="num">1</span>{{ t('steps.upload') }}
      </li>
      <li :class="{ done: items.length > 0 }">
        <span class="num">2</span>{{ t('steps.adjust') }}
      </li>
      <li :class="{ done: Boolean(output) }">
        <span class="num">3</span>{{ t('steps.download') }}
      </li>
    </ol>

    <n-grid x-gap="25" y-gap="25" :cols="12" item-responsive responsive="screen">
      <n-grid-item span="12 s:5 m:4 l:4">
        <n-space vertical :size="16">
          <n-card size="small">
            <h2 class="step-title"><span class="num">1</span>{{ t('steps.uploadTitle') }}</h2>
            <FileUpload v-if="!items.length" multiple @update:files="addFiles" />
            <template v-else>
              <FileList
                :items="listItems"
                :active-id="activeId"
                :busy="busy"
                @select="activeId = $event"
                @remove="removeFile"
                @download="downloadOne"
              />
              <div class="add-more">
                <FileUpload compact multiple @update:files="addFiles" />
              </div>
            </template>
          </n-card>

          <div>
            <h2 class="step-title outside"><span class="num">2</span>{{ t('steps.adjustTitle') }}</h2>
            <ScanSettingsCard v-model:config="config" />
          </div>
          <ScanExtrasCard v-model:overlays="overlays" v-model:metadata="metadata" />
        </n-space>
      </n-grid-item>

      <n-grid-item span="12 s:7 m:8 l:8">
        <n-space vertical :size="16">
          <n-card size="small" class="download-card" :class="{ ready: Boolean(output) }">
            <h2 class="step-title"><span class="num">3</span>{{ t('steps.downloadTitle') }}</h2>
            <SaveButtonCard
              :count="loading ? 0 : pendingItems.length"
              :loading="loading"
              :busy="busy"
              :progress="progress"
              :progress-text="progressText"
              :output="outputInfo"
              @generate="generate"
              @download="downloadOutput"
            />
          </n-card>

          <div v-if="!items.length" class="sample-banner">
            <n-icon :component="Info16Regular" />
            <span>{{ t('upload.sampleBanner') }}</span>
          </div>
          <p v-else-if="activeItem" class="preview-of">
            {{ t('files.previewOf', { name: activeItem.file.name }) }}
          </p>

          <PreviewCompare
            :pdfRenderer="pdfRenderer"
            :scanRenderer="scanRenderer"
            :scale="config.scale"
          />
        </n-space>
      </n-grid-item>
    </n-grid>
  </MainContainer>
</template>

<script lang="ts" setup>
import { NCard, NGrid, NGridItem, NIcon, NSpace, useMessage } from 'naive-ui'
import { Info16Regular } from '@vicons/fluent'
import { computed, markRaw, ref, shallowRef, watch } from 'vue'
import { useHead } from '@unhead/vue'
import { useI18n } from 'vue-i18n'
import MainContainer from '@/components/MainContainer.vue'
import FileUpload from '@/components/pdf-upload/FileUpload.vue'
import FileList, { type FileListItem, type FileStatus } from '@/components/pdf-upload/FileList.vue'
import ScanSettingsCard from '@/components/scan-settings/ScanSettingsCard.vue'
import ScanExtrasCard from '@/components/scan-settings/ScanExtrasCard.vue'
import PreviewCompare from '@/components/page-preview/PreviewCompare.vue'
import SaveButtonCard, { type SaveOutput } from '@/components/save-button/SaveButtonCard.vue'
import PDFURL from '@/assets/examples/pdfs/test.pdf'
import { PDF } from '@/utils/pdf-renderer/pdfjs'
import { ScanCacher } from '@/utils/scan-renderer/scan-cacher'
import { OverlayScanner } from '@/utils/overlays/overlay-scanner'
import {
  defaultOverlayConfig,
  defaultPdfMetadata,
  type OverlayConfig
} from '@/utils/overlays/types'
import { generateScannedPdf } from '@/composables/save-scanned-pdf'
import { normalizeToPdf } from '@/utils/document-source/normalize-to-pdf'
import { downloadFile } from '@/utils/download-file'
import { zipFiles } from '@/utils/zip-files'
import type { ScanConfig } from '@/utils/scan-renderer'
import type { ScanRenderer } from '@/utils/scan-renderer'

interface SourceItem {
  id: string
  file: File
  status: FileStatus
  pages?: number
  renderer?: PDF
  result?: File
  error?: string
}

const props = defineProps<{
  pageTitle: string
  defaultConfig: ScanConfig
  createScanner: (config: ScanConfig) => ScanRenderer
}>()

const { t } = useI18n()
const message = useMessage()

useHead({
  title: props.pageTitle + ' - ' + t('base.title'),
  meta: [{ name: 'description', content: t('base.description') }]
})

const config = ref<ScanConfig>({ ...props.defaultConfig })
const overlays = ref<OverlayConfig>({ ...defaultOverlayConfig })
const metadata = ref({ ...defaultPdfMetadata })

const items = ref<SourceItem[]>([])
const activeId = ref<string>()
const busy = ref(false)
const output = shallowRef<File>()
const outputCount = ref(0)
const progressState = ref({ file: 0, files: 0, page: 0, pages: 0 })

// A sample document fills the preview until the visitor uploads their own files
const sampleRenderer = shallowRef<PDF>()
fetch(PDFURL)
  .then((response) => response.blob())
  .then((blob) => {
    sampleRenderer.value = markRaw(new PDF(new File([blob], 'sample.pdf', { type: 'application/pdf' })))
  })

const activeItem = computed(() => items.value.find((item) => item.id === activeId.value))
const pdfRenderer = computed(() =>
  items.value.length ? activeItem.value?.renderer : sampleRenderer.value
)

const loading = computed(() => items.value.some((item) => item.status === 'loading'))
// Everything that opened fine and has no result for the current settings yet
const pendingItems = computed(() => items.value.filter((item) => item.renderer && !item.result))

const listItems = computed<FileListItem[]>(() =>
  items.value.map((item) => ({
    id: item.id,
    name: item.file.name,
    size: item.file.size,
    pages: item.pages,
    status: item.status,
    error: item.error,
    hasResult: Boolean(item.result)
  }))
)

const outputInfo = computed<SaveOutput | undefined>(() =>
  output.value
    ? { name: output.value.name, size: output.value.size, count: outputCount.value }
    : undefined
)

const progress = computed(() => {
  const { file, files, page, pages } = progressState.value
  if (!files) return 0
  return (file - 1 + (pages ? page / pages : 0)) / files
})

const progressText = computed(() => {
  const { file, files, page, pages } = progressState.value
  if (!files) return ''
  const pageText = pages ? t('save.progress', { current: page, total: pages }) : ''
  return files > 1 ? `${t('save.fileProgress', { current: file, total: files })} · ${pageText}` : pageText
})

let nextId = 0
let loadQueue = Promise.resolve()

function findItem(id: string) {
  return items.value.find((item) => item.id === id)
}

function addFiles(files: File[]) {
  const added = files.map((file) => ({
    id: String(++nextId),
    // Blobs must stay raw: a reactive proxy breaks file.arrayBuffer() and friends
    file: markRaw(file),
    status: 'loading' as const
  }))
  items.value.push(...added)
  output.value = undefined
  if (!activeItem.value) activeId.value = added[0]?.id
  // Convert one file at a time so large Word or Excel files do not freeze the tab
  for (const item of added) loadQueue = loadQueue.then(() => loadItem(item.id))
}

async function loadItem(id: string) {
  const item = findItem(id)
  if (!item) return
  try {
    const pdf = await normalizeToPdf(item.file)
    const renderer = markRaw(new PDF(pdf))
    // Opening the document up front catches broken or password-protected files
    const pages = await renderer.getNumPages()
    const current = findItem(id)
    if (!current) return
    current.renderer = renderer
    current.pages = pages
    current.status = 'ready'
  } catch (error) {
    console.error(error)
    const current = findItem(id)
    if (!current) return
    current.status = 'failed'
    current.error = t('files.openError')
    message.error(
      t('upload.readError', { name: current.file.name, error: (error as Error).message }),
      { duration: 8000 }
    )
    if (activeId.value === id) activeId.value = items.value.find((other) => other.renderer)?.id ?? id
  }
}

function removeFile(id: string) {
  items.value = items.value.filter((item) => item.id !== id)
  output.value = undefined
  if (activeId.value === id) activeId.value = items.value[0]?.id
}

const cachedScanner = ref<ScanRenderer>(new ScanCacher(props.createScanner(config.value)))

watch(
  config,
  (scanConfig) => {
    cachedScanner.value = new ScanCacher(props.createScanner(scanConfig))
  },
  { deep: true }
)

const scanRenderer = computed(() => new OverlayScanner(cachedScanner.value, overlays.value))

// Results made with old settings are stale: drop them so the next run redoes every file
watch(
  [config, overlays, metadata],
  () => {
    if (busy.value) return
    for (const item of items.value) {
      item.result = undefined
      if (item.status === 'done') item.status = 'ready'
    }
    output.value = undefined
  },
  { deep: true }
)

async function generate() {
  const queue = pendingItems.value
  if (!queue.length || busy.value) return
  busy.value = true
  output.value = undefined
  const scanner = scanRenderer.value
  const scale = config.value.scale
  const meta = { ...metadata.value }
  let failures = 0

  for (const [index, item] of queue.entries()) {
    progressState.value = { file: index + 1, files: queue.length, page: 0, pages: item.pages ?? 0 }
    item.status = 'processing'
    item.error = undefined
    try {
      const result = await generateScannedPdf({
        sourceName: item.file.name,
        pdfRenderer: item.renderer!,
        scanRenderer: scanner,
        scale,
        metadata: meta,
        onProgress: (page, pages) => {
          progressState.value = { ...progressState.value, page, pages }
        }
      })
      item.result = markRaw(result)
      item.status = 'done'
    } catch (error) {
      console.error(error)
      failures += 1
      item.status = 'failed'
      item.error = (error as Error).message
    }
  }

  const results = items.value.map((item) => item.result).filter(Boolean) as File[]
  try {
    if (results.length === 1) {
      output.value = results[0]
    } else if (results.length > 1) {
      const zip = await zipFiles(results)
      output.value = markRaw(new File([zip], 'scanned-pdfs.zip', { type: 'application/zip' }))
    }
    outputCount.value = results.length
  } finally {
    busy.value = false
    progressState.value = { file: 0, files: 0, page: 0, pages: 0 }
  }

  if (failures) message.error(t('save.someFailed', { n: failures }, failures))
  if (output.value) {
    // Start the download right away: the visitor does not need a second click
    downloadOutput()
    message.success(t('save.downloadStarted'))
  }
}

function downloadOutput() {
  if (output.value) downloadFile(output.value, output.value.name)
}

function downloadOne(id: string) {
  const result = findItem(id)?.result
  if (result) downloadFile(result, result.name)
}
</script>

<style scoped>
.stepper {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 28px;
  margin: 8px 0 20px;
  padding: 0;
  list-style: none;
  color: #a1a1aa;
  font-size: 14px;
}

.stepper li {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.num {
  display: inline-grid;
  place-items: center;
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #27272a;
  color: #f4f4f5;
  font-size: 13px;
  font-weight: 700;
}

.stepper li.done {
  color: #f4f4f5;
}

.stepper li.done .num,
.step-title .num {
  background: #8fd14f;
  color: #10200a;
}

.step-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font-size: 16px;
  font-weight: 600;
  color: #f4f4f5;
}

.step-title.outside {
  margin: 4px 0 10px;
}

.download-card.ready {
  border-color: #8fd14f;
}

.add-more {
  margin-top: 12px;
}

.preview-of {
  margin: 0;
  font-size: 13px;
  color: #a1a1aa;
  overflow-wrap: anywhere;
}

.sample-banner {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  padding: 10px 14px;
  border: 1px solid #3f3f46;
  border-radius: 8px;
  background: #18181b;
  color: #d4d4d8;
  font-size: 13px;
  line-height: 1.5;
}

.sample-banner .n-icon {
  flex: none;
  margin-top: 3px;
  color: #8fd14f;
}
</style>
