import { createI18n } from 'vue-i18n'

import en from './messages/en.json'
import { DEFAULT_LANGUAGE, type Language } from './languages'

export * from './languages'

export type MessageSchema = typeof en

const i18n = createI18n({
  legacy: false,
  locale: DEFAULT_LANGUAGE.code,
  fallbackLocale: DEFAULT_LANGUAGE.code,
  messages: { [DEFAULT_LANGUAGE.code]: en } as Record<string, MessageSchema>
})

const loaders = import.meta.glob<MessageSchema>(['./messages/*.json', '!./messages/en.json'], {
  import: 'default'
})

export async function setLanguage(language: Language) {
  const { global } = i18n
  if (!global.availableLocales.includes(language.code)) {
    const load = loaders[`./messages/${language.code}.json`]
    if (load) global.setLocaleMessage(language.code, await load())
  }
  global.locale.value = language.code
  document.documentElement.lang = language.code
}

export default i18n
