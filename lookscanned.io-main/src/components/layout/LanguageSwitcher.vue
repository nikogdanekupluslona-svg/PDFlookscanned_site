<template>
  <div ref="root" class="lang-switcher" @keydown.esc="open = false">
    <button
      type="button"
      class="toggle"
      aria-haspopup="true"
      :aria-expanded="open"
      :aria-label="`${t('base.language')}: ${language.name}`"
      @click="open = !open"
    >
      <svg class="globe" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="9" />
        <path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z" />
      </svg>
      <span class="code">{{ label(language) }}</span>
      <svg class="caret" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5 6 7.5l3-3" /></svg>
    </button>
    <ul v-if="open" class="menu">
      <li v-for="item in LANGUAGES" :key="item.code">
        <RouterLink
          :to="targetFor(item)"
          :hreflang="item.code"
          :lang="item.code"
          :aria-current="item.code === language.code ? 'true' : undefined"
          @click="open = false"
        >
          <span>{{ item.name }}</span>
          <span class="item-code">{{ label(item) }}</span>
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRoute, type RouteLocationRaw } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { onClickOutside } from '@vueuse/core'
import { LANGUAGES, type Language } from '@/locale'
import { useLanguage } from '@/composables/use-language'

const { t } = useI18n()
const route = useRoute()
const { language } = useLanguage()
const open = ref(false)
const root = ref<HTMLElement>()

onClickOutside(root, () => (open.value = false))

const label = (item: Language) => (item.path || item.code).toUpperCase()

// The same page in the other language: /de/scan -> /fr/scan
function targetFor(item: Language): RouteLocationRaw {
  return {
    name: route.name ?? 'index',
    params: { ...route.params, lang: item.path },
    query: route.query
  }
}
</script>

<style scoped>
.lang-switcher {
  position: relative;
  flex-shrink: 0;
}

.toggle {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 36px;
  padding: 0 10px;
  border: 1px solid #2a2b33;
  border-radius: 999px;
  background: transparent;
  color: #d8d8de;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
}

.toggle:hover,
.toggle[aria-expanded='true'] {
  border-color: #8fd14f;
  color: #fff;
}

.globe,
.caret {
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.globe {
  width: 16px;
  height: 16px;
}

.caret {
  width: 10px;
  height: 10px;
}

.menu {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  z-index: 40;
  min-width: 210px;
  max-height: min(70vh, 480px);
  overflow-y: auto;
  margin: 0;
  padding: 6px;
  list-style: none;
  background: #14151b;
  border: 1px solid #26272f;
  border-radius: 12px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
}

.menu a {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 8px 10px;
  border-radius: 8px;
  color: #d8d8de;
  text-decoration: none;
  font-size: 14px;
}

.menu a:hover {
  background: #1b1c23;
  color: #fff;
}

.menu a[aria-current] {
  color: #8fd14f;
  font-weight: 600;
}

.item-code {
  color: #8e8e99;
  font-size: 12px;
}
</style>
