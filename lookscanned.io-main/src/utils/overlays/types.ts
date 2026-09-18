export interface OverlayConfig {
  watermarkText: string
  watermarkImage?: File
  stampImage?: File
  stampX: number
  stampY: number
  stampScale: number
}

export const defaultOverlayConfig: OverlayConfig = {
  watermarkText: '',
  stampX: 78,
  stampY: 82,
  stampScale: 0.22
}

export function hasOverlays(config: OverlayConfig): boolean {
  return Boolean(config.watermarkText.trim() || config.watermarkImage || config.stampImage)
}

export interface PdfMetadata {
  title?: string
  author?: string
  subject?: string
  keywords?: string
  producer?: string
  creator?: string
}

export const defaultPdfMetadata: PdfMetadata = {
  title: '',
  author: '',
  subject: '',
  keywords: '',
  producer: '',
  creator: ''
}
