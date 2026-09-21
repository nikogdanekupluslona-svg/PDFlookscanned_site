// Opens the native file dialog. input.click() runs synchronously inside the click handler,
// which Safari requires; awaiting anything first makes Safari silently ignore the call.
export function pickFile(accept: string): Promise<File | undefined> {
  return new Promise((resolve) => {
    const input = document.createElement('input')
    input.type = 'file'
    input.accept = accept
    input.style.display = 'none'
    input.addEventListener('change', () => {
      resolve(input.files?.[0])
      input.remove()
    })
    input.addEventListener('cancel', () => {
      resolve(undefined)
      input.remove()
    })
    document.body.append(input)
    input.click()
  })
}
