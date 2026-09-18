<template>
  <a
    class="chrome-badge"
    :href="CHROME_WEB_STORE_URL"
    target="_blank"
    rel="noopener noreferrer"
    :aria-label="`${t('base.chrome.label')} ${CHROME_EXTENSION_RATING}`"
  >
    <svg class="logo" viewBox="0 0 48 48" aria-hidden="true">
      <circle cx="24" cy="24" r="20" fill="#fff" />
      <path fill="#EA4335" d="M24 8a16 16 0 0 1 13.856 8H24z" />
      <path fill="#FBBC04" d="M37.856 16A16 16 0 0 1 24 40l8-13.856z" />
      <path fill="#34A853" d="M24 40A16 16 0 0 1 10.144 16H24z" />
      <path fill="#4285F4" d="M24 8a16 16 0 0 0-13.856 8L24 24z" />
      <circle cx="24" cy="24" r="7.2" fill="#fff" />
      <circle cx="24" cy="24" r="5.1" fill="#4285F4" />
    </svg>
    <span class="copy">
      <span class="title">{{ t('base.chrome.label') }}</span>
      <span class="meta">
        <strong>{{ CHROME_EXTENSION_RATING }}</strong>
        <span class="stars" aria-hidden="true">★★★★★</span>
        <span class="free">{{ t('base.chrome.free') }}</span>
      </span>
    </span>
  </a>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import { CHROME_WEB_STORE_URL, CHROME_EXTENSION_RATING } from '@/constants'

const { t } = useI18n()
</script>

<style scoped>
.chrome-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 8px 14px 8px 8px;
  border-radius: 18px;
  background: #fff;
  border: 1px solid #ececec;
  box-shadow: 0 8px 24px rgba(15, 15, 20, 0.12);
  text-decoration: none;
  color: #1f1f1f;
  min-height: 56px;
  flex-shrink: 0;
}

.logo {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
}

.copy {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.title {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

.meta {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
}

.meta strong {
  font-weight: 700;
}

.stars {
  color: #f5b400;
  letter-spacing: 1px;
  font-size: 11px;
}

.free {
  display: inline-flex;
  align-items: center;
  padding: 1px 7px;
  border-radius: 999px;
  background: #f3d5c4;
  color: #8a4b2b;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.04em;
}

@media (max-width: 720px) {
  .chrome-badge {
    padding: 6px 10px 6px 6px;
    min-height: 48px;
  }

  .logo {
    width: 32px;
    height: 32px;
  }

  .title {
    font-size: 12px;
  }
}
</style>
