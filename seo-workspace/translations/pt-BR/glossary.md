# Glossário pt-BR — pdflookscanned.com

Language code `pt-BR`, URL path `/pt-br/`, market: **Brazil**. Every translator of this language must follow this
file together with `seo-workspace/translations/TRANSLATOR-GUIDE.md`. Interface labels must match
`lookscanned.io-main/src/locale/messages/pt-BR.json` exactly (section 5 below is generated from that file).

## 1. Keyword strategy: "escaneado" vs "digitalizado" (read first)

Brazilians use both words for "scanned". They are synonyms, but they sit in different search intents:

- **escaneado / escanear / escaneamento** — colloquial, the word people use for the *look* and the action:
  "fazer PDF parecer escaneado", "deixar documento com cara de escaneado", "escanear em lote". Used in the
  interface (Gerar PDF escaneado, Escanear em lote), on the home page and in the "look" articles
  (how-to, document, scan effect, black and white).
- **digitalizado / digitalizar / digitalização** — formal, the word of offices, government and OCR tools for the
  *file type* and the *copy*: "PDF digitalizado", "cópia digitalizada", "documento digitalizado". It is the main
  keyword family of `what-is-a-scanned-pdf`, `pdf-to-scanned-pdf` and `image-to-scanned-pdf`.

Rules:
1. Inside one article, use the family of that article's main keyword for "scanned PDF" (see section 7), and
   mention the synonym once early ("PDF digitalizado, também chamado de PDF escaneado") so both queries match.
2. When you quote an interface label, keep it exactly as in the app even if it uses the other word
   (e.g. in a "digitalizado" article the button is still **Gerar PDF escaneado**).
3. "scanned copy" (what an HR team, landlord or agency asks for) = **cópia digitalizada** in every article.
4. "scan effect" = **efeito de scanner** in every article (not "efeito de digitalização").
5. The QA checks the main keyword by words: every word of `main_keyword` must appear in the title, the H1, the
   first sentence of `.lead` and in at least two H2s. Phrase the H2s so the full keyword fits naturally
   (suggested H2 phrasings are in section 7).

## 2. Address form and style

- Address the reader as **você** (never "tu", never "o senhor"). Instructions in the imperative that goes with
  você: "Abra", "Solte", "Clique em", "Baixe", "Confira".
- Brazilian vocabulary only. Use: arquivo (not ficheiro), tela (not ecrã), celular (not telemóvel), baixar /
  download (not descarregar), usuário (not utilizador), cadastro (not registo), aplicativo / app, compartilhar,
  equipe, contato, fotocópia / cópia.
- **Never write "xerox"** for a photocopy, even though Brazilians say it: it is a brand name and the owner rule
  forbids brands. Use "fotocópia", "cópia" or "copiadora".
- Headings and titles in **sentence case** (only the first word and proper nouns capitalized), even where the
  English uses Title Case. Question headings stay questions.
- Short, direct sentences; answer-first paragraphs (40–60 words after each H2). No hype ("revolucionário").
- Brand: **Make PDF look scanned** stays in English. Refer to it as "a ferramenta gratuita Make PDF look scanned",
  "a ferramenta", "a extensão" (feminine). "Chrome Web Store" is feminine: "na Chrome Web Store".
- Expert quote attribution, exactly: `<cite><strong>Equipe Make PDF look scanned</strong> — criadores da
  ferramenta web e da extensão do Chrome</cite>`. The quote itself speaks as "nós" (we).
- Table of contents: `<nav class="toc" aria-label="Sumário"><h2>Sumário</h2>`. FAQ heading pattern:
  "<keyword>: perguntas frequentes".
- Menu paths keep the source's arrow: "Arquivo → Exportar". Quotation marks: straight double quotes as in the
  source ("cópia digitalizada"). Em dash — as in the source.
- Ethics callout title used on the home page: "Use a aparência de escaneado com honestidade". Courts = tribunais;
  agencies = órgãos públicos; a court filing = petição. US bodies (USCIS, IRS, NARA, FADGI, CM/ECF) keep their
  English names; you may add a short explanation in parentheses the first time.

