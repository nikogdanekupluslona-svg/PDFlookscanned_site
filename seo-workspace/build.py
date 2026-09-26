#!/usr/bin/env python3
"""Build the static blog for pdflookscanned.com (Stage 10 + 12 of the article pipeline).

Sources:  seo-workspace/articles/<slug>/meta.json + body.html             (English originals)
          seo-workspace/translations/<lang>/<slug>/meta.json + body.html  (translations; <slug> is the English slug)
          seo-workspace/translations/en.chrome.json, translations/<lang>/chrome.json (page chrome per language)
Output:   lookscanned.io-main/public/blog/<slug>/index.html, public/blog/index.html,
          public/<lang>/blog/<localized-slug>/index.html, public/<lang>/blog/index.html,
          public/sitemap.xml, public/llms.txt, public/robots.txt,
          lookscanned.io-main/src/locale/blog-slugs.json (localized slugs, used by the app for links),
          seo-workspace/article-index.json (internal-link library for Stage 7)

body.html holds the article content from `<p class="lead">` down to the FAQ.
The header, trust badge, CTA, JSON-LD and page chrome are added here so every
article gets identical, validated brand elements. Translated bodies keep the English
internal links (/scan, /blog/<en-slug>/); they are pointed at the language's own pages here.
Languages come from lookscanned.io-main/src/locale/languages.json; the blog of a language is
built once its chrome.json exists, and each article once its translation exists.
"""
import html
import json
import math
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTICLES = ROOT / "articles"
TRANSLATIONS = ROOT / "translations"
APP = ROOT.parent / "lookscanned.io-main"
PUBLIC = APP / "public"
LANGUAGES = json.loads((APP / "src" / "locale" / "languages.json").read_text())
EN = LANGUAGES[0]

SITE = "https://pdflookscanned.com"
BRAND = "Make PDF look scanned"
STORE_URL = "https://chromewebstore.google.com/detail/make-pdf-look-scanned/ijhpnlcipgiokgignkbbbgkobdmdoila"
CJK = {"ja", "ko"}
GLOBE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/>'
         '<path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>')
# Closes the language menu on a click outside it
SWITCHER_JS = ("<script>document.addEventListener('click',function(e){document.querySelectorAll('details.lang[open]')"
               ".forEach(function(d){if(!d.contains(e.target))d.removeAttribute('open')})})</script>")

