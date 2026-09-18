#!/usr/bin/env python3
"""Build the static blog for pdflookscanned.com (Stage 10 + 12 of the article pipeline).

Sources:  seo-workspace/articles/<slug>/meta.json + body.html
Output:   lookscanned.io-main/public/blog/<slug>/index.html, public/blog/index.html,
          public/sitemap.xml, public/llms.txt, public/robots.txt,
          seo-workspace/article-index.json (internal-link library for Stage 7)

body.html holds the article content from `<p class="lead">` down to the FAQ.
The header, trust badge, CTA, JSON-LD and page chrome are added here so every
article gets identical, validated brand elements.
"""
import html
import json
import math
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTICLES = ROOT / "articles"
PUBLIC = ROOT.parent / "lookscanned.io-main" / "public"

SITE = "https://pdflookscanned.com"
BRAND = "Make PDF look scanned"
STORE_URL = "https://chromewebstore.google.com/detail/make-pdf-look-scanned/ijhpnlcipgiokgignkbbbgkobdmdoila"
BADGE_TITLE = "rated 5 stars in the Chrome Web Store"
BADGE_SUB = "{year} — free scan-effect tool that runs locally in your browser, no signup"
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

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
.site-header .get{margin-left:auto;background:var(--accent);color:var(--accent-ink);font-weight:700;text-decoration:none;padding:8px 16px;border-radius:999px;font-size:14px}
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
.site-footer{border-top:1px solid var(--line);color:var(--dim);font-size:14px;text-align:center;padding:28px 20px 48px}
.site-footer a{color:var(--muted)}
@media (max-width:600px){body{font-size:16px}.pls-article .container{padding:32px 16px 60px}.pls-article .lead{font-size:17px;padding:16px 18px}.pls-article .trust-badge{flex-direction:column;align-items:flex-start;gap:8px}.pls-article .cta-block{padding:22px}.pls-article .cta-btn{width:100%;text-align:center}.pls-article .spec-list{grid-template-columns:1fr}.pls-article .spec-list dd{border-top:0}.site-header .get{margin-left:0}}
"""


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s)).strip()


def squash(s):
    return re.sub(r"\s+", " ", strip_tags(s)).strip()


def words(s):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.%-]*", strip_tags(s)))


def human_date(iso, day=False):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{MONTHS[m - 1]} {d}, {y}" if day else f"{MONTHS[m - 1]} {y}"


def header_html(active):
    items = [("/", "Home"), ("/scan", "Scan a PDF"), ("/scan/bulk", "Bulk scan"), ("/blog/", "Guides")]
    links = "".join(
        f'<a href="{u}"{" aria-current=\"page\"" if u == active else ""}>{t}</a>' for u, t in items)
    return (f'<header class="site-header"><div class="inner"><a class="brand" href="/">{BRAND}</a>'
            f'<nav aria-label="Primary">{links}</nav>'
            f'<a class="get" href="{STORE_URL}" target="_blank" rel="noopener">Add to Chrome — free</a></div></header>')


FOOTER = (f'<footer class="site-footer">© {date.today().year} {BRAND} · <a href="/">Scan-effect tool</a> · '
          f'<a href="/blog/">Guides</a> · <a href="{STORE_URL}" target="_blank" rel="noopener">Chrome extension</a></footer>')


def page(title, description, canonical, body, jsonld, og_type="article", active="/blog/"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
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
{header_html(active)}
{body}
{FOOTER}
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
    arts = []
    for d in sorted(ARTICLES.iterdir()):
        mf, bf = d / "meta.json", d / "body.html"
        if not (mf.exists() and bf.exists()):
            continue
        meta = json.loads(mf.read_text())
        if meta.get("draft"):
            continue
        meta["body"] = bf.read_text()
        meta["slug"] = d.name
        meta["url"] = f"{SITE}/blog/{d.name}/"
        meta["words"] = words(meta["body"])
        arts.append(meta)
    arts.sort(key=lambda a: a.get("order", 99))
    return arts


def render_article(a, all_articles):
    url, year = a["url"], a["date_published"][:4]
    body = a["body"]
    minutes = max(1, math.ceil(a["words"] / 230))
    updated = ""
    if a.get("date_modified") and a["date_modified"] != a["date_published"]:
        updated = (f'<span>🔄 Updated: <time datetime="{a["date_modified"]}">'
                   f'{human_date(a["date_modified"], day=True)}</time></span>')
    header = f"""<header class="article-header">
  <span class="article-tag">{esc(a["tag"])}</span>
  <h1>{esc(a["h1"])}</h1>
  <div class="article-meta">
    <span>📅 <time datetime="{a["date_published"][:7]}">{human_date(a["date_published"])}</time></span>
    {updated}
    <span>⏱ {minutes} min read</span>
    <span>✍ <a href="/">{BRAND} team</a></span>
  </div>
