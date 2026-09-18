import { imageToPdf } from './image-to-pdf'
import { textToPdf } from './text-to-pdf'

function extensionOf(file: File): string {
  const fromName = file.name.split('.').pop()?.toLowerCase()
  return fromName ?? ''
}

const IMAGE_EXT = new Set(['jpg', 'jpeg', 'png', 'webp', 'gif', 'svg', 'bmp'])

async function htmlToText(file: File): Promise<string> {
  const html = await file.text()
  const doc = new DOMParser().parseFromString(html, 'text/html')
  return (doc.body?.innerText || doc.documentElement.textContent || '').trim()
}

async function docxToText(file: File): Promise<string> {
  const mammoth = await import('mammoth')
  const result = await mammoth.extractRawText({ arrayBuffer: await file.arrayBuffer() })
  return result.value.trim()
}

async function spreadsheetToText(file: File): Promise<string> {
  const XLSX = await import('xlsx')
  const workbook = XLSX.read(await file.arrayBuffer(), { type: 'array' })
  const parts: string[] = []
  for (const name of workbook.SheetNames) {
    const sheet = workbook.Sheets[name]
    if (!sheet) continue
    const csv = XLSX.utils.sheet_to_csv(sheet)
    parts.push(workbook.SheetNames.length > 1 ? `${name}\n${csv}` : csv)
  }
  return parts.join('\n\n').trim()
}

export function isSupportedSourceFile(file: File): boolean {
  const ext = extensionOf(file)
  if (file.type === 'application/pdf' || ext === 'pdf') return true
  if (IMAGE_EXT.has(ext) || file.type.startsWith('image/')) return true
  return ['txt', 'md', 'markdown', 'html', 'htm', 'docx', 'xlsx', 'xls', 'csv'].includes(ext)
}

export async function normalizeToPdf(file: File): Promise<File> {
  const ext = extensionOf(file)
  if (file.type === 'application/pdf' || ext === 'pdf') return file
  if (IMAGE_EXT.has(ext) || file.type.startsWith('image/')) return imageToPdf(file)

  if (ext === 'docx') {
    const text = await docxToText(file)
    if (!text) throw new Error('This Word file has no readable text')
    return textToPdf(text, file.name)
  }

  if (ext === 'xlsx' || ext === 'xls' || ext === 'csv') {
    const text = await spreadsheetToText(file)
    if (!text) throw new Error('This spreadsheet is empty')
    return textToPdf(text, file.name)
  }

  if (ext === 'html' || ext === 'htm') {
    const text = await htmlToText(file)
    if (!text) throw new Error('This HTML file has no readable text')
    return textToPdf(text, file.name)
  }

  if (ext === 'txt' || ext === 'md' || ext === 'markdown' || file.type.startsWith('text/')) {
    return textToPdf(await file.text(), file.name)
  }

  throw new Error('This file type is not supported yet')
}