CSS = """
:root{--bg:#0b0b0f;--card:#14151b;--card2:#1b1c23;--line:#26272f;--text:#e7e7ea;--muted:#b8b8c2;--dim:#8e8e99;--accent:#8fd14f;--accent-ink:#10200a;--accent-soft:#1a2512;--warn:#e8a020;--warn-soft:#2a2112;--font:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
*,*::before,*::after{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--font);font-size:17px;line-height:1.75;-webkit-text-size-adjust:100%}
a{color:var(--accent)}
.site-header{position:sticky;top:0;z-index:10;background:rgba(11,11,15,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.site-header .inner{max-width:1100px;margin:0 auto;padding:14px 20px;display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.site-header .brand{color:#f4f4f5;font-weight:700;text-decoration:none;font-size:17px}
.site-header nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}
.site-header nav a{color:var(--muted);text-decoration:none}
.site-header nav a:hover,.site-header nav a[aria-current]{color:#fff}
.site-header .get{background:var(--accent);color:var(--accent-ink);font-weight:700;text-decoration:none;padding:8px 16px;border-radius:999px;font-size:14px}
.pls-article .container{max-width:820px;margin:0 auto;padding:48px 20px 80px}
.pls-article .breadcrumbs{font-size:14px;color:var(--dim);margin-bottom:22px}
.pls-article .breadcrumbs a{color:var(--muted);text-decoration:none}
.pls-article .article-header{margin-bottom:36px;padding-bottom:28px;border-bottom:1px solid var(--line)}
.pls-article .article-tag{display:inline-block;background:var(--accent-soft);color:var(--accent);font-size:13px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;padding:4px 12px;border-radius:20px;margin-bottom:16px}
.pls-article h1{font-size:clamp(28px,4.4vw,42px);line-height:1.15;letter-spacing:-.03em;margin:0 0 18px;color:#fff}
.pls-article .article-meta{font-size:14px;color:var(--dim);display:flex;gap:18px;flex-wrap:wrap}
.pls-article .article-meta a{color:var(--muted);font-weight:700;text-decoration:none}
.pls-article .lead{font-size:19px;line-height:1.65;color:#f0f0f2;margin:0 0 32px;padding:22px 26px;background:var(--card);border-left:4px solid var(--accent);border-radius:0 10px 10px 0}
.pls-article .trust-badge{display:flex;align-items:center;gap:16px;padding:18px 24px;margin:0 0 36px;background:var(--accent-soft);border:1px solid #2f4520;border-radius:14px}
.pls-article .trust-badge-icon{font-size:28px;line-height:1;flex-shrink:0}
.pls-article .trust-badge-title{font-size:18px;font-weight:800;line-height:1.3;color:#fff}
.pls-article .trust-badge-title span{color:var(--accent)}
.pls-article .trust-badge-sub{font-size:14px;line-height:1.5;color:var(--muted);margin-top:4px}
.pls-article .toc{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:22px 26px;margin-bottom:44px}
.pls-article .toc h2{font-size:13px;text-transform:uppercase;letter-spacing:.07em;margin:0 0 10px;padding:0;border:0;color:var(--muted)}
.pls-article .toc ol{margin:0;padding-left:20px;display:grid;gap:4px}
.pls-article .toc a{color:var(--text);text-decoration:none;font-size:15px}
.pls-article .toc a:hover{color:var(--accent)}
.pls-article h2{font-size:clamp(22px,3vw,29px);line-height:1.25;letter-spacing:-.02em;color:#fff;margin:56px 0 18px;padding-bottom:10px;border-bottom:1px solid var(--line);scroll-margin-top:80px}
.pls-article h3{font-size:20px;line-height:1.35;color:#fff;margin:34px 0 12px}
.pls-article p{margin:0 0 18px}
.pls-article ul,.pls-article ol{padding-left:22px;margin:0 0 20px}
.pls-article li{margin-bottom:6px}
.pls-article strong{color:#fff}
.pls-article code{background:var(--card2);padding:1px 6px;border-radius:5px;font-size:.9em}
.pls-article .stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px;margin:28px 0}
.pls-article .stat-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;text-align:center}
.pls-article .stat-number{display:block;font-size:28px;font-weight:900;color:var(--accent);line-height:1.1}
.pls-article .stat-label{display:block;font-size:13px;color:var(--muted);margin-top:6px;line-height:1.4}
.pls-article .table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:28px 0;border:1px solid var(--line);border-radius:12px}
.pls-article table{width:100%;min-width:520px;border-collapse:collapse;font-size:15px;line-height:1.5}
.pls-article caption{caption-side:top;text-align:left;padding:12px 16px;color:var(--muted);font-size:14px;font-weight:600;background:var(--card)}
.pls-article th{background:var(--card2);color:#fff;font-weight:700;padding:11px 14px;text-align:left;vertical-align:top}
.pls-article tbody th{background:transparent;color:#fff}
.pls-article td{padding:11px 14px;border-top:1px solid var(--line);vertical-align:top;color:var(--text)}
.pls-article tbody th{border-top:1px solid var(--line)}
.pls-article .callout{border-radius:12px;padding:18px 22px;margin:28px 0;font-size:16px;line-height:1.65}
.pls-article .callout strong{display:block;margin-bottom:6px}
.pls-article .callout-tip{background:var(--card);border-left:4px solid var(--muted)}
.pls-article .callout-warn{background:var(--warn-soft);border-left:4px solid var(--warn)}
.pls-article .callout-info{background:var(--accent-soft);border-left:4px solid var(--accent)}
.pls-article .spec-list{display:grid;grid-template-columns:minmax(140px,34%) 1fr;gap:0;margin:24px 0;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.pls-article .spec-list dt,.pls-article .spec-list dd{margin:0;padding:10px 14px;border-top:1px solid var(--line)}
.pls-article .spec-list dt{font-weight:700;color:#fff;background:var(--card)}
.pls-article .spec-list dt:first-of-type,.pls-article .spec-list dt:first-of-type+dd{border-top:0}
.pls-article .step-list{list-style:none;padding:0;margin:22px 0;counter-reset:steps}
.pls-article .step-list li{counter-increment:steps;position:relative;padding:14px 16px 14px 58px;border-bottom:1px solid var(--line);margin:0}
.pls-article .step-list li:last-child{border-bottom:0}
.pls-article .step-list li::before{content:counter(steps);position:absolute;left:12px;top:15px;width:30px;height:30px;border-radius:50%;background:var(--accent);color:var(--accent-ink);font-weight:800;font-size:14px;display:flex;align-items:center;justify-content:center}
.pls-article .expert-quote{margin:36px 0;padding:26px 30px;background:var(--accent-soft);border-left:4px solid var(--accent);border-radius:0 12px 12px 0}
.pls-article .expert-quote blockquote{margin:0 0 12px;font-size:18px;line-height:1.7;font-style:italic;color:#f4f4f5}
.pls-article .expert-quote cite{font-style:normal;font-size:14px;color:var(--muted)}
.pls-article .faq-item{border-bottom:1px solid var(--line);padding:18px 0}
.pls-article .faq-q{font-size:18px;font-weight:700;color:#fff;margin:0 0 8px}
.pls-article .faq-a{margin:0;color:var(--text)}
.pls-article .cta-block{margin:56px 0 0;background:linear-gradient(135deg,#1a2512,#14151b 70%);border:1px solid #2f4520;border-radius:16px;padding:32px 34px;display:flex;align-items:center;gap:28px;flex-wrap:wrap}
.pls-article .cta-text{flex:1;min-width:220px}
.pls-article .cta-title{font-size:22px;font-weight:800;color:#fff;margin:0 0 6px}
.pls-article .cta-body{color:var(--muted);margin:0;font-size:15px}
.pls-article .cta-buttons{display:flex;gap:10px;flex-wrap:wrap}
.pls-article .cta-btn{display:inline-block;border:2px solid var(--accent);color:var(--accent);font-weight:800;font-size:15px;padding:11px 20px;border-radius:10px;text-decoration:none;white-space:nowrap}
.pls-article .cta-btn:first-child{background:var(--accent);color:var(--accent-ink)}
.pls-article .article-footer{margin-top:56px;padding-top:24px;border-top:1px solid var(--line);font-size:14px;color:var(--dim)}
.pls-article .related{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin:18px 0 0;padding:0;list-style:none}
.pls-article .related a{display:block;height:100%;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;text-decoration:none;color:var(--text);font-weight:600;line-height:1.4}
.pls-article .related a:hover{border-color:var(--accent)}
.pls-article .related span{display:block;color:var(--dim);font-weight:400;font-size:14px;margin-top:6px}
.site-header .lang{position:relative;margin-left:auto}
.site-header .row-break{display:none}
.site-header .lang summary{list-style:none;display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 10px;border:1px solid #2a2b33;border-radius:999px;color:#d8d8de;font-size:13px;font-weight:600;cursor:pointer;user-select:none}
.site-header .lang summary::-webkit-details-marker{display:none}
.site-header .lang[open] summary,.site-header .lang summary:hover{border-color:var(--accent);color:#fff}
.site-header .lang svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.site-header .lang ul{position:absolute;top:calc(100% + 8px);right:0;z-index:20;min-width:210px;max-height:70vh;overflow-y:auto;margin:0;padding:6px;list-style:none;background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:0 16px 40px rgba(0,0,0,.45)}
.site-header .lang ul a{display:flex;justify-content:space-between;gap:16px;padding:8px 10px;border-radius:8px;color:var(--text);text-decoration:none;font-size:14px;line-height:1.4}
.site-header .lang ul a:hover{background:var(--card2);color:#fff}
.site-header .lang ul a[aria-current]{color:var(--accent);font-weight:600}
.site-header .lang ul span{color:var(--dim);font-size:12px}
.site-footer{border-top:1px solid var(--line);color:var(--dim);font-size:14px;text-align:center;padding:28px 20px 48px}
.site-footer a{color:var(--muted)}
@media (max-width:600px){body{font-size:16px}.pls-article .container{padding:32px 16px 60px}.pls-article .lead{font-size:17px;padding:16px 18px}.pls-article .trust-badge{flex-direction:column;align-items:flex-start;gap:8px}.pls-article .cta-block{padding:22px}.pls-article .cta-btn{width:100%;text-align:center}.pls-article .spec-list{grid-template-columns:1fr}.pls-article .spec-list dd{border-top:0}.site-header .inner{gap:8px 12px;padding:10px 14px}.site-header .brand{flex:1;min-width:0;font-size:15px;line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.site-header .get{display:none}.site-header .row-break{display:block;order:3;flex-basis:100%;height:0}.site-header nav{order:4;flex:1;min-width:0;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;white-space:nowrap}.site-header .lang{order:2}}
"""

