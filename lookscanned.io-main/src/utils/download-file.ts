// Plain <a download> works the same in every browser and lands in the Downloads folder,
// unlike showSaveFilePicker, which only exists in Chromium and throws when the dialog is cancelled.
export function downloadFile(file: Blob, fileName: string) {
  const url = URL.createObjectURL(file)
  const link = document.createElement('a')
  link.href = url
  link.download = fileName
  link.rel = 'noopener'
  link.style.display = 'none'
  document.body.append(link)
  link.click()
  link.remove()
  setTimeout(() => URL.revokeObjectURL(url), 60_000)
}
