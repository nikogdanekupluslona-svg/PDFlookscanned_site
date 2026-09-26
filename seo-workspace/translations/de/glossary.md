# Glossar Deutsch (de): pdflookscanned.com

Markt: Deutschland, Österreich, Schweiz. Rechtschreibung wie in Deutschland (mit ß: „weiß“, „Größe“, „groß“).
Dieses Glossar ist verbindlich für alle deutschen Seiten (UI `messages/de.json`, `home-guide/de.html`,
`translations/de/chrome.json`, alle `translations/de/<en-slug>/meta.json` + `body.html`).

## 1. Anrede und Stil

- **Anrede: „Sie“**, durchgehend, auch in FAQ-Fragen aus Nutzersicht („Wie lasse ich …?“ ist als Frage erlaubt, die Antwort spricht mit „Sie“ an).
- Kurze, klare Sätze; Antwort zuerst. Keine Übersetzungs-Calques („Das ist, warum …“, „am Ende des Tages“). Lieber Verbalstil als Nominalketten („Sie wandeln das PDF um“ statt „die Durchführung der Umwandlung“).
- Überschriften, die im Englischen Fragen sind, bleiben Fragen. Maximal ~70 Zeichen.
- **Hauptkeyword in H2 (QA-Regel!)**: `qa_i18n.py` prüft, ob die H2 entweder die exakte Phrase oder **alle Wörter** des Hauptkeywords enthält (Teilstring-Suche, Kleinschreibung). Deutsche Verbstellung trennt Verben, deshalb:
  - Trennbare Verben nicht zerreißen: „Wie wandeln Sie … um?“ enthält **nicht** „umwandeln“. Stattdessen: „Wie Sie ein Bild in ein gescanntes PDF umwandeln“, „Wie kann man … umwandeln?“, „… umwandeln: so geht’s“.
  - „lassen“ nicht konjugieren: „Wie lässt man …?“ enthält **nicht** „lassen“. Stattdessen: „Wie können Sie ein PDF wie gescannt aussehen lassen?“, „PDF wie gescannt aussehen lassen: …“.
  - Deklination beachten: „gescanntes“ ist nicht in „gescannten“ enthalten. Für das Keyword „gescanntes pdf“ Nominativ/Akkusativ Neutrum verwenden („ein gescanntes PDF“, „Was ist ein gescanntes PDF?“).
  - „Scan-Effekt“ erfüllt das Keyword „scan effekt“ (beide Wörter enthalten); „Schwarz-Weiß“ erfüllt „schwarz weiß“.
- Genus: **das PDF** (Plural: die PDFs), **das ZIP-Archiv**, **die Datei**, **der Scan** (Plural: die Scans).
- Typografie: deutsche Anführungszeichen „…“ (U+201E/U+201C); Gedankenstrich „–“ mit Leerzeichen; Auslassung „…“ mit Leerzeichen davor in UI-Texten („Wird erstellt …“); Pfeil für Menüpfade „Datei → Speichern unter“.
- Anglizismen sparsam, aber so, wie die Zielgruppe sucht: „Scan“, „Tool“, „Browser“, „Download“, „Live-Vorschau“, „Look“ (nur in „Kopierer-Look“, „5 Looks“) sind üblich. „Upload“ nur im Snippet („ohne Upload“), im Fließtext „hochladen“.
- Marke **„Make PDF look scanned“** bleibt englisch und unverändert (Eigenname). Umschreibung: „unser kostenloses Tool“, „das kostenlose Browser-Tool“, „das Scan-Effekt-Tool“. Das Keyword „lookscanned“ nie verwenden.
- Keine Konkurrenz- oder Drittprodukte nennen (Liste `seo-workspace/qa.py` → `FORBIDDEN`). Statt Produktnamen: „ein Bildbearbeitungsprogramm“, „eine Scanner-App fürs Handy“, „PDF-Software für den Desktop“. Achtung: „Canvas“ ist erlaubt; „Kami“, „Nitro“, „Grainy“ etc. nicht verwenden.
- Ehrlichkeits-Callout: sachlich, nicht belehrend („Die Scan-Optik ehrlich einsetzen“).
- US-Behörden und Gerichte als Quellen bleiben im Original (USCIS, IRS, NARA, FADGI, CM/ECF, Bundesgerichte der USA); bei Bedarf kurz erklären („die US-Einwanderungsbehörde USCIS“).