## 3. Numbers, units, dates

- Decimal comma: 0,3 · 0,5° · 1,5× · 0,05–0,2 · 0,92. Thousands with a dot: 2.200 px, 10.000. Years without a
  separator: 2026.
- Ranges with an en dash and no spaces: 0,5–2°, 20–60 segundos, 300–400%. "−10° a 10°" for signed ranges.
- Units: 144 dpi, 300 ppi, 11 pt, 72 dpi × escala, 1 bit, 8 bits, 256 tons de cinza, 5 MB, 2× / 3× (keep the ×
  sign), 1° (degree sign attached), 300% (percent attached, as in the source).
- 0.75-inch margins = "margens de 0,75 polegada" (singular "polegada" below 2). A4 is the Brazilian standard;
  US Letter = "formato Carta (Letter)".
- Dates: "18 de setembro de 2026" (month in lowercase); numeric 18/09/2026. Times: "menos de 1 minuto",
  "10 segundos".
- Keyboard: Ctrl+P (Windows), Cmd+P / ⌘P (Mac).

## 4. Recurring terms EN → PT-BR

| English | pt-BR | Notes |
|---|---|---|
| scan (verb) | escanear | formal synonym: digitalizar |
| scan (noun, act or result) | escaneamento | formal: digitalização |
| scanned (look) | escaneado | "parecer escaneado", "com cara de escaneado" |
| make a PDF look scanned | fazer um PDF parecer escaneado | variant: deixar o PDF com cara de escaneado |
| scanned PDF | PDF escaneado / PDF digitalizado | family per article, see section 1 |
| scanned copy | cópia digitalizada | what offices ask for; "cópia escaneada" also fine |
| scanned document | documento digitalizado | "documento escaneado" in look articles |
| scan effect | efeito de scanner | never "efeito de digitalização" |
| scan look / scanned look | aparência de escaneado | colloquial: cara de escaneado |
| scanner | scanner (pl. scanners) | |
| flatbed scanner | scanner de mesa | |
| office scanner / copier | scanner de escritório / copiadora | |
| photocopy / photocopier | fotocópia / fotocopiadora | never "xerox" |
| fax look | aparência de fax / estilo fax | |
| digital PDF (born-digital) | PDF digital | "PDF nativo" once as synonym |
| image-only PDF | PDF só com imagens | |
| searchable PDF | PDF pesquisável | |
| text layer | camada de texto | |
| OCR | OCR (reconhecimento ótico de caracteres) | expand on first use |
| flatten / flattened | achatar / PDF achatado | noun: achatamento |
| rasterize / render / page image | rasterizar / renderizar / imagem da página | noun: rasterização |
| grayscale | escala de cinza | adj.: em escala de cinza; "tons de cinza" as variant |
| black and white | preto e branco | abbreviation P&B only in tight spaces |
| bitonal / pure black and white | bitonal (preto e branco puro, 1 bit) | |
| color (mode) | colorido / em cores | UI value: Colorido |
| colorspace | espaço de cor | UI label: Espaço de cor |
| bit depth | profundidade de bits | |
| skew / tilt | inclinação / inclinar | "leve inclinação" |
| rotation | rotação | UI label: Rotação |
| rotation variance | variação da rotação | UI label: Variação da rotação |
| noise | ruído | UI label: Ruído |
| grain (adj. with grain) | granulação (adj. granulado) | |
| blur | desfoque | UI label: Desfoque |
| soft focus / sharpness | foco suave / nitidez | |
| moiré | moiré (padrão moiré) | |
| halftone | retícula (meio-tom) | |
| paper tone | tom do papel | |
| yellowish / aged paper | amarelado / papel envelhecido | UI label: Amarelado |
| brightness / contrast | brilho / contraste | UI labels: Brilho, Contraste |
| border (1-px frame line) | borda (linha fina de borda) | UI label: Borda (Sim/Não) |
| edge shadows | sombras nas bordas | not a tool feature |
| creases, folds, coffee stains | vincos, dobras, manchas de café | not tool features |
| perspective warp | distorção de perspectiva | not a tool feature |
| JPEG artifacts / compression | artefatos de JPEG / compressão | |
| resolution | resolução | UI label: Resolução |
| dpi / ppi | dpi / ppi | pontos por polegada / pixels por polegada |
| file size | tamanho do arquivo | "arquivo leve / pesado" |
| preset / recipe | predefinição / receita | |
| settings / default | configurações / padrão | in prose "ajustes" is acceptable |
| slider | controle deslizante | |
| live preview | prévia ao vivo | "prévia em tempo real" as variant |
| bulk scan | Escanear em lote (feature) | generic: escaneamento em lote, "em lote" = batch |
| side panel | painel lateral | |
| Chrome extension | extensão do Chrome | |
| web tool / browser | ferramenta web / navegador | "ferramenta online" as variant |
| upload / nothing is uploaded | enviar / nada é enviado | "sem upload" only in snippets |
| download (verb / noun) | baixar / download | |
| signup / free | cadastro / grátis, gratuito(a) | "sem cadastro" |
| local processing / progressive web app | processamento local / aplicativo web progressivo (PWA) | |
| watermark | marca d'água | UI label: Marca d'água |
| stamp / signature / e-signature | carimbo / assinatura / assinatura eletrônica | UI label: Carimbo ou assinatura |
| metadata | metadados | UI label: Metadados do PDF |
| form fields | campos de formulário | |
| screen reader / accessibility | leitor de tela / acessibilidade | |
| print dialog / print to PDF | caixa de diálogo de impressão / imprimir em PDF | |
| phone photo / phone scanner app | foto do celular / app de scanner no celular | never name an app |
| raster image editor | editor de imagens rasterizadas | never name one |
| desktop PDF software | programa de PDF para computador | never name one |
| trust badge "rated 5 stars in the Chrome Web Store" | nota 5 estrelas na Chrome Web Store | in prose: "a extensão, avaliada com 5 estrelas na Chrome Web Store" |