def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s)).strip()


def squash(s):
    return re.sub(r"\s+", " ", strip_tags(s)).strip()


def words(s, lang=EN):
    if lang["code"] == "en":
        return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.%-]*", strip_tags(s)))
    return len(re.findall(r"\w[\w'’.%-]*", strip_tags(s)))


def reading_minutes(body, lang):
    if lang["code"] in CJK:
        return max(1, math.ceil(len(re.sub(r"\s+", "", strip_tags(body))) / 500))
    return max(1, math.ceil(words(body, lang) / 230))


def localize_path(path, lang):
    """`/scan` in the given language: `/de/scan`, or `/scan` for English (same rule as the app)."""
    if not lang["path"]:
        return path
    return f"/{lang['path']}/" if path == "/" else f"/{lang['path']}{path}"


def localize_links(body, lang, slugs):
    """Points English internal links at the language's pages; untranslated articles keep the English link."""
    if not lang["path"]:
        return body

    def repl(m):
        path, anchor = m.group(1), m.group(2) or ""
        article = re.fullmatch(r"/blog/([^/]+)/", path)
        if article:
            slug = slugs.get(article.group(1))
            return f'href="/{lang["path"]}/blog/{slug}/{anchor}"' if slug else m.group(0)
        return f'href="{localize_path(path, lang)}{anchor}"'

    return re.sub(r'href="(/[^"#]*)(#[^"]*)?"', repl, body)


