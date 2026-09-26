// Language list and URL helpers. Kept free of browser and vue-i18n imports so vite.config.ts can use it too.
import languages from './languages.json'
import blogSlugs from './blog-slugs.json'

export interface Language {
  /** BCP 47 code used for hreflang, <html lang> and the messages file name */
  code: string
  /** URL prefix without slashes; empty for English at the site root */
  path: string
  /** Native name shown in the language switcher */
  name: string
  ogLocale: string
}

export const LANGUAGES = languages as Language[]
export const DEFAULT_LANGUAGE = LANGUAGES[0]

/** URL prefixes of the translated copies, for route paths like `/:lang(de|fr)?/scan` */
export const LANGUAGE_PATHS = LANGUAGES.filter((l) => l.path).map((l) => l.path)

export function languageByPath(path: unknown): Language {
  return LANGUAGES.find((l) => l.path && l.path === path) ?? DEFAULT_LANGUAGE
}

/** `/scan` in the given language: `/de/scan`, or `/scan` for English */
export function localizePath(path: string, language: Language): string {
  if (!language.path) return path
  return path === '/' ? `/${language.path}/` : `/${language.path}${path}`
}

/**
 * Points the site-internal links of an English-authored HTML snippet at the given language:
 * `/scan` -> `/de/scan`, `/blog/scan-effect/` -> `/de/blog/scan-effekt/` (slugs come from
 * blog-slugs.json, written by seo-workspace/build.py). Articles without a translation keep the English link.
 */
export function localizeLinks(html: string, language: Language): string {
  if (!language.path) return html
  const slugs = (blogSlugs as Record<string, Record<string, string>>)[language.code] ?? {}
  return html.replace(/href="(\/[^"#]*)(#[^"]*)?"/g, (link, path: string, hash = '') => {
    const article = path.match(/^\/blog\/([^/]+)\/$/)
    if (article) {
      const slug = slugs[article[1]]
      return slug ? `href="/${language.path}/blog/${slug}/${hash}"` : link
    }
    return `href="${localizePath(path, language)}${hash}"`
  })
}
