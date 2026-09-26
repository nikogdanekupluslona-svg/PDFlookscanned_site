# Glossary — Norwegian Bokmål (`no`, market: Norway)

Use this file for every Norwegian page (home guide, UI, blog chrome, 7 articles) so all texts agree.
Interface labels must match `lookscanned.io-main/src/locale/messages/no.json` character for character.

## Address form and style

- **Bokmål**, moderate/conservative forms that tech sites use: `-en` for feminine nouns (siden, boken — not sida, boka),
  `-et` past tense (skannet, lagret — not skanna, lagra).
- Address the reader as **du** (du/deg/din). The team speaks as **vi**. Never "De".
- Verb for scanning: **skanne** (skanner, skannet, har skannet), noun **skanning** (the act or the result), device **skanner**.
  Always with *k* (Språkrådet norm). Never "scanne/scannet" in running text.
- Inflection of the key adjective: **en skannet PDF** · **den skannede PDF-en** · **skannede PDF-er**. PDF is masculine:
  en PDF, PDF-en, PDF-er, PDF-ene; PDF-fil, PDF-side. Abbreviations take the ending after a hyphen (PDF-en, ZIP-filen, OCR-en).
- Headings in **sentence case** (only the first word and proper names capitalized), also where the English source uses
  Title Case. Keep question headings as questions. Norwegian how-to heading pattern: "Slik …" (not "Hvordan å …").
- Short, plain sentences; no anglicisms or calques. "klikk på" (desktop), "trykk på" (phone), "slipp inn" / "dra og slipp"
  (drop in), "last opp" / "last ned" (upload / download). Avoid "anvende", "generere" in running text (use "lage", "bruke").
- Quotation marks: **« »** (inner: ‘ ’). Parenthetical dash: spaced en dash **" – "**. Ranges: unspaced en dash **0,5–2°**.
  Menu paths with arrows: **Arkiv → Eksporter …**.
- Brand **Make PDF look scanned** stays in English and is not inflected: "verktøyet Make PDF look scanned",
  "teamet bak Make PDF look scanned". Expert quote cite: `<strong>Teamet bak Make PDF look scanned</strong> — utviklerne av nettverktøyet og Chrome-utvidelsen`.
- Standard section names: Table of Contents → **Innhold**; FAQ heading pattern → "…: ofte stilte spørsmål";
  ethics callout heading → "Bruk skanneutseendet ærlig" (or similar short heading).
- Never name competitors or third-party apps (see `seo-workspace/qa.py` → FORBIDDEN). Chrome's store is called
  **Chrome Nettmarked** in the Norwegian UI.

## Numbers, dates and units

| Item | Norwegian convention | Example |
|---|---|---|
| Decimal separator | comma | 0,3 · 0,05–0,2 · 1,5× |
| Thousands separator | (non-breaking) space | 2 200 px · 10 000 sider |
| Percent | space before % | 300–400 % |
| Degrees | no space | 1° · −10° til 10° · 0,5°–2° |
| Multiplier | × symbol, no space | 2× · 1×–3× |
| Resolution | lowercase "dpi", space before | 144 dpi · 300 dpi |
| Dates | day-period-month (lowercase)-year | 18. september 2026 |
| Months | januar, februar, mars, april, mai, juni, juli, august, september, oktober, november, desember | |
| Time | kl. 14.30 | |
| Paper | A4 is the Norwegian standard; "Letter" is the US format ("amerikansk Letter-format") | |
| Inches | keep the fact; you may add cm in parentheses | 0,75 tommer (1,9 cm) |
| Font size | pt | 11 pt |
| "10+ minutes" | 30+ minutter | |

## Recurring terms EN → NO