def fmt_date(iso, chrome, day=False):
    y, m, d = (int(x) for x in iso.split("-"))
    return chrome["date_day" if day else "date_month"].format(year=y, month=chrome["months"][m - 1], day=d)


def load_chrome(lang):
    en = json.loads((TRANSLATIONS / "en.chrome.json").read_text())
    if lang is EN:
        return en
    f = TRANSLATIONS / lang["code"] / "chrome.json"
    return {**en, **json.loads(f.read_text())} if f.exists() else None


def home_languages():
    """Languages whose home page the app build writes (same rule as vite.config.ts)."""
    return [l for l in LANGUAGES if (APP / "src" / "locale" / "messages" / f"{l['code']}.json").exists()
            and (APP / "src" / "content" / "home-guide" / f"{l['code']}.html").exists()]


def lang_label(lang):
    return (lang["path"] or lang["code"]).upper()


def switcher_html(lang, chrome, alternates):
    items = "".join(
        f'<li><a href="{path}" hreflang="{l["code"]}" lang="{l["code"]}"'
        f'{" aria-current=\"true\"" if l is lang else ""}>{esc(l["name"])}<span>{lang_label(l)}</span></a></li>'
        for l, path in alternates)
    return (f'<details class="lang"><summary aria-label="{esc(chrome["language"])}: {esc(lang["name"])}">'
            f'{GLOBE}<span>{lang_label(lang)}</span></summary><ul>{items}</ul></details>')


