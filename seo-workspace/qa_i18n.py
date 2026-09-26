#!/usr/bin/env python3
"""QA for translations: python3 seo-workspace/qa_i18n.py <lang> [ui|chrome|home|<en-slug> ...]

<lang> is a code from lookscanned.io-main/src/locale/languages.json (de, fr, pt-BR, ja, ...).
With no parts given, every part that exists for that language is checked.

A translation must keep the English source's structure (heading ids, FAQ, tables, steps, links,
placeholders) so the builders can render it with the same templates and schema. Exit code 1 on any FAIL.
"""
import collections
import json
import re
import sys
from pathlib import Path

from qa import ALLOWED_CLASSES, EMOJI, FORBIDDEN

ROOT = Path(__file__).resolve().parent
SITE_SRC = ROOT.parent / "lookscanned.io-main" / "src"
ARTICLES = ROOT / "articles"
TRANSLATIONS = ROOT / "translations"
LANGUAGES = json.loads((SITE_SRC / "locale" / "languages.json").read_text())
CJK = {"ja", "ko"}
PLACEHOLDER = re.compile(r"\{[a-z_]+\}")
# Frequent English function words; a translated page that still contains many of them has untranslated passages.
EN_MARKERS = re.compile(r"\b(the|and|with|your|which|this|that|from|you|are)\b", re.I)
META_FIELDS = ["slug", "title", "description", "h1", "tag", "main_keyword", "keywords", "howto_name",
               "cta_title", "cta_body", "about", "mentions", "source_modified"]


def strip(s):
    import html
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def flat(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict):
            out.update(flat(v, key + "."))
        else:
            out[key] = v
    return out


def structure(body):
    """Everything that must survive translation unchanged."""
    return {
        "h2 ids": re.findall(r'<h2 id="([^"]+)"', body),
        "h3 count": len(re.findall(r"<h3[ >]", body)),
        "toc ids": re.findall(r'<a href="#([^"]+)"', (re.findall(r'<nav class="toc".*?</nav>', body, re.S) or [""])[0]),
        "faq items": body.count('class="faq-item"'),
        "tables": body.count("<table"),
        "table rows": body.count("<tr"),
        "step items": sum(len(re.findall(r"<li[ >]", m)) for m in re.findall(r'<ol class="step-list">(.*?)</ol>', body, re.S)),
        "list items": len(re.findall(r"<li[ >]", body)),
        "callouts": len(re.findall(r'class="callout', body)),
        "expert quotes": body.count('class="expert-quote"'),
        "stat cards": body.count('class="stat-card"'),
        "spec terms": body.count("<dt"),
        "links": sorted(re.findall(r'href="([^"]+)"', body)),
    }


def english_leftovers(text):
    return len(EN_MARKERS.findall(text))


