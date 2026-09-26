# Glossary — Japanese (ja) · pdflookscanned.com

Market: Japan. This file is binding for every Japanese page (home guide, blog chrome, 7 article bodies).
Interface labels must match `lookscanned.io-main/src/locale/messages/ja.json` character for character.

## 1. Style notes

- **Register:** body text in です・ます調 throughout. Headings (H2/H3, FAQ questions) may use short plain or question
  forms ending in 「？」 (e.g. 「PDFをスキャン風にする設定は？」「スキャンPDFとは？」). Do not mix だ・である into body text.
- **Answer-first:** every H2 opens with a direct answer paragraph of 80–150 characters.
- **Characters:** numbers and Latin letters are half-width (`2×`, `0.3`, `144dpi`, `PDF`, `JPG`). Japanese
  punctuation is full-width: 、。「」（）：？！. Use full-width （） around Japanese text; they may also wrap
  Latin text inside Japanese sentences, e.g. 「DOCX（Word）」. Use half-width `%` (`300〜400%`).
- **Spacing:** no space between Japanese and half-width text: 「PDFをスキャン風に」「Chrome拡張機能」「2×で」
  「144dpi」「約20〜60秒」. Exceptions — official names keep their own spacing: 「Chrome ウェブストア」
  「Google ドキュメント」「Microsoft Print to PDF」「デベロッパー ツール」. When a multi-word Latin name sits next to
  Japanese, prefer wrapping it in 「」 (「Microsoft Print to PDF」を選択) instead of adding spaces.
- **Ranges:** use 〜 (0.5°〜2°, 10〜20分). Keep the minus sign −, the degree sign °, and × as in the source.
  Decimal point stays「.」(0.3). Thousands: 2,200px.
- **UI labels and menu paths:** wrap in 「」 and write exactly as in ja.json or the Japanese OS UI:
  「スキャン風PDFを作成」をクリック, 「ファイル」→「書き出す」. Setting names used as nouns in running text may
  appear without brackets when unambiguous (回転のばらつきを0より大きく), but never in another wording.
- **Keyword forms:** 「スキャン風」 = scanned look (noun modifier, e.g. スキャン風PDF, スキャン風にする);
  「スキャンしたように見せる」 = make (it) look scanned (verb phrase). Both are natural search phrases; do not
  invent other variants such as 「スキャンっぽく」 in headings.
- **Brand:** 「Make PDF look scanned」 stays in English. Refer to it as 「無料ツール」「このツール」「スキャンツール」.
  In a byline: 「Make PDF look scanned チーム」.
- **Tone on use cases:** never suggest deceiving anyone. Avoid 「偽装」「バレない」「ごまかす」. Use neutral wording:
  「スキャン風に仕上げる」「本物らしく見える」「自然な仕上がり」.
- **Sources:** US agencies/courts stay as sources; name them in Japanese on first mention with the English
  abbreviation (same names as in meta.json `about`/`mentions`): アメリカ国立公文書記録管理局（NARA）,
  アメリカ合衆国市民権・移民業務局（USCIS）, 内国歳入庁（IRS）, 米国連邦裁判所の電子ファイリングシステム（CM/ECF）,
  FADGI（米国連邦政府機関のデジタル化ガイドライン）, WCAG, W3C, GOV.UK. Translate quoted words, keep attribution and link.
- **Paper sizes:** the tool places images on A4 pages — say 「A4」. US Letter = 「レターサイズ」.

## 2. Terms (EN → JA)

