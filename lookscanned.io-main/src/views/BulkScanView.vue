<template>
  <MainContainer>
    <n-grid x-gap="25" y-gap="25" :cols="12" item-responsive responsive="screen">
      <n-grid-item span="12 s:5 m:4 l:3">
        <n-space vertical>
          <FileUpload multiple @update:files="onAddFiles" />
          <ScanSettingsCard v-model:config="config" />
          <n-card>
            <n-space>
              <n-button type="primary" :disabled="!items.length || busy" @click="processAll">
                {{ t('actions.processAll') }}
              </n-button>
              <n-button :disabled="!doneFiles.length || busy" @click="downloadZip">
                {{ t('actions.downloadZip') }}
              </n-button>
            </n-space>
            <n-progress
              v-if="busy"
              type="line"
              :percentage="Math.round(progress * 100)"
              style="margin-top: 12px"
            />
          </n-card>
          <ScanExtrasCard v-model:overlays="overlays" v-model:metadata="metadata" />
        </n-space>
      </n-grid-item>
      <n-grid-item span="12 s:7 m:8 l:9">
        <n-card>
          <n-empty v-if="!items.length" :description="t('settings.pdfNoSelectMessage')" />
          <n-space v-else vertical>
            <div v-for="item in items" :key="item.id" class="row">
              <div>
                <strong>{{ item.file.name }}</strong>
                <p class="status">{{ statusLabel(item) }}</p>
              </div>
              <n-button v-if="item.result" size="small" @click="downloadOne(item.result)">
                {{ t('actions.downloadScannedPDF') }}
              </n-button>
            </div>
          </n-space>
        </n-card>
      </n-grid-item>
    </n-grid>
  </MainContainer>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
import { useHead } from '@unhead/vue'
import { useI18n } from 'vue-i18n'
import {
  NGrid,
  NGridItem,
  NSpace,
  NCard,
  NButton,
  NProgress,
  NEmpty,
  useMessage
} from 'naive-ui'
import { fileSave } from 'browser-fs-access'
import MainContainer from '@/components/MainContainer.vue'
import FileUpload from '@/components/pdf-upload/FileUpload.vue'
import ScanSettingsCard from '@/components/scan-settings/ScanSettingsCard.vue'
import ScanExtrasCard from '@/components/scan-settings/ScanExtrasCard.vue'
import { defaultConfig, CanvasScanner, featureDetect } from '@/utils/scan-renderer/canvas-scan'
import { MagicaScanner } from '@/utils/scan-renderer/magica-scan'
import { PDF } from '@/utils/pdf-renderer/pdfjs'
import { OverlayScanner } from '@/utils/overlays/overlay-scanner'
import {
  defaultOverlayConfig,
  defaultPdfMetadata,
  type OverlayConfig
} from '@/utils/overlays/types'
import { generateScannedPdf } from '@/composables/save-scanned-pdf'
import { normalizeToPdf } from '@/utils/document-source/normalize-to-pdf'
import type { ScanConfig, ScanRenderer } from '@/utils/scan-renderer'

type Status = 'queued' | 'processing' | 'done' | 'failed'

interface BatchItem {
  id: string
  file: File
  status: Status
  error?: string
  result?: File
}

const { t } = useI18n()
const message = useMessage()

useHead({
  title: t('base.bulkTitle') + ' - ' + t('base.title'),
  meta: [{ name: 'description', content: t('base.description') }]
})

const config = ref<ScanConfig>({ ...defaultConfig })
const overlays = ref<OverlayConfig>({ ...defaultOverlayConfig })
const metadata = ref({ ...defaultPdfMetadata })
const items = ref<BatchItem[]>([])
const busy = ref(false)
const finished = ref(0)
const total = ref(0)
const progress = computed(() => (total.value ? finished.value / total.value : 0))
const doneFiles = computed(() => items.value.map((item) => item.result).filter(Boolean) as File[])

function createScanner(scanConfig: ScanConfig): ScanRenderer {
  return featureDetect() ? new CanvasScanner(scanConfig) : new MagicaScanner(scanConfig)
}

function onAddFiles(files: File[]) {
  const next = files.map((file) => ({
    id: `${file.name}-${file.size}-${file.lastModified}-${Math.random().toString(16).slice(2)}`,
    file,
    status: 'queued' as const
  }))
  items.value = [...items.value, ...next]
}

function statusLabel(item: BatchItem) {
  if (item.status === 'failed') return `${t('actions.failed')}: ${item.error ?? ''}`
  if (item.status === 'processing') return t('actions.generating')
  if (item.status === 'done') return t('actions.done')
  return t('actions.queued')
}

async function processAll() {
  busy.value = true
  finished.value = 0
  total.value = items.value.length
  const scanner = new OverlayScanner(createScanner(config.value), overlays.value)

  for (const item of items.value) {
    if (item.status === 'done' && item.result) {
      finished.value += 1
      continue
    }
    item.status = 'processing'
    item.error = undefined
    try {
      const pdfFile = await normalizeToPdf(item.file)
      const renderer = new PDF(pdfFile)
      item.result = await generateScannedPdf({
        sourceName: item.file.name,
        pdfRenderer: renderer,
        scanRenderer: scanner,
        scale: config.value.scale,
        metadata: metadata.value
      })
      item.status = 'done'
    } catch (error) {
      item.status = 'failed'
      item.error = (error as Error).message
    }
    finished.value += 1
  }

  busy.value = false
  const failures = items.value.filter((item) => item.status === 'failed').length
  if (failures) message.error(t('actions.generateError') + failures)
  else message.success(t('actions.generateSuccess'))
}

async function downloadOne(file: File) {
  await fileSave(file, {
    fileName: file.name,
    extensions: ['.pdf'],
    mimeTypes: ['application/pdf'],
    startIn: 'downloads',
    description: 'PDF File',
    id: 'pdflookscanned'
  })
}

async function downloadZip() {
  const JSZip = (await import('jszip')).default
  const zip = new JSZip()
  for (const file of doneFiles.value) {
    zip.file(file.name, await file.arrayBuffer())
  }
  const blob = await zip.generateAsync({ type: 'blob' })
  await fileSave(blob, {
    fileName: 'scanned-pdfs.zip',
    extensions: ['.zip'],
    mimeTypes: ['application/zip'],
    startIn: 'downloads',
    description: 'ZIP File',
    id: 'pdflookscanned-zip'
  })
}
</script>

<style scoped>
.row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.status {
  margin: 4px 0 0;
  font-size: 12px;
  opacity: 0.7;
}
</style>
