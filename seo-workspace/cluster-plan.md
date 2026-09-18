# Make PDF look scanned — план пула страниц (кластер-план)

Сайт: `https://pdflookscanned.com/` · Расширение: `https://chromewebstore.google.com/detail/make-pdf-look-scanned/ijhpnlcipgiokgignkbbbgkobdmdoila`
Источник ключей: `Captain Bootcamp - Make PDF look scanned.docx` (объёмы и KD берутся оттуда, новые не придумываем).
Методика: `geo-seo-article-pipeline-template — копия.md` (стадии 0–12).
Дата анализа выдачи: 18.09.2026, выдача US/EN.

---

## 1. Анализ конкурентов (замер текста без меню/футера)

| Кластер | Кто в топе | Макс. объём у конкурента | Типичный объём | Сниппет-паттерн топа |
|---|---|---|---|---|
| make pdf look scanned | lookscanned.io, supertool, scannedmaker, lightpdf, toscanned, 10015.io, Wondershare | 2 598 слов / 16,5 тыс. знаков (Wondershare) | 600–1 900 слов | «Make PDF Look Scanned — Free, Online, Private» |
| how to make a pdf look like it was scanned | 10015.io, Wondershare, sliksafe, toscanned, pypi | 2 598 слов | 700–900 слов | «How to…: A Step-by-Step Guide» |
| make a document look scanned / make it look scanned | Adobe Make-it, pdfgear, 10015.io, doc2scan | 856 слов (pdfgear) | 200–900 слов | «How to Make Document Look Scanned [3 Ways]» |
| pdf to scanned pdf / pdf to scanned | Adobe helpx, pdfFiller, imagestool, safepdfkit | 2 583 слов (pdfFiller) | 1 500–1 800 слов | «Convert PDF to Scanned PDF Online» |
| scanned pdf / scanned copy | PDF Association, Adobe Scan, echovera, Indeed, Quora | ~1 500 (оценка, pdfa.org отдаёт 403) | 400–1 400 слов | «What Is a Scanned PDF…» |
| image to scanned pdf | 10015.io, 11zon, pdf-lab, onlinescanner | 934 слова | 400–900 слов | «Scan Image to PDF Online Free» |
| convert color pdf to black and white | pdfgear, Smallpdf, Zamzar, Wondershare, Adobe | 1 829 слов (Wondershare) | 400–1 800 слов | «How to… (3/4 ways)» |
| scan effect / look scanned | konfuzio, Envato, Medialoot, научные PDF | 164 слова (konfuzio) | — | выдача смешанная, слабая |

**Выводы:**
- Топ состоит из **страниц-инструментов** с коротким текстом (600–1 900 слов) и 2–3 гайдов по 2 500+ слов. Никто не даёт одновременно рабочий инструмент + исчерпывающий гайд + точные настройки.
- Почти ни у кого нет FAQPage/HowTo-разметки на гайдах, конкретных значений параметров (угол, DPI, шум), таблиц сравнения методов и честного блока «когда так делать нельзя».
- Наша главная страница — SPA с **нулём текста** в HTML (в `index.html` только `<div id="app">`). По ключу `make pdf look scanned` (320) это главный разрыв с топом.
- `scan effect` — выдача смешанная (наука, видео-шаблоны) → слабая конкуренция, но и интент размыт: страницу делаем как справочник «эффект скана для документов».

## 2. Правило длины

Цель пользователя — превзойти конкурентов по объёму знаков и качеству. Формула: **max(макс. конкурент × 1,4; топ-10 средн. × 1,15)**, но не меньше 2 500 слов.
Решение владельца (18.09.2026): пол 10 000 слов из шаблона НЕ применяется; цель = max-конкурент ×1,4.

## 3. Пул страниц: распределение ключей без каннибализации

Правило шаблона: длинные хвосты одного интента — на одну страницу. 18 вариантов «make pdf look scanned» — это один интент, их нельзя разносить по разным статьям.

