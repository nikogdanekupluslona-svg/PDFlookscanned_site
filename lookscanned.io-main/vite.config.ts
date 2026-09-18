import { copyFileSync, existsSync, readFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import { VitePWA } from 'vite-plugin-pwa'

function spaFallback() {
  return {
    name: 'spa-github-pages-fallback',
    closeBundle() {
      const index = resolve(__dirname, 'dist/index.html')
      if (existsSync(index)) {
        copyFileSync(index, resolve(__dirname, 'dist/404.html'))
      }
    }
  }
}

const SITE = 'https://pdflookscanned.com'
const STORE_URL =
  'https://chromewebstore.google.com/detail/make-pdf-look-scanned/ijhpnlcipgiokgignkbbbgkobdmdoila'

function plainText(html: string) {
  return html
    .replace(/<[^>]+>/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/\s+/g, ' ')
    .trim()
}

// Puts the home-page guide into the static HTML (for crawlers that do not run JS)
// and derives the home JSON-LD from the same source, so text and schema never drift apart.
function homePrerender() {
  return {
    name: 'home-prerender',
    transformIndexHtml(html: string) {
      const guide = readFileSync(resolve(__dirname, 'src/content/home-guide.html'), 'utf8')
      const faq = [...guide.matchAll(/<p class="faq-q">(.*?)<\/p><p class="faq-a">(.*?)<\/p>/gs)].map(
        ([, q, a]) => ({
          '@type': 'Question',
          name: plainText(q),
          acceptedAnswer: { '@type': 'Answer', text: plainText(a) }
        })
      )
      const stepsBlock = guide.match(/<ol class="step-list">(.*?)<\/ol>/s)?.[1] ?? ''
      const steps = [...stepsBlock.matchAll(/<li>(.*?)<\/li>/gs)].map(([, li], i) => ({
        '@type': 'HowToStep',
        position: i + 1,
        text: plainText(li)
      }))
      const jsonld = {
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'Organization',
            '@id': `${SITE}/#org`,
            name: 'Make PDF look scanned',
            url: `${SITE}/`,
            logo: `${SITE}/pwa-512x512.png`,
            sameAs: [STORE_URL]
          },
          { '@type': 'WebSite', '@id': `${SITE}/#website`, name: 'Make PDF look scanned', url: `${SITE}/` },
          {
            '@type': 'WebApplication',
            name: 'Make PDF look scanned',
            url: `${SITE}/`,
            applicationCategory: 'UtilitiesApplication',
            operatingSystem: 'Any (runs in the browser)',
            browserRequirements: 'Requires a modern browser with JavaScript',
            offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
            publisher: { '@id': `${SITE}/#org` }
          },
          {
            '@type': 'HowTo',
            name: 'How to make a PDF look scanned online',
            totalTime: 'PT1M',
            step: steps
          },
          { '@type': 'FAQPage', mainEntity: faq }
        ]
      }
      const prerender =
        '<div class="prerender"><h1>Make PDF look scanned</h1>' +
        '<p>Turn PDFs, images, Word and Excel files into realistic scanned copies with blur, noise, rotation, ' +
        'watermarks and stamps — right in your browser. Source files stay on your device.</p>' +
        '<p><a href="/scan">Convert to Scanned PDF</a> · <a href="/blog/">Guides</a></p>' +
        guide +
        '</div>'
      return html
        .replace('<!--home-prerender-->', prerender)
        .replace(
          '<!--home-jsonld-->',
          `<script type="application/ld+json">${JSON.stringify(jsonld)}</script>`
        )
    }
  }
}

export default defineConfig({
  base: '/',
  assetsInclude: ['**/*.pfb', '**/*.ttf'],
  plugins: [
    vue(),
    homePrerender(),
    spaFallback(),
    VitePWA({
      includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'favicon.svg'],
      workbox: {
        globPatterns: ['assets/*', '**/*.{js,css,html}'],
        globIgnores: ['blog/**'],
        // Static blog pages, sitemap and llms.txt must never be answered by the SPA shell
        navigateFallbackDenylist: [/^\/blog(\/|$)/, /^\/sitemap\.xml$/, /^\/llms\.txt$/, /^\/robots\.txt$/],
        maximumFileSizeToCacheInBytes: 10000000
      },
      manifest: {
        name: 'Make PDF look scanned',
        short_name: 'PDF scanned',
        description:
          'Make a clean digital file look like a real scan. Processed locally in your browser.',
        theme_color: '#0b0b0f',
        background_color: '#0b0b0f',
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png',
            purpose: 'any'
          },
          {
            src: 'pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'any'
          },
          {
            src: 'pwa-maskable-192x192.png',
            sizes: '192x192',
            type: 'image/png',
            purpose: 'maskable'
          },
          {
            src: 'pwa-maskable-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'maskable'
          }
        ]
      }
    })
  ],
  define: { 'process.env': {} },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