def header_html(lang, chrome, alternates, active):
    nav = chrome["nav"]
    items = [(localize_path("/", lang), nav["home"]), (localize_path("/scan", lang), nav["scan"]),
             (localize_path("/scan/bulk", lang), nav["bulk"]), (localize_path("/blog/", lang), nav["guides"])]
    links = "".join(
        f'<a href="{u}"{" aria-current=\"page\"" if u == active else ""}>{esc(t)}</a>' for u, t in items)
    return (f'<header class="site-header"><div class="inner"><a class="brand" href="{localize_path("/", lang)}">{BRAND}</a>'
            f'<nav aria-label="Primary">{links}</nav>{switcher_html(lang, chrome, alternates)}'
            f'<a class="get" href="{STORE_URL}" target="_blank" rel="noopener">{esc(chrome["get_extension"])}</a>'
            f'<span class="row-break" aria-hidden="true"></span></div></header>')


def footer_html(lang, chrome):
    return (f'<footer class="site-footer">© {date.today().year} {BRAND} · '
            f'<a href="{localize_path("/", lang)}">{esc(chrome["footer_tool"])}</a> · '
            f'<a href="{localize_path("/blog/", lang)}">{esc(chrome["footer_guides"])}</a> · '
            f'<a href="{STORE_URL}" target="_blank" rel="noopener">{esc(chrome["footer_extension"])}</a></footer>')


def page(lang, chrome, title, description, path, body, jsonld, alternates, og_type="article"):
    """alternates: [(language, path)] of every language version of this page, including this one."""
    canonical = SITE + path
    links = [f'<link rel="alternate" hreflang="{l["code"]}" href="{SITE}{p}">' for l, p in alternates]
    links += [f'<link rel="alternate" hreflang="x-default" href="{SITE}{p}">' for l, p in alternates if l is EN]
    hreflang = "\n".join(links)
    return f"""<!DOCTYPE html>
<html lang="{lang["code"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
{hreflang}
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{lang["ogLocale"]}">
<meta property="og:image" content="{SITE}/pwa-512x512.png">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0b0b0f">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" sizes="any" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
{header_html(lang, chrome, alternates, localize_path("/blog/", lang))}
{body}
{footer_html(lang, chrome)}
{SWITCHER_JS}
</body>
</html>
"""


def extract_faq(body):
    out = []
    for q, a in re.findall(r'<p class="faq-q">(.*?)</p>\s*<p class="faq-a">(.*?)</p>', body, re.S):
        out.append({"@type": "Question", "name": squash(q),
                    "acceptedAnswer": {"@type": "Answer", "text": squash(a)}})
    return out


def extract_steps(body):
    m = re.search(r'<ol class="step-list">(.*?)</ol>', body, re.S)
    if not m:
        return []
    return [squash(li) for li in re.findall(r"<li>(.*?)</li>", m.group(1), re.S)]


def load_articles():
    """{english slug: {language code: article}} for every published article and its translations."""
    groups = {}
    for d in sorted(ARTICLES.iterdir()):
        mf, bf = d / "meta.json", d / "body.html"
        if not (mf.exists() and bf.exists()):
            continue
        meta = json.loads(mf.read_text())
        if meta.get("draft"):
            continue
        group = {"en": dict(meta, key=d.name, slug=d.name, lang=EN, body=bf.read_text())}
        for lang in LANGUAGES[1:]:
            td = TRANSLATIONS / lang["code"] / d.name
            if not ((td / "meta.json").exists() and (td / "body.html").exists()):
                continue
            tbody = (td / "body.html").read_text()
            # A draft cut off mid-way has fewer sections than the original: keep it off the site
            if re.findall(r'<h2 id="([^"]+)"', tbody) != re.findall(r'<h2 id="([^"]+)"', group["en"]["body"]):
                print(f"skipped {lang['code']}/{d.name}: headings differ from the English original (unfinished?)")
                continue
            tmeta = json.loads((td / "meta.json").read_text())
            source = meta.get("date_modified") or meta["date_published"]
            if tmeta.get("source_modified") != source:
                print(f"warning: {lang['code']}/{d.name} was translated from {tmeta.get('source_modified')}, "
                      f"the English article changed on {source}")
            group[lang["code"]] = dict(meta, **tmeta, key=d.name, lang=lang, body=tbody)
        for a in group.values():
            a["path"] = localize_path(f"/blog/{a['slug']}/", a["lang"])
            a["url"] = SITE + a["path"]
            a["words"] = words(a["body"], a["lang"])
        groups[d.name] = group
    return dict(sorted(groups.items(), key=lambda kv: kv[1]["en"].get("order", 99)))


