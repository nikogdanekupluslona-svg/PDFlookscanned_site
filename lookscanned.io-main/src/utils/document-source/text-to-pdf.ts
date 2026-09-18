import { PDFDocument, StandardFonts, rgb } from 'pdf-lib'

const PAGE_WIDTH = 595.28
const PAGE_HEIGHT = 841.89
const MARGIN = 54
const FONT_SIZE = 11
const LINE_HEIGHT = 15

function wrapLine(text: string, measure: (value: string) => number, maxWidth: number): string[] {
  if (!text) return ['']
  const words = text.split(/\s+/)
  const lines: string[] = []
  let current = ''
  for (const word of words) {
    const next = current ? `${current} ${word}` : word
    if (measure(next) <= maxWidth) {
      current = next
      continue
    }
    if (current) lines.push(current)
    if (measure(word) <= maxWidth) {
      current = word
      continue
    }
    let chunk = ''
    for (const char of word) {
      const trial = chunk + char
      if (measure(trial) <= maxWidth) chunk = trial
      else {
        if (chunk) lines.push(chunk)
        chunk = char
      }
    }
    current = chunk
  }
  if (current) lines.push(current)
  return lines
}

export async function textToPdf(text: string, filename: string): Promise<File> {
  const pdf = await PDFDocument.create()
  const font = await pdf.embedFont(StandardFonts.Helvetica)
  const maxWidth = PAGE_WIDTH - MARGIN * 2
  const measure = (value: string) => font.widthOfTextAtSize(value, FONT_SIZE)
  const rawLines = text.replace(/\r\n/g, '\n').split('\n')
  const lines = rawLines.flatMap((line) => wrapLine(line, measure, maxWidth))

  let page = pdf.addPage([PAGE_WIDTH, PAGE_HEIGHT])
  let y = PAGE_HEIGHT - MARGIN
  for (const line of lines) {
    if (y < MARGIN) {
      page = pdf.addPage([PAGE_WIDTH, PAGE_HEIGHT])
      y = PAGE_HEIGHT - MARGIN
    }
    page.drawText(line || ' ', {
      x: MARGIN,
      y,
      size: FONT_SIZE,
      font,
      color: rgb(0.1, 0.1, 0.1)
    })
    y -= LINE_HEIGHT
  }

  const bytes = await pdf.save()
  const name = `${filename.replace(/\.[^/.]+$/, '')}.pdf`
  return new File([bytes], name, { type: 'application/pdf' })
}