| English | Norwegian | Notes |
|---|---|---|
| make a PDF look scanned | få en PDF til å se skannet ut | core phrase; "få PDF til å se skannet ut" in home/headlines |
| scanned-looking PDF | PDF som ser skannet ut | "en PDF som ser skannet ut," |
| scan effect | skanneeffekt | def. skanneeffekten; pl. skanneeffekter |
| scan look / scanned look | skanneutseende / skannet utseende | |
| scanned PDF | skannet PDF | den skannede PDF-en; skannede PDF-er |
| scanned copy | skannet kopi | what HR/landlords ask for |
| scanned document | skannet dokument | |
| digital (born-digital) PDF | digital PDF | "digitalt opprettet PDF" when contrast matters |
| image-only PDF / image-based PDF | PDF med bare bilder / bildebasert PDF | |
| searchable PDF | søkbar PDF | "PDF med søkbar tekst" |
| text layer | tekstlag | "skjult tekstlag" (hidden) |
| OCR | OCR (optisk tegngjenkjenning) | expand once per page |
| flatten / flattening | flate ut / utflating | "flatet ut", "en flat PDF" |
| rasterize / rasterization | rasterisere / rasterisering | |
| render a page as an image / page image | gjengi siden som bilde / sidebilde | |
| grayscale | gråtoner | "i gråtoner", "PDF i gråtoner" |
| black and white | svart-hvitt | "kopi i svart-hvitt", "svart-hvit utskrift" |
| bitonal / 1-bit | bitonal (rent svart-hvitt, 1 bit) | |
| color PDF | farge-PDF | pl. farge-PDF-er |
| colorspace | fargerom | UI label: Fargerom |
| bit depth | bitdybde | |
| skew / tilt | skråstilling (adj. skjev, skråstilt) | "skråstille siden" |
| rotation | rotasjon | |
| rotation variance (per page) | rotasjonsvariasjon | UI label: Rotasjonsvariasjon |
| noise | støy | |
| grain / speckles | korn (kornete) / prikker | |
| blur | uskarphet | |
| soft focus / sharpness | mykt fokus / skarphet | |
| brightness / contrast | lysstyrke / kontrast | UI labels: Lysstyrke, Kontrast |
| paper tone | papirtone | |
| yellowish / aged paper | gultone / gulnet papir | UI label: Gultone |
| border (thin scanner-edge line) | ramme (tynn kantlinje) | UI label: Ramme |
| edge shadow | kantskygge | not a tool feature |
| creases, folds, coffee stains | bretter, brettemerker, kaffeflekker | not tool features |
| perspective warp | perspektivforvrengning | not a tool feature |
| moiré | moaré | "moarémønster" |
| halftone | halvtone (rastermønster) | |
| JPEG artifacts / compression | JPEG-artefakter (JPEG-blokker) / komprimering | |
| artifact (scan flaw) | artefakt | pl. artefakter |
| resolution | oppløsning | UI label: Oppløsning |
| dpi / ppi | dpi (punkter per tomme) / ppi (piksler per tomme) | |
| file size | filstørrelse | |
| flatbed scanner | flatbedskanner | |
| document feeder | dokumentmater | |
| photocopy / photocopier | fotokopi / kopimaskin | "kopimaskinpreg" = photocopier look |
| fax / fax look | faks / fakspreg | |
| print / printout / printer / print dialog | skrive ut / utskrift / skriver / utskriftsdialog | |
| look / preset / recipe | stil / oppsett (forhåndsinnstilling) / oppskrift | "5 stiler", "5 oppsett for skanneeffekt" |
| bulk scan | masseskanning | UI + nav label: Masseskanning |
| live preview | forhåndsvisning i sanntid | |
| slider | glidebryter | |
| side panel | sidepanel | |
| Chrome extension | Chrome-utvidelse | |
| Chrome Web Store | Chrome Nettmarked | Norwegian name in Chrome's UI |
| trust badge: "rated 5 stars in the Chrome Web Store" | vurdert til 5 stjerner i Chrome Nettmarked | fixed wording |
| web tool / browser tool | nettverktøy / nettleserverktøy | |
| processed locally, not uploaded | behandles lokalt i nettleseren, lastes ikke opp til en (behandlings)server | |
| free, no signup | gratis, uten registrering | |
| offline | uten nett | "fungerer uten nett" |
| progressive web app | progressiv nettapp (PWA) | |
| watermark / stamp / signature / e-signature | vannmerke / stempel / signatur / elektronisk signatur | |
| metadata | metadata | "PDF-metadata" |
| screen reader / accessibility | skjermleser / tilgjengelighet (universell utforming) | |
| raster image editor | bilderedigeringsprogram | never name products |
| phone scanner app | skanneapp på mobilen | never name products |
| desktop PDF software | PDF-program for datamaskin | never name products |
| court / agency / filing; landlord / HR | domstol / etat / innsending; utleier / HR | US agencies/courts keep English names |