def render_article(a, chrome, lang_articles, slugs, alternates):
    lang, url, path, year = a["lang"], a["url"], a["path"], a["date_published"][:4]
    body = localize_links(a["body"], lang, slugs)
    updated = ""
    if a.get("date_modified") and a["date_modified"] != a["date_published"]:
        updated = (f'<span>🔄 {esc(chrome["updated"])} <time datetime="{a["date_modified"]}">'
                   f'{fmt_date(a["date_modified"], chrome, day=True)}</time></span>')
    header = f"""<header class="article-header">
  <span class="article-tag">{esc(a["tag"])}</span>
  <h1>{esc(a["h1"])}</h1>
  <div class="article-meta">
    <span>📅 <time datetime="{a["date_published"][:7]}">{fmt_date(a["date_published"], chrome)}</time></span>
    {updated}
    <span>⏱ {esc(chrome["min_read"].format(n=reading_minutes(a["body"], lang)))}</span>
    <span>✍ <a href="{localize_path("/", lang)}">{esc(chrome["author"].format(brand=BRAND))}</a></span>
  </div>
</header>"""
    badge = f"""<div class="trust-badge">
  <span class="trust-badge-icon" aria-hidden="true">🏆</span>
  <div class="trust-badge-text">
    <div class="trust-badge-title">{BRAND} — <span>{esc(chrome["badge_title"])}</span></div>
    <div class="trust-badge-sub">{esc(chrome["badge_sub"].format(year=year))}</div>
  </div>
</div>"""
    body = re.sub(r'(<p class="lead">.*?</p>)', lambda m: m.group(1) + "\n" + badge, body, count=1, flags=re.S)
    cta = f"""<div class="cta-block">
  <div class="cta-text">
    <p class="cta-title">{esc(a.get("cta_title") or chrome["cta_title"])}</p>
    <p class="cta-body">{esc(a.get("cta_body") or chrome["cta_body"])}</p>
  </div>
  <div class="cta-buttons">
    <a href="{localize_path("/scan", lang)}" class="cta-btn">{esc(chrome["cta_tool"])}</a>
    <a href="{STORE_URL}" target="_blank" rel="noopener" class="cta-btn">{esc(chrome["cta_chrome"])}</a>
    <a href="{localize_path("/blog/", lang)}" class="cta-btn">{esc(chrome["cta_more"])}</a>
  </div>
</div>"""
    related = [r for r in lang_articles if r["key"] in a.get("related", [])] or \
              [r for r in lang_articles if r["key"] != a["key"]][:3]
    rel_html = ""
    if related:
        rel_html = f'<p><strong>{esc(chrome["related"])}</strong></p><ul class="related">' + "".join(
            f'<li><a href="{r["path"]}">{esc(r["h1"])}<span>{esc(r["description"][:110])}…</span></a></li>'
            for r in related) + "</ul>"
    footer = (f'<footer class="article-footer"><p>{esc(chrome["article_footer"].format(brand=BRAND))}</p>'
              f'{rel_html}</footer>')
    crumbs = (f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{localize_path("/", lang)}">'
              f'{esc(chrome["breadcrumb_home"])}</a> › <a href="{localize_path("/blog/", lang)}">'
              f'{esc(chrome["breadcrumb_guides"])}</a> › {esc(a["tag"])}</nav>')
    html_body = (f'<div class="pls-article"><article class="container">{crumbs}{header}\n{body}\n'
                 f'{cta}\n{footer}</article></div>')

    org = {"@type": "Organization", "@id": f"{SITE}/#org", "name": BRAND, "url": SITE + "/",
           "logo": f"{SITE}/pwa-512x512.png", "sameAs": [STORE_URL]}
    article = {
        "@type": "Article", "@id": url + "#article", "headline": a["title"], "description": a["description"],
        "url": url, "mainEntityOfPage": url, "inLanguage": lang["code"], "image": f"{SITE}/pwa-512x512.png",
        "author": {"@id": f"{SITE}/#org"}, "publisher": {"@id": f"{SITE}/#org"},
        "datePublished": a["date_published"], "dateModified": a.get("date_modified") or a["date_published"],
        "wordCount": a["words"], "keywords": ", ".join(a.get("keywords", [])),
        "about": [{"@type": "Thing", "name": x} for x in a.get("about", [])],
        "mentions": [{"@type": "Thing", "name": x} for x in a.get("mentions", [])],
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".lead", ".faq-a"]}}
    if lang["code"] == "ja":
        del article["wordCount"]  # Japanese has no word boundaries to count
    if lang is not EN:
        article["translationOfWork"] = {"@id": f"{SITE}/blog/{a['key']}/#article"}
    graph = [org, article]
    faq = extract_faq(body)
    if faq:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "inLanguage": lang["code"], "mainEntity": faq})
    steps = extract_steps(body)
    if steps and a.get("howto_name"):
        graph.append({"@type": "HowTo", "name": a["howto_name"], "inLanguage": lang["code"],
                      "step": [{"@type": "HowToStep", "position": i + 1, "text": s} for i, s in enumerate(steps)]})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": chrome["breadcrumb_home"], "item": SITE + localize_path("/", lang)},
        {"@type": "ListItem", "position": 2, "name": chrome["breadcrumb_guides"],
         "item": SITE + localize_path("/blog/", lang)},
        {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]})
    out = PUBLIC / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(lang, chrome, a["title"], a["description"], path, html_body,
                        {"@context": "https://schema.org", "@graph": graph}, alternates))
    return out