def common_checks(ok, lang, body, en_body):
    text = re.sub(r"\s+", " ", strip(body))
    en_s, tr_s = structure(en_body), structure(body)
    for key in en_s:
        if key == "links":
            missing = collections.Counter(en_s[key]) - collections.Counter(tr_s[key])
            extra = collections.Counter(tr_s[key]) - collections.Counter(en_s[key])
            ok("same links as English", not missing and not extra, f"missing {dict(missing)} extra {dict(extra)}"
               if missing or extra else f"{len(en_s[key])} links")
        else:
            ok(f"same {key} as English", en_s[key] == tr_s[key],
               "" if en_s[key] == tr_s[key] else f"en={en_s[key]} tr={tr_s[key]}")
    classes = set(c for cl in re.findall(r'class="([^"]+)"', body) for c in cl.split())
    en_classes = set(c for cl in re.findall(r'class="([^"]+)"', en_body) for c in cl.split())
    ok("only classes used by the English source", classes <= (ALLOWED_CLASSES | en_classes),
       ", ".join(sorted(classes - ALLOWED_CLASSES - en_classes)))
    ok("no <h1> / inline style", "<h1" not in body and "style=" not in body)
    ok("no emoji", not EMOJI.search(text))
    low = text.lower()
    hits = [f for f in FORBIDDEN if re.search(r"(?<![a-z])" + re.escape(f) + r"(?![a-z])", low)]
    ok("no forbidden brands", not hits, ", ".join(sorted(set(hits))))
    left = english_leftovers(text)
    en_left = english_leftovers(re.sub(r"\s+", " ", strip(en_body)))
    limit = max(12, en_left // 25)
    ok("no untranslated English passages", left <= limit,
       f"{left} English function words (limit {limit}); look for sentences left in English")
    ratio = len(text) / max(1, len(re.sub(r"\s+", " ", strip(en_body))))
    lo, hi = (0.25, 0.9) if lang in CJK else (0.8, 1.7)
    ok("length close to the English source", lo <= ratio <= hi, f"{ratio:.2f}× the English character count")


def check_ui(lang, ok):
    en = flat(json.loads((SITE_SRC / "locale" / "messages" / "en.json").read_text()))
    path = SITE_SRC / "locale" / "messages" / f"{lang}.json"
    if not path.exists():
        ok("UI file exists", False, str(path))
        return
    tr = flat(json.loads(path.read_text()))
    ok("same keys as en.json", set(tr) == set(en),
       f"missing {sorted(set(en) - set(tr))} extra {sorted(set(tr) - set(en))}")
    bad_ph, bad_pipe, bad_char, same = [], [], [], []
    for k, v in en.items():
        t = tr.get(k)
        if not isinstance(t, str):
            continue
        if sorted(PLACEHOLDER.findall(v)) != sorted(PLACEHOLDER.findall(t)):
            bad_ph.append(k)
        if v.count("|") != t.count("|"):
            bad_pipe.append(k)
        if re.search(r"[@$%]|\{(?![a-z_]+\})", t):
            bad_char.append(k)
        if t == v and len(v) > 12 and not re.fullmatch(r"[A-Z0-9 ,.·/-]+", v):
            same.append(k)
    ok("placeholders kept", not bad_ph, ", ".join(bad_ph))
    ok("plural '|' forms kept", not bad_pipe, ", ".join(bad_pipe))
    ok("no @ $ % or stray braces (vue-i18n syntax)", not bad_char, ", ".join(bad_char))
    ok("strings are translated", len(same) <= 3, ", ".join(same))
    title, desc = tr.get("base.seo.homeTitle", ""), tr.get("base.seo.homeDescription", "")
    tmax, dmin, dmax = (32, 50, 120) if lang in CJK else (65, 120, 165)
    ok("home title length", 0 < len(title) <= tmax, f"{len(title)} chars (max {tmax})")
    ok("home description length", dmin <= len(desc) <= dmax, f"{len(desc)} chars ({dmin}–{dmax})")


def check_chrome(lang, ok):
    en = json.loads((TRANSLATIONS / "en.chrome.json").read_text())
    path = TRANSLATIONS / lang / "chrome.json"
    if not path.exists():
        ok("chrome.json exists", False, str(path))
        return
    tr = json.loads(path.read_text())
    ok("same keys as en.chrome.json", set(flat(tr)) == set(flat(en)),
       f"missing {sorted(set(flat(en)) - set(flat(tr)))} extra {sorted(set(flat(tr)) - set(flat(en)))}")
    bad = [k for k, v in flat(en).items() if isinstance(v, str) and isinstance(flat(tr).get(k), str)
           and sorted(PLACEHOLDER.findall(v)) != sorted(PLACEHOLDER.findall(flat(tr)[k]))]
    for k in ("date_month", "date_day"):
        if "{year}" not in tr.get(k, ""):
            bad.append(k)
    ok("placeholders kept", not bad, ", ".join(bad))
    ok("12 month names", isinstance(tr.get("months"), list) and len(tr["months"]) == 12)
    tmax, dmin, dmax = (32, 50, 120) if lang in CJK else (65, 120, 165)
    ok("index title length", 0 < len(tr.get("index_title", "")) <= tmax, f"{len(tr.get('index_title', ''))}")
    ok("index description length", dmin <= len(tr.get("index_description", "")) <= dmax,
       f"{len(tr.get('index_description', ''))}")


def check_home(lang, ok):
    en_body = (SITE_SRC / "content" / "home-guide" / "en.html").read_text()
    path = SITE_SRC / "content" / "home-guide" / f"{lang}.html"
    if not path.exists():
        ok("home guide exists", False, str(path))
        return
    body = path.read_text()
    ok("wrapper kept", body.lstrip().startswith('<section class="home-guide" aria-labelledby="hg-what">'))
    common_checks(ok, lang, body, en_body)


def has_kw(kw, s):
    s, kw = s.lower(), kw.lower()
    return kw in s or all(w in s for w in kw.split())


def check_article(lang, slug, ok, all_slugs):
    src = ARTICLES / slug
    en_meta = json.loads((src / "meta.json").read_text())
    en_body = (src / "body.html").read_text()
    d = TRANSLATIONS / lang / slug
    if not (d / "meta.json").exists() or not (d / "body.html").exists():
        ok("meta.json + body.html exist", False, str(d))
        return
    meta = json.loads((d / "meta.json").read_text())
    body = (d / "body.html").read_text()
    missing = [f for f in META_FIELDS if not meta.get(f)]
    ok("meta fields present", not missing, ", ".join(missing))
    s = meta.get("slug", "")
    ok("slug is lowercase ASCII with hyphens", bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", s)), s)
    if lang in CJK:
        ok("CJK slug = English slug", s == slug, f"{s} (expected {slug})")
    ok("slug unique in this language", all_slugs.count(s) == 1, s)
    ok("source_modified matches English", meta.get("source_modified") == (en_meta.get("date_modified") or en_meta["date_published"]),
       f"{meta.get('source_modified')} vs {en_meta.get('date_modified')}")
    tmax, dmin, dmax = (32, 50, 120) if lang in CJK else (65, 120, 165)
    ok("title length", 0 < len(meta.get("title", "")) <= tmax, f"{len(meta.get('title', ''))} chars (max {tmax})")
    ok("description length", dmin <= len(meta.get("description", "")) <= dmax,
       f"{len(meta.get('description', ''))} chars ({dmin}–{dmax})")
    kw = meta.get("main_keyword", "")
    ok("main keyword in title", has_kw(kw, meta.get("title", "")), kw)
    ok("main keyword in H1", has_kw(kw, meta.get("h1", "")), kw)
    lead = re.search(r'<p class="lead">(.*?)</p>', body, re.S)
    ok("lead paragraph with main keyword", bool(lead) and has_kw(kw, strip(lead.group(1))))
    h2s = [strip(t) for t in re.findall(r"<h2 id=\"[^\"]+\">(.*?)</h2>", body, re.S)]
    ok("main keyword in 2+ H2", sum(has_kw(kw, h) for h in h2s) >= 2, f"{sum(has_kw(kw, h) for h in h2s)}")
    long_heads = [h for h in h2s if len(h) > (40 if lang in CJK else 75)]
    ok("H2 not too long", not long_heads, "; ".join(long_heads[:3]))
    common_checks(ok, lang, body, en_body)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    lang = sys.argv[1]
    codes = [l["code"] for l in LANGUAGES if l["code"] != "en"]
    if lang not in codes:
        sys.exit(f"unknown language {lang}; use one of {', '.join(codes)}")
    en_slugs = sorted(p.name for p in ARTICLES.iterdir() if (p / "meta.json").exists())
    parts = sys.argv[2:] or ["ui", "chrome", "home"] + [s for s in en_slugs if (TRANSLATIONS / lang / s).exists()]
    all_slugs = [json.loads((TRANSLATIONS / lang / s / "meta.json").read_text()).get("slug", "")
                 for s in en_slugs if (TRANSLATIONS / lang / s / "meta.json").exists()]
    failed = False
    for part in parts:
        res = []

        def ok(name, passed, note=""):
            res.append((name, bool(passed), note))

        if part == "ui":
            check_ui(lang, ok)
        elif part == "chrome":
            check_chrome(lang, ok)
        elif part == "home":
            check_home(lang, ok)
        elif part in en_slugs:
            check_article(lang, part, ok, all_slugs)
        else:
            sys.exit(f"unknown part {part}")
        print(f"\n== {lang} / {part}")
        for name, passed, note in res:
            failed |= not passed
            print(f"  {'PASS' if passed else 'FAIL'}  {name}{'  — ' + note if note else ''}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