## Interface labels (exactly as in `messages/no.json`)

| Key | English | Norwegian |
|---|---|---|
| base.title | Make PDF look scanned | Make PDF look scanned |
| base.scanTitle / nav.scan | Scan | Skann |
| base.bulkTitle / nav.bulk | Bulk Scan | Masseskanning |
| nav.home | Home | Hjem |
| nav.guides | Guides | Guider |
| chrome.label | Chrome Extension | Chrome-utvidelse |
| chrome.free | FREE | GRATIS |
| landing.headline (home H1) | Make PDF look scanned | Få PDF til å se skannet ut |
| landing.cta | Convert to Scanned PDF | Konverter til skannet PDF |
| landing.stepsTitle | Three steps to a scanned PDF | Tre steg til en skannet PDF |
| landing.step1Title / step2Title / step3Title | Choose a file / Adjust the scan effect / Export the PDF | Velg en fil / Juster skanneeffekten / Eksporter PDF-en |
| landing.featuresTitle | Key features | Hovedfunksjoner |
| language | Language | Språk |
| actions.navigateToScan | Start scanning | Start skanning |
| actions.backToIndex | Back | Tilbake |
| actions.preview | Preview | Forhåndsvis |
| actions.save | Save | Lagre |
| actions.generateScannedPDF | Generate Scanned PDF | **Lag skannet PDF** |
| actions.generating | Generating... | Lager … |
| actions.downloadScannedPDF | Download Scanned PDF | Last ned skannet PDF |
| actions.generateSuccess | Successfully generated | PDF-en er laget |
| actions.addFiles | Add files | Legg til filer |
| actions.processAll | Generate scanned PDFs | Lag skannede PDF-er |
| actions.downloadZip | Download all as ZIP | **Last ned alle som ZIP** |
| actions.converting | Preparing file… | Klargjør filen … |
| actions.queued / done / failed | Queued / Done / Failed | I kø / Ferdig / Mislyktes |
| settings.settings | Scan Settings | Skanneinnstillinger |
| settings.noise (and attenuate) | Noise | Støy |
| settings.blur | Blur | Uskarphet |
| settings.rotate | Rotate | Rotasjon |
| settings.rotateVariance | Rotate Variance | Rotasjonsvariasjon |
| settings.yellowish | Yellowish | Gultone |
| settings.brightness | Brightness | Lysstyrke |
| settings.contrast | Contrast | Kontrast |
| settings.scale | Resolution | Oppløsning |
| settings.colorspace.label | Colorspace | Fargerom |
| settings.colorspace.grayscale | Gray | Gråtoner |
| settings.colorspace.colorful | Colorful | Farge |
| settings.border.label | Border | Ramme |
| settings.border.true / false | Yes / No | Ja / Nei |
| settings.pdfSelectLabel | Select or drop your file here | Velg eller slipp filen her |
| settings.pdfNoSelectMessage | No file selected | Ingen fil valgt |
| settings.extras.watermark | Watermark | Vannmerke |
| settings.extras.watermarkText | Watermark text | Vannmerketekst |
| settings.extras.watermarkImage | Watermark image | Vannmerkebilde |
| settings.extras.stamp | Stamp or signature | Stempel eller signatur |
| settings.extras.stampImage | Add stamp or signature | Legg til stempel eller signatur |
| settings.extras.stampX / stampY | Horizontal position / Vertical position | Vannrett posisjon / Loddrett posisjon |
| settings.extras.stampScale | Size | Størrelse |
| settings.extras.metadata | PDF metadata | PDF-metadata |
| settings.extras.title / author / subject / keywords | Title / Author / Subject / Keywords | Tittel / Forfatter / Emne / Nøkkelord |
| settings.extras.producer / creator | Producer / Creator | Produsent / Program |
| settings.extras.clearImage | Remove | Fjern |
| upload.dropTitle / dropTitleMany | Drop your file here / Drop your files here | Slipp filen her / Slipp filene her |
| upload.choose / chooseMany | Choose file / Choose files | Velg fil / Velg filer |
| upload.replace | Choose another file | Velg en annen fil |
| upload.addMore | Add more files | Legg til flere filer |
| upload.privacy | Processed in your browser — nothing is uploaded | Behandles i nettleseren – ingenting lastes opp |
| upload.ready | Loaded | Lastet inn |
| upload.pages | {n} page / {n} pages | {n} side / {n} sider |
| save.create (main button) | Create scanned PDF / Create {n} scanned PDFs | **Lag skannet PDF** / Lag {n} skannede PDF-er |
| save.readyTitle | Your scanned PDF is ready | Den skannede PDF-en er klar |
| save.downloadAgain | Download again | Last ned igjen |
| save.downloadStarted | Done — the download has started | Ferdig – nedlastingen har startet |
| save.whereSaved | Look for it in your Downloads folder. | Du finner den i mappen Nedlastinger. |
| files.preview | Show in preview | Vis i forhåndsvisningen |
| files.downloadOne | Download this scanned PDF | Last ned denne skannede PDF-en |
| files.remove | Remove file | Fjern filen |
| files.status.* | Preparing… / Ready / Scanning… / Scanned | Klargjør … / Klar / Skanner … / Skannet |
| steps.upload / adjust / download | Upload / Adjust / Download | Last opp / Juster / Last ned |
| steps.uploadTitle | Upload your files | Last opp filene dine |
| steps.adjustTitle | Adjust the scan look | Juster skanneutseendet |
| steps.downloadTitle | Get your scanned PDF | Hent den skannede PDF-en |
| preview.original / scanned | Original / Scanned preview | Original / Skannet forhåndsvisning |
| features.openSource.github | Chrome Web Store | Chrome Nettmarked |