def render_index(lang, chrome, arts, alternates):
    path = localize_path("/blog/", lang)
    url = SITE + path
    title, desc = chrome["index_title"], chrome["index_description"]
    cards = "".join(
        f'<li><a href="{a["path"]}">{esc(a["h1"])}<span>{esc(a["description"])}</span></a></li>' for a in arts)
    body = f"""<div class="pls-article"><main class="container">
<header class="article-header"><span class="article-tag">{esc(chrome["index_tag"])}</span>
<h1>{esc(chrome["index_h1"])}</h1></header>
<p class="lead">{esc(chrome["index_lead"].format(brand=BRAND))}</p>
<ul class="related">{cards}</ul>
</main></div>"""
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": title, "url": url, "description": desc, "inLanguage": lang["code"],
         "hasPart": [{"@type": "Article", "headline": a["title"], "url": a["url"]} for a in arts]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": chrome["breadcrumb_home"],
             "item": SITE + localize_path("/", lang)},
            {"@type": "ListItem", "position": 2, "name": chrome["breadcrumb_guides"], "item": url}]}]}
    out = PUBLIC / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(lang, chrome, title, desc, path, body, ld, alternates, og_type="website"))


def render_sitemap(entries):
    """entries: [(path, lastmod, priority, alternates)] — alternates as in page()."""
    def alt_links(alternates):
        if len(alternates) < 2:
            return ""
        links = [f'<xhtml:link rel="alternate" hreflang="{l["code"]}" href="{SITE}{p}"/>' for l, p in alternates]
        links += [f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{p}"/>' for l, p in alternates if l is EN]
        return "".join(links)

    body = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{d}</lastmod><priority>{pr}</priority>{alt_links(alt)}</url>\n"
                   for p, d, pr, alt in entries)
    (PUBLIC / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "</urlset>\n")