| # | URL | Тип | Главный ключ (vol/KD) | Кластер ключей | Цель, слов (≈ знаков) | Конкурент-максимум |
|---|---|---|---|---|---|---|
| 0 | `/` (главная, инструмент) | лендинг + SEO-текст под инструментом | make pdf look scanned (320/31) | make a pdf look scanned (210/37), make pdf looks scanned (210/32), make pdf look scanned online (20), make pdf looks like scanned (20), make pdf look like scanned (20), make pdf file look scanned (20), lookscanned (110/58)* | 2 000–2 500 (≈14–16 тыс.) | 1 869 (supertool) |
| 1 | `/blog/how-to-make-a-pdf-look-scanned/` | SEO-гайд, pillar | how to make a pdf look scanned (20/25) | how to make a pdf look like it was scanned / like a scanned document / like scanned / document look scanned / how to make my pdf look like scanned document, make pdf look like a scan, make a pdf look like a scan, make pdf look like it was scanned | 4 000 (≈25 тыс.) | 2 598 |
| 2 | `/blog/make-a-document-look-scanned/` | SEO-гайд | make it look scanned (320/38–41) | make a document look scanned (70/71–78), make document look scanned (90/29), make it look like scanned (90/45) — Word, Google Docs, фото документа, подписанные формы | 3 000 (≈19 тыс.) | 856 (+ Adobe) |
| 3 | `/blog/pdf-to-scanned-pdf/` | SEO-гайд | pdf to scanned pdf (390/28) | pdf to scanned (260/30) — растеризация, flatten, DPI, grayscale, размер файла, проверка результата | 3 600 (≈23 тыс.) | 2 583 |
| 4 | `/blog/what-is-a-scanned-pdf/` | информационная / GEO-справка | scanned pdf (720/36) | scanned copy (140/21) — определение, scanned vs digital PDF, как отличить, OCR, когда требуют скан-копию | 3 000 (≈19 тыс.) | ~1 500 |
| 5 | `/blog/image-to-scanned-pdf/` | SEO-гайд | image to scanned pdf (390/92) | JPG/PNG/фото с телефона → скан, несколько страниц в один PDF | 2 800 (≈18 тыс.) | 934 |
| 6 | `/blog/convert-color-pdf-to-black-and-white/` | SEO-гайд | how to convert a color pdf to black and white (140/60) | grayscale vs чистый ч/б, Windows print-to-PDF, Mac Preview Quartz filter, браузер, эффект копира | 3 000 (≈19 тыс.) | 1 829 |
| 7 | `/blog/scan-effect/` | GEO-справочник | look scanned (390/32) | scan effect (110/29), look scan (170/53) — каждый артефакт (шум, наклон, blur, тон бумаги, тени, сгибы) + готовые пресеты «офисный скан / факс / ксерокс / старый документ / телефон» | 3 000 (≈19 тыс.) | 164 |
| 8* | `/blog/best-ways-to-make-a-pdf-look-scanned/` | GEO-сравнение подходов | (fan-out к #1) | сравнение методов: браузер / расширение / графредактор / печать+скан / скрипт — без названий конкурентов | 3 500 | — |

\* `lookscanned` и #8 — см. вопросы.

**Перелинковка (hub-and-spoke):** хаб = главная `/` + гайд #1. Каждая статья → главная (CTA «Open the tool») + расширение + #1. Связки: #3↔#4 (scanned pdf), #5↔#2 (фото/документы), #6↔#7 (ч/б как часть эффекта скана), #7↔#1 (настройки).

## 4. Сниппеты для выдачи (Title ≤ 60 · Description 148–158 знаков)

| # | `<title>` | `meta description` |
|---|---|---|
| 0 | Make PDF Look Scanned Online — Free, Private, No Upload | Make PDF look scanned: add grain, blur, a slight tilt and an aged paper tone. Free, no signup — your file never leaves the browser. Works with images and Word. |
| 1 | How to Make a PDF Look Scanned: 6 Free Methods (2026) | How to make a PDF look like it was scanned: 6 tested methods — browser tool, Chrome extension, print dialog, image editor, phone photo, print-and-scan. |
| 2 | Make a Document Look Scanned: Word, Google Docs & Photos | Make a document look scanned without a scanner: turn Word files, Google Docs and phone photos into a realistic scan with noise, skew and paper tone. Free. |
| 3 | PDF to Scanned PDF: Convert, Flatten & Keep It Readable | Convert a PDF to a scanned PDF: flatten text into page images, pick DPI and grayscale, keep the file small and make it look scanned. Step-by-step and free. |
| 4 | What Is a Scanned PDF? Scanned Copy vs Digital PDF | What a scanned PDF is, how it differs from a digital PDF and a scanned copy, how to tell them apart in 10 seconds, and when you need OCR or a scan look. |
| 5 | Image to Scanned PDF: Turn a JPG or Photo Into a Scan | Turn an image into a scanned PDF: crop and whiten a phone photo, add a realistic scan effect and save JPG or PNG pages as one PDF. Free, in your browser. |
| 6 | How to Convert a Color PDF to Black and White (5 Ways) | How to convert a color PDF to black and white on Windows, Mac and online: print to PDF, Preview Quartz filter, browser tool. Grayscale vs pure B&W explained. |
| 7 | Scan Effect: What Makes a Document Look Scanned | The scan effect explained: noise, skew, blur, paper tone, edge shadows, grayscale — what makes a file look scanned, plus ready settings for 5 looks. |

Принципы: главный ключ в начале title и в первых 5 словах description; число/год в title (CTR); в description — результат + бенефит (free / no upload / step-by-step), без кликбейта; ключевая фраза не разбивается пунктуацией.

## 5. Чем статьи будут лучше конкурентов (кроме объёма)

1. **Точные настройки**, а не «добавьте немного шума»: угол 0,5–3°, DPI 150/200/300, уровень шума, тон бумаги — и таблица пресетов под сценарии.
2. **Сравнительные таблицы методов** (время, качество, приватность, цена, ОС).
3. **Блок «как проверить, что PDF выглядит как скан»**: выделение текста, свойства файла, размер, зум 400%.
4. **Честный блок об использовании**: инструмент — для внешнего вида документов (печать, архив, оформление); не для подделки подписей/официальных документов — это ещё и E-E-A-T-сигнал.
5. **Приватность как факт**: обработка локально в браузере (pdf.js + canvas) — объясняем, как это проверить (DevTools → Network).
6. **GEO-слой**: BLUF 40–60 слов в лиде и 40–50 в начале каждого H2, FAQ 8–12 вопросов, JSON-LD Article + FAQPage + HowTo + BreadcrumbList, `dl.spec-list`, таблицы с `caption`.
7. **5–6 внешних цитат** только из проверяемых источников (PDF Association, W3C/WCAG, ISO 32000 / PDF/A, документация Apple/Microsoft, университеты, крупные СМИ) — каждая открыта и проверена по ссылке; если дословной нет — атрибутированный пересказ.

## 6. Техническая часть (до первой публикации)

1. Статьи — статические файлы `lookscanned.io-main/public/blog/<slug>/index.html` (Vite копирует `public/` в `dist/`, GitHub Pages отдаёт их напрямую).
2. **Исправить PWA**: Workbox по умолчанию отдаёт `index.html` на любую навигацию → `/blog/*` у вернувшегося пользователя превратится в SPA и через catch-all редирект уйдёт на главную. Нужно `workbox.navigateFallbackDenylist: [/^\/blog/, /^\/sitemap\.xml$/, /^\/llms\.txt$/]`.
3. Проверить пустой `public/index.html` (0 байт) — может перезаписать собранный `dist/index.html`.
4. `seo-workspace/build.py`: сборка статьи из JSON стадий → HTML, индекс блога `/blog/`, `sitemap.xml`, `llms.txt`, строка `Sitemap:` в `robots.txt`.
5. Главная: статический SEO-блок (H2/FAQ/HowTo) в HTML — видимый без JS, т.к. SPA сейчас отдаёт боту пустую страницу; canonical, OG-теги, JSON-LD `SoftwareApplication` + `FAQPage`.
6. Дизайн статей: токены с сайта (тёмная тема `#0b0b0f`, акцент `#8fd14f`, светлый текст) — CSS шаблона адаптируется под тёмный фон, класс-обёртка `pls-article`.

## 7. Порядок работ

| Этап | Что | Результат |
|---|---|---|
| 0 | Ответы на вопросы, заполнение SETUP шаблона | `seo-workspace/project-config.md` |
| 1 | Техчасть (п. 6.1–6.4) | блог открывается, sitemap/llms.txt |
| 2 | Главная `/` — SEO-блок + сниппет | самый частотный ключ получает текст |
| 3 | #1 pillar → бриф на согласование → стадии 2–10 → QA → публикация | первая статья |
| 4 | #3, #4 (самые объёмные ключи 390–720) | |
| 5 | #2, #5, #6, #7 | |
| 6 | (опц.) #8 GEO-сравнение, локализация | |

По каждой статье: бриф (стадия 1b) показываю перед написанием, как требует шаблон; дальше пайплайн без остановок до QA.

## 8. Решения владельца проекта (18.09.2026)
- Длина: max-конкурент × 1,4 (не 10 000 слов).
- Конкуренты и сторонние продукты не называются нигде (включая Photoshop, GIMP, Acrobat и т.п.). Встроенные функции ОС/браузера (диалог печати Windows/macOS, Preview, Chrome) описываются как платформа.
- Ключ `lookscanned` не продвигаем.
- Trust badge: «Make PDF look scanned — rated 5 stars in the Chrome Web Store».
- Язык: только английский на старте.
- Публикация: автоматически (commit + push в main).
- #8 (GEO-сравнение) — отложено; сравнение методов встроено в #1 и главную.
