<template>
  <n-space vertical>
    <n-card>
      <n-collapse :default-expanded-names="[]">
        <n-collapse-item :title="t('settings.extras.watermark')" name="watermark">
          <n-space vertical>
            <n-input
              :value="overlays.watermarkText"
              :placeholder="t('settings.extras.watermarkText')"
              @update:value="update({ watermarkText: $event })"
            />
            <n-space>
              <n-button size="small" @click="pickWatermark">{{ t('settings.extras.watermarkImage') }}</n-button>
              <n-button
                size="small"
                quaternary
                v-if="overlays.watermarkImage"
                @click="update({ watermarkImage: undefined })"
              >
                {{ t('settings.extras.clearImage') }}
              </n-button>
            </n-space>
            <n-text v-if="overlays.watermarkImage" depth="3">{{ overlays.watermarkImage.name }}</n-text>
          </n-space>
        </n-collapse-item>
      </n-collapse>
    </n-card>

    <n-card>
      <n-collapse :default-expanded-names="[]">
        <n-collapse-item :title="t('settings.extras.stamp')" name="stamp">
          <n-space vertical>
            <n-space>
              <n-button size="small" @click="pickStamp">{{ t('settings.extras.stampImage') }}</n-button>
              <n-button
                size="small"
                quaternary
                v-if="overlays.stampImage"
                @click="update({ stampImage: undefined })"
              >
                {{ t('settings.extras.clearImage') }}
              </n-button>
            </n-space>
            <n-text v-if="overlays.stampImage" depth="3">{{ overlays.stampImage.name }}</n-text>
            <template v-if="overlays.stampImage">
              <label class="slider">
                <span>{{ t('settings.extras.stampX') }}</span>
                <n-slider
                  :value="overlays.stampX"
                  :min="0"
                  :max="100"
                  @update:value="(value) => update({ stampX: Number(value) })"
                />
              </label>
              <label class="slider">
                <span>{{ t('settings.extras.stampY') }}</span>
                <n-slider
                  :value="overlays.stampY"
                  :min="0"
                  :max="100"
                  @update:value="(value) => update({ stampY: Number(value) })"
                />
              </label>
              <label class="slider">
                <span>{{ t('settings.extras.stampScale') }}</span>
                <n-slider
                  :value="overlays.stampScale"
                  :min="0.08"
                  :max="0.6"
                  :step="0.01"
                  @update:value="(value) => update({ stampScale: Number(value) })"
                />
              </label>
            </template>
          </n-space>
        </n-collapse-item>
      </n-collapse>
    </n-card>

    <n-card>
      <n-collapse :default-expanded-names="[]">
        <n-collapse-item :title="t('settings.extras.metadata')" name="metadata">
          <n-space vertical>
            <n-input
              :value="metadata.title"
              :placeholder="t('settings.extras.title')"
              @update:value="updateMeta({ title: $event })"
            />
            <n-input
              :value="metadata.author"
              :placeholder="t('settings.extras.author')"
              @update:value="updateMeta({ author: $event })"
            />
            <n-input
              :value="metadata.subject"
              :placeholder="t('settings.extras.subject')"
              @update:value="updateMeta({ subject: $event })"
            />
            <n-input
              :value="metadata.keywords"
              :placeholder="t('settings.extras.keywords')"
              @update:value="updateMeta({ keywords: $event })"
            />
            <n-input
              :value="metadata.producer"
              :placeholder="t('settings.extras.producer')"
              @update:value="updateMeta({ producer: $event })"
            />
            <n-input
              :value="metadata.creator"
              :placeholder="t('settings.extras.creator')"
              @update:value="updateMeta({ creator: $event })"
            />
          </n-space>
        </n-collapse-item>
      </n-collapse>
    </n-card>
  </n-space>
</template>

<script lang="ts" setup>
import { NCard, NCollapse, NCollapseItem, NSpace, NInput, NButton, NSlider, NText } from 'naive-ui'
import { fileOpen } from 'browser-fs-access'
import { useI18n } from 'vue-i18n'
import { useVModel } from '@vueuse/core'
import type { OverlayConfig, PdfMetadata } from '@/utils/overlays/types'

const { t } = useI18n()

const props = defineProps<{
  overlays: OverlayConfig
  metadata: PdfMetadata
}>()

const emit = defineEmits<{
  (e: 'update:overlays', value: OverlayConfig): void
  (e: 'update:metadata', value: PdfMetadata): void
}>()

const overlays = useVModel(props, 'overlays', emit)
const metadata = useVModel(props, 'metadata', emit)

function update(partial: Partial<OverlayConfig>) {
  overlays.value = { ...overlays.value, ...partial }
}

function updateMeta(partial: Partial<PdfMetadata>) {
  metadata.value = { ...metadata.value, ...partial }
}

async function pickWatermark() {
  const file = await fileOpen({
    description: 'Image',
    mimeTypes: ['image/*'],
    extensions: ['.png', '.jpg', '.jpeg', '.webp', '.svg']
  })
  update({ watermarkImage: file })
}

async function pickStamp() {
  const file = await fileOpen({
    description: 'Image',
    mimeTypes: ['image/*'],
    extensions: ['.png', '.jpg', '.jpeg', '.webp', '.svg']
  })
  update({ stampImage: file })
}
</script>

<style scoped>
.slider {
  display: grid;
  gap: 4px;
  font-size: 13px;
}
</style>
