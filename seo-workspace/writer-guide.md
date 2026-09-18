# Writer guide — pdflookscanned.com blog (project config for the GEO/SEO pipeline)

This file is the filled SETUP of `geo-seo-article-pipeline-template — копия.md` (repo root) for this project,
plus the exact output format. Read the template's Stages 1–9 for the norms; this file overrides where they differ.

## Project configuration

| Placeholder | Value |
|---|---|
| BRAND_NAME | Make PDF look scanned |
| WEBSITE_URL | https://pdflookscanned.com/ |
| BLOG_URL / pattern | https://pdflookscanned.com/blog/ · `/blog/{slug}/` |
| LANGUAGE / MARKET | English (US) / United States, worldwide English readers |
| EXPERT | "The Make PDF look scanned team" — no named person. The single `.expert-quote` is written in first person plural ("we") as the team that builds the tool. JSON-LD author = Organization (build.py does this). |
| CTA | added automatically by build.py (Open the free tool → /scan · Add to Chrome · More guides) — do NOT write a CTA block |
| TRUST BADGE | added automatically by build.py after `.lead` — do NOT write it |
| FORBIDDEN | **Never name any competitor or third-party product/app/site**: no scan-effect sites, no PDF suites (Adobe/Acrobat, Smallpdf, iLovePDF, pdfgear, Wondershare, etc.), no image editors by name (Photoshop, GIMP, Affinity…), no scanner apps (CamScanner, Lens…), no ImageMagick/Ghostscript, no "lookscanned". Say "a raster image editor", "a phone scanner app", "desktop PDF software" instead. `seo-workspace/qa.py` has the full list and fails the article on any hit. |
| ALLOWED to name | Google Chrome, Chrome Web Store, Microsoft Edge, Windows and its built-in "Microsoft Print to PDF", macOS and its built-in Preview app (Quartz filters, Export as PDF), iPhone/Android built-in camera and Files/Notes scanning as OS features, Microsoft Word and Google Docs only as the *source document format* (export steps), PDF/A, ISO 32000, JPEG, PNG, OCR, WCAG. |
| Year / date | 2026, date_published 2026-09-18 |

## The product — describe ONLY what really exists

