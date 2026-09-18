<template>
  <!-- eslint-disable-next-line vue/no-v-html -- trusted static content, shared with the prerendered index.html -->
  <div class="home-guide-wrap" v-html="guideHtml" />
</template>

<script setup lang="ts">
import guideHtml from '@/content/home-guide.html?raw'
</script>

<style>
.home-guide {
  max-width: 860px;
  margin: 0 auto;
  padding: 24px 24px 72px;
  color: #d8d8de;
  font-size: 16px;
  line-height: 1.7;
}
.home-guide h2 {
  margin: 56px 0 16px;
  font-size: 26px;
  line-height: 1.25;
  letter-spacing: -0.02em;
  color: #f4f4f5;
}
.home-guide p,
.home-guide ul,
.home-guide ol {
  margin: 0 0 16px;
}
.home-guide a {
  color: #8fd14f;
}
.home-guide strong {
  color: #f4f4f5;
}
.home-guide .step-list {
  list-style: none;
  padding: 0;
  counter-reset: s;
}
.home-guide .step-list li {
  counter-increment: s;
  position: relative;
  padding: 12px 0 12px 48px;
  border-bottom: 1px solid #22232a;
}
.home-guide .step-list li::before {
  content: counter(s);
  position: absolute;
  left: 0;
  top: 13px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #8fd14f;
  color: #10200a;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}
.home-guide .table-wrap {
  overflow-x: auto;
  margin: 24px 0;
  border: 1px solid #22232a;
  border-radius: 12px;
}
.home-guide table {
  width: 100%;
  min-width: 540px;
  border-collapse: collapse;
  font-size: 14px;
}
.home-guide caption {
  text-align: left;
  padding: 10px 14px;
  color: #b8b8c2;
  font-weight: 600;
  background: #14151b;
}
.home-guide th,
.home-guide td {
  padding: 10px 14px;
  border-top: 1px solid #22232a;
  text-align: left;
  vertical-align: top;
}
.home-guide th {
  color: #f4f4f5;
}
.home-guide .callout {
  margin: 24px 0;
  padding: 16px 20px;
  border-radius: 12px;
  background: #2a2112;
  border-left: 4px solid #e8a020;
}
.home-guide .callout strong {
  display: block;
  margin-bottom: 4px;
}
.home-guide .faq-item {
  padding: 16px 0;
  border-bottom: 1px solid #22232a;
}
.home-guide .faq-q {
  margin: 0 0 6px;
  font-weight: 700;
  color: #f4f4f5;
}
.home-guide .faq-a {
  margin: 0;
}
</style>