## 5. Interface labels (exact text in pt-BR.json)

Quote these exactly when the text names a button, slider or option. Generated from
`lookscanned.io-main/src/locale/messages/pt-BR.json` (long descriptive sentences omitted).

| Key | English | pt-BR (exact) |
|---|---|---|
| `base.title` | Make PDF look scanned | Make PDF look scanned |
| `base.scanTitle` | Scan | Escanear |
| `base.bulkTitle` | Bulk Scan | Escanear em lote |
| `base.serviceWorker.offlineReady` | App ready to work offline | App pronto para funcionar offline |
| `base.serviceWorker.needRefresh` | New version available, click to refresh. | Nova versão disponível. Clique para atualizar. |
| `base.nav.home` | Home | Início |
| `base.nav.scan` | Scan | Escanear |
| `base.nav.bulk` | Bulk Scan | Escanear em lote |
| `base.nav.guides` | Guides | Guias |
| `base.chrome.label` | Chrome Extension | Extensão do Chrome |
| `base.chrome.free` | FREE | GRÁTIS |
| `base.landing.headline` | Make PDF look scanned | Fazer PDF parecer escaneado |
| `base.landing.cta` | Convert to Scanned PDF | Converter em PDF escaneado |
| `base.landing.note` | Free · No signup · Files stay on your device | Grátis · Sem cadastro · Os arquivos ficam no seu dispositivo |
| `base.landing.points.formats` | PDF, images and Office-lite formats | PDF, imagens e formatos básicos do Office |
| `base.landing.points.local` | Local processing · Source files stay put | Processamento local · Os arquivos não saem do dispositivo |
| `base.landing.points.free` | Scanning is free · No signup | Escanear é grátis · Sem cadastro |
| `base.landing.points.preview` | Real-time preview · What you see is what you export | Prévia em tempo real · O que você vê é o que você exporta |
| `base.landing.stepsTitle` | Three steps to a scanned PDF | Três passos para um PDF escaneado |
| `base.landing.step1Title` | Choose a file | Escolha um arquivo |
| `base.landing.step2Title` | Adjust the scan effect | Ajuste o efeito de scanner |
| `base.landing.step3Title` | Export the PDF | Exporte o PDF |
| `base.landing.featuresTitle` | Key features | Principais recursos |
| `base.language` | Language | Idioma |
| `features.privacy.title` | Private, local processing | Processamento local e privado |
| `features.speed.title` | Fast conversion | Conversão rápida |
| `features.customization.title` | Scan effects | Efeitos de scanner |
| `features.openSource.title` | Chrome extension | Extensão do Chrome |
| `features.openSource.github` | Chrome Web Store | Chrome Web Store |
| `features.openSource.scanyourpdf` | Chrome extension | Extensão do Chrome |
| `features.mobileFriendly.title` | Works on phones | Funciona no celular |
| `features.offlineUse.title` | Works offline | Funciona offline |
| `actions.navigateToScan` | Start scanning | Começar a escanear |
| `actions.navigateToHomePage` | Home | Início |
| `actions.navigateToSupportMe` | Chrome Extension | Extensão do Chrome |
| `actions.backToIndex` | Back | Voltar |
| `actions.preview` | Preview | Prévia |
| `actions.save` | Save | Salvar |
| `actions.generateScannedPDF` | Generate Scanned PDF | Gerar PDF escaneado |
| `actions.generating` | Generating... | Gerando... |
| `actions.downloadScannedPDF` | Download Scanned PDF | Baixar PDF escaneado |
| `actions.generateSuccess` | Successfully generated | Gerado com sucesso |
| `actions.generateError` | Failed to generate: | Falha ao gerar: |
| `actions.addFiles` | Add files | Adicionar arquivos |
| `actions.processAll` | Generate scanned PDFs | Gerar PDFs escaneados |
| `actions.downloadZip` | Download all as ZIP | Baixar tudo em ZIP |
| `actions.converting` | Preparing file… | Preparando o arquivo… |
| `actions.queued` | Queued | Na fila |
| `actions.done` | Done | Concluído |
| `actions.failed` | Failed | Falhou |
| `settings.settings` | Scan Settings | Configurações de escaneamento |
| `settings.attenuate` | Noise | Ruído |
| `settings.noise` | Noise | Ruído |
| `settings.blur` | Blur | Desfoque |
| `settings.border.label` | Border | Borda |
| `settings.border.true` | Yes | Sim |
| `settings.border.false` | No | Não |
| `settings.colorspace.label` | Colorspace | Espaço de cor |
| `settings.colorspace.colorful` | Colorful | Colorido |
| `settings.colorspace.grayscale` | Gray | Cinza |
| `settings.rotate` | Rotate | Rotação |
| `settings.rotateVariance` | Rotate Variance | Variação da rotação |
| `settings.pdfSelectLabel` | Select or drop your file here | Selecione ou arraste seu arquivo para cá |
| `settings.pdfNoSelectMessage` | No file selected | Nenhum arquivo selecionado |
| `settings.supportedHint` | PDF, JPG, PNG, WebP, SVG, DOCX, XLSX, CSV, TXT, MD, HTML | PDF, JPG, PNG, WebP, SVG, DOCX, XLSX, CSV, TXT, MD, HTML |
| `settings.scale` | Resolution | Resolução |
| `settings.yellowish` | Yellowish | Amarelado |
| `settings.brightness` | Brightness | Brilho |
| `settings.contrast` | Contrast | Contraste |
| `settings.extras.watermark` | Watermark | Marca d'água |
| `settings.extras.watermarkText` | Watermark text | Texto da marca d'água |
| `settings.extras.watermarkImage` | Watermark image | Imagem da marca d'água |
| `settings.extras.stamp` | Stamp or signature | Carimbo ou assinatura |
| `settings.extras.stampImage` | Add stamp or signature | Adicionar carimbo ou assinatura |
| `settings.extras.stampX` | Horizontal position | Posição horizontal |
| `settings.extras.stampY` | Vertical position | Posição vertical |
| `settings.extras.stampScale` | Size | Tamanho |
| `settings.extras.metadata` | PDF metadata | Metadados do PDF |
| `settings.extras.title` | Title | Título |
| `settings.extras.author` | Author | Autor |
| `settings.extras.subject` | Subject | Assunto |
| `settings.extras.keywords` | Keywords | Palavras-chave |
| `settings.extras.producer` | Producer | Produtor |
| `settings.extras.creator` | Creator | Criador |
| `settings.extras.clearImage` | Remove | Remover |
| `status.notStarted` | Not started | Não iniciado |
| `status.error` | Error: {error} | Erro: {error} |
| `status.finished` | Finished | Concluído |
| `status.processsing.default` | Processing | Processando |
| `status.processsing.combine` | Combining PDF pages | Juntando as páginas do PDF |
| `status.processsing.progress` | Processing PDF pages: {current}/{total} | Processando páginas do PDF: {current}/{total} |
| `upload.dropTitle` | Drop your file here | Solte seu arquivo aqui |
| `upload.dropTitleMany` | Drop your files here | Solte seus arquivos aqui |
| `upload.or` | or | ou |
| `upload.choose` | Choose file | Escolher arquivo |
| `upload.chooseMany` | Choose files | Escolher arquivos |
| `upload.replace` | Choose another file | Escolher outro arquivo |
| `upload.addMore` | Add more files | Adicionar mais arquivos |
| `upload.privacy` | Processed in your browser — nothing is uploaded | Processado no seu navegador — nada é enviado |
| `upload.dropOverlay` | Drop the file to load it | Solte o arquivo para carregá-lo |
| `upload.dropOverlayMany` | Drop the files to add them | Solte os arquivos para adicioná-los |
| `upload.unsupported` | This file type is not supported: {name} | Tipo de arquivo não suportado: {name} |
| `upload.readError` | Could not open {name}: {error} | Não foi possível abrir {name}: {error} |
| `upload.ready` | Loaded | Carregado |
| `upload.pages` | {n} page \| {n} pages | {n} página \| {n} páginas |
| `save.create` | Create scanned PDF \| Create {n} scanned PDFs | Criar PDF escaneado \| Criar {n} PDFs escaneados |
| `save.readyTitle` | Your scanned PDF is ready \| Your {n} scanned PDFs are ready | Seu PDF escaneado está pronto \| Seus {n} PDFs escaneados estão prontos |
| `save.progress` | page {current} of {total} | página {current} de {total} |
| `save.fileProgress` | File {current} of {total} | Arquivo {current} de {total} |
| `save.noFileHint` | Upload a file in step 1 to start. | Carregue um arquivo no passo 1 para começar. |
| `save.downloadAgain` | Download again | Baixar novamente |
| `save.downloadStarted` | Done — the download has started | Pronto — o download começou |
| `save.whereSaved` | Look for it in your Downloads folder. | Procure o arquivo na pasta Downloads. |
| `save.zipHint` | To get a single file, use the download icon next to it in step 1. | Para baixar um único arquivo, use o ícone de download ao lado dele no passo 1. |
| `save.someFailed` | {n} file could not be scanned \| {n} files could not be scanned | {n} arquivo não pôde ser escaneado \| {n} arquivos não puderam ser escaneados |
| `files.preview` | Show in preview | Mostrar na prévia |
| `files.previewOf` | Preview: {name} | Prévia: {name} |
| `files.downloadOne` | Download this scanned PDF | Baixar este PDF escaneado |
| `files.remove` | Remove file | Remover arquivo |
| `files.hint` | Click a file to preview it. All files use the same settings. | Clique em um arquivo para ver a prévia. Todos os arquivos usam as mesmas configurações. |
| `files.openError` | Could not open this file | Não foi possível abrir este arquivo |
| `files.status.loading` | Preparing… | Preparando… |
| `files.status.ready` | Ready | Pronto |
| `files.status.processing` | Scanning… | Escaneando… |
| `files.status.done` | Scanned | Escaneado |
| `steps.upload` | Upload | Carregar |
| `steps.adjust` | Adjust | Ajustar |
| `steps.download` | Download | Baixar |
| `steps.uploadTitle` | Upload your files | Carregue seus arquivos |
| `steps.adjustTitle` | Adjust the scan look | Ajuste o efeito de scanner |
| `steps.downloadTitle` | Get your scanned PDF | Baixe seu PDF escaneado |
| `preview.original` | Original | Original |
| `preview.scanned` | Scanned preview | Prévia escaneada |
| `errors.wordNoText` | This Word file has no readable text | Este arquivo do Word não tem texto legível |
| `errors.sheetEmpty` | This spreadsheet is empty | Esta planilha está vazia |
| `errors.htmlNoText` | This HTML file has no readable text | Este arquivo HTML não tem texto legível |
| `errors.unsupportedType` | This file type is not supported yet | Este tipo de arquivo ainda não é suportado |

