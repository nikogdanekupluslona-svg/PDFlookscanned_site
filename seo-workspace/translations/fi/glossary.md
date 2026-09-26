# Finnish (fi) glossary: pdflookscanned.com

Market: Finland. Output: `translations/fi/<en-slug>/body.html`, `meta.json` is already written (do not change the
slug, title, h1 or main_keyword without updating this file too). UI strings: `lookscanned.io-main/src/locale/messages/fi.json`.

## 1. Address and style

- Informal **sinä**, always in the singular: imperatives *Avaa, Pudota, Valitse, Säädä, Lataa*; *voit, selaimessasi,
  tiedostosi*. Never *te/Te*. Headings may use the neutral passive (*Miten PDF muunnetaan skannatuksi?*).
- Plain, concrete standard Finnish (yleiskieli). Short sentences, no anglicisms such as *klikata* (use *napsauttaa*),
  *uploadata* or *feikki* (use *väärennetyn näköinen*, *epäaito*). Avoid hype words (*mullistava*, *uskomaton*).
- Keep the answer-first style: each H2 opens with a 40–60-word paragraph that answers the heading on its own and
  names the subject (no *Se/Tämä* as the first word).
- Question headings stay questions (*Mikä…?, Miten…?, Milloin…?, Kumpi…?*). H2 ≤ 70 characters.
- Brand **Make PDF look scanned** is never translated or inflected directly. Attach Finnish words with a space +
  hyphen: *Make PDF look scanned -työkalu*, *Make PDF look scanned -tiimi*, *Make PDF look scanned -laajennus*.
  Otherwise say *ilmainen työkalu*, *selaintyökalu*, *verkkotyökalu*.
- Expert quote cite: `<cite><strong>Make PDF look scanned -tiimi</strong> — verkkotyökalun ja Chrome-laajennuksen
  tekijät</cite>` (the quote itself in first person plural: *me, teemme, suosittelemme*).
- TOC: `<nav class="toc" aria-label="Sisällysluettelo"><h2>Sisällys</h2>…`
- FAQ heading pattern: *<keyword>: usein kysytyt kysymykset* (or *…: UKK* only if space is short).
- Ethics callout title: *Käytä skannausilmettä rehellisesti*.
- Method numbering: EN "Method 1" / "Way 1" → **Tapa 1:** (both).
- Abbreviations with case endings take a colon: *PDF:n, PDF:ää, PDF:ssä, PDF:stä, PDF:ksi, PDF:t, PDF:ien; OCR:n,
  OCR:ää; ZIP:n*. Compounds take a hyphen: *PDF-tiedosto, PDF-muoto, JPG-kuva, ZIP-arkisto, A4-sivu, Word-tiedosto*.
- Button/label + noun: *Napsauta Luo skannattu PDF -painiketta*; *Kierron vaihtelu -asetus*; *Väriavaruus-valikko*
  (single-word label: plain hyphen; multi-word label: space + hyphen).
- Quotation marks: Finnish **”…”** (same mark on both sides); nested ’…’. Dash: en dash **–** with spaces for
  asides; menu paths with → (*Tiedosto → Lataa → PDF-dokumentti (.pdf)*).
- Other fixed terms: *lomakekentät* (form fields), *asettelu* (layout), *tuomioistuin* (court), *viranomainen*
  (agency), *väärentää* (forge), *renderöidä* (render).
- Honest-use wording stays factual: the scan look changes appearance, not authenticity; do not forge or alter official
  documents, IDs or signatures that are not yours; some courts and agencies require searchable PDFs.

## 2. Numbers, units and dates