Notes for article writers:
- The English articles call the main button "Generate Scanned PDF"; in Norwegian always write **Lag skannet PDF**
  (this is also the text of the real button, `save.create`).
- Write slider names as labels when you refer to the control ("sett Støy til 0,1", "Fargerom: Gråtoner",
  "Rotasjonsvariasjon 0,5°"); in general prose lowercase is fine ("litt støy og uskarphet").

## OS and app built-ins (names in the Norwegian UI)

| English | Norwegian UI | Notes |
|---|---|---|
| macOS Preview | Forhåndsvisning | "Forhåndsvisning på Mac" |
| Preview: File → Export… | Arkiv → Eksporter … | macOS calls the File menu "Arkiv" |
| Export as PDF… | Eksporter som PDF … | |
| Quartz Filter | Quartz-filter | options: Svart-hvitt (Black & White), Gråtone (Gray Tone), Reduser filstørrelse (Reduce File Size) |
| Print… (⌘P) | Skriv ut … | |
| PDF menu → Save as PDF (macOS print dialog) | PDF → Arkiver som PDF | |
| Thumbnails sidebar | Miniatyrer | Forhåndsvisning → Vis → Miniatyrer |
| Downloads folder | Nedlastinger | same on Mac and Windows |
| Photos (macOS/iOS/Windows) | Bilder | |
| Microsoft Print to PDF | Microsoft Print to PDF | keeps its English name |
| Windows print dialog (Ctrl+P) | Skriv ut | |
| Color mode: Color / Black and white | Fargemodus: Farge / Svart-hvitt (some drivers: Gråtoner) | |
| Printing preferences | Utskriftsinnstillinger | |
| File Explorer | Filutforsker | |
| Snipping Tool | Utklippsverktøy | |
| Settings | Innstillinger | |
| Word: File → Save As → PDF | Fil → Lagre som → PDF (*.pdf) | source-format step only |
| Word: File → Export → Create PDF/XPS | Fil → Eksporter → Opprett PDF/XPS-dokument | |
| Excel: File → Save As → PDF | Fil → Lagre som → PDF | |
| Google Docs: File → Download → PDF Document (.pdf) | Fil → Last ned → PDF-dokument (.pdf) | plain instructions, no quotes |
| Chrome: Print → Destination: Save as PDF | Skriv ut → Mål: Lagre som PDF | |
| Chrome: More settings → Color | Flere innstillinger → Farge (Farge / Svart-hvitt) | |
| Chrome/Edge developer tools → Network tab | utviklerverktøy → fanen Nettverk | |
| Microsoft Edge: Print → Printer: Save as PDF | Skriv ut → Skriver: Lagre som PDF | |
| iPhone Notes → Scan Documents | Notater → Skann dokumenter | |
| iPhone/Android Files app | Filer | |
| Camera | Kamera | |
| iPhone: Settings → Camera → Formats → Most Compatible | Innstillinger → Kamera → Formater → Mest kompatibelt | HEIC → JPG |
| Share / Print (iOS) | Del / Skriv ut | |