## 2. Zahlen, Einheiten, Datum

| Was | Deutsch | Beispiel |
|---|---|---|
| Dezimaltrennzeichen | Komma | 0,3 · 0,5° · 1,5× · 0,05–0,2 |
| Tausendertrennzeichen | Punkt | 2.200 px · 1.000 Seiten |
| Bereiche | Halbgeviertstrich ohne Leerzeichen | 0,5–2° · 20–60 Sekunden · 300–400 % |
| Prozent | mit Leerzeichen (DIN 5008) | 300 % · 50 % |
| Grad | ohne Leerzeichen | 1° · −10° bis 10° |
| Faktor | ohne Leerzeichen | 2× · 3× |
| Auflösung | „dpi“ klein, mit Leerzeichen | 144 dpi · 300 dpi · 72 dpi × Faktor |
| Pixel | „px“ oder „Pixel“ | 2.200 px |
| Dateigröße | KB, MB mit Komma | 1,2 MB |
| Datum im Text | Tag. Monat Jahr | 18. September 2026 |
| Datum numerisch | TT.MM.JJJJ | 18.09.2026 |
| Uhrzeit/Dauer | „unter einer Minute“, „10–20 Minuten“, „30+ Minuten“ | |
| Papierformat | DIN A4 / A4; US-Letter für Letter | „auf einer A4-Seite“ |
| Tastenkürzel | Strg (Windows), Cmd (Mac) | Strg+P · Cmd+P · Strg/Cmd+F |

## 3. Fachbegriffe EN → DE

| English | Deutsch | Hinweis |
|---|---|---|
| make a PDF look scanned | ein PDF wie gescannt aussehen lassen | Hauptkeyword Start-/Pillar-Seite |
| scan effect | Scan-Effekt | Keyword-Schreibweise „scan effekt“ |
| scan look / scanned look | Scan-Optik | auch „gescannter Look“ (sparsam) |
| scanned-looking PDF | gescannt wirkendes PDF | |
| scanned PDF | gescanntes PDF | Genus: das |
| scanned copy | eingescannte Kopie | umgangssprachlich auch „Scan“ |
| scanned document | gescanntes / eingescanntes Dokument | |
| digital PDF (born-digital) | digitales PDF / digital erstelltes PDF | |
| image-only / image-based PDF | reines Bild-PDF / bildbasiertes PDF | |
| searchable PDF | durchsuchbares PDF | |
| text layer | Textebene | „unsichtbare Textebene“ nach OCR |
| OCR | OCR (Texterkennung) | beim ersten Vorkommen erklären |
| flatten | abflachen | „PDF abflachen (engl. flatten)“ beim ersten Vorkommen |
| rasterize | rastern | Substantiv: Rasterung |
| render a page as an image | eine Seite als Bild rendern | Ergebnis: Seitenbild |
| grayscale / gray levels | Graustufen / Grauwerte | „in Graustufen“, „256 Graustufen“, „Graustufen-PDF“ |
| black and white (pure, bitonal) | Schwarz-Weiß (reines Schwarz-Weiß, bitonal, 1 Bit) | Adjektiv: schwarz-weiß; immer mit Bindestrich |
| color PDF | farbiges PDF / Farb-PDF | |
| bit depth | Farbtiefe / Bittiefe | |
| skew / tilt | Schräglage / leichte Neigung | „leicht schief“ |
| rotation | Drehung | Reglername: Drehung |
| per-page variance | zufällige Abweichung pro Seite | Reglername: Drehvarianz |
| noise / grain | Rauschen / Körnung | Reglername: Rauschen |
| blur / soft focus | Unschärfe / weiche Schärfe | Reglername: Unschärfe |
| moiré | Moiré (Moiré-Effekt) | |
| paper tone | Papierton | |
| yellowed / aged paper | vergilbtes / altes Papier | Reglername: Vergilbung |
| brightness / contrast | Helligkeit / Kontrast | |
| border / edge line | Rand / Randlinie | Reglername: Rand |
| edge shadow | Randschatten | kein Tool-Feature |
| creases, stains, perspective warp | Knicke, Flecken, perspektivische Verzerrung | keine Tool-Features |
| JPEG compression / artifacts | JPEG-Kompression / Kompressionsartefakte | „JPEG-Blöcke“ |
| halftone | Druckraster | |
| resolution | Auflösung | Reglername: Auflösung |
| dpi / ppi | dpi / ppi (Punkte bzw. Pixel pro Zoll) | |
| file size | Dateigröße | |
| bulk scan / batch | Stapelscan / Stapelverarbeitung | Funktionsname: Stapelscan |
| live preview | Live-Vorschau | |
| slider | Regler | |
| preset / recipe | Vorlage / Einstellungswerte | keine Tool-Funktion, nur Werte |
| presets: office scan, photocopy, fax-like, aged paper, phone-scan look | Büro-Scan, Fotokopie, Fax-Optik, altes Papier, Handy-Scan-Optik | |
| copier / photocopy look | Kopierer / Kopierer-Look | |
| watermark | Wasserzeichen | |
| stamp | Stempel | |
| signature (handwritten image) | Unterschrift | „elektronische Signatur“ nur für E-Signatur |
| metadata | Metadaten | „PDF-Metadaten“ |
| side panel | Seitenleiste | Chrome-UI-Begriff |
| Chrome extension | Chrome-Erweiterung | |
| Chrome Web Store | Chrome Web Store | unverändert |
| rated 5 stars in the Chrome Web Store | im Chrome Web Store mit 5 Sternen bewertet | Trust-Badge-Wortlaut |
| free, no signup | kostenlos, ohne Anmeldung | „gratis“ nur in knappen Snippets |
| processed locally in the browser | lokal im Browser verarbeitet | |
| upload / download | hochladen / herunterladen | Substantiv: der Download |
| offline / PWA | offline / Progressive Web App | |
| phone / phone photo | Handy / Handyfoto | „Smartphone“ als Variante erlaubt |
| phone scanner app | Scanner-App fürs Handy | nie Produktnamen |
| raster image editor | Bildbearbeitungsprogramm | |
| desktop PDF software | PDF-Software für den Desktop | |
| flatbed scanner | Flachbettscanner | |
| print and scan | ausdrucken und einscannen | |
| print dialog | Druckdialog | |
| screen reader / accessibility | Screenreader / Barrierefreiheit | |
| form fields, annotations, layers | Formularfelder, Anmerkungen, Ebenen | |
| certified (true) copy | beglaubigte Kopie | |
| court / agency / filing | Gericht / Behörde / Einreichung | |
| honest use / forge, pass off | ehrlicher Einsatz / fälschen, als echt ausgeben | |

