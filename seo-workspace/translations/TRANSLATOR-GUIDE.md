# Translator guide — pdflookscanned.com

The site is English at the root and has 12 localized copies under `/<path>/` (see
`lookscanned.io-main/src/locale/languages.json`: de, fr, es, it, pt-BR, nl, sv, da, no, fi, ja, ko).
This is **localization for search, not 1:1 translation**: every page must read as if it was written for that
market and must use the phrases people there actually type into a search engine. Facts, structure, numbers,
links and schema stay exactly as in the English source.

## Where things go

| What | English source | Your output |
|---|---|---|
| App interface strings | `lookscanned.io-main/src/locale/messages/en.json` | `lookscanned.io-main/src/locale/messages/<code>.json` |
| Home-page guide (long text under the tool) | `lookscanned.io-main/src/content/home-guide/en.html` | `lookscanned.io-main/src/content/home-guide/<code>.html` |
| Blog chrome (header, badge, CTA, dates, blog index) | `seo-workspace/translations/en.chrome.json` | `seo-workspace/translations/<code>/chrome.json` |
| Glossary for your language | — | `seo-workspace/translations/<code>/glossary.md` |
| Article metadata | `seo-workspace/articles/<en-slug>/meta.json` | `seo-workspace/translations/<code>/<en-slug>/meta.json` |
| Article body | `seo-workspace/articles/<en-slug>/body.html` | `seo-workspace/translations/<code>/<en-slug>/body.html` |

`<code>` is the `code` field (`pt-BR`, not `pt-br`). Folder names under `translations/<code>/` are always the
**English** slug; the localized slug goes into `meta.json`.

Check your work with `python3 seo-workspace/qa_i18n.py <code> [ui|chrome|home|<en-slug>]` and fix every FAIL.

## Owner rules (hard)

- **Never name competitors or third-party products** (other scan-effect sites, PDF suites, image editors, scanner
  apps — full list in `seo-workspace/qa.py` → `FORBIDDEN`). The English texts already comply; do not add any.
  OS built-ins are fine: Windows "Microsoft Print to PDF", macOS Preview, Chrome, iPhone/Android camera/Files/Notes.
  Use the names these OS features have **in that language's UI** (e.g. macOS Preview = "Vorschau" in German,
  "Aperçu" in French, "プレビュー" in Japanese); "Microsoft Print to PDF" keeps its name.
- The product/brand name **"Make PDF look scanned"** stays in English as a proper name (it is also the Chrome
  Web Store listing name). Do not translate it; you may describe it ("the free tool", "unser kostenloses Tool").
- Trust badge wording must keep the meaning "rated 5 stars in the Chrome Web Store".
- Do not target or mention the keyword "lookscanned".
- Describe only features that exist (see `seo-workspace/writer-guide.md`, section "The product"). Do not add
  claims, numbers, sources or links that are not in the English source.

## Localization for search

1. For every page pick a **local main keyword**: the most natural, most-searched way to say the English main
   keyword in that language (e.g. EN "make a pdf look scanned" → DE "pdf wie gescannt aussehen lassen",
   FR "faire paraître un pdf scanné" / "pdf effet scanné" — choose what people really search). Prefer the verb
   the market uses for scanning (FR "scanner/numériser", ES "escanear", IT "scansionare", PT-BR "digitalizar/
   escanear", JA "スキャン", KO "스캔"). You may use WebSearch to see which phrasing appears in local results or
   autocomplete; spend at most a few searches per language and never copy competitor text.
2. Put the local main keyword: at the start of `title`, in `h1`, in the first sentence of `.lead`, in at least
   two H2 headings, and naturally about 5+ times across the body. Do not stuff.
3. `title` ≤ 60 characters (hard limit 65); CJK ≤ 30 (hard 32). `description` 140–160 characters (hard 120–165);
   CJK 60–110 (hard 50–120). Write them fresh for the market; do not translate word by word.
4. `keywords`: the local main keyword first, then 5–9 local secondary phrases (local synonyms and long-tail
   variants), all in the target language (English terms only if locals really search them, e.g. "PDF").
5. Headings stay questions where the English heading is a question. Keep them short (≤ 70 chars; CJK ≤ 38).
6. Localize examples inside existing sentences where natural (A4 vs Letter, local date/number format), but
   keep every fact true. US agencies and courts cited in the English text stay as they are (they are sources).

## Style

- Natural, fluent, native-speaker prose; short sentences; no calques. Keep the answer-first style: each H2 opens
  with a 40–60-word direct answer paragraph (CJK: 80–150 characters).
- Address: DE "Sie", FR "vous", ES "tú", IT "tu", PT-BR "você", NL "je", SV/DA/NO "du", FI informal "sinä"
  (or neutral passive), JA です・ます調, KO 합니다체/해요체 mix used on modern tool sites (consistently 합니다체 in body text).
- Numbers: use the local decimal separator in running text (DE "0,3", FR "0,3"), keep the values themselves.
  Degree sign, ×, % as in the source. Thousands separator per local convention.
- Quotes from English sources: translate the quoted words into the target language and keep the attribution
  and the link. Do not present a paraphrase as a verbatim quote.
- Interface labels mentioned in text (buttons, sliders: "Generate Scanned PDF", "Noise", "Blur", "Rotate
  variance", "Yellowish", "Colorspace", "Gray", "Border", "Resolution", "Bulk Scan", "Download all as ZIP"…)
  must be written **exactly as in your language's `messages/<code>.json`**, so readers find them in the app.
- Use your language's `glossary.md` for recurring terms so all pages agree.

## HTML rules (checked by qa_i18n.py)

- Translate only human-readable text: text nodes, `<caption>`, `aria-label`, `alt`. Keep every tag, attribute,
  class, `id` and `href` exactly as in the source; keep the same number of headings, lists, list items, tables,
  rows, callouts, FAQ items, stat cards and links, in the same order.
- `id` values and `#anchors` stay English. Internal links stay as English paths (`/scan`, `/scan/bulk`,
  `/blog/<en-slug>/`): the builder rewrites them to the localized URLs. Translate the anchor text.
- External links (sources) stay unchanged.
- No new classes, no inline styles, no `<h1>`, no emoji.
- `body.html` starts with `<p class="lead">` exactly like the source; the badge, CTA and header are added by the
  builder.

## meta.json for a translated article

```json
{
  "slug": "localized-ascii-slug",
  "title": "…",
  "description": "…",
  "h1": "…",
  "tag": "Short category tag",
  "main_keyword": "local main keyword, lowercase",
  "keywords": ["local main keyword", "…"],
  "howto_name": "Localized name of the HowTo (from the English howto_name)",
  "cta_title": "…",
  "cta_body": "…",
  "about": ["entity names as used in that language's Wikipedia", "…"],
  "mentions": ["…"],
  "source_modified": "<date_modified of the English meta.json>"
}
```

Slug: lowercase ASCII, words joined by hyphens, built from the local main keyword (transliterate: ä→ae, ö→oe,
ü→ue, ß→ss in German; å→a, æ→ae, ø→o in Scandinavian; ä→a, ö→o in Finnish; drop accents elsewhere), 2–6 words,
unique within the language. **ja and ko keep the English slug** (non-Latin slugs turn into %-encoded URLs).