| English | Japanese | Notes |
|---|---|---|
| make a PDF look scanned | PDFをスキャン風にする／PDFをスキャンしたように見せる | home main keyword: 「PDF スキャン風」 |
| scan effect | スキャン効果 | the effect/controls in general |
| scan look, scanned look | スキャン風の見た目 | |
| scan-effect tool | スキャン風加工ツール | |
| applying a scan effect (the process) | スキャン風加工 | main keyword of scan-effect article |
| scanned PDF (real scan, image-only) | スキャンPDF | also 「画像PDF」 when contrasting with text |
| scanned-looking PDF (tool output) | スキャン風PDF | UI uses this form |
| scanned copy | スキャンしたコピー | organisations often say 「スキャンデータ」 |
| scanned document | スキャンした書類／スキャン文書 | |
| document (everyday) | 書類 | 「文書」 for technical/file context (Word文書) |
| digital PDF, born-digital PDF | テキストPDF（デジタルで作成したPDF） | short form テキストPDF |
| image-only PDF | 画像PDF（画像のみのPDF） | |
| searchable PDF | 検索可能なPDF | OCR'd: 透明テキスト付きPDF |
| text layer / hidden text layer | テキストレイヤー／透明テキスト | |
| OCR | OCR（光学文字認識） | spell out on first mention |
| flatten | フラット化 | |
| rasterize, render as image | 画像化／ラスタライズ | prefer 画像化 in running text |
| render | レンダリング | |
| page image | ページ画像 | |
| grayscale | グレースケール | UI option is 「グレー」 |
| black and white (pure, 1-bit) | 白黒（2値） | |
| bitonal | 2値 | |
| monochrome | モノクロ | |
| color | カラー | |
| color mode (scanner) | カラーモード | |
| skew, tilt | 傾き | technical: スキュー |
| deskew | 傾き補正 | |
| rotation | 回転 | |
| rotation variance (concept) | 回転のばらつき | = UI label |
| noise | ノイズ | sensor noise: センサーノイズ |
| grain | 粒状感 | |
| blur | ぼかし | |
| soft focus | ピントの甘さ／やわらかいピント | |
| moiré | モアレ | |
| halftone | 網点 | |
| paper tone | 紙の色味 | |
| yellowing, aged paper | 黄ばみ／古い紙 | |
| edge shadow | 端の影 | not a tool feature |
| crease, fold, stain | 折り目、しわ、しみ | not tool features |
| border (frame line) | 枠線 | |
| brightness | 明るさ | |
| contrast | コントラスト | |
| resolution | 解像度 | |
| dpi / ppi | dpi／ppi | 「約144dpi」, no space |
| JPEG compression artifacts | JPEGの圧縮ノイズ（ブロックノイズ） | |
| bit depth | ビット深度 | |
| file size | ファイルサイズ | |
| compression | 圧縮 | |
| photocopy / photocopier | コピー／コピー機 | |
| fax look | FAX風 | |
| flatbed scanner | フラットベッドスキャナー | |
| document feeder (ADF) | 自動原稿送り装置（ADF） | |
| multifunction printer | 複合機 | |
| phone scanner app | スマホのスキャンアプリ | never name one |
| raster image editor | ラスター画像編集ソフト | never name one |
| desktop PDF software | パソコン用のPDFソフト | never name one |
| print dialog | 印刷ダイアログ | |
| virtual printer | 仮想プリンター | |
| live preview | ライブプレビュー | |
| bulk scan (feature) | 一括スキャン | = UI label |
| side panel | サイドパネル | |
| Chrome extension | Chrome拡張機能 | |
| Chrome Web Store | Chrome ウェブストア | official spacing |
| trust badge | Chrome ウェブストアで5つ星評価 | meaning must stay "rated 5 stars" |
| local processing | ローカル処理／端末内で処理 | |
| upload / not uploaded | アップロード／アップロードされません | |
| processing server | 処理用サーバー | |
| offline, PWA | オフライン、プログレッシブウェブアプリ（PWA） | |
| no signup | 登録不要 | |
| free | 無料 | |
| watermark | 透かし | |
| stamp | スタンプ | Japanese seal image: 印影（はんこ） |
| signature / e-signature | 署名／電子署名 | |
| metadata | メタデータ | |
| multi-page PDF | 複数ページのPDF | |
| phone photo | スマホで撮った写真 | |
| screenshot | スクリーンショット | |
| screen reader | スクリーンリーダー | |
| accessibility | アクセシビリティ | |
| court filing | 裁判所への提出書類 | |
| agency | 行政機関 | |
| landlord / HR | 大家さん／人事部 | |
| honest use | 誠実な使い方 | callout title style |

## 3. Interface labels (exactly as in `messages/ja.json`)