| Item | Finnish convention | Example |
|---|---|---|
| Decimal separator | comma | 0,3 · 0,5° · 1,2 |
| Ranges | en dash, no spaces | 0,2–0,4 · 20–60 sekuntia · 0,5°–2° |
| Negative values | minus sign | −10°…10° |
| Thousands | (non-breaking) space | 2 200 px · 10 000 sivua |
| Percent | space before % | 300–400 % · inflected *300 %:iin* |
| Degrees, scale | as source, no space | 1° · 2× · 3× |
| dpi / ppi | lowercase after the number | noin 144 dpi · 300 ppi |
| File size | space before unit | 1,2 Mt (or MB) · 350 kt (or kB); pick one per article, prefer MB/kB as in the source |
| Dates in text | day.month.year | 18.9.2026 |
| Blog dates (chrome.json) | `{month} {year}` → *syyskuu 2026*; `{day}. {month}ta {year}` → *18. syyskuuta 2026* (months list is nominative; the partitive is built by adding *-ta*) |
| Paper | A4 is the default in Finland; US Letter = *Letter-koko* | A4-sivu (210 × 297 mm) |
| Time | *alle minuutissa*, *10–20 minuuttia*, *yli 30 minuuttia* | |

US agencies and courts cited in the English source stay as they are (USCIS, IRS, NARA, FADGI, CM/ECF, GOV.UK);
explain once in Finnish if needed (*Yhdysvaltain kansallisarkisto NARA*).

## 3. Main keywords and QA-safe forms

`qa_i18n.py` checks the main keyword with a plain substring test: the whole phrase, or **every word of it as a
substring**, must appear in the title, H1, `.lead` and in at least **two H2s**. Finnish inflection can break this, so
use the forms marked OK below in those places (elsewhere inflect freely).

| en-slug | Local main keyword | OK in H2 / lead | Not enough on its own |
|---|---|---|---|
| (home) | pdf skannatun näköiseksi | *PDF skannatun näköiseksi*, *muuttaa PDF:n skannatun näköiseksi* | *skannatun näköinen PDF* |
| how-to-make-a-pdf-look-scanned | skannatun näköinen pdf | *skannatun näköinen PDF(-tiedosto)* | *skannatun näköisen PDF:n* (näköisen ≠ näköinen) |
| make-a-document-look-scanned | asiakirja skannatun näköiseksi | *asiakirja / asiakirjan / Word-asiakirja … skannatun näköiseksi* | *dokumentti…*, *skannatun näköinen asiakirja* |
| pdf-to-scanned-pdf | pdf skannatuksi | *PDF skannatuksi (PDF:ksi)*, *PDF:n muuntaminen skannatuksi* | *skannattu PDF* |
| what-is-a-scanned-pdf | skannattu pdf | *skannattu PDF*, *skannattua PDF:ää*, *skannattuun PDF:ään* | *skannatun PDF:n*, *skannatussa* (no *-ttu*) |
| image-to-scanned-pdf | kuva skannatuksi pdf:ksi | *kuva / kuvan / JPG-kuva … skannatuksi PDF:ksi* | *…skannatuksi PDF-tiedostoksi* (no "PDF:ksi") |
| convert-color-pdf-to-black-and-white | pdf mustavalkoiseksi | *PDF mustavalkoiseksi*, *värillinen PDF mustavalkoiseksi* | *mustavalkoinen PDF* |
| scan-effect | skannausefekti | *skannausefekti, -efektin, -efektiä, -efektit* | *skannausefektejä* (plural stem -efekte-) |

Example H2 patterns: *Tapa 1: skannatun näköinen PDF selaimessa* · *Miten asiakirja muutetaan skannatun
näköiseksi?* · *Miten PDF muunnetaan skannatuksi selaimessa?* · *Miten skannattu PDF eroaa digitaalisesta PDF:stä?* ·
*Miten kuva muunnetaan skannatuksi PDF:ksi?* · *Tapa 2: PDF mustavalkoiseksi Macilla* · *Mikä on skannausefekti?*

Use the keyword naturally about 5+ times in the body; secondary phrases are in each `meta.json` → `keywords`.

## 4. Recurring terms (EN → FI)