## 4. Interface-Beschriftungen (exakt wie in `messages/de.json`)

Im Fließtext immer genau so schreiben (Buttons in „…“, Reglernamen ohne Anführungszeichen, großgeschrieben).

| English UI | Deutsch (de.json) | Schlüssel |
|---|---|---|
| Make PDF look scanned (brand) | Make PDF look scanned | base.title |
| Scan | Scannen | base.scanTitle, nav.scan |
| Bulk Scan | Stapelscan | base.bulkTitle, nav.bulk |
| Home | Startseite | nav.home |
| Guides | Anleitungen | nav.guides |
| Chrome Extension | Chrome-Erweiterung | chrome.label |
| FREE | GRATIS | chrome.free |
| Make PDF look scanned (H1) | PDF wie gescannt aussehen lassen | landing.headline |
| Convert to Scanned PDF | In gescanntes PDF umwandeln | landing.cta |
| Three steps to a scanned PDF | In drei Schritten zum gescannten PDF | landing.stepsTitle |
| Choose a file | Datei auswählen | landing.step1Title |
| Adjust the scan effect | Scan-Effekt anpassen | landing.step2Title |
| Export the PDF | PDF exportieren | landing.step3Title |
| Key features | Die wichtigsten Funktionen | landing.featuresTitle |
| Language | Sprache | base.language |
| Start scanning | Jetzt scannen | actions.navigateToScan |
| Back | Zurück | actions.backToIndex |
| Preview | Vorschau | actions.preview |
| Save | Speichern | actions.save |
| Generate Scanned PDF | Gescanntes PDF erstellen | actions.generateScannedPDF |
| Generating... | Wird erstellt … | actions.generating |
| Download Scanned PDF | Gescanntes PDF herunterladen | actions.downloadScannedPDF |
| Successfully generated | Erfolgreich erstellt | actions.generateSuccess |
| Failed to generate: | Erstellung fehlgeschlagen: | actions.generateError |
| Add files | Dateien hinzufügen | actions.addFiles |
| Generate scanned PDFs | Gescannte PDFs erstellen | actions.processAll |
| Download all as ZIP | Alle als ZIP herunterladen | actions.downloadZip |
| Preparing file… | Datei wird vorbereitet … | actions.converting |
| Queued / Done / Failed | In Warteschlange / Fertig / Fehlgeschlagen | actions.queued/done/failed |
| Scan Settings | Scan-Einstellungen | settings.settings |
| Noise | Rauschen | settings.noise, settings.attenuate |
| Blur | Unschärfe | settings.blur |
| Border (Yes / No) | Rand (Ja / Nein) | settings.border.* |
| Colorspace | Farbraum | settings.colorspace.label |
| Colorful | Farbe | settings.colorspace.colorful |
| Gray | Graustufen | settings.colorspace.grayscale |
| Rotate | Drehung | settings.rotate |
| Rotate Variance | Drehvarianz | settings.rotateVariance |
| Select or drop your file here | Datei auswählen oder hier ablegen | settings.pdfSelectLabel |
| No file selected | Keine Datei ausgewählt | settings.pdfNoSelectMessage |
| Resolution | Auflösung | settings.scale |
| Yellowish | Vergilbung | settings.yellowish |
| Brightness | Helligkeit | settings.brightness |
| Contrast | Kontrast | settings.contrast |
| Watermark | Wasserzeichen | settings.extras.watermark |
| Watermark text / image | Wasserzeichentext / Wasserzeichenbild | settings.extras.watermarkText/Image |
| Stamp or signature | Stempel oder Unterschrift | settings.extras.stamp |
| Add stamp or signature | Stempel oder Unterschrift hinzufügen | settings.extras.stampImage |
| Horizontal / Vertical position | Horizontale / Vertikale Position | settings.extras.stampX/Y |
| Size | Größe | settings.extras.stampScale |
| PDF metadata | PDF-Metadaten | settings.extras.metadata |
| Title / Author / Subject / Keywords | Titel / Autor / Thema / Stichwörter | settings.extras.* |
| Producer / Creator | PDF-Erzeuger / Anwendung | settings.extras.producer/creator |
| Remove | Entfernen | settings.extras.clearImage |
| Drop your file(s) here | Datei hier ablegen / Dateien hier ablegen | upload.dropTitle(Many) |
| Choose file(s) | Datei auswählen / Dateien auswählen | upload.choose(Many) |
| Choose another file | Andere Datei auswählen | upload.replace |
| Add more files | Weitere Dateien hinzufügen | upload.addMore |
| Processed in your browser — nothing is uploaded | Verarbeitung im Browser – nichts wird hochgeladen | upload.privacy |
| Create scanned PDF / Create {n} scanned PDFs | Gescanntes PDF erstellen / {n} gescannte PDFs erstellen | save.create |
| Download again | Erneut herunterladen | save.downloadAgain |
| Show in preview | In der Vorschau anzeigen | files.preview |
| Download this scanned PDF | Dieses gescannte PDF herunterladen | files.downloadOne |
| Remove file | Datei entfernen | files.remove |
| Upload / Adjust / Download (steps) | Hochladen / Anpassen / Herunterladen | steps.* |
| Upload your files | Dateien hochladen | steps.uploadTitle |
| Adjust the scan look | Scan-Optik anpassen | steps.adjustTitle |
| Get your scanned PDF | Gescanntes PDF erhalten | steps.downloadTitle |
| Original / Scanned preview | Original / Scan-Vorschau | preview.* |

