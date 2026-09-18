interface ImageInfo {
  blob: Blob
  width: number
  height: number
  ppi: number
}

export interface PdfMetadata {
  title?: string
  author?: string
  subject?: string
  keywords?: string
  producer?: string
  creator?: string
}

const fallbackMetadata = {
  producer: 'SECnvtToPDF V1.0',
  creator: 'TOSHIBA e-STUDIO2010AC'
}

export async function buildPDF(images: ImageInfo[], metadata?: PdfMetadata): Promise<Blob> {
  const { PDFDocument } = await import('pdf-lib')
  const pdfDoc = await PDFDocument.create()

  for (const image of images) {
    const { blob, width, height, ppi } = image
    const physicalWidthDots = (width / ppi) * 72
    const physicalHeightDots = (height / ppi) * 72
    const page = pdfDoc.addPage([physicalWidthDots, physicalHeightDots])

    const imageBytes = await blob.arrayBuffer()
    let pdfImage
    if (blob.type === 'image/png') {
      pdfImage = await pdfDoc.embedPng(imageBytes)
    } else if (blob.type === 'image/jpeg') {
      pdfImage = await pdfDoc.embedJpg(imageBytes)
    } else {
      const pngBlob = await blobToPng(blob)
      pdfImage = await pdfDoc.embedPng(await pngBlob.arrayBuffer())
    }

    page.drawImage(pdfImage, {
      x: 0,
      y: 0,
      width: physicalWidthDots,
      height: physicalHeightDots
    })
  }

  if (metadata?.title?.trim()) pdfDoc.setTitle(metadata.title.trim())
  if (metadata?.author?.trim()) pdfDoc.setAuthor(metadata.author.trim())
  if (metadata?.subject?.trim()) pdfDoc.setSubject(metadata.subject.trim())
  if (metadata?.keywords?.trim()) {
    pdfDoc.setKeywords(metadata.keywords.split(',').map((item) => item.trim()).filter(Boolean))
  }
  pdfDoc.setProducer(metadata?.producer?.trim() || fallbackMetadata.producer)
  pdfDoc.setCreator(metadata?.creator?.trim() || fallbackMetadata.creator)

  const pdfBytes = await pdfDoc.save()
  return new Blob([pdfBytes], { type: 'application/pdf' })
}

async function blobToPng(blob: Blob): Promise<Blob> {
  const bitmap = await createImageBitmap(blob)
  const canvas = document.createElement('canvas')
  canvas.width = bitmap.width
  canvas.height = bitmap.height
  const ctx = canvas.getContext('2d')
  if (!ctx) {
    bitmap.close()
    throw new Error('Canvas is not supported')
  }
  ctx.drawImage(bitmap, 0, 0)
  bitmap.close()
  const png = await new Promise<Blob>((resolve, reject) => {
    canvas.toBlob((result) => {
      if (result) resolve(result)
      else reject(new Error('Could not convert page image'))
    }, 'image/png')
  })
  canvas.remove()
  return png
}