| English (en.json) | Japanese (ja.json) | key |
|---|---|---|
| Scan | スキャン | base.scanTitle, base.nav.scan |
| Bulk Scan | 一括スキャン | base.bulkTitle, base.nav.bulk |
| Home | ホーム | base.nav.home |
| Guides | ガイド | base.nav.guides |
| Chrome Extension | Chrome拡張機能 | base.chrome.label |
| FREE | 無料 | base.chrome.free |
| Make PDF look scanned (H1) | PDFをスキャン風に変換 | base.landing.headline |
| Convert to Scanned PDF | スキャン風PDFに変換 | base.landing.cta |
| Three steps to a scanned PDF | 3ステップでスキャン風PDFに | base.landing.stepsTitle |
| Choose a file | ファイルを選ぶ | base.landing.step1Title |
| Adjust the scan effect | スキャン効果を調整 | base.landing.step2Title |
| Export the PDF | PDFを書き出す | base.landing.step3Title |
| Key features | 主な機能 | base.landing.featuresTitle |
| Language | 言語 | base.language |
| Start scanning | スキャンを始める | actions.navigateToScan |
| Back | 戻る | actions.backToIndex |
| Preview | プレビュー | actions.preview |
| Save | 保存 | actions.save |
| Generate Scanned PDF | スキャン風PDFを作成 | actions.generateScannedPDF |
| Generating... | 作成中… | actions.generating |
| Download Scanned PDF | スキャン風PDFをダウンロード | actions.downloadScannedPDF |
| Add files | ファイルを追加 | actions.addFiles, upload.addMore |
| Generate scanned PDFs | スキャン風PDFを一括作成 | actions.processAll |
| Download all as ZIP | ZIPで一括ダウンロード | actions.downloadZip |
| Queued / Done / Failed | 待機中／完了／失敗 | actions.* |
| Scan Settings | スキャン設定 | settings.settings |
| Noise | ノイズ | settings.noise |
| Blur | ぼかし | settings.blur |
| Border · Yes · No | 枠線・あり・なし | settings.border.* |
| Colorspace | カラーモード | settings.colorspace.label |
| Colorful | カラー | settings.colorspace.colorful |
| Gray | グレー | settings.colorspace.grayscale |
| Rotate | 回転 | settings.rotate |
| Rotate Variance | 回転のばらつき | settings.rotateVariance |
| Resolution | 解像度 | settings.scale |
| Yellowish | 黄ばみ | settings.yellowish |
| Brightness | 明るさ | settings.brightness |
| Contrast | コントラスト | settings.contrast |
| Select or drop your file here | ファイルを選択するか、ここにドロップ | settings.pdfSelectLabel |
| Watermark | 透かし | settings.extras.watermark |
| Watermark text | 透かしのテキスト | settings.extras.watermarkText |
| Watermark image | 透かしの画像 | settings.extras.watermarkImage |
| Stamp or signature | スタンプ・署名 | settings.extras.stamp |
| Add stamp or signature | スタンプ・署名を追加 | settings.extras.stampImage |
| Horizontal position | 横位置 | settings.extras.stampX |
| Vertical position | 縦位置 | settings.extras.stampY |
| Size | サイズ | settings.extras.stampScale |
| PDF metadata | PDFメタデータ | settings.extras.metadata |
| Title / Author / Subject / Keywords | タイトル／作成者／件名／キーワード | settings.extras.* |
| Producer / Creator | PDF変換ソフト／作成アプリケーション | settings.extras.* |
| Remove | 削除 | settings.extras.clearImage |
| Drop your file(s) here | ここにファイルをドロップ／ここにファイルをまとめてドロップ | upload.dropTitle* |
| Choose file / Choose files | ファイルを選択 | upload.choose* |
| Choose another file | 別のファイルを選択 | upload.replace |
| Create scanned PDF | スキャン風PDFを作成 | save.create |
| Download again | もう一度ダウンロード | save.downloadAgain |
| Show in preview | プレビューに表示 | files.preview |
| Download this scanned PDF | このスキャン風PDFをダウンロード | files.downloadOne |
| Remove file | ファイルを削除 | files.remove |
| Upload / Adjust / Download (steps) | アップロード／調整／ダウンロード | steps.* |
| Upload your files | ファイルをアップロード | steps.uploadTitle |
| Adjust the scan look | スキャンの見た目を調整 | steps.adjustTitle |
| Get your scanned PDF | スキャン風PDFを保存 | steps.downloadTitle |
| Original / Scanned preview | 元のファイル／スキャン風プレビュー | preview.* |

Blog chrome (chrome.json): nav 「PDFをスキャン風に」, CTA 「無料ツールを開く →」「Chromeに追加（無料）→」
「ほかのガイドを見る →」, badge 「Chrome ウェブストアで5つ星評価」, related 「関連ガイド」.

## 4. OS and app built-ins (names as shown in the Japanese UI)

