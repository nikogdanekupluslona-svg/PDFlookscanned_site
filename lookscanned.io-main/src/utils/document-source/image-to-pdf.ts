import { PDFDocument } from 'pdf-lib'
import { rasterizeImageFile } from './rasterize-image'

const A4 = { width: 595.28, height: 841.89 }

export async function imageToPdf(file: File): Promise<File> {
  const lower = file.name.toLowerCase()
  const pdf = await PDFDocument.create()
  const isJpeg = lower.endsWith('.jpg') || lower.endsWith('.jpeg') || file.type === 'image/jpeg'
  const isPng = lower.endsWith('.png') || file.type === 'image/png'

  let width: number
  let height: number
  let image

  if (isJpeg || isPng) {
    const bytes = new Uint8Array(await file.arrayBuffer())
    image = isPng ? await pdf.embedPng(bytes) : await pdf.embedJpg(bytes)
    width = image.width
    height = image.height
  } else {
    const raster = await rasterizeImageFile(file)
    image = await pdf.embedJpg(raster.bytes)
    width = raster.width
    height = raster.height
  }

  const landscape = width > height
  const pageWidth = landscape ? A4.height : A4.width
  const pageHeight = landscape ? A4.width : A4.height
  const scale = Math.min(pageWidth / width, pageHeight / height)
  const drawWidth = width * scale
  const drawHeight = height * scale
  const page = pdf.addPage([pageWidth, pageHeight])
  page.drawImage(image, {
    x: (pageWidth - drawWidth) / 2,
    y: (pageHeight - drawHeight) / 2,
    width: drawWidth,
    height: drawHeight
  })

  const bytes = await pdf.save()
  const name = `${file.name.replace(/\.[^/.]+$/, '')}.pdf`
  return new File([bytes], name, { type: 'application/pdf' })
}