## Keyword and slug plan

| en-slug | Local main keyword | Localized slug | Title |
|---|---|---|---|
| (home `/no/`) | få pdf til å se skannet ut | — | Få PDF til å se skannet ut på nett – gratis og privat |
| how-to-make-a-pdf-look-scanned | få en pdf til å se skannet ut | pdf-se-skannet-ut | Slik får du en PDF til å se skannet ut: 6 gratis metoder |
| make-a-document-look-scanned | få et dokument til å se skannet ut | dokument-se-skannet-ut | Få et dokument til å se skannet ut: Word, Google Docs, foto |
| pdf-to-scanned-pdf | pdf til skannet pdf | pdf-til-skannet-pdf | PDF til skannet PDF: konverter, flat ut og hold den lesbar |
| what-is-a-scanned-pdf | skannet pdf | hva-er-en-skannet-pdf | Hva er en skannet PDF? Skannet kopi vs. digital PDF |
| image-to-scanned-pdf | bilde til skannet pdf | bilde-til-skannet-pdf | Bilde til skannet PDF: fra JPG eller foto til skannet kopi |
| convert-color-pdf-to-black-and-white | konverter pdf til svart-hvitt | konverter-pdf-til-svart-hvitt | Konverter PDF til svart-hvitt: 5 gratis måter som fungerer |
| scan-effect | skanneeffekt | skanneeffekt-pdf | Skanneeffekt: hva som får et dokument til å se skannet ut |
| (blog index) | få pdf til å se skannet ut | — | Få PDF til å se skannet ut: guider, innstillinger og tips |

How `qa_i18n.py` matches the keyword in the lead and H2s: the exact phrase, **or** every word of it appearing as a
substring (case-insensitive). Practical consequences:
- "skannede" does **not** contain "skannet". Where the keyword must appear (title, H1, lead, 2+ H2s), use the
  form **skannet** ("en skannet PDF", "til skannet PDF"), not only "skannede PDF-er".
- "konverter" is contained in "konverterer/konvertere/konvertering", so "Slik konverterer du PDF til svart-hvitt" matches;
  always write **svart-hvitt** with a hyphen.
- "få" is contained in "får"; "bilde" in "bildet/bilder"; "dokument" in "dokumentet"; "skanneeffekt" in "skanneeffekten".

Internal link anchor texts (use these so the site agrees): "slik får du en PDF til å se skannet ut",
"få et dokument til å se skannet ut", "PDF til skannet PDF", "hva er en skannet PDF", "bilde til skannet PDF",
"slik konverterer du en farge-PDF til svart-hvitt", "innstillinger for skanneeffekt", "skanneren" (/scan),
"Masseskanning" (/scan/bulk).
