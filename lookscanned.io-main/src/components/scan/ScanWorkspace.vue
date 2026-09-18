<template>
  <MainContainer>
    <n-grid x-gap="25" y-gap="25" :cols="12" item-responsive responsive="screen">
      <n-grid-item span="12 s:5 m:4 l:3">
        <n-space vertical>
          <FileUpload @update:file="onPickFile" />
          <PDFInfo :pdf="sourceFile" v-if="sourceFile" />
          <n-text v-if="converting" depth="3">{{ t('actions.converting') }}</n-text>

          <ScanSettingsCard v-model:config="config" />
          <SaveButtonCard
            @generate="generate"
            :progress="progress"
            :saving="saving || converting"
            :pdf="scannedPDF"
          />
          <ScanExtrasCard v-model:overlays="overlays" v-model:metadata="metadata" />
        </n-space>
      </n-grid-item>
      <n-grid-item span="12 s:7 m:8 l:9">
        <PreviewCompare
          :pdfRenderer="pdfRenderer"
          :scanRenderer="scanRenderer"
          :scale="config.scale"
        />
      </n-grid-item>
    </n-grid>
  </MainContainer>
</template>

<script lang="ts" setup>
import { NGrid, NGridItem, NSpace, NText, useMessage } from 'naive-ui'
import { computed, ref, watch } from 'vue'
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

const sourceFile = ref<File | undefined>(undefined)
const normalizedPdf = ref<File | undefined>(undefined)
const converting = ref(false)
const config = ref<ScanConfig>({ ...props.defaultConfig })
const overlays = ref<OverlayConfig>({ ...defaultOverlayConfig })
const metadata = ref({ ...defaultPdfMetadata })

const initExamplePDF = async () => {
  const response = await fetch(PDFURL)
  const blob = await response.blob()
  const file = new File([blob], 'example.pdf', { type: 'application/pdf' })
  if (!sourceFile.value) sourceFile.value = file
}

initExamplePDF()

async function onPickFile(file: File) {
  sourceFile.value = file
}

const convertToken = ref(0)

watch(
  sourceFile,
  async (file) => {
    const token = ++convertToken.value
    if (!file) {
      normalizedPdf.value = undefined
      return
    }
    converting.value = true
    try {
      const pdf = await normalizeToPdf(file)
      if (token !== convertToken.value) return
      normalizedPdf.value = pdf
    } catch (error) {
      if (token !== convertToken.value) return
      normalizedPdf.value = undefined
      message.error(t('actions.generateError') + (error as Error).message)
    } finally {
      if (token === convertToken.value) converting.value = false
    }
  }
)

const pdfRenderer = computed(() => {
  if (!normalizedPdf.value) return
  return new PDF(normalizedPdf.value)
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
const sourceForSave = computed(() => sourceFile.value)

const { save, progress, saving, scannedPDF } = useSaveScannedPDF(
  sourceForSave,
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
