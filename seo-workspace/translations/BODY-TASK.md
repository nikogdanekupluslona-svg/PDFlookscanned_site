# Task: translate article bodies (phase 2)

Repository root: /Users/alenamumladze/Desktop/HHB/PDFlookscanned_site. Your prompt names a language `<code>` and
a list of English article slugs. Interface strings, the glossary and every article's meta.json for that language
already exist (phase 1). You write `seo-workspace/translations/<code>/<en-slug>/body.html` for each listed slug.

## Read first
- `seo-workspace/translations/TRANSLATOR-GUIDE.md` — the rules; follow them exactly
- `seo-workspace/translations/<code>/glossary.md` — terminology, style, interface labels, keyword notes
- `lookscanned.io-main/src/locale/messages/<code>.json` — exact interface labels
- `seo-workspace/writer-guide.md`, section "The product" — the facts

## For each listed article
1. Read the full English source `seo-workspace/articles/<en-slug>/body.html` and
   `seo-workspace/translations/<code>/<en-slug>/meta.json` (local main keyword, title, h1).
2. **If `body.html` already exists** and `qa_i18n.py` fails on it, it is an unfinished draft from an earlier run,
   cut off at a chunk boundary. Read it, find the exact point where it stops relative to the English source, and
   append the rest from there — do not rewrite the finished part (fix it only if QA or proofreading needs it).
   If it already passes QA, just proofread it.
3. Otherwise write it from scratch: a complete, fluent, localized version with identical markup, ids, hrefs,
   classes and structure; only human-readable text translated; the local main keyword in the first sentence of the
   lead, in at least two H2 headings and naturally ~5+ times; interface labels exactly as in `<code>.json`.
   Translate EVERYTHING — every paragraph, list item, table caption/cell, callout, quote and FAQ answer; never
   shorten, summarize or skip.
4. **Writing mechanics (long single writes time out):** write in chunks of at most ~6,000 characters
   (~4,000 for ja/ko): create the file with the first chunk (Write tool), then append each next chunk with Bash
   `cat >> <file> <<'EOF' ... EOF` (quoted EOF). Go through the source in order, section by section.
5. Run `python3 seo-workspace/qa_i18n.py <code> <en-slug>` and fix every FAIL (structure mismatch → compare counts
   with the source; untranslated English → translate leftover sentences). You may adjust title/description/h1 in
   meta.json only if QA requires it; never change `slug` or `main_keyword`.
6. Proofread once as a native editor: fluency, glossary consistency, no calques, numbers and facts identical to
   the English source (keep source figures even if you believe the product differs; mention such doubts in your
   final reply).

Only create/edit files in `seo-workspace/translations/<code>/<your slugs>/`; never touch other files, languages or
git. Final reply (short): per article, the QA result (all PASS, or what remains) and any doubts about facts.