| English | Finnish (use this) | Notes |
|---|---|---|
| scan effect | skannausefekti | synonym *skannaustehoste* only in keywords |
| scan look / scanned look | skannausilme, skannattu ilme | |
| make (a PDF) look scanned | muuttaa PDF skannatun näköiseksi; tehdä PDF:stä skannatun näköinen | |
| scanned-looking PDF | skannatun näköinen PDF | |
| scanned PDF | skannattu PDF | |
| scanned copy | skannattu kopio | *skannaus* colloquially |
| scanned document | skannattu asiakirja | *dokumentti* only as a keyword variant |
| digital / born-digital PDF | digitaalinen PDF (alun perin sähköinen) | |
| image-only PDF | kuvapohjainen PDF, pelkistä kuvista koostuva PDF | |
| searchable PDF | haettava PDF | *PDF, jonka tekstiä voi hakea* |
| text layer | tekstikerros | *piilotettu tekstikerros* (hidden) |
| OCR | tekstintunnistus (OCR) | first mention in full, then *OCR* |
| flatten / flattened | tasoittaa / tasoitettu PDF; tasoitus | *litistää* only in keywords |
| rasterize / rasterization | rasteroida / rasterointi | |
| page image | sivukuva | |
| grayscale | harmaasävy; harmaasävyinen PDF | UI option: **Harmaasävy** |
| color (PDF) | värillinen PDF | UI option: **Värillinen** |
| black and white / bitonal | mustavalkoinen; kaksisävyinen (1-bittinen) | bitonal = only black and white pixels |
| colorspace | väriavaruus | UI: **Väriavaruus** |
| skew | vinous | *vino sivu* |
| tilt | kallistus; *kallellaan* | |
| rotation | kierto | UI: **Kierto** |
| rotation variance | kierron vaihtelu | UI: **Kierron vaihtelu** |
| noise | kohina | UI: **Kohina** |
| grain / grainy | rakeisuus / rakeinen | |
| blur / soft focus | sumennus / lievä epätarkkuus | UI: **Sumennus**; *epätarkkuus* for real scanners |
| brightness / contrast | kirkkaus / kontrasti | UI: **Kirkkaus**, **Kontrasti** |
| paper tone | paperin sävy | |
| yellowish / aged paper | kellertävyys (UI) / kellastunut, vanhentunut paperi | UI: **Kellertävyys** |
| moiré | moiré-kuvio | |
| halftone | painorasteri, rasteripisteet | |
| edge shadows, creases, stains | reunavarjot, taitokset, tahrat | not tool features |
| perspective (warp) | perspektiivi(vääristymä) | not a tool feature |
| border (1-px frame) | reunus (UI); reunaviiva | UI: **Reunus** |
| resolution | tarkkuus | UI: **Tarkkuus**; *resoluutio* acceptable in running text |
| dpi / ppi | dpi (pistettä tuumalle) / ppi (pikseliä tuumalle) | |
| bit depth | bittisyvyys | |
| JPEG compression | JPEG-pakkaus | |
| compression artifacts | pakkausartefaktit, pakkausjäljet | |
| file size | tiedostokoko | |
| scanner artifacts / marks | skannausjäljet | |
| bulk scan / batch | joukkoskannaus | UI page: **Joukkoskannaus** |
| ZIP archive | ZIP-arkisto, ZIP-tiedosto | |
| live preview | reaaliaikainen esikatselu | |
| slider | liukusäädin | |
| preset / recipe | valmisasetus / resepti (asetusyhdistelmä) | |
| side panel | sivupaneeli | as in Finnish Chrome |
| Chrome extension | Chrome-laajennus | |
| Chrome Web Store | Chrome Web Store | *Chrome Web Storessa / -Storesta* |
| trust badge meaning | *5 tähden arvio Chrome Web Storessa*; *Chrome Web Storessa 5 tähden arvion saanut laajennus* | |
| web tool / browser tool | verkkotyökalu / selaintyökalu | |
| processed locally | käsitellään paikallisesti (omalla laitteellasi) | |
| upload (to a server) | lähettää palvelimelle | never *ladata* for upload |
| download | ladata (koneelle), latautua | |
| signup / account | rekisteröityminen / käyttäjätili | |
| works offline / PWA | toimii ilman verkkoyhteyttä / progressiivinen verkkosovellus (PWA) | |
| watermark | vesileima | |
| stamp / signature | leima / allekirjoitus | |
| electronic signature | sähköinen allekirjoitus | |
| metadata | metatiedot | |
| flatbed scanner | tasoskanneri | |
| document feeder (ADF) | asiakirjansyöttölaite (ADF) | |
| photocopy / photocopier | valokopio / kopiokone | |
| fax | faksi | |
| print dialog / print to PDF | tulostusikkuna / tulostaa PDF-tiedostoksi | |
| raster image editor | kuvankäsittelyohjelma (rasterigrafiikkaohjelma) | never name products |
| phone scanner app | puhelimen skannaussovellus | never name products |
| desktop PDF software | tietokoneen PDF-ohjelma | never name products |
| screen reader / accessibility | ruudunlukuohjelma / saavutettavuus | |