</header>"""
    badge = f"""<div class="trust-badge">
  <span class="trust-badge-icon" aria-hidden="true">🏆</span>
  <div class="trust-badge-text">
    <div class="trust-badge-title">{BRAND} — <span>{BADGE_TITLE}</span></div>
    <div class="trust-badge-sub">{BADGE_SUB.format(year=year)}</div>
  </div>
</div>"""
    body = re.sub(r'(<p class="lead">.*?</p>)', lambda m: m.group(1) + "\n" + badge, body, count=1, flags=re.S)
    cta = f"""<div class="cta-block">
  <div class="cta-text">
    <p class="cta-title">{esc(a.get("cta_title", "Make your PDF look scanned in under a minute"))}</p>
    <p class="cta-body">{esc(a.get("cta_body", "Noise, blur, tilt, paper tone and grayscale with a live preview. Free, no signup, and your file is processed on your own device."))}</p>
  </div>
  <div class="cta-buttons">
    <a href="/scan" class="cta-btn">Open the free tool →</a>
    <a href="{STORE_URL}" target="_blank" rel="noopener" class="cta-btn">Add to Chrome — free →</a>
    <a href="/blog/" class="cta-btn">More guides →</a>
  </div>
</div>"""
    related = [r for r in all_articles if r["slug"] in a.get("related", [])] or \
              [r for r in all_articles if r["slug"] != a["slug"]][:3]
    rel_html = ""
    if related:
        rel_html = '<p><strong>Related guides</strong></p><ul class="related">' + "".join(
            f'<li><a href="/blog/{r["slug"]}/">{esc(r["h1"])}<span>{esc(r["description"][:110])}…</span></a></li>'
            for r in related) + "</ul>"
    footer = (f'<footer class="article-footer"><p>Published by the {BRAND} team. '
              f'Settings and defaults described here match the current version of the web tool and the '
              f'Chrome extension.</p>{rel_html}</footer>')
    crumbs = (f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> › '
              f'<a href="/blog/">Guides</a> › {esc(a["tag"])}</nav>')
    html_body = (f'<div class="pls-article"><article class="container">{crumbs}{header}\n{body}\n'
                 f'{cta}\n{footer}</article></div>')

    org = {"@type": "Organization", "@id": f"{SITE}/#org", "name": BRAND, "url": SITE + "/",
           "logo": f"{SITE}/pwa-512x512.png", "sameAs": [STORE_URL]}
    graph = [org, {
        "@type": "Article", "@id": url + "#article", "headline": a["title"], "description": a["description"],
        "url": url, "mainEntityOfPage": url, "inLanguage": "en", "image": f"{SITE}/pwa-512x512.png",
        "author": {"@id": f"{SITE}/#org"}, "publisher": {"@id": f"{SITE}/#org"},
        "datePublished": a["date_published"], "dateModified": a.get("date_modified") or a["date_published"],
        "wordCount": a["words"], "keywords": ", ".join(a.get("keywords", [])),
        "about": [{"@type": "Thing", "name": x} for x in a.get("about", [])],
        "mentions": [{"@type": "Thing", "name": x} for x in a.get("mentions", [])],
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".lead", ".faq-a"]}}]
    faq = extract_faq(a["body"])
    if faq:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": faq})
    steps = extract_steps(a["body"])
    if steps and a.get("howto_name"):
        graph.append({"@type": "HowTo", "name": a["howto_name"],
                      "step": [{"@type": "HowToStep", "position": i + 1, "text": s} for i, s in enumerate(steps)]})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]})
    out = PUBLIC / "blog" / a["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(a["title"], a["description"], url, html_body, {"@context": "https://schema.org", "@graph": graph}))
    return out


def render_index(arts):
    url = f"{SITE}/blog/"
    title = "Make PDF Look Scanned: Guides, Settings & How-Tos"
    desc = ("Step-by-step guides to make a PDF look scanned: settings for a realistic scan effect, "
            "PDF to scanned PDF, image to scanned PDF, black and white PDFs.")
    cards = "".join(
        f'<li><a href="/blog/{a["slug"]}/">{esc(a["h1"])}<span>{esc(a["description"])}</span></a></li>' for a in arts)
    body = f"""<div class="pls-article"><main class="container">
