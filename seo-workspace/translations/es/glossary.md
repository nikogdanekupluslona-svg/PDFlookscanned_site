# Glosario ES (español) — pdflookscanned.com

Code `es`, URL path `/es/`, ogLocale `es_ES`. Market: Spain and Latin America. Write **neutral international
Spanish** that reads naturally on both sides of the Atlantic. This glossary is binding for every Spanish page
(interface, home guide, blog chrome, the 7 article bodies). If a term is not here, pick the most neutral option
and use it consistently inside the article.

## 1. Address form and style

- Address the reader with **tú** (informal, singular): "abre", "suelta", "descarga", "tu archivo", "puedes".
  Never "usted", never "vosotros". Imperatives: abre, elige, suelta, ajusta, mueve, haz clic, descarga, guarda.
- Tone: plain, concrete, friendly, like modern software help pages. Short sentences. No hype
  ("revolucionario", "increíble"), no filler, no English calques ("aplicar a" for "apply for", "en orden a", etc.).
- Answer-first: every H2 opens with a 40–60-word paragraph that answers the heading on its own and names the
  subject (no "Esto…" / "Ello…" openers).
- Headings: sentence case (only the first word and proper names capitalized), even where English uses Title Case.
  Question headings use both marks: **¿…?** Keep them ≤ 70 characters.
- Neutral vocabulary (Spain + LatAm):
  - phone → **móvil** (matches the UI: "Funciona en el móvil"); you may vary with "teléfono". Avoid "celular".
  - computer → prefer **equipo** / **dispositivo**; if unavoidable, "ordenador" (the UI locale is es_ES).
  - add → **añadir** (matches UI "Añadir archivos"). Avoid "agregar".
  - file → **archivo** (not "fichero"). Folder → **carpeta**.
  - click → **hacer clic** (not "pinchar", not "cliquear").
  - online → **online** (widely searched) or "en línea"; in keywords prefer "online".
  - free → **gratis** (adverb/adjective after verb: "es gratis") / **gratuito, gratuita** (adjective: "herramienta gratuita").
- Plural of PDF is invariable: **los PDF**, "tres PDF escaneados" (not "PDFs"). Same for ZIP, JPG, PNG.
- Brand: **Make PDF look scanned** stays in English as a proper name, never translated, never in quotes.
  Describe it as "la herramienta gratuita", "nuestra herramienta", "la herramienta web", "la extensión".
  Team: **el equipo de Make PDF look scanned**. Expert-quote cite:
  `<strong>El equipo de Make PDF look scanned</strong> — creadores de la herramienta web y de la extensión de Chrome`
- Interface labels in running text: write them **exactly as in `messages/es.json`**, with their initial capital
  and **without quotes**: "haz clic en Generar PDF escaneado", "deja Espacio de color en Gris",
  "sube Ruido a 0,15", "activa Borde". In tables and spec lists use the label alone ("Rotación", "Amarillento").
- Quotation marks: use **« »** for quoted words from sources and for phrases people say
  («copia escaneada»); nested quotes “ ”. Translate quotes from English sources into Spanish, keep attribution
  and link; a paraphrase is written without quotation marks ("según la NARA, …").
- TOC: `<nav class="toc" aria-label="Índice"><h2>Índice</h2>…`. FAQ heading: "…: preguntas frecuentes"
  (or "Preguntas frecuentes sobre …"); short tag-style: "FAQ" is not used in Spanish headings.
- Callout headings (the `<strong>` inside callouts) have no final period.
- US agencies and courts stay as sources; you may add the Spanish gloss once:
  "el Servicio de Ciudadanía e Inmigración de EE. UU. (USCIS)", "la Administración Nacional de Archivos y
  Registros de EE. UU. (NARA)", "el IRS", "los tribunales federales de EE. UU. (sistema CM/ECF)", "FADGI",
  "el W3C", "las pautas WCAG". Write **EE. UU.** (with spaces and periods).

## 2. Numbers, units, dates

