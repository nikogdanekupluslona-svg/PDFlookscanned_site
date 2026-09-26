import { copyFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import { VitePWA } from 'vite-plugin-pwa'

import {
  LANGUAGES,
  LANGUAGE_PATHS,
  localizeLinks,
  localizePath,
  type Language
} from './src/locale/languages'

const SITE = 'https://pdflookscanned.com'
const BRAND = 'Make PDF look scanned'
const STORE_URL =
  'https://chromewebstore.google.com/detail/make-pdf-look-scanned/ijhpnlcipgiokgignkbbbgkobdmdoila'

function plainText(html: string) {
  return html
    .replace(/<[^>]+>/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/\s+/g, ' ')
    .trim()
}

function attr(text: string) {
  return text.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;')
}

interface HomeMessages {
  base: {
    landing: { headline: string; subhead: string; cta: string }
    nav: { guides: string }
    seo: { homeTitle: string; homeDescription: string }
  }
}

function readSource(path: string) {
  const file = resolve(__dirname, path)
  return existsSync(file) ? readFileSync(file, 'utf8') : undefined
}

// A language gets its own static home page once both its interface strings and its home guide exist
function homeLanguages() {
  return LANGUAGES.filter(
    (l) =>
      readSource(`src/locale/messages/${l.code}.json`) && readSource(`src/content/home-guide/${l.code}.html`)
  )
}

// Writes the home page of one language into the built index.html: search snippet, canonical, hreflang,
// JSON-LD and the guide text (for crawlers that do not run JS). Text and schema come from the same source.
function renderHome(template: string, language: Language, available: Language[]) {
  const m = JSON.parse(readSource(`src/locale/messages/${language.code}.json`)!) as HomeMessages
  const guide = localizeLinks(readSource(`src/content/home-guide/${language.code}.html`)!, language)
  const url = SITE + localizePath('/', language)
  const { homeTitle, homeDescription } = m.base.seo

  const alternates = available
    .map((l) => `<link rel="alternate" hreflang="${l.code}" href="${SITE}${localizePath('/', l)}">`)
    .concat(`<link rel="alternate" hreflang="x-default" href="${SITE}/">`)
  const head = [
    `<title>${attr(homeTitle)}</title>`,
    `<meta name="description" content="${attr(homeDescription)}">`,
    `<link rel="canonical" href="${url}">`,
    ...alternates,
    '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">',
    `<meta property="og:site_name" content="${BRAND}">`,
    `<meta property="og:title" content="${attr(homeTitle)}">`,
    `<meta property="og:description" content="${attr(homeDescription)}">`,
    '<meta property="og:type" content="website">',
    `<meta property="og:url" content="${url}">`,
    `<meta property="og:locale" content="${language.ogLocale}">`,
    `<meta property="og:image" content="${SITE}/pwa-512x512.png">`,
    '<meta name="twitter:card" content="summary">'
  ].join('\n    ')

  const faq = [...guide.matchAll(/<p class="faq-q">(.*?)<\/p>\s*<p class="faq-a">(.*?)<\/p>/gs)].map(([, q, a]) => ({
    '@type': 'Question',
    name: plainText(q),
    acceptedAnswer: { '@type': 'Answer', text: plainText(a) }
  }))
  const stepsBlock = guide.match(/<ol class="step-list">(.*?)<\/ol>/s)?.[1] ?? ''
  const steps = [...stepsBlock.matchAll(/<li>(.*?)<\/li>/gs)].map(([, li], i) => ({
    '@type': 'HowToStep',
    position: i + 1,
    text: plainText(li)
  }))
  const howToName = plainText(guide.match(/<h2 id="hg-steps">(.*?)<\/h2>/s)?.[1] ?? '')
  const jsonld = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Organization',
        '@id': `${SITE}/#org`,
        name: BRAND,
        url: `${SITE}/`,
        logo: `${SITE}/pwa-512x512.png`,
        sameAs: [STORE_URL]
      },
      { '@type': 'WebSite', '@id': `${SITE}/#website`, name: BRAND, url: `${SITE}/` },
      {
        '@type': 'WebApplication',
        name: BRAND,
        url,
        inLanguage: language.code,
        description: homeDescription,
        applicationCategory: 'UtilitiesApplication',
        operatingSystem: 'Any (runs in the browser)',
        browserRequirements: 'Requires a modern browser with JavaScript',
        offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
        publisher: { '@id': `${SITE}/#org` }
      },
      { '@type': 'HowTo', name: howToName, inLanguage: language.code, totalTime: 'PT1M', step: steps },
      { '@type': 'FAQPage', inLanguage: language.code, mainEntity: faq }
    ]
  }
  const prerender =
    `<div class="prerender"><h1>${m.base.landing.headline}</h1>` +
    `<p>${m.base.landing.subhead}</p>` +
    `<p><a href="${localizePath('/scan', language)}">${m.base.landing.cta}</a> · ` +
    `<a href="${localizePath('/blog/', language)}">${m.base.nav.guides}</a></p>` +
    guide +
    '</div>'
  return template
    .replace(/<html lang="[^"]*">/, `<html lang="${language.code}">`)
    .replace('<!--home-head-->', head)
    .replace('<!--home-prerender-->', prerender)
    .replace('<!--home-jsonld-->', `<script type="application/ld+json">${JSON.stringify(jsonld)}</script>`)
}

// index.html becomes the English home page; every translated language gets <lang>/index.html.
// GitHub Pages answers /scan and /<lang>/scan from scan.html with HTTP 200; other app routes use 404.html.
function multilingualHome() {
  let template = ''
  return {
    name: 'multilingual-home',
    transformIndexHtml: {
      order: 'post' as const,
      handler(html: string) {
        template = html
        return renderHome(html, LANGUAGES[0], homeLanguages())
      }
    },
    closeBundle() {
      const dist = resolve(__dirname, 'dist')
      if (!template || !existsSync(resolve(dist, 'index.html'))) return
      copyFileSync(resolve(dist, 'index.html'), resolve(dist, '404.html'))
      copyFileSync(resolve(dist, 'index.html'), resolve(dist, 'scan.html'))
      const available = homeLanguages()
      for (const language of available.filter((l) => l.path)) {
        const html = renderHome(template, language, available)
        mkdirSync(resolve(dist, language.path), { recursive: true })
        writeFileSync(resolve(dist, language.path, 'index.html'), html)
        writeFileSync(resolve(dist, language.path, 'scan.html'), html)
      }
    }
  }
}

// Static blog pages (English /blog/ and /<lang>/blog/) must never be answered by the SPA shell
const BLOG_PATH = new RegExp(`^/(?:(?:${LANGUAGE_PATHS.join('|')})/)?blog(/|$)`)

export default defineConfig({
  base: '/',
  assetsInclude: ['**/*.pfb', '**/*.ttf'],
  plugins: [
    vue(),
    multilingualHome(),
    VitePWA({
      includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'favicon.svg'],
      workbox: {
        globPatterns: ['assets/*', '**/*.{js,css,html}'],
        // Translated home pages are served from the network; offline, the root shell renders them
        globIgnores: ['blog/**', '*/blog/**', '*/index.html', '*/scan.html'],
        navigateFallbackDenylist: [BLOG_PATH, /^\/sitemap\.xml$/, /^\/llms\.txt$/, /^\/robots\.txt$/],
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
