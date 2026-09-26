# Glossary: Dutch (nl), for the Netherlands and Flanders

Use this glossary for every Dutch page (app UI, home guide, blog chrome, the 7 articles) so the same thing is
always called by the same name. Interface labels must match `lookscanned.io-main/src/locale/messages/nl.json`
exactly.

## Address and style

- **Address the reader as "je/jij"** (informal, as on modern Dutch tool sites). Never "u". Possessive "je" ("je
  bestand"), stressed "jouw" only for contrast ("met jouw instellingen").
- Steps use the imperative: "Open de tool", "Sleep de PDF erin", "Klik op Gescande PDF maken".
- Short sentences, active voice, neutral Dutch that works in both NL and BE. Avoid Hollandisms that sound odd
  in Flanders (no "effe", "hartstikke") and avoid English filler ("basically", "actually").
- Answer first: each H2 opens with a direct 40–60-word answer paragraph.
- Headings use sentence case (only the first word and proper names get a capital): "Wat is een gescande PDF?".
  Keep questions as questions.
- **Brand:** "Make PDF look scanned" stays in English, never translated. Describe it as "de gratis tool", "onze
  gratis tool" or "de browsertool". Never write or target the old domain name as a keyword (see TRANSLATOR-GUIDE).
- No competitor or third-party product names (see `seo-workspace/qa.py` → FORBIDDEN). Say "een
  beeldbewerkingsprogramma", "een scan-app op je telefoon", "PDF-software voor de desktop".
- Honest-use callouts: factual, not preachy. Standard title: "Gebruik de scanlook eerlijk".
- Quotation marks: straight double quotes "…" (as in the English source); nested: '…'.
- Trust badge wording (fixed): "beoordeeld met 5 sterren in de Chrome Web Store".

## Spelling and house style

- **PDF** in capitals (as in the Dutch macOS and Windows UI). Plural **PDF's**. Compounds with a hyphen:
  PDF-bestand, PDF-pagina, PDF-metadata, PDF-engine, kleuren-PDF, zwart-wit-PDF.
- Other format names the same way: JPG-bestand, PNG-afbeelding, Word-bestand, Word-document, Excel-bestand,
  ZIP-bestand, ZIP-archief, HTML-bestand, DOCX-bestand.
- **zwart-wit** always with a hyphen (as noun and adjective: "een PDF zwart-wit maken", "zwart-witkopie").
- **scaneffect** is one word (Dutch compound); likewise scanlook, scanengine, scaninstellingen, scannerrand,
  scannerkorrel, kantoorscan, flatbedscanner. With an English or abbreviated first part use a hyphen:
  scaneffect-tool, Chrome-extensie, OCR-software.
- "e-mail", "wifi", "online", "offline", "live voorbeeld", "hr-afdeling" (lowercase hr).
- "Google Docs" (product) / "een Google-document" (a single doc).

## Numbers, units and dates

- Decimal comma in running text and tables: 0,3 · 0,5° · 1,5× · 0,05–0,2. Values themselves never change.
- Thousands separator: a dot: 2.200 px, 10.000 woorden. Years without a separator: 2026.
- Ranges with an en dash and no spaces: 0,5–2°, 20–60 seconden, 300–400%. "−10° tot 10°" for signed ranges.
- Units: 144 dpi, 300 ppi, 11 pt, 2×, 3× (multiplication sign, no space). Percent without a space: 400%.
- Paper: A4 is the default in NL/BE; US Letter (8,5 × 11 inch) only where the English source compares with it.
  Inches: "0,75 inch" (keep the source value; you may add "(ca. 1,9 cm)" only if it is exact).
- Dates: "18 september 2026" (day month year, month in lowercase). Month names: januari, februari, maart,
  april, mei, juni, juli, augustus, september, oktober, november, december.
- Keyboard shortcuts: Ctrl+P, Ctrl+F, Cmd+P (Mac: "Command-P" in Apple's own texts; we use Cmd+P).

## Core terms (EN → NL)

| English | Dutch | Notes |
|---|---|---|
| make a PDF look scanned | een PDF gescand laten lijken / een PDF er gescand uit laten zien | both phrasings are searched; see keyword table |
| scan effect | scaneffect | one word |
| scanner effect | scaneffect, "het effect van een scanner" | **never "scannereffect"**: that string is a competitor name on the FORBIDDEN list and fails QA |
| scanned look / scan look | scanlook, gescande look | |
| scanned PDF | gescande PDF | |
| scanned-looking PDF | gescand ogende PDF, PDF die er gescand uitziet | |
| scanned copy | gescande kopie | |
| scanned document | gescand document | |
| digital (native) PDF | digitale PDF | |
| image-only PDF | PDF met alleen afbeeldingen | also "PDF op basis van afbeeldingen" |
| searchable PDF | doorzoekbare PDF | |
| text layer (hidden) | (verborgen) tekstlaag | |
| OCR | OCR (tekstherkenning) | explain once as "optische tekenherkenning (OCR)" |
| flatten (a PDF) | (een PDF) afvlakken | noun: afvlakken; adj.: afgevlakt |
| rasterize | rasteren | "omzetten naar pixels" when explaining |
| render a page as an image | een pagina als afbeelding weergeven (renderen) | |
| page image | paginabeeld | |
| grayscale | grijstinten; "in grijstinten" | UI option is "Grijs" |
| black and white / bitonal | zwart-wit / bitonaal (1-bit) | pure B&W = "puur zwart-wit" |
| color PDF | kleuren-PDF | |
| colorspace | kleurruimte | UI label "Kleurruimte" |
| bit depth | kleurendiepte (bits per pixel) | |
| skew / tilt | scheefstand / kanteling | adj.: scheef, gekanteld |
| rotation | rotatie | UI label "Rotatie" |
| rotation variance | rotatievariatie | UI label "Rotatievariatie" |
| noise | ruis | sensor noise = sensorruis |
| grain | korrel | adj.: korrelig |
| blur / soft focus | vervaging / zachte focus | blurry = wazig |
| moiré | moiré, moirépatroon | |
| halftone | rasterpunten, halftoon | |
| paper tone | papiertint | |
| yellowed / aged paper | vergeeld papier / oud papier | UI slider "Vergeling" |
| brightness | helderheid | |
| contrast | contrast | |
| resolution | resolutie | UI label "Resolutie" |
| dpi / ppi | dpi / ppi | "144 dpi" |
| JPEG compression / artifacts | JPEG-compressie / compressieartefacten | |
| edge shadow / lid line | randschaduw / lijn van de scannerklep | not tool features |
| border (frame line) | rand | UI label "Rand" |
| crease, fold, coffee stain, perspective warp | kreukel, vouw, koffievlek, perspectiefvervorming | not tool features |
| flatbed scanner | flatbedscanner | |
| document feeder (ADF) | documentinvoer | |
| photocopy / photocopier | fotokopie / kopieerapparaat | |
| presets: office scan / photocopy / fax-like / aged paper / phone-scan look | kantoorscan / fotokopie / faxlook / oud papier / telefoonscanlook | |
| preset / recipe | voorinstelling / recept | |
| watermark | watermerk | |
| stamp / signature | stempel / handtekening | |
| metadata | metadata | "PDF-metadata" |
| bulk scan | Bulkscan | as UI name; verb: "in bulk scannen" |
| ZIP archive | ZIP-archief, ZIP-bestand | |
| browser tool / web tool | browsertool / webtool | |
| Chrome extension | Chrome-extensie | |
| side panel | zijpaneel | |
| live preview | live voorbeeld | |
| slider | schuifregelaar | |
| default (value) | standaardwaarde, standaard | |
| setting / control | instelling | |
| upload / download | uploaden / downloaden | "geüpload", "gedownload" |
| file size | bestandsgrootte | |
| print dialog | afdrukvenster | |
| print / print out | afdrukken (UI), printen (running text) | printout = afdruk |
| raster image editor | rasterbeeldbewerker, beeldbewerkingsprogramma | never a brand name |
| phone scanner app | scan-app op je telefoon | never a brand name |
| desktop PDF software | PDF-software voor de desktop | never a brand name |
| free, no signup, processed locally | gratis, zonder account, lokaal verwerkt | |
| progressive web app / processing server | progressieve webapp / verwerkingsserver | |
| screen reader | schermlezer | |
| court / agency / filing | rechtbank / instantie / processtuk (indiening) | US names (CM/ECF, USCIS, IRS, NARA, FADGI) stay in English |
| electronic signature | elektronische handtekening | |
| rated 5 stars in the Chrome Web Store | beoordeeld met 5 sterren in de Chrome Web Store | fixed wording |

## Interface labels (exactly as in `messages/nl.json`)

| English UI | Dutch UI (use verbatim) |
|---|---|
| Scan (nav, page title) | Scannen |
| Bulk Scan | Bulkscan |
| Guides | Handleidingen |
| Home | Home |
| Chrome Extension | Chrome-extensie |
| FREE | GRATIS |
| Convert to Scanned PDF | Omzetten naar gescande PDF |
| Start scanning | Begin met scannen |
| Generate Scanned PDF | Gescande PDF maken |
| Generating... | Bezig met maken... |
| Download Scanned PDF | Gescande PDF downloaden |
| Create scanned PDF / Create {n} scanned PDFs | Gescande PDF maken / {n} gescande PDF's maken |
| Generate scanned PDFs | Gescande PDF's maken |
| Add files | Bestanden toevoegen |
| Add more files | Meer bestanden toevoegen |
| Download all as ZIP | Alles downloaden als ZIP |
| Download again | Opnieuw downloaden |
| Download this scanned PDF | Deze gescande PDF downloaden |
| Remove file | Bestand verwijderen |
| Choose file / Choose files | Bestand kiezen / Bestanden kiezen |
| Choose another file | Ander bestand kiezen |
| Drop your file(s) here | Sleep je bestand hierheen / Sleep je bestanden hierheen |
| Select or drop your file here | Kies je bestand of sleep het hierheen |
| Preview / Show in preview | Voorbeeld / Tonen in voorbeeld |
| Original / Scanned preview | Origineel / Gescand voorbeeld |
| Save | Opslaan |
| Back | Terug |
| Queued / Done / Failed | In wachtrij / Klaar / Mislukt |
| Preparing… / Ready / Scanning… / Scanned | Voorbereiden… / Gereed / Scannen… / Gescand |
| Steps: Upload / Adjust / Download | Uploaden / Aanpassen / Downloaden |
| Upload your files | Upload je bestanden |
| Adjust the scan look | Stel het scaneffect in |
| Get your scanned PDF | Download je gescande PDF |
| Scan Settings | Scaninstellingen |
| Noise | Ruis |
| Blur | Vervaging |
| Rotate | Rotatie |
| Rotate Variance | Rotatievariatie |
| Brightness | Helderheid |
| Contrast | Contrast |
| Yellowish | Vergeling |
| Colorspace | Kleurruimte |
| Colorful / Gray | Kleur / Grijs |
| Border (Yes / No) | Rand (Ja / Nee) |
| Resolution | Resolutie |
| Watermark | Watermerk |
| Watermark text / Watermark image | Watermerktekst / Watermerkafbeelding |
| Stamp or signature | Stempel of handtekening |
| Add stamp or signature | Stempel of handtekening toevoegen |
| Horizontal position / Vertical position / Size | Horizontale positie / Verticale positie / Grootte |
| PDF metadata | PDF-metadata |
| Title / Author / Subject / Keywords / Producer / Creator | Titel / Auteur / Onderwerp / Trefwoorden / Producent / Maker |
| Remove (image) | Verwijderen |
| Language | Taal |

In running text, name a control with its exact label and no quotes, e.g. "zet Kleurruimte op Grijs", "klik op
Gescande PDF maken", "houd Rotatievariatie boven 0". Lowercase generic mentions are fine when you describe the
effect rather than the control ("een beetje ruis en vervaging").

Blog chrome (from `translations/nl/chrome.json`): "Open de gratis tool →", "Toevoegen aan Chrome — gratis",
"Meer handleidingen →", "Gerelateerde handleidingen", "Bijgewerkt:", "{n} min. leestijd".

## OS and app built-ins as they appear in the Dutch UI

| English | Dutch UI name |
|---|---|
| macOS Preview | Voorvertoning |
| File (macOS menu) | Archief |
| File → Export… | Archief → Exporteer… |
| File → Export as PDF… | Archief → Exporteer als PDF… |
| File → Print… | Archief → Druk af… |
| PDF menu → Save as PDF (macOS print dialog) | PDF ▾ → Bewaar als PDF |
| Quartz Filter | Quartz-filter (the filter names themselves, e.g. "Black & White", "Gray Tone", stay in English in Dutch macOS) |
| Open With → Preview | Open met → Voorvertoning |
| Windows "Microsoft Print to PDF" | Microsoft Print to PDF (unchanged) |
| Windows Photos app | Foto's |
| Print | Afdrukken |
| Printer Properties / Preferences | Printereigenschappen / Voorkeuren |
| Color: Color / Black and white | Kleur: Kleur / Zwart-wit |
| Grayscale (printer driver, Office) | Grijswaarden |
| Chrome / Edge print: Destination → Save as PDF | Bestemming → Opslaan als PDF |
| More settings | Meer instellingen |
| Downloads folder | map Downloads |
| Chrome developer tools / Network tab | ontwikkelaarstools / tabblad Netwerk |
| Microsoft Word: File → Save As → PDF | Bestand → Opslaan als → PDF (*.pdf) |
| Word: File → Export | Bestand → Exporteren |
| Word "Optimize for: Standard / Minimum size" | Standaard / Minimale grootte |
| Excel Page Layout / Page Setup | Pagina-indeling / Pagina-instelling |
| Excel "Fit All Columns on One Page" | Alle kolommen op één pagina weergeven |
| Document Properties | Documenteigenschappen |
| "Print as image" (advanced print option) | Afdrukken als afbeelding |
| Google Docs: File → Download → PDF Document | Bestand → Downloaden → PDF-document (.pdf) |
| iPhone Notes / Files | Notities / Bestanden |
| Scan Documents (Notes, Files) | Scan documenten |
| iPhone Settings → Camera → Formats → Most Compatible | Instellingen → Camera → Formaten → Meest compatibel |
| Android camera / Files app | Camera / Bestanden-app |
| Google Chrome, Microsoft Edge, Chrome Web Store | unchanged |

## Keywords, slugs and titles per page

| en-slug | Local main keyword | Localized slug | Title |
|---|---|---|---|
| (home) | pdf gescand laten lijken | /nl/ | PDF gescand laten lijken — gratis online, zonder upload |
| (blog index) | pdf gescand laten lijken | /nl/blog/ | PDF gescand laten lijken: handleidingen en instellingen |
| how-to-make-a-pdf-look-scanned | pdf er gescand uit laten zien | pdf-er-gescand-uit-laten-zien | PDF er gescand uit laten zien: 6 gratis methoden (2026) |
| make-a-document-look-scanned | document gescand laten lijken | document-gescand-laten-lijken | Document gescand laten lijken: Word, Google Docs en foto's |
| pdf-to-scanned-pdf | pdf naar gescande pdf | pdf-naar-gescande-pdf | PDF naar gescande PDF: omzetten, afvlakken, leesbaar houden |
| what-is-a-scanned-pdf | gescande pdf | wat-is-een-gescande-pdf | Wat is een gescande PDF? Gescande kopie vs digitale PDF |
| scan-effect | scaneffect | scaneffect-instellingen | Scaneffect: waardoor een document er gescand uitziet |
| image-to-scanned-pdf | afbeelding naar gescande pdf | afbeelding-naar-gescande-pdf | Afbeelding naar gescande PDF: van JPG of foto een scan maken |
| convert-color-pdf-to-black-and-white | pdf zwart-wit maken | pdf-zwart-wit-maken | PDF zwart-wit maken: 5 gratis manieren voor Windows en Mac |

Why these: Dutch searchers use the verb "scannen" and the participle "gescand" ("gescande PDF"), and phrase the
task as "… gescand laten lijken" or "… er gescand uit laten zien". The home page and the how-to article each take
one of the two phrasings so the site covers both. "PDF zwart-wit maken" is how people search for colour-to-B&W
("maken" + "zwart-wit"), not the literal "kleuren-PDF converteren naar zwart-wit".

### Keyword placement tips for body translators

`qa_i18n.py` counts a heading as containing the keyword if the exact phrase is in it **or all its words appear
somewhere in it**. Dutch separable verbs split the phrase, so write the infinitive with "te":

- pdf er gescand uit laten zien → "Wat is de snelste manier om een PDF er gescand uit te laten zien?",
  "Methode 1: een PDF er gescand uit laten zien in je browser". ("Laat een PDF er gescand uitzien" misses
  "laten" and "zien" as words.)
- document gescand laten lijken → "Een Word-document gescand laten lijken", "Hoe kun je een document gescand
  laten lijken?" ("Hoe laat je een document gescand lijken?" misses "laten".)
- pdf zwart-wit maken → always "zwart-wit" with the hyphen: "Manier 1: een PDF zwart-wit maken in de browser".
- pdf naar gescande pdf, afbeelding naar gescande pdf, gescande pdf, scaneffect → keep the words as written
  ("gescande", not "gescand", when the keyword has it).

Internal link anchors to the other articles should use that article's Dutch main keyword or title (see table).
