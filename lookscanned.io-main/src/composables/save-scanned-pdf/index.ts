import type { Ref } from 'vue'
import { get } from '@vueuse/core'
import { ref, computed, watch, unref } from 'vue'
import { buildPDF, type PdfMetadata } from '@/utils/pdf-builder/pdf-lib/build-pdf'

interface PDFRenderer {
  renderPage(
    page: number,
    scale: number
  ): Promise<{
    blob: Blob
    height: number
    width: number
    ppi: number
  }>
  getNumPages(): Promise<number>
}

interface ScanRenderer {
  renderPage(image: Blob): Promise<{
    blob: Blob
  }>
}

export async function generateScannedPdf(options: {
  sourceName: string
  pdfRenderer: PDFRenderer
  scanRenderer: ScanRenderer
  scale: number
  metadata?: PdfMetadata
  onProgress?: (current: number, total: number) => void
}): Promise<File> {
  const numPages = await options.pdfRenderer.getNumPages()
  const pages = Array.from({ length: numPages }, (_, i) => i + 1)
  let finished = 0
  options.onProgress?.(0, numPages)

  const scanPages = []
  for (const page of pages) {
    const { blob: pdfPage, height, width } = await options.pdfRenderer.renderPage(page, options.scale)
    const { blob: scanPage } = await options.scanRenderer.renderPage(pdfPage)
    finished += 1
    options.onProgress?.(finished, numPages)
    scanPages.push({
      blob: scanPage,
      width,
      height,
      ppi: options.scale * 72
    })
  }

  const pdfDocument = await buildPDF(scanPages, options.metadata)
  const filename = `${options.sourceName.replace(/\.[^/.]+$/, '')}-scan.pdf`
  return new File([pdfDocument], filename, { type: 'application/pdf' })
}

export function useSaveScannedPDF(
  pdf: Ref<File | undefined>,
  pdfRenderer: Ref<PDFRenderer | undefined>,
  scanRenderer: Ref<ScanRenderer | undefined>,
  scale: Ref<number>,
  metadata?: Ref<PdfMetadata>
) {
  const finishedPages = ref(0)
  const totalPages = ref(0)
  const progress = computed(() => {
    if (totalPages.value === 0) return 0
    return finishedPages.value / totalPages.value
  })

  const saving = ref(false)
  const scannedPDF = ref<File | undefined>(undefined)

  const reset = () => {
    finishedPages.value = 0
    totalPages.value = 0
    scannedPDF.value = undefined
    saving.value = false
  }

  watch(pdfRenderer, reset)
  watch(scanRenderer, reset)
  watch(scale, reset)
  if (metadata) watch(metadata, reset, { deep: true })

  const save = async () => {
    try {
      finishedPages.value = 0
      totalPages.value = 0
      saving.value = true

      const renderer = get(pdfRenderer)
      const scan = get(scanRenderer)
      const scale_ = get(scale)
      const source = get(pdf)

      if (!renderer || !scan || !source) {
        throw new Error('No PDF or Scan Renderer')
      }

      const result = await generateScannedPdf({
        sourceName: source.name,
        pdfRenderer: renderer,
        scanRenderer: scan,
        scale: scale_,
        metadata: metadata ? unref(metadata) : undefined,
        onProgress: (current, total) => {
          finishedPages.value = current
          totalPages.value = total
        }
      })

      scannedPDF.value = result
      return result
    } catch (e) {
      console.error(e)
      throw e
    } finally {
      saving.value = false
    }
  }

  return { save, progress, saving, scannedPDF }
}