In running text, write labels in bold or as plain text with the exact capitalization above, e.g. "clique em
**Gerar PDF escaneado**", "deixe o **Espaço de cor** em **Cinza**", "ative a **Borda** (**Sim**)",
"use **Escanear em lote** e depois **Baixar tudo em ZIP**". Slider values use the decimal comma: "Ruído 0,1",
"Desfoque 0,3", "Rotação 1°", "Variação da rotação 0,5°", "Amarelado 0,2", "Resolução 2×".

## 6. OS and browser built-ins as named in Brazilian Portuguese

| English | pt-BR UI name |
|---|---|
| macOS Preview | Pré-Visualização (app do macOS) |
| Preview: File → Export… / Export as PDF… | Arquivo → Exportar... / Exportar como PDF... |
| Quartz Filter (menu) | Filtro Quartz |
| Quartz filters: Black & White / Gray Tone / Reduce File Size | Preto e Branco / Tom de Cinza / Reduzir Tamanho do Arquivo |
| Preview: View → Thumbnails | Visualizar → Miniaturas |
| macOS print dialog: File → Print… → PDF → Save as PDF | Arquivo → Imprimir... → PDF → Salvar como PDF |
| macOS Downloads folder | Downloads |
| Windows "Microsoft Print to PDF" | Microsoft Print to PDF (name unchanged) |
| Windows print dialog / Printer properties / Preferences | Imprimir / Propriedades da impressora / Preferências |
| Windows color option: Color / Black and white / Grayscale | Cor / Preto e branco / Escala de cinza |
| Windows Photos app | Fotos |
| Windows File Explorer | Explorador de Arquivos |
| Microsoft Word: File → Save As → PDF | Arquivo → Salvar como → PDF (*.pdf) |
| Microsoft Word: File → Export → Create PDF/XPS | Arquivo → Exportar → Criar documento PDF/XPS |
| Microsoft Excel: File → Save As → PDF | Arquivo → Salvar como → PDF (*.pdf) |
| Google Docs: File → Download → PDF document (.pdf) | Arquivo → Fazer o download → Documento PDF (.pdf) |
| Chrome print: Destination → Save as PDF | Destino → Salvar como PDF |
| Chrome print: Color → Black and white / More settings | Cor → Preto e branco / Mais configurações |
| Chrome: More tools → Developer tools → Network tab | Mais ferramentas → Ferramentas do desenvolvedor → guia Rede |
| Chrome side panel | painel lateral |
| Chrome Web Store install button "Add to Chrome" | Usar no Chrome (store button); our own CTA text is "Adicionar ao Chrome — grátis" |
| Microsoft Edge print: Save as PDF / Black and white | Salvar como PDF / Preto e branco |
| iPhone Notes → Scan Documents | Notas → Escanear Documentos |
| iPhone Files app → Scan Documents | Arquivos → Escanear Documentos |
| iPhone / Android Camera, Photos | Câmera, Fotos |