<header class="article-header"><span class="article-tag">Guides</span>
<h1>Make PDF Look Scanned — Guides and Settings</h1></header>
<p class="lead">Practical guides to making a PDF look scanned: which scan-effect settings look real, how to turn a PDF or an image into a scanned PDF, and how to convert color pages to black and white. Every guide uses the free {BRAND} tool, which processes files locally in your browser.</p>
<ul class="related">{cards}</ul>
</main></div>"""
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": title, "url": url, "description": desc,
         "hasPart": [{"@type": "Article", "headline": a["title"], "url": a["url"]} for a in arts]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": url}]}]}
    (PUBLIC / "blog").mkdir(parents=True, exist_ok=True)
    (PUBLIC / "blog" / "index.html").write_text(page(title, desc, url, body, ld, og_type="website"))


def render_sitemap(arts):
    today = date.today().isoformat()
    urls = [(SITE + "/", today, "1.0"), (SITE + "/blog/", today, "0.8")]
    urls += [(a["url"], a.get("date_modified") or a["date_published"], "0.8") for a in arts]
    body = "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod><priority>{p}</priority></url>\n" for u, d, p in urls)
    (PUBLIC / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + body + "</urlset>\n")


def render_llms(arts):
    lines = [f"# {BRAND}", "",
             "> Free browser tool and Chrome extension that makes a PDF, image, Word or Excel file look like a "
             "real scan (noise, blur, tilt, paper tone, grayscale, border). Files are processed locally in the "
             "browser; nothing is uploaded for processing. Rated 5 stars in the Chrome Web Store.", "",
             "## Tool", "",
             f"- [Make PDF look scanned — online tool]({SITE}/): upload a file, adjust the scan effect with a live preview, download a scanned-looking PDF",
             f"- [Chrome extension]({STORE_URL}): the same scan engine in the Chrome side panel", "",
             "## Guides", ""]
    lines += [f"- [{a['h1']}]({a['url']}): {a['description']}" for a in arts]
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
    arts = load_articles()
    for a in arts:
        out = render_article(a, arts)
        print(f"built {out.relative_to(ROOT.parent)}  ({a['words']} words)")
    render_index(arts)
    render_sitemap(arts)
    render_llms(arts)
    render_robots()
    (ROOT / "article-index.json").write_text(json.dumps(
        [{"url": f"/blog/{a['slug']}/", "title": a["h1"], "description": a["description"],
          "keywords": a.get("keywords", [])} for a in arts], indent=2, ensure_ascii=False))
    print(f"{len(arts)} articles, index, sitemap.xml, llms.txt, robots.txt written")


if __name__ == "__main__":
    sys.exit(main())
