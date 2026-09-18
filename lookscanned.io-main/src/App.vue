<template>
  <n-config-provider :theme="darkTheme">
    <n-global-style />
    <n-message-provider>
      <SiteHeader />
      <main class="view">
        <RouterView :key="route.fullPath" />
      </main>
      <ServieWorkerReloadPrompt />
    </n-message-provider>
  </n-config-provider>
</template>

<script lang="ts" setup>
import { darkTheme, NConfigProvider, NGlobalStyle, NMessageProvider } from 'naive-ui'
import { RouterView, useRoute } from 'vue-router'
import ServieWorkerReloadPrompt from '@/components/Misc/ServiceWorkerReloadPrompt.vue'
import SiteHeader from '@/components/layout/SiteHeader.vue'

const route = useRoute()
</script>

<style>
html,
body,
#app {
  min-height: 100%;
  background: #0b0b0f;
}

body {
  margin: 0;
}

.view {
  min-height: calc(100vh - 72px);
}
</style>
