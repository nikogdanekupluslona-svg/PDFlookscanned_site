import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { languageByPath, localizePath } from '@/locale'

/** The language of the current URL and a helper that builds links in that language */
export function useLanguage() {
  const route = useRoute()
  const language = computed(() => languageByPath(route.params.lang))
  const localePath = (path: string) => localizePath(path, language.value)
  return { language, localePath }
}
