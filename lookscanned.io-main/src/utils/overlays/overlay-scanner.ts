import type { ScanRenderer } from '@/utils/scan-renderer'
import { applyOverlays } from './apply-overlays'
import { type OverlayConfig } from './types'

export class OverlayScanner implements ScanRenderer {
  constructor(
    private readonly inner: ScanRenderer,
    private readonly overlays: OverlayConfig
  ) {}

  async renderPage(
    image: Blob,
    options?: {
      signal?: AbortSignal
    }
  ): Promise<{ blob: Blob }> {
    const scanned = await this.inner.renderPage(image, options)
    return { blob: await applyOverlays(scanned.blob, this.overlays) }
  }
}