## 5. Interface labels (exactly as in `messages/fi.json`)

Write these exactly (capitalized as shown) when a text refers to the control or button.

| English UI | Finnish UI |
|---|---|
| Generate Scanned PDF | Luo skannattu PDF |
| Create scanned PDF / Create {n} scanned PDFs | Luo skannattu PDF / Luo {n} skannattua PDF:ää |
| Generate scanned PDFs (bulk) | Luo skannatut PDF:t |
| Download Scanned PDF | Lataa skannattu PDF |
| Download all as ZIP | Lataa kaikki ZIP-tiedostona |
| Download again | Lataa uudelleen |
| Download this scanned PDF | Lataa tämä skannattu PDF |
| Add files / Add more files | Lisää tiedostoja / Lisää muita tiedostoja |
| Choose file / Choose files / Choose another file | Valitse tiedosto / Valitse tiedostot / Valitse toinen tiedosto |
| Drop your file here | Pudota tiedosto tähän |
| Select or drop your file here | Valitse tiedosto tai pudota se tähän |
| Start scanning | Aloita skannaus |
| Convert to Scanned PDF (home button) | Muunna skannatuksi PDF:ksi |
| Scan (nav) / Scan a PDF (blog nav) | Skannaa / Skannaa PDF |
| Bulk Scan | Joukkoskannaus |
| Guides / Home | Oppaat / Etusivu |
| Chrome Extension / FREE | Chrome-laajennus / ILMAINEN |
| Add to Chrome — free | Lisää Chromeen – ilmainen |
| Scan Settings | Skannausasetukset |
| Noise | Kohina |
| Blur | Sumennus |
| Rotate | Kierto |
| Rotate Variance | Kierron vaihtelu |
| Brightness | Kirkkaus |
| Contrast | Kontrasti |
| Yellowish | Kellertävyys |
| Colorspace | Väriavaruus |
| Gray / Colorful | Harmaasävy / Värillinen |
| Border (Yes / No) | Reunus (Kyllä / Ei) |
| Resolution | Tarkkuus |
| Watermark / Watermark text / Watermark image | Vesileima / Vesileiman teksti / Vesileimakuva |
| Stamp or signature / Add stamp or signature | Leima tai allekirjoitus / Lisää leima tai allekirjoitus |
| Horizontal position / Vertical position / Size | Vaakasijainti / Pystysijainti / Koko |
| PDF metadata | PDF-metatiedot |
| Title / Author / Subject / Keywords / Producer / Creator | Otsikko / Tekijä / Aihe / Avainsanat / Tuottaja / Luoja |
| Remove / Remove file | Poista / Poista tiedosto |
| Preview / Show in preview | Esikatselu / Näytä esikatselussa |
| Original / Scanned preview | Alkuperäinen / Skannauksen esikatselu |
| Steps: Upload / Adjust / Download | Lisää / Säädä / Lataa |
| Upload your files / Adjust the scan look / Get your scanned PDF | Lisää tiedostosi / Säädä skannauksen ulkoasua / Lataa skannattu PDF-tiedostosi |
| Queued / Done / Failed / Ready / Scanned | Jonossa / Valmis / Epäonnistui / Valmis / Skannattu |
| Processed in your browser — nothing is uploaded | Käsitellään selaimessasi – mitään ei lähetetä palvelimelle |
| Key features / Scan effects | Tärkeimmät ominaisuudet / Skannausefektit |
| Open the free tool → / More guides → | Avaa ilmainen työkalu → / Lisää oppaita → |

