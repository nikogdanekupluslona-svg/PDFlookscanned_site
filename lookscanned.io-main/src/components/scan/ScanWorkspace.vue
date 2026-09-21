<template>
  <MainContainer>
    <ol class="stepper">
      <li :class="{ done: hasOwnFile }">
        <span class="num">1</span>{{ t('steps.upload') }}
      </li>
      <li :class="{ done: hasOwnFile }">
        <span class="num">2</span>{{ t('steps.adjust') }}
      </li>
      <li :class="{ done: Boolean(scannedPDF) }">
        <span class="num">3</span>{{ t('steps.download') }}
      </li>
    </ol>

    <n-grid x-gap="25" y-gap="25" :cols="12" item-responsive responsive="screen">
      <n-grid-item span="12 s:5 m:4 l:4">
        <n-space vertical :size="16">
          <n-card size="small">
            <h2 class="step-title"><span class="num">1</span>{{ t('steps.uploadTitle') }}</h2>
            <FileUpload v-if="!hasOwnFile" @update:file="onPickFile" />
            <PDFInfo v-else :pdf="sourceFile!" :pages="numPages" :loading="converting">
              <FileUpload compact @update:file="onPickFile" />
            </PDFInfo>
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
          <n-card size="small" class="download-card" :class="{ ready: Boolean(scannedPDF) }">
            <h2 class="step-title"><span class="num">3</span>{{ t('steps.downloadTitle') }}</h2>
            <SaveButtonCard
              @generate="generate"
              :progress="progress"
              :finished-pages="finishedPages"
              :total-pages="totalPages"
              :saving="saving"
              :disabled="converting || !pdfRenderer"
              :sample="isSample"
              :pdf="scannedPDF"
            />
          </n-card>

          <div v-if="isSample" class="sample-banner">
            <n-icon :component="Info16Regular" />
            <span>{{ t('upload.sampleBanner') }}</span>
          </div>

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
import { computed, ref, shallowRef, watch } from 'vue'
import { useHead } from '@unhead/vue'
import { useI18n } from 'vue-i18n'
import MainContainer from '@/components/MainContainer.vue'
import FileUpload from '@/components/pdf-upload/FileUpload.vue'
import PDFInfo from '@/components/pdf-upload/PDFInfo.vue'
import ScanSettingsCard from '@/components/scan-settings/ScanSettingsCard.vue'
import ScanExtrasCard from '@/components/scan-settings/ScanExtrasCard.vue'
import PreviewCompare from '@/components/page-preview/PreviewCompare.vue'
import SaveButtonCard from '@/components/save-button/SaveButtonCard.vue'
import PDFURL from '@/assets/examples/pdfs/test.pdf'
import { PDF } from '@/utils/pdf-renderer/pdfjs'
import { ScanCacher } from '@/utils/scan-renderer/scan-cacher'
import { OverlayScanner } from '@/utils/overlays/overlay-scanner'
import {
  defaultOverlayConfig,
  defaultPdfMetadata,
  type OverlayConfig
} from '@/utils/overlays/types'
import { useSaveScannedPDF } from '@/composables/save-scanned-pdf'
import { normalizeToPdf } from '@/utils/document-source/normalize-to-pdf'
import type { ScanConfig } from '@/utils/scan-renderer'
import type { ScanRenderer } from '@/utils/scan-renderer'

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

const sampleFile = shallowRef<File | undefined>(undefined)
const sourceFile = shallowRef<File | undefined>(undefined)
const pdfRenderer = shallowRef<PDF | undefined>(undefined)
const numPages = ref<number | undefined>(undefined)
const converting = ref(false)
const config = ref<ScanConfig>({ ...props.defaultConfig })
const overlays = ref<OverlayConfig>({ ...defaultOverlayConfig })
const metadata = ref({ ...defaultPdfMetadata })

const isSample = computed(() => !sourceFile.value || sourceFile.value === sampleFile.value)
const hasOwnFile = computed(() => !isSample.value)

// A sample document fills the preview until the visitor uploads their own file
const initExamplePDF = async () => {
  const response = await fetch(PDFURL)
  const blob = await response.blob()
  const file = new File([blob], 'sample.pdf', { type: 'application/pdf' })
  sampleFile.value = file
  if (!sourceFile.value) sourceFile.value = file
}

initExamplePDF()

function onPickFile(file: File) {
  sourceFile.value = file
}

let convertToken = 0

watch(sourceFile, async (file) => {
  const token = ++convertToken
  if (!file) {
    pdfRenderer.value = undefined
    numPages.value = undefined
    return
  }
  converting.value = true
  numPages.value = undefined
  // Drop the previous document right away so its preview and result are never shown for the new file
  pdfRenderer.value = undefined
  try {
    const pdf = await normalizeToPdf(file)
    const renderer = new PDF(pdf)
    // Opening the document up front catches broken or password-protected files
    const pages = await renderer.getNumPages()
    if (token !== convertToken) return
    pdfRenderer.value = renderer
    numPages.value = pages
  } catch (error) {
    if (token !== convertToken) return
    console.error(error)
    message.error(t('upload.readError', { name: file.name, error: (error as Error).message }), {
      duration: 8000
    })
    // Fall back to the sample so the page never ends up empty
    if (file !== sampleFile.value) sourceFile.value = sampleFile.value
  } finally {
    if (token === convertToken) converting.value = false
  }
})

const cachedScanner = ref<ScanRenderer>(new ScanCacher(props.createScanner(config.value)))

watch(
  config,
  (scanConfig) => {
    cachedScanner.value = new ScanCacher(props.createScanner(scanConfig))
  },
  { deep: true }
)

const scanRenderer = computed(() => new OverlayScanner(cachedScanner.value, overlays.value))

const scale = computed(() => config.value.scale)

const { save, progress, finishedPages, totalPages, saving, scannedPDF } = useSaveScannedPDF(
  sourceFile,
  pdfRenderer,
  scanRenderer,
  scale,
  metadata
)

const generate = async () => {
  try {
    await save()
    message.success(t('actions.generateSuccess'))
  } catch (e) {
    message.error(t('actions.generateError') + (e as Error).message)
  }
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
