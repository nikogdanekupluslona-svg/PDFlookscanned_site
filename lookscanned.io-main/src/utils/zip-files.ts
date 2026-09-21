// Packs files into one ZIP; duplicate names get a " (2)" suffix instead of overwriting each other
export async function zipFiles(files: File[]): Promise<Blob> {
  const JSZip = (await import('jszip')).default
  const zip = new JSZip()
  const used = new Set<string>()
  for (const file of files) {
    let name = file.name
    const dot = name.lastIndexOf('.')
    const base = dot > 0 ? name.slice(0, dot) : name
    const ext = dot > 0 ? name.slice(dot) : ''
    for (let n = 2; used.has(name.toLowerCase()); n++) name = `${base} (${n})${ext}`
    used.add(name.toLowerCase())
    zip.file(name, await file.arrayBuffer())
  }
  return zip.generateAsync({ type: 'blob' })
}