def render_llms(arts, blog_langs, homes):
    lines = [f"# {BRAND}", "",
             "> Free browser tool and Chrome extension that makes a PDF, image, Word or Excel file look like a "
             "real scan (noise, blur, tilt, paper tone, grayscale, border). Files are processed locally in the "
             "browser; nothing is uploaded for processing. Rated 5 stars in the Chrome Web Store.", "",
             "## Tool", "",
             f"- [Make PDF look scanned — online tool]({SITE}/): upload a file, adjust the scan effect with a live preview, download a scanned-looking PDF",
             f"- [Chrome extension]({STORE_URL}): the same scan engine in the Chrome side panel", "",
             "## Guides", ""]
    lines += [f"- [{a['h1']}]({a['url']}): {a['description']}" for a in arts]
    others = [l for l in LANGUAGES[1:] if l in homes or l in blog_langs]
    if others:
        lines += ["", "## Other languages", "",
                  "The tool and the guides are also available in these languages:", ""]
        for l in others:
            parts = []
            if l in homes:
                parts.append(f"[tool]({SITE}{localize_path('/', l)})")
            if l in blog_langs:
                parts.append(f"[guides]({SITE}{localize_path('/blog/', l)})")
            lines.append(f"- {l['name']} ({l['code']}): " + " · ".join(parts))
    (PUBLIC / "llms.txt").write_text("\n".join(lines) + "\n")


def render_robots():
    (PUBLIC / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        "# AI search and answer engines are welcome\n"
        "User-agent: GPTBot\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: ChatGPT-User\nAllow: /\n\n"
        "User-agent: ClaudeBot\nAllow: /\n\nUser-agent: Claude-SearchBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\n"
        "User-agent: Google-Extended\nAllow: /\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n")


def main():
    groups = load_articles()
    chromes = {l["code"]: load_chrome(l) for l in LANGUAGES}
    blog_langs = [l for l in LANGUAGES if chromes[l["code"]]]
    homes = home_languages()
    # Language folders are fully generated: drop them so renamed slugs leave no stale pages behind
    for l in LANGUAGES[1:]:
        shutil.rmtree(PUBLIC / l["path"] / "blog", ignore_errors=True)

    slugs = {l["code"]: {k: g[l["code"]]["slug"] for k, g in groups.items() if l["code"] in g} for l in blog_langs}
    today = date.today().isoformat()
    index_alts = [(l, localize_path("/blog/", l)) for l in blog_langs]
    home_alts = [(l, localize_path("/", l)) for l in homes]
    sitemap = [(p, today, "1.0", home_alts) for _, p in home_alts]
    sitemap += [(p, today, "0.8", index_alts) for _, p in index_alts]
    for lang in blog_langs:
        code, chrome = lang["code"], chromes[lang["code"]]
        lang_articles = [g[code] for g in groups.values() if code in g]
        for a in lang_articles:
            alts = [(l, groups[a["key"]][l["code"]]["path"]) for l in blog_langs if l["code"] in groups[a["key"]]]
            out = render_article(a, chrome, lang_articles, slugs[code], alts)
            sitemap.append((a["path"], a.get("date_modified") or a["date_published"], "0.8", alts))
            print(f"built {out.relative_to(ROOT.parent)}  ({a['words']} words)")
        render_index(lang, chrome, lang_articles, index_alts)
    en_articles = [g["en"] for g in groups.values()]
    render_sitemap(sitemap)
    render_llms(en_articles, blog_langs, homes)
    render_robots()
    (APP / "src" / "locale" / "blog-slugs.json").write_text(
        json.dumps({k: v for k, v in slugs.items() if k != "en"}, indent=2, ensure_ascii=False) + "\n")
    (ROOT / "article-index.json").write_text(json.dumps(
        [{"url": f"/blog/{a['slug']}/", "title": a["h1"], "description": a["description"],
          "keywords": a.get("keywords", [])} for a in en_articles], indent=2, ensure_ascii=False))
    total = sum(len(g) for g in groups.values())
    print(f"{total} article pages in {len(blog_langs)} languages, {len(homes)} home pages; "
          f"indexes, sitemap.xml, llms.txt, robots.txt, blog-slugs.json written")


if __name__ == "__main__":
    sys.exit(main())