Blog-Chrome (`translations/de/chrome.json`): „PDF scannen“ (Nav), „Zu Chrome hinzufügen – kostenlos“, „Kostenloses Tool öffnen →“, „Weitere Anleitungen →“, „Passende Anleitungen“, Autor „Team von {brand}“, „Aktualisiert:“, „{n} Min. Lesezeit“, Datum „{day}. {month} {year}“.

## 5. Betriebssystem- und Programmfunktionen (deutsche Oberfläche)

| English | Deutsch (so in der UI) |
|---|---|
| macOS Preview | Vorschau |
| File menu (macOS) | Ablage |
| File → Export… (Preview) | Ablage → Exportieren … |
| File → Export as PDF… | Ablage → Als PDF exportieren … |
| Quartz Filter | Quartz-Filter |
| Quartz: Black & White | Schwarzweiß |
| Quartz: Gray Tone | Grauton |
| Quartz: Reduce File Size | Dateigröße reduzieren |
| Print… / Save as PDF (macOS print dialog) | Drucken … / Als PDF sichern |
| Thumbnails (Preview sidebar) | Miniaturen |
| Windows „Microsoft Print to PDF“ | Microsoft Print to PDF (Name bleibt) |
| Windows Photos app | Fotos |
| Print (Windows) | Drucken |
| Color mode / Black and white / Grayscale (Windows print) | Farbmodus / Schwarzweiß / Graustufen |
| Downloads folder | Ordner „Downloads“ |
| Chrome/Edge: Print → Destination → Save as PDF | Drucken → Ziel → Als PDF speichern |
| Chrome: More settings | Weitere Einstellungen |
| Chrome: Color → Black and white | Farbe → Schwarz-Weiß |
| Chrome side panel | Seitenleiste |
| Chrome Extensions | Erweiterungen |
| Add to Chrome (Web Store button) | Zu Chrome hinzufügen |
| Developer tools / Network tab | Entwicklertools / Tab „Netzwerk“ |
| iPhone Files app | Dateien |
| iPhone Notes app | Notizen |
| Scan Documents (iOS) | Dokumente scannen |
| Camera | Kamera |
| Word: File → Save As → PDF | Datei → Speichern unter → PDF |
| Word/Excel: File → Export → Create PDF/XPS Document | Datei → Exportieren → PDF/XPS-Dokument erstellen |
| Google Docs: File → Download → PDF Document (.pdf) | Datei → Herunterladen → PDF-Dokument (.pdf) |
| Google Doc (a single document) | Google-Dokument (Produkt: Google Docs) |