## 7. Pages: main keyword, localized slug, title

| en-slug | Local main keyword | Localized slug | Title (pt-BR) |
|---|---|---|---|
| (home `/pt-br/`) | fazer pdf parecer escaneado | — | Fazer PDF parecer escaneado online — grátis e sem upload |
| (blog index) | fazer pdf parecer escaneado | — | Fazer PDF parecer escaneado: guias, ajustes e tutoriais |
| how-to-make-a-pdf-look-scanned | fazer um pdf parecer escaneado | como-fazer-pdf-parecer-escaneado | Como fazer um PDF parecer escaneado: 6 métodos grátis |
| make-a-document-look-scanned | documento com cara de escaneado | documento-com-cara-de-escaneado | Documento com cara de escaneado: Word, Google Docs e fotos |
| pdf-to-scanned-pdf | converter pdf para pdf digitalizado | converter-pdf-para-pdf-digitalizado | Converter PDF para PDF digitalizado: achatar, DPI e tamanho |
| what-is-a-scanned-pdf | pdf digitalizado | o-que-e-pdf-digitalizado | O que é PDF digitalizado? Cópia digitalizada x PDF digital |
| image-to-scanned-pdf | transformar imagem em pdf digitalizado | transformar-imagem-em-pdf-digitalizado | Transformar imagem em PDF digitalizado: JPG, PNG e fotos |
| convert-color-pdf-to-black-and-white | converter pdf colorido para preto e branco | converter-pdf-colorido-preto-e-branco | Converter PDF colorido para preto e branco: 5 formas grátis |
| scan-effect | efeito de scanner | efeito-de-scanner | Efeito de scanner: o que faz um documento parecer escaneado |

