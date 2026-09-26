import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '@/views/IndexView.vue'
import { LANGUAGE_PATHS, languageByPath, setLanguage } from '@/locale'

// Every page exists at the root (English) and under /<language>/, e.g. /scan and /de/scan
const lang = `/:lang(${LANGUAGE_PATHS.join('|')})?`

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: `${lang}/`,
      name: 'index',
      component: IndexView
    },
    {
      path: `${lang}/scan`,
      name: 'scan',
      component: () => import('@/views/ScanViewFeatureDetectView.vue')
    },
    {
      path: `${lang}/scan/bulk`,
      name: 'bulk',
      component: () => import('@/views/BulkScanView.vue')
    },
    {
      path: `${lang}/scan-canvas`,
      name: 'scan-canvas',
      component: () => import('@/views/CanvasScanView.vue')
    },
    {
      path: `${lang}/scan-magica`,
      name: 'scan-magica',
      component: () => import('@/views/MagicaScanView.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'catch-all',
      // Unknown pages go to the home page of the language in the URL
      redirect: (to) => ({ name: 'index', params: { lang: languageByPath(to.path.split('/')[1]).path } })
    }
  ],
  scrollBehavior() {
    return { top: 0 }
  }
})

router.beforeEach(async (to) => {
  await setLanguage(languageByPath(to.params.lang))
})

export default router