| Item | Rule | Example |
|---|---|---|
| Decimal separator | comma | 0,3 · 0,5° · 1,5× · 0,05–0,2 |
| Thousands | no separator for 4 digits; non-breaking space for 5+ digits (RAE) | 2200 px · 10 000 páginas |
| Ranges | en dash without spaces, or "entre X y Y" in prose | 0,5°–2° · entre 20 y 60 segundos |
| Degrees, ×, % | as in the English source, no space before ° and × and % | 1° · 2× · 400% |
| dpi | **ppp** (puntos por pulgada); first mention in an article: "ppp (dpi)" | 144 ppp · 300 ppp (dpi) |
| ppi | "ppi (píxeles por pulgada)" only where the dpi/ppi difference matters; else ppp | 300 ppi |
| Negative numbers | real minus sign as in source | −10° |
| Dates | day + "de" + month (lowercase) + "de" + year | 18 de septiembre de 2026 |
| Paper sizes | A4 as-is; US Letter → **tamaño carta** ("Carta") | A4 o carta |
| Keyboard | Ctrl+P, Ctrl+F, Cmd+P, Cmd+F (keep "Cmd") | pulsa Ctrl+P (Cmd+P en Mac) |
| Times | "menos de 1 minuto", "10–20 minutos", "más de 30 minutos" | |
| File sizes | KB, MB with decimal comma and a space | 1,2 MB · 350 KB |

## 3. Recurring terms EN → ES