Term family and suggested keyword H2s per article (adapt freely; keep them ≤ 70 characters):

- **how-to-make-a-pdf-look-scanned** — family "escaneado". Methods are "Método 1 … 6". H2 ideas: "Qual é a forma
  mais rápida de fazer um PDF parecer escaneado?", "Método 1: fazer um PDF parecer escaneado no navegador",
  "Fazer um PDF parecer escaneado: perguntas frequentes".
- **make-a-document-look-scanned** — family "escaneado"; "make it look scanned" = "deixar com cara de escaneado".
  H2 ideas: "Como deixar um documento com cara de escaneado?", "Como deixar um documento do Word com cara de
  escaneado", "Documento com cara de escaneado: perguntas frequentes".
- **pdf-to-scanned-pdf** — family "digitalizado" (PDF digitalizado). H2 ideas: "Como converter PDF para PDF
  digitalizado no navegador?", "Como converter vários PDFs para PDF digitalizado de uma vez?", "Converter PDF para
  PDF digitalizado: perguntas frequentes".
- **what-is-a-scanned-pdf** — family "digitalizado"; "scanned copy" = "cópia digitalizada". H2 ideas: "O que é um
  PDF digitalizado, exatamente?", "Como um PDF digitalizado difere de um PDF digital?", "PDF digitalizado: o que
  mais as pessoas perguntam?".
- **image-to-scanned-pdf** — family "digitalizado"; photo = "foto do celular". H2 ideas: "Qual é o jeito mais
  rápido de transformar imagem em PDF digitalizado?", "Como transformar uma imagem em PDF digitalizado?",
  "Transformar imagem em PDF digitalizado: perguntas frequentes".
- **convert-color-pdf-to-black-and-white** — "Way 1…5" = "Forma 1 … 5". H2 ideas: "Como converter PDF colorido
  para preto e branco", "Forma 2: converter PDF colorido para preto e branco no Mac", "Qual forma usar para
  converter PDF colorido para preto e branco?".
- **scan-effect** — family "escaneado"; "5 looks" = "5 estilos". H2 ideas: "O que é efeito de scanner?",
  "Efeito de scanner: qual controle faz o quê", "Configurações de efeito de scanner para 5 estilos",
  "Efeito de scanner: perguntas frequentes".

Internal link anchor texts: use the localized titles above (or natural parts of them); keep the English hrefs
(`/blog/<en-slug>/`, `/scan`, `/scan/bulk`) — the builder rewrites them.
