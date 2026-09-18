#!/usr/bin/env python3
"""Stage 9 QA for one article: python3 seo-workspace/qa.py <slug> [<slug> ...]  (no args = all)

Measures the pipeline norms instead of eyeballing them. Exit code 1 if any hard check fails.
"""
import collections
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTICLES = ROOT / "articles"

# Competitors and third-party products that must never be named (project owner rule).
FORBIDDEN = [
    "lookscanned", "look scanned io", "supertool", "super tool", "scannedmaker", "scanned maker", "lightpdf",
    "toscanned", "10015", "wondershare", "pdfelement", "sliksafe", "doc2scan", "adobe", "acrobat", "photoshop",
    "gimp", "smallpdf", "ilovepdf", "pdfgear", "zamzar", "pdffiller", "safepdfkit", "imagestool", "konfuzio",
    "camscanner", "microsoft lens", "office lens", "genius scan", "scanner pro", "scannable", "sejda", "pdf24",
    "foxit", "nitro", "canva", "affinity", "pixelmator", "paint.net", "imagemagick", "ghostscript", "scanyourpdf",
    "falsisign", "look-like-scanned", "11zon", "pdf-lab", "onlinescanner", "photext", "scannereffect",
    "google drive scan", "tinywow", "docfly", "pdfescape", "xodo", "kami", "dochub", "docusign", "grainy",
]
ALLOWED_CLASSES = {
    "lead", "toc", "stats-grid", "stat-card", "stat-number", "stat-label", "callout", "callout-tip",
    "callout-warn", "callout-info", "expert-quote", "table-wrap", "spec-list", "faq-item", "faq-q", "faq-a",
    "step-list",
}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⭕⌚-⏿]")
STOP = set("""a an the and or of to in on for with is are be it this that as at by from your you can if not
your's its was were will would should could than then there their they them these those have has had do does
did so but when which what how why who into out up down more most less about over under also just only one two
all any each other some such no nor too very s t don isn aren we our us my me i he she his her after before
while same own both few where because through during between against again further once here off above below
use using used make makes made page pages file files""".split())


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def wc(s):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.%-]*", strip(s)))


