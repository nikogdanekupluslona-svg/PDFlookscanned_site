import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import i18n from './locale'
import { createHead } from '@unhead/vue'

const app = createApp(App)
const head = createHead()

app.use(router)
app.use(head)
app.use(i18n)

// Mount only after the first route has loaded its language, so the prerendered page is not replaced by English text
router.isReady().then(() => app.mount('#app'))
