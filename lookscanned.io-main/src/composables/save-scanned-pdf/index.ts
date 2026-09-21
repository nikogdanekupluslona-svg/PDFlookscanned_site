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