def check(slug):
    d = ARTICLES / slug
    meta = json.loads((d / "meta.json").read_text())
    body = (d / "body.html").read_text()
    text = re.sub(r"\s+", " ", strip(body)).lower()
    res = []

    def ok(name, passed, note=""):
        res.append((name, bool(passed), note))

    kw = meta["main_keyword"].lower()
    total = wc(body)
    target = meta.get("word_target", 2500)
    ok("length >= target", total >= target, f"{total} / {target} words, {len(strip(body))} chars")
    ok("title <= 60 chars", len(meta["title"]) <= 60, f"{len(meta['title'])}")
    ok("description 140-160 chars", 140 <= len(meta["description"]) <= 160, f"{len(meta['description'])}")
    kw_words = kw.split()

    def has_kw(s):
        s = s.lower()
        return kw in s or all(w in s for w in kw_words)

    ok("keyword in title", has_kw(meta["title"]))
    ok("keyword in H1", has_kw(meta["h1"]))
    first150 = " ".join(re.findall(r"\S+", strip(body))[:150])
    ok("keyword in first 150 words", has_kw(first150))
    ok("no <h1> / inline style in body", "<h1" not in body and "style=" not in body)

    h2s = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)
    toc = re.findall(r'<nav class="toc"[^>]*>.*?</nav>', body, re.S)
    toc_ids = re.findall(r'href="#([^"]+)"', toc[0]) if toc else []
    ok("TOC present with aria-label", bool(toc) and 'aria-label=' in toc[0])
    ok("TOC ids == H2 ids", toc_ids == [i for i, _ in h2s], f"toc={len(toc_ids)} h2={len(h2s)}")
    ok("H2 with keyword >= 2", sum(has_kw(strip(t)) for _, t in h2s) >= 2,
       f"{sum(has_kw(strip(t)) for _, t in h2s)}")
    heads = [strip(t).strip() for t in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body, re.S)]
    long_heads = [h for h in heads if len(h) > 60 and h != "Table of Contents"]
    ok("H2/H3 <= 60 chars", not long_heads, "; ".join(long_heads))

    lead = re.search(r'<p class="lead">(.*?)</p>', body, re.S)
    lw = wc(lead.group(1)) if lead else 0
    ok("lead 40-60 words", 40 <= lw <= 60, f"{lw}")
    bluf_bad = []
    for m in re.finditer(r'<h2 id="([^"]+)">.*?</h2>\s*<p>(.*?)</p>', body, re.S):
        n = wc(m.group(2))
        if not 30 <= n <= 60:
            bluf_bad.append(f"{m.group(1)}={n}")
    missing_bluf = [i for i, _ in h2s if not re.search(rf'<h2 id="{re.escape(i)}">.*?</h2>\s*<p>', body, re.S)]
    ok("H2 opens with 40-50w answer (±10)", not bluf_bad and not missing_bluf,
       ", ".join(bluf_bad + [f"{i}=no <p>" for i in missing_bluf]))
    long_p = [wc(p) for p in re.findall(r"<p>(.*?)</p>", body, re.S) if wc(p) > 75]
    ok("paragraphs <= ~70 words", not long_p, f"{len(long_p)} long: {long_p[:8]}")

    tables = re.findall(r"<table>(.*?)</table>", body, re.S)
    ok("tables have caption + scope", all("<caption>" in t and "scope=" in t for t in tables), f"{len(tables)} tables")
    ok("no emoji in body", not EMOJI.search(strip(body)))
    classes = set(c for cl in re.findall(r'class="([^"]+)"', body) for c in cl.split())
    ok("only allowed classes", classes <= ALLOWED_CLASSES, ", ".join(sorted(classes - ALLOWED_CLASSES)))
    hits = [f for f in FORBIDDEN if re.search(r"(?<![a-z])" + re.escape(f) + r"(?![a-z])", text)]
    hits += [f for f in FORBIDDEN if re.search(re.escape(f), " ".join(re.findall(r'href="([^"]+)"', body)).lower())]
    ok("no forbidden brands", not hits, ", ".join(sorted(set(hits))))
    faq = len(re.findall(r'class="faq-item"', body))
    ok("FAQ >= 5", faq >= 5, f"{faq}")
    ok("comparison table present", len(tables) >= 1)
    ok("one .expert-quote (brand team)", body.count('class="expert-quote"') == 1)
    ext = [u for u in re.findall(r'href="(https?://[^"]+)"', body) if "pdflookscanned.com" not in u
           and "chromewebstore.google.com" not in u]
    ok("external sources >= 5", len(set(ext)) >= 5, f"{len(set(ext))}")
    internal = re.findall(r'href="(/[^"]*)"', body)
    ok("links to the tool", any(u.startswith("/scan") or u == "/" for u in internal), f"{len(internal)} internal")
    blocks = len(re.findall(r'<(table|dl|ol class="step-list"|div class="(?:callout|stats-grid))', body))
    ok("non-text block per ~500 words", blocks >= total // 500, f"{blocks} blocks / {total // 500} needed")
    kwc = text.count(kw)
    ok("main keyword used 5+ times", kwc >= 5, f"{kwc}× exact, density {kwc * len(kw_words) / max(total, 1):.2%}")
    freq = collections.Counter(w for w in re.findall(r"[a-z][a-z'-]+", text) if w not in STOP and len(w) > 2)
    top = [w for w, _ in freq.most_common(10)]
    ok("top words on-topic (info)", True, ", ".join(top))
    return res


def main():
    slugs = sys.argv[1:] or sorted(p.name for p in ARTICLES.iterdir() if (p / "meta.json").exists())
    failed = False
    for s in slugs:
        print(f"\n== {s}")
        for name, passed, note in check(s):
            failed |= not passed
            print(f"  {'PASS' if passed else 'FAIL'}  {name}{'  — ' + note if note else ''}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