## 6. OS built-ins and document apps (Finnish UI names)

| Feature | Finnish name / path |
|---|---|
| macOS Preview | **Esikatselu** (*Esikatselu-sovellus*) |
| macOS menu File / Print / Export / Export as PDF | Arkisto / Tulosta… / Vie… / Vie PDF:nä… |
| macOS print dialog → PDF → Save as PDF | PDF-valikko → Tallenna PDF:nä… |
| macOS Quartz filter | Quartz-suodin (menu in the *Vie…* dialog; if unsure of a filter's exact name, describe it: *harmaasävysuodin*, *mustavalkosuodin*) |
| Windows virtual printer | **Microsoft Print to PDF** (unchanged) |
| Windows Photos app → Print | Valokuvat → Tulosta |
| Downloads folder | Windows: *Ladatut tiedostot*; macOS: *Lataukset* (generic: *latauskansio*) |
| Chrome / Edge print dialog | Tulosta → Kohde: *Tallenna PDF-muodossa*; Väri: *Mustavalkoinen* |
| Chrome developer tools / Network tab | kehittäjätyökalut / *Network (Verkko) -välilehti* |
| Microsoft Word | Tiedosto → Tallenna nimellä → PDF (or Tiedosto → Vie → Luo PDF/XPS-tiedosto) |
| Microsoft Excel | Tiedosto → Tallenna nimellä → PDF |
| Google Docs | name it **Google Docs** (what Finns search); menu path in the Finnish UI: Tiedosto → Lataa → PDF-dokumentti (.pdf) |
| iPhone Notes / Files / Camera | Muistiinpanot / Tiedostot / Kamera; command *Skannaa dokumentteja* |
| Android camera | Kamera |

## 7. Articles: keyword, slug, title

| en-slug | Local main keyword | Localized slug | Title |
|---|---|---|---|
| (home page `/fi/`) | pdf skannatun näköiseksi | — | PDF skannatun näköiseksi verkossa – ilmainen ja yksityinen |
| how-to-make-a-pdf-look-scanned | skannatun näköinen pdf | skannatun-nakoinen-pdf | Skannatun näköinen PDF: näin teet sen – 6 tapaa (2026) |
| make-a-document-look-scanned | asiakirja skannatun näköiseksi | asiakirja-skannatun-nakoiseksi | Asiakirja skannatun näköiseksi: Word, Google Docs ja kuvat |
| pdf-to-scanned-pdf | pdf skannatuksi | pdf-skannatuksi | PDF skannatuksi PDF:ksi: muunna, tasoita ja pidä luettavana |
| what-is-a-scanned-pdf | skannattu pdf | mika-on-skannattu-pdf | Mikä on skannattu PDF? Skannattu kopio vs. digitaalinen PDF |
| image-to-scanned-pdf | kuva skannatuksi pdf:ksi | kuva-skannatuksi-pdfksi | Kuva skannatuksi PDF:ksi: JPG tai valokuva skannaukseksi |
| convert-color-pdf-to-black-and-white | pdf mustavalkoiseksi | pdf-mustavalkoiseksi | PDF mustavalkoiseksi: 5 tapaa muuntaa värillinen PDF |
| scan-effect | skannausefekti | skannausefekti-asetukset | Skannausefekti: mikä saa asiakirjan näyttämään skannatulta |

Anchor texts for internal links (hrefs stay English, e.g. `/blog/scan-effect/`):
`/` → *PDF skannatun näköiseksi -työkalu* · `/scan` → *skanneri*, *ilmainen selaintyökalu* · `/scan/bulk` →
*Joukkoskannaus* · pillar → *näin teet PDF:stä skannatun näköisen* · document → *asiakirja skannatun näköiseksi* ·
pdf-to-scanned → *PDF skannatuksi PDF:ksi* · what-is → *mikä on skannattu PDF* · image → *kuva skannatuksi PDF:ksi* ·
B&W → *PDF mustavalkoiseksi* · scan-effect → *skannausefektin asetukset*.