| English | Spanish (use this) | Notes |
|---|---|---|
| make a PDF look scanned | hacer que un PDF parezca escaneado | main keyword of home + pillar; imperative: "haz que tu PDF parezca escaneado" |
| make a document look scanned | hacer que un documento parezca escaneado | |
| scan effect | efecto escaneado | plural: efectos de escaneado; "efecto de escaneo" only as keyword variant |
| scan look / scanned look | aspecto escaneado | "un PDF con aspecto escaneado" |
| scanned-looking PDF | PDF con aspecto escaneado | |
| scanned PDF | PDF escaneado | |
| digital PDF / born-digital PDF | PDF digital / PDF nativo digital | |
| scanned copy | copia escaneada | |
| scanned document | documento escaneado | |
| scan (noun) / to scan | escaneo / escanear | "escaneado" = past participle/adjective |
| scanner | escáner (pl. escáneres) | |
| flatbed scanner | escáner plano | |
| sheet-fed scanner / ADF | escáner con alimentador automático (ADF) | |
| office scan | escaneo de oficina | preset name |
| photocopy / photocopier | fotocopia / fotocopiadora | photocopy look: aspecto de fotocopia |
| fax / fax-like | fax / estilo fax | preset name "Estilo fax" |
| aged paper | papel envejecido | preset name |
| phone-scan look | escaneo con móvil | preset name |
| printout | copia impresa | |
| text layer | capa de texto | |
| OCR | OCR (reconocimiento óptico de caracteres) | expand once per article |
| searchable PDF | PDF con texto buscable | short form: PDF buscable |
| selectable text | texto seleccionable | |
| image-only PDF | PDF de solo imagen | |
| page image | imagen de página | |
| flatten / flattening | aplanar / aplanado | "aplanar un PDF" |
| rasterize / rasterization | rasterizar / rasterización | |
| raster image editor | editor de imágenes rasterizadas | never name a product |
| desktop PDF software | software de PDF de escritorio | never name a product |
| phone scanner app | app de escaneo para el móvil | never name a product |
| vector (edges, logos) | vectorial (bordes vectoriales, logotipos vectoriales) | |
| grayscale / colorspace | escala de grises / espacio de color | UI **Espacio de color** → **Gris** / **Color** |
| black and white (B&W) | blanco y negro (B/N) | |
| bitonal / pure black and white | bitonal / blanco y negro puro (1 bit) | |
| color PDF | PDF en color | keyword variant "PDF a color" (LatAm) allowed in titles/keywords |
| bit depth | profundidad de bits | "profundidad de color" as synonym |
| skew / tilt / rotation | inclinación / rotación | "inclinado", "leve inclinación"; UI **Rotación**, **Variación de rotación** |
| noise / grain | ruido / grano | UI **Ruido**; "grano del escáner" |
| deskew | enderezar | the tool does not deskew |
| speckle | motas | "motas y puntitos" |
| blur / soft focus / sharpness | desenfoque / enfoque suave / nitidez | UI label **Desenfoque**; crisp: nítido |
| moiré | efecto moiré | |
| halftone | semitono (trama de semitonos) | |
| paper tone / yellowish | tono del papel / amarillento | UI **Amarillento** |
| edge shadow | sombra en el borde | real-scanner artifact, NOT a tool feature |
| crease, fold, coffee stain | pliegue, doblez, mancha de café | NOT tool features |
| perspective warp | deformación de perspectiva | NOT a tool feature |
| resolution / dpi | resolución / ppp (puntos por pulgada) | UI **Resolución**; see numbers |
| JPEG compression / JPEG blocks | compresión JPEG / bloques JPEG | |
| compression artifact | artefacto de compresión | "artifact" in general: artefacto |
| file size | tamaño del archivo | "pesa más" for "is larger" |
| live preview | vista previa en directo | UI: **Vista previa** |
| settings / default | ajustes / valor predeterminado | "los valores predeterminados" |
| preset / recipe | ajuste predefinido / receta | |
| slider | control deslizante | |
| bulk scan | escaneo por lotes | UI label **Escaneo por lotes** |
| batch | lote / por lotes | |
| side panel | panel lateral | |
| Chrome extension | extensión de Chrome | UI label **Extensión de Chrome** |
| web tool / browser tool | herramienta web / herramienta del navegador | |
| free, no signup | gratis, sin registro | |
| processed locally | se procesa localmente (en local) | "no se sube a ningún servidor" |
| upload / download / drop a file | subir / descargar / soltar un archivo | "arrastra y suelta" |
| print dialog | cuadro de diálogo de impresión | |
| print to PDF | imprimir a PDF / guardar como PDF | |
| trust badge | valorada con 5 estrellas en Chrome Web Store | exact wording; feminine (la herramienta / la extensión) |
| screen reader | lector de pantalla | |
| e-filing | presentación electrónica | |
| court / agency | tribunal / organismo | US federal agency: agencia federal |
| honest use (callout heading) | Usa el aspecto escaneado con honestidad | ethics callout |

## 4. Interface labels (exactly as in `lookscanned.io-main/src/locale/messages/es.json`)