## 6. Keyword-Plan und Slugs

| en-slug | Lokales Hauptkeyword | Lokalisierter Slug | Titel |
|---|---|---|---|
| (Startseite /) | pdf wie gescannt aussehen lassen | /de/ | PDF wie gescannt aussehen lassen – kostenlos, ohne Upload |
| (Blog-Index /blog/) | pdf wie gescannt aussehen lassen (Anleitungen) | /de/blog/ | PDF wie gescannt aussehen lassen: Anleitungen & Tipps |
| how-to-make-a-pdf-look-scanned | pdf wie gescannt aussehen lassen | pdf-wie-gescannt-aussehen-lassen | PDF wie gescannt aussehen lassen: 6 kostenlose Methoden |
| make-a-document-look-scanned | dokument wie gescannt aussehen lassen | dokument-wie-gescannt-aussehen-lassen | Dokument wie gescannt aussehen lassen: Word & Google Docs |
| pdf-to-scanned-pdf | pdf in gescanntes pdf umwandeln | pdf-in-gescanntes-pdf-umwandeln | PDF in gescanntes PDF umwandeln – flach und gut lesbar |
| what-is-a-scanned-pdf | gescanntes pdf | was-ist-ein-gescanntes-pdf | Was ist ein gescanntes PDF? Unterschied zum digitalen PDF |
| image-to-scanned-pdf | bild in gescanntes pdf umwandeln | bild-in-gescanntes-pdf-umwandeln | Bild in gescanntes PDF umwandeln: JPG oder Foto als Scan |
| convert-color-pdf-to-black-and-white | pdf in schwarz weiß umwandeln | pdf-in-schwarz-weiss-umwandeln | PDF in Schwarz-Weiß umwandeln: 5 kostenlose Wege |
| scan-effect | scan effekt | scan-effekt | Scan-Effekt: Was ein Dokument gescannt aussehen lässt |

Interne Linktexte (Ankertext deutsch, `href` bleibt englisch, z. B. `/blog/scan-effect/`): „PDF wie gescannt aussehen lassen“, „Dokument wie gescannt aussehen lassen“, „PDF in gescanntes PDF umwandeln“, „Was ist ein gescanntes PDF?“, „Bild in gescanntes PDF umwandeln“, „farbiges PDF in Schwarz-Weiß umwandeln“, „Scan-Effekt-Einstellungen“, „den Scanner“ (`/scan`), „Stapelscan“ (`/scan/bulk`).