Web tool (https://pdflookscanned.com/scan) and Chrome extension (same engine, side panel). Verified from the source code:
- Input formats: PDF, JPG, PNG, WebP, SVG, GIF, BMP, DOCX, XLSX/XLS, CSV, TXT, MD, HTML.
- CONVERSION FIDELITY (verified in src/utils/document-source): PDFs are used as-is (layout preserved). DOCX → only the raw text is extracted (formatting, fonts, tables, images, headers are LOST) and re-typeset on A4 pages in Helvetica 11 pt with 0.75-inch margins. XLSX/XLS/CSV → each sheet becomes CSV text on A4 pages. HTML → visible text only. TXT/MD → plain text on A4. Therefore: for any document whose layout matters (Word, Google Docs, Excel, letters, forms) the correct route is to Save/Export as PDF first, then make the PDF look scanned. State this honestly.
- Images: each image is scaled to fit and centered on an A4 page (landscape A4 if the image is wider than tall) — one image = one page; JPG and PNG are embedded as-is; WebP/SVG/GIF/BMP are first rasterized to JPEG (quality 0.92, longest edge capped at 2,200 px). One image file = one single-page PDF; the tool does not crop, deskew, correct perspective or merge several images into one PDF (bulk scan outputs one PDF per file in a ZIP). To combine images, put them into one PDF first (e.g. macOS Preview → select pages → Print → Save as PDF; Windows Photos → Print → Microsoft Print to PDF), then scan-effect that PDF.
- Controls (range · default): Rotate −10°…10° · 1°; Rotate variance 0…10° · 0.5° (random per page); Blur 0…1 · 0.3; Noise 0…1 · 0.1; Brightness 0…2 · 1; Contrast 0…2 · 1; Yellowish (paper tone) 0…2 · 0; Colorspace Gray/Color · Gray; Border (1-px dark frame line around the page) on/off · off; Resolution 1×…3× in 0.5 steps · 2× (PDF pages render at 72 dpi × scale, so 2× ≈ 144 dpi, 3× ≈ 216 dpi). Pages are exported as JPEG images inside a new PDF.
- Extras: text or image watermark; stamp/signature image with horizontal/vertical position and size; editable PDF metadata (title, author, subject, keywords, producer, creator).
- Bulk scan (web: /scan/bulk; extension: several files) → download all as ZIP.
- Live preview; processing is local in the browser (pdf.js + canvas); files are not uploaded to a processing server; works offline after first load (PWA); free, no signup; mobile browsers supported for the website.
- Chrome extension is rated 5 stars in the Chrome Web Store: https://chromewebstore.google.com/detail/make-pdf-look-scanned/ijhpnlcipgiokgignkbbbgkobdmdoila
- The tool has NO creases, folds, coffee stains, edge shadows, perspective warp or OCR. Never claim these as tool features (you may describe them as artifacts of real scanners or as things other methods produce).

## Ethics block (every article)
Include one short `.callout.callout-warn` on honest use: the scan look changes appearance, not authenticity; don't forge or alter official documents/IDs/signatures that are not yours; some courts/agencies require text-searchable PDFs — check rules. Keep it factual, not preachy.

## Sources
- `seo-workspace/fact-bank.json` — verified facts and quotes per topic. Use them first; you may research more with WebSearch/WebFetch but only from allowed source types (government, standards bodies W3C/ISO/PDF Association, universities, Library of Congress/NARA/FADGI, Apple/Microsoft support for OS features, Wikipedia for facts, major news). Never from competitors.
- 5–6 external expert quotes per article, spread over ≥3 sections, each inline in a `<p>` (or `.callout.callout-info`) with the organization/person named and a link to the exact source URL. Only verbatim if you saw the exact text; otherwise an attributed paraphrase ("according to the Library of Congress …"). Never invent.
- Any number not from a source must be our own measurable product fact (settings above) or phrased as a clearly marked estimate.

## Output files (per article, folder `seo-workspace/articles/<slug>/`)

### meta.json
```json
{
  "order": 1,
  "title": "≤60 chars, main keyword at start",
  "description": "140–160 chars",
  "h1": "H1 with main keyword near the start + benefit hook",
  "tag": "Short category tag",
  "main_keyword": "exact main keyword (lowercase)",
  "keywords": ["main", "secondary", "..."],
  "word_target": 4000,
  "date_published": "2026-09-18",
  "date_modified": "2026-09-18",
  "about": ["entity", "..."],
  "mentions": ["entity", "..."],
  "howto_name": "How to … (name for HowTo schema from the first ol.step-list)",
  "related": ["other-slug", "other-slug", "other-slug"],
  "cta_title": "optional custom CTA headline",
  "cta_body": "optional custom CTA text"
}
```

### body.html — inner content only, in this order
1. `<p class="lead">` — 40–60 words, self-contained direct answer containing the main keyword (BLUF). No other element before it.
2. `<p>` "about this article" paragraph (pain → what you'll get → where data comes from).
3. `<nav class="toc" aria-label="Table of contents"><h2>Table of Contents</h2><ol><li><a href="#id">…</a></li>…</ol></nav>` — hrefs exactly equal to the H2 ids, in order.
4. Sections: `<h2 id="kebab-id">Question-form heading ≤60 chars</h2>` immediately followed by a `<p>` of 40–50 words that answers it on its own (name the entity, no "it/this" openers). H3 allowed inside. At least 2 H2s contain the main keyword; every H2/H3 contains a search keyword/phrase.
5. Exactly one `<div class="expert-quote"><blockquote>…</blockquote><cite><strong>The Make PDF look scanned team</strong> — builders of the web tool and Chrome extension</cite></div>`.
6. FAQ section: `<h2 id="faq">… FAQ heading with keyword</h2>` + intro `<p>` 40–50 words + 8–12 × `<div class="faq-item"><p class="faq-q">Question?</p><p class="faq-a">Answer 2–4 sentences.</p></div>` (faq-q and faq-a on the same line/adjacent).
7. Final short H2 "verdict/next step" section is optional — do not write a CTA block.

Allowed classes only: lead, toc, stats-grid, stat-card, stat-number, stat-label, callout (+ callout-tip | callout-warn | callout-info), expert-quote, table-wrap, spec-list, faq-item, faq-q, faq-a, step-list.
- Tables: `<div class="table-wrap"><table><caption>…</caption><thead><tr><th scope="col">…</th></tr></thead><tbody><tr><th scope="row">…</th><td>…</td></tr></tbody></table></div>`.
- Steps: `<ol class="step-list"><li><strong>Step name.</strong> text</li></ol>` (the first step-list becomes HowTo schema — make it the main procedure).
- Callouts: `<div class="callout callout-tip"><strong>Heading</strong>Text</div>`.
- `<dl class="spec-list"><dt>…</dt><dd>…</dd></dl>` for parameter → value pairs.
- Links: internal as root-relative (`/scan`, `/scan/bulk`, `/blog/<slug>/`); external `https://…` with `target="_blank" rel="noopener"`. Link to the tool (/scan) at least 3 times naturally.
- No `<h1>`, no inline style, no images, no emoji anywhere in body. Paragraphs ≤ 70 words (split longer). At least one non-text block (table/list block/callout/stats/spec-list) per ~500 words.
- Use US English, plain and concrete; one fact per paragraph minimum; consistent terminology; no hype words ("revolutionary", "game-changing"), no filler, no repetition to reach length. Length comes from depth: methods, exact settings, comparisons, troubleshooting, checks, use-cases, glossary, FAQ.

## Published slugs (for internal links — link 3–6 of these naturally in the body)
- `/` — the tool home ("make PDF look scanned online")
- `/scan` — the scanner, `/scan/bulk` — bulk scan
- `/blog/how-to-make-a-pdf-look-scanned/` — pillar: 6 methods
- `/blog/make-a-document-look-scanned/` — Word, Google Docs, photos
- `/blog/pdf-to-scanned-pdf/` — flatten/convert, DPI, file size
- `/blog/what-is-a-scanned-pdf/` — definition, scanned copy, how to tell
- `/blog/image-to-scanned-pdf/` — JPG/phone photo to scanned PDF
- `/blog/convert-color-pdf-to-black-and-white/` — grayscale vs B&W
- `/blog/scan-effect/` — artifacts and presets

## Done criteria
Run `python3 seo-workspace/qa.py <slug>` — every line must be PASS (fix and re-run until it is). Then run `python3 seo-workspace/build.py` to be sure it builds. Do not commit or push.

## Fact-bank caveats
- Do not name Xerox, WordPerfect or any other brand from a quote; use an attributed paraphrase without the brand name instead (e.g. "BBC News reported in 2013 that some office copiers altered digits in scans because of JBIG2 compression").
- Library of Congress, ISO and pdfa.org pages could not be fetched — do not quote them.
- Google Docs support pages are not a source; describe Google Docs export steps (File → Download → PDF document) as plain instructions without quoting.

## Writing mechanics (IMPORTANT — previous attempts timed out)
Never produce the whole article in one tool call. Write body.html in 5–7 chunks of roughly 500–800 words each: create the file with the first chunk (Write tool), then append each next chunk with Bash `cat >> file <<'EOF' ... EOF` (quoted EOF). Keep each tool call's content under ~6,000 characters. Do research in short, focused steps (fact-bank first; at most a few extra fetches). Run qa.py after the full draft, then fix issues with Edit.