| English UI | Spanish UI | Key |
|---|---|---|
| Make PDF look scanned (brand) | Make PDF look scanned | base.title |
| Scan | Escanear | nav.scan / scanTitle |
| Bulk Scan | Escaneo por lotes | nav.bulk / bulkTitle |
| Home | Inicio | nav.home |
| Guides | Guías | nav.guides |
| Chrome Extension | Extensión de Chrome | chrome.label |
| FREE | GRATIS | chrome.free |
| Make PDF look scanned (home H1) | Hacer que un PDF parezca escaneado | landing.headline |
| Convert to Scanned PDF | Convertir a PDF escaneado | landing.cta |
| Free · No signup · Files stay on your device | Gratis · Sin registro · Los archivos no salen de tu dispositivo | landing.note |
| Start scanning | Empezar a escanear | actions.navigateToScan |
| Back | Volver | actions.backToIndex |
| Preview | Vista previa | actions.preview |
| Save | Guardar | actions.save |
| Generate Scanned PDF | Generar PDF escaneado | actions.generateScannedPDF |
| Generating... | Generando... | actions.generating |
| Download Scanned PDF | Descargar PDF escaneado | actions.downloadScannedPDF |
| Add files | Añadir archivos | actions.addFiles |
| Generate scanned PDFs | Generar PDF escaneados | actions.processAll |
| Download all as ZIP | Descargar todo en ZIP | actions.downloadZip |
| Queued / Done / Failed | En cola / Hecho / Error | actions.* |
| Scan Settings | Ajustes de escaneo | settings.settings |
| Noise | Ruido | settings.noise |
| Blur | Desenfoque | settings.blur |
| Border (Yes / No) | Borde (Sí / No) | settings.border |
| Colorspace | Espacio de color | settings.colorspace.label |
| Gray | Gris | settings.colorspace.grayscale |
| Colorful | Color | settings.colorspace.colorful |
| Rotate | Rotación | settings.rotate |
| Rotate Variance | Variación de rotación | settings.rotateVariance |
| Resolution | Resolución | settings.scale |
| Yellowish | Amarillento | settings.yellowish |
| Brightness | Brillo | settings.brightness |
| Contrast | Contraste | settings.contrast |
| Watermark | Marca de agua | extras.watermark |
| Watermark text / image | Texto de la marca de agua / Imagen de la marca de agua | extras.* |
| Stamp or signature | Sello o firma | extras.stamp |
| Add stamp or signature | Añadir sello o firma | extras.stampImage |
| Horizontal position / Vertical position / Size | Posición horizontal / Posición vertical / Tamaño | extras.* |
| Title / Author / Subject / Keywords / Producer / Creator | Título / Autor / Asunto / Palabras clave / Productor / Creador | extras.* |
| Remove | Quitar | extras.clearImage |
| Select or drop your file here | Selecciona o suelta tu archivo aquí | settings.pdfSelectLabel |
| Drop your file(s) here | Suelta tu archivo aquí / Suelta tus archivos aquí | upload.dropTitle* |
| Choose file(s) / Choose another file / Add more files | Elegir archivo / Elegir archivos / Elegir otro archivo / Añadir más archivos | upload.* |
| Processed in your browser — nothing is uploaded | Se procesa en tu navegador: no se sube nada | upload.privacy |
| Upload / Adjust / Download (steps) | Subir / Ajustar / Descargar | steps.* |
| Upload your files / Adjust the scan look / Get your scanned PDF | Sube tus archivos / Ajusta el aspecto escaneado / Obtén tu PDF escaneado | steps.*Title |
| Original / Scanned preview | Original / Vista previa escaneada | preview.* |
| Download again | Descargar de nuevo | save.downloadAgain |
| Download this scanned PDF | Descargar este PDF escaneado | files.downloadOne |
| Remove file | Quitar archivo | files.remove |
| Ready / Scanning… / Scanned | Listo / Escaneando… / Escaneado | files.status.* |
| Downloads folder | carpeta Descargas | save.whereSaved |

Blog chrome (`translations/es/chrome.json`): CTA buttons "Abrir la herramienta gratis →", "Añadir a Chrome gratis →",
"Más guías →"; header "Escanear un PDF", "Escaneo por lotes", "Guías"; "min de lectura"; "Actualizado:".

## 5. OS built-ins as named in the Spanish UI

| Feature | Spanish name / path |
|---|---|
| macOS Preview | **Vista Previa** |
| Preview export | Vista Previa → Archivo → Exportar… → Formato: PDF → **Filtro Quartz** |
| Preview "Export as PDF" | Archivo → Exportar como PDF… |
| Quartz filters | **Blanco y negro**, **Tono gris**, **Reducir tamaño del archivo** |
| macOS print to PDF | Archivo → Imprimir… → menú desplegable **PDF** → **Guardar como PDF** |
| Windows virtual printer | **Microsoft Print to PDF** (name unchanged in Spanish Windows) |
| Windows Photos app | **Fotos** → Imprimir → Microsoft Print to PDF |
| Windows/Edge print dialog color | **Color** → **Blanco y negro** |
| Chrome print preview | Imprimir (Ctrl+P) → Destino: **Guardar como PDF** → Color: **Blanco y negro** → Más ajustes |
| Microsoft Edge | Microsoft Edge (Imprimir → Impresora: Guardar como PDF / Microsoft Print to PDF) |
| Chrome developer tools | Más herramientas → **Herramientas para desarrolladores** → pestaña **Red** |
| Chrome side panel | **panel lateral** |
| Chrome Web Store | Chrome Web Store (unchanged) |
| Microsoft Word export | Archivo → Guardar como → **PDF (*.pdf)**; or Archivo → Exportar → Crear documento PDF/XPS |
| Excel export | Archivo → Guardar como → PDF |
| Google Docs export | Archivo → Descargar → **Documento PDF (.pdf)** |
| iPhone Notes scan | App **Notas** → botón de la cámara → **Escanear documentos** |
| iPhone Files scan | App **Archivos** → menú (…) → **Escanear documentos** |
| iPhone/Android camera | **Cámara** |
| Downloads folder | **Descargas** (Windows and macOS) |