| English | Japanese UI |
|---|---|
| macOS Preview | プレビュー（「プレビュー」App） |
| File → Export… | 「ファイル」→「書き出す…」 |
| Export as PDF… | 「PDFとして書き出す…」 |
| Quartz filter | Quartzフィルタ |
| Quartz: Black & White / Gray Tone / Reduce File Size | 「白黒」／「グレイトーン」／「ファイルサイズを減らす」 |
| Open With → Preview | 「このアプリケーションで開く」→「プレビュー」 |
| macOS Print → PDF → Save as PDF | 「プリント」→「PDF」→「PDFとして保存…」 |
| sidebar (Preview) | サイドバー |
| Windows "Microsoft Print to PDF" | 「Microsoft Print to PDF」（名前はそのまま） |
| Print (Windows) / Ctrl+P / Command-P | 「印刷」／Ctrl+P／Command+P |
| Printer Properties / Preferences | 「プリンターのプロパティ」／「基本設定」 |
| Windows Photos app | 「フォト」アプリ |
| Show more options (Windows 11) | 「その他のオプションを確認」 |
| Full page photo (print layout) | 「全ページ写真」 |
| Fit picture to frame | 「写真をフレームに合わせる」 |
| Chrome print: Destination / Save as PDF | 「送信先」／「PDFに保存」 |
| Chrome print: More settings / Color / Black and white | 「詳細設定」／「カラー」／「白黒」 |
| Edge print: Color → Color / Black and white | 「色」→「カラー」／「白黒」 |
| Chrome puzzle-piece icon, Pin | 拡張機能アイコン（パズルのピース）、「固定」 |
| Chrome side panel | サイドパネル |
| Developer tools / Network tab | デベロッパー ツール／「ネットワーク」タブ |
| Word: File → Save As → PDF / Export | 「ファイル」→「名前を付けて保存」→ PDF／「エクスポート」 |
| Word: File → Print | 「ファイル」→「印刷」 |
| Google Docs: File → Download → PDF document | 「ファイル」→「ダウンロード」→「PDF ドキュメント（.pdf）」 |
| Excel: Page setup | 「ページ設定」 |
| iPhone Notes / Files app | 「メモ」App／「ファイル」App |
| Scan Documents (iPhone) | 「書類をスキャン」 |
| iPhone Settings → Camera → Formats → Most Compatible | 「設定」→「カメラ」→「フォーマット」→「互換性優先」 |
| Android camera document mode | Androidのカメラの書類（ドキュメント）モード |
| Document Properties / Fonts tab (PDF viewers) | 「文書のプロパティ」／「フォント」タブ |
| Downloads folder | 「ダウンロード」フォルダ |

## 5. Keyword and title plan

Slugs stay English for ja (non-Latin slugs become %-encoded). `main_keyword` uses a half-width space between
parts; QA accepts the exact string or all space-separated parts, so 「PDFをスキャンしたように見せる」 matches
`pdf スキャンしたように見せる`.

| en-slug | Local main keyword | Slug | Title |
|---|---|---|---|
| (home) | pdf スキャン風 | / | PDFをスキャン風に無料変換｜登録・アップロード不要 |
| (blog index) | pdf スキャン風 | /blog/ | PDFをスキャン風にする方法｜設定と使い方ガイド |
| how-to-make-a-pdf-look-scanned | pdf スキャンしたように見せる | how-to-make-a-pdf-look-scanned | PDFをスキャンしたように見せる方法6選【2026年】 |
| make-a-document-look-scanned | 書類 スキャン風 | make-a-document-look-scanned | 書類をスキャン風にする方法｜Word・写真にも対応 |
| pdf-to-scanned-pdf | pdf 画像化 | pdf-to-scanned-pdf | PDFを画像化してスキャンPDFに｜変換・フラット化の手順 |
| what-is-a-scanned-pdf | スキャンpdf | what-is-a-scanned-pdf | スキャンPDFとは？テキストPDFとの違いと見分け方 |
| image-to-scanned-pdf | 画像 スキャン風 pdf | image-to-scanned-pdf | 画像をスキャン風PDFに変換｜JPG・スマホ写真に対応 |
| convert-color-pdf-to-black-and-white | pdf 白黒 変換 | convert-color-pdf-to-black-and-white | PDFを白黒に変換する方法5選｜Mac・Windows対応 |
| scan-effect | スキャン風 加工 | scan-effect | スキャン風加工とは？スキャンしたように見える要素 |

Anchor text for internal links (use these or close variants):
- `/blog/how-to-make-a-pdf-look-scanned/` → PDFをスキャンしたように見せる方法
- `/blog/make-a-document-look-scanned/` → 書類をスキャン風にする方法
- `/blog/pdf-to-scanned-pdf/` → PDFを画像化してスキャンPDFにする方法
- `/blog/what-is-a-scanned-pdf/` → スキャンPDFとは
- `/blog/image-to-scanned-pdf/` → 画像をスキャン風PDFに変換する方法
- `/blog/convert-color-pdf-to-black-and-white/` → カラーPDFを白黒に変換する方法
- `/blog/scan-effect/` → スキャン風加工（の設定ガイド）
- `/scan` → スキャンツール／無料ツール · `/scan/bulk` → 一括スキャン
