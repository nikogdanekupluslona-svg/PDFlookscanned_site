import { hasOverlays, type OverlayConfig } from './types'

function canvasToBlob(canvas: HTMLCanvasElement, type: string, quality?: number): Promise<Blob> {
  return new Promise((resolve, reject) => {
    canvas.toBlob((blob) => {
      if (blob) resolve(blob)
      else reject(new Error('Could not export page'))
    }, type, quality)
  })
}

export async function applyOverlays(page: Blob, config: OverlayConfig): Promise<Blob> {
  if (!hasOverlays(config)) return page

  const img = await createImageBitmap(page)
  const canvas = document.createElement('canvas')
  canvas.width = img.width
  canvas.height = img.height
  const ctx = canvas.getContext('2d')
  if (!ctx) {
    img.close()
    throw new Error('Canvas is not supported')
  }

  ctx.drawImage(img, 0, 0)
  img.close()

  const text = config.watermarkText.trim()
  if (text) {
    ctx.save()
    ctx.globalAlpha = 0.14
    ctx.fillStyle = '#333333'
    ctx.font = `bold ${Math.max(28, Math.round(canvas.width / 16))}px sans-serif`
    ctx.textAlign = 'center'
    ctx.translate(canvas.width / 2, canvas.height / 2)
    ctx.rotate(-Math.PI / 5)
    const stepX = Math.max(220, canvas.width / 2.4)
    const stepY = Math.max(140, canvas.height / 4.5)
    for (let y = -canvas.height; y <= canvas.height; y += stepY) {
      for (let x = -canvas.width; x <= canvas.width; x += stepX) {
        ctx.fillText(text, x, y)
      }
    }
    ctx.restore()
  }

  if (config.watermarkImage) {
    const watermark = await createImageBitmap(config.watermarkImage)
    ctx.save()
    ctx.globalAlpha = 0.18
    const width = canvas.width * 0.42
    const height = (watermark.height / watermark.width) * width
    ctx.drawImage(watermark, (canvas.width - width) / 2, (canvas.height - height) / 2, width, height)
    ctx.restore()
    watermark.close()
  }

  if (config.stampImage) {
    const stamp = await createImageBitmap(config.stampImage)
    const width = canvas.width * config.stampScale
    const height = (stamp.height / stamp.width) * width
    const x = (config.stampX / 100) * canvas.width - width / 2
    const y = (config.stampY / 100) * canvas.height - height / 2
    ctx.drawImage(stamp, x, y, width, height)
    stamp.close()
  }

  const outputType = config.stampImage ? 'image/png' : 'image/jpeg'
  const blob = await canvasToBlob(canvas, outputType, 0.92)
  canvas.remove()
  return blob
}