## 6. Keyword plan and slugs

Home page (`/es/`): main keyword **hacer que un pdf parezca escaneado** (H1 = "Hacer que un PDF parezca escaneado";
secondary: efecto escaneado pdf, convertir pdf a escaneado online, pdf con aspecto escaneado).
Blog index (`/es/blog/`): title "Hacer que un PDF parezca escaneado: guías y ajustes".

| en-slug | Local main keyword | Localized slug | Title |
|---|---|---|---|
| how-to-make-a-pdf-look-scanned | hacer que un pdf parezca escaneado | hacer-que-un-pdf-parezca-escaneado | Cómo hacer que un PDF parezca escaneado: 6 métodos gratis |
| make-a-document-look-scanned | hacer que un documento parezca escaneado | hacer-que-un-documento-parezca-escaneado | Hacer que un documento parezca escaneado: Word, Docs y fotos |
| pdf-to-scanned-pdf | convertir pdf a pdf escaneado | convertir-pdf-a-pdf-escaneado | Convertir PDF a PDF escaneado: aplanar y mantenerlo legible |
| what-is-a-scanned-pdf | pdf escaneado | que-es-un-pdf-escaneado | ¿Qué es un PDF escaneado? Copia escaneada vs. PDF digital |
| image-to-scanned-pdf | imagen a pdf escaneado | imagen-a-pdf-escaneado | Imagen a PDF escaneado: convierte un JPG o foto en escaneo |
| convert-color-pdf-to-black-and-white | convertir pdf a blanco y negro | convertir-pdf-a-blanco-y-negro | Convertir PDF a blanco y negro: 5 formas en Windows y Mac |
| scan-effect | efecto escaneado | efecto-escaneado | Efecto escaneado: por qué un documento parece escaneado |

Notes for body translators (qa_i18n checks the main keyword word-by-word, accents included):
- The `.lead` must contain every word of `main_keyword` (e.g. "convertir … pdf … escaneado"), ideally the
  exact phrase in the first sentence. At least 2 H2s must contain all its words.
- how-to-make-a-pdf-look-scanned: "Método 1: hacer que un PDF parezca escaneado en el navegador",
  FAQ "Hacer que un PDF parezca escaneado: preguntas frecuentes".
- pdf-to-scanned-pdf: "¿Cómo convertir un PDF a PDF escaneado en el navegador?",
  "¿Es seguro convertir un PDF a PDF escaneado online?", FAQ "Convertir PDF a PDF escaneado: preguntas frecuentes".
- convert-color-pdf-to-black-and-white: "Cómo convertir un PDF a color en blanco y negro",
  "Forma 1: convertir PDF a blanco y negro en el navegador" ("Way N" → "Forma N").
- what-is-a-scanned-pdf / image-to-scanned-pdf / scan-effect: keep "PDF escaneado" / "imagen a PDF escaneado" /
  "efecto escaneado" verbatim in the question headings, as the English does.
- Section ids, `#anchors`, internal hrefs (`/scan`, `/scan/bulk`, `/blog/<en-slug>/`) stay English.
