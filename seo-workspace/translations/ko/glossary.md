# Korean (ko) glossary — pdflookscanned.com

Market: South Korea. Read `seo-workspace/translations/TRANSLATOR-GUIDE.md` first; this file fixes the Korean
wording so every page, the app and the blog agree. Interface labels below are copied exactly from
`lookscanned.io-main/src/locale/messages/ko.json` — quote them character for character.

## 1. Style

- **Register:** body text consistently in 합니다체 (…합니다, …입니다, …할 수 있습니다). Polite imperatives in
  instructions: …하세요 / …해 보세요. Headings may end in a question with …나요? / …까요? / …인가요? or in a noun
  phrase (…하는 방법, …만들기). No 반말, no 해요체 in body text.
- **Tone:** plain, factual, short sentences, like a Korean IT help page. No hype (혁신적인, 최고의, 완벽한 are out).
  Avoid translationese: drop needless 당신/여러분, 그것은/이것은 openers and passive calques (…되어지다).
  Answer-first: every H2 opens with an 80–150-character paragraph that answers the heading by itself and names the
  subject (e.g. "스캔 PDF는 …입니다", never "그것은 …").
- **Spacing (띄어쓰기):** particles attach (PDF를, 워드로); dependent nouns take a space (할 수 있습니다,
  만드는 것, 넣은 뒤, 1분 안에). Arabic numerals attach to counters: 6가지, 3단계, 10페이지, 1분, 5점, 2개, 1단계.
  Compound terms in this glossary are written exactly as listed (스캔 효과, 스캔 PDF, 회전 편차, 색 공간).
- **Particles after Latin words** (by Korean pronunciation): PDF/JPG/PNG/SVG/CSV/DOCX/XLSX/DPI/Word/WebP →
  를/는/가/와/로 (vowel ending); OCR/HTML/Excel/엑셀 → 을/은/이/과/로 (ㄹ ending); JPEG, ZIP, Chrome →
  을/은/이/과/으로 (ZIP으로, Chrome으로, JPEG으로).
- **Brand:** "Make PDF look scanned" stays in English, never translated, never followed directly by a particle —
  use a noun bridge: "무료 도구 Make PDF look scanned", "Make PDF look scanned 확장 프로그램은 …". Never write or
  target "lookscanned".
- **Numbers:** decimal point "." (0.3, 0.5°), thousands separator "," (2,200 px). Values exactly as in English.
  Ranges with "~": 0.5°~2°, 20~60초, 300~400%, 1×~3×, −10°~10° (minus sign "−" kept). Degree sign, ×, % attached:
  1°, 2×, 400%. Latin units with a space as in the source: 144 dpi, 2,200 px, 11 pt, 2.5 MB. "DPI" in capitals when
  it stands alone as a term (DPI란 무엇인가요?), lowercase dpi after a number (144 dpi).
- **Dates:** 2026년 9월 18일; month-year 2026년 9월. Time: 1분 미만, 30분 이상, 몇 초 만에.
- **Paper sizes:** keep A4 (the Korean standard) and "레터(Letter)" when the English text mentions US Letter.
- **Quotes from sources:** translate the words, keep the organization and the link: "미국 국립문서기록관리청(NARA)은
  … 라고 설명합니다." Mark paraphrases as such ("…에 따르면"). Do not add sources.
- **Words:** 휴대폰 (not 핸드폰/스마트폰), 사진 (photo), 이미지 (image file), 파일 용량 (file size), 회원가입 (signup),
  워드 / 엑셀 / 구글 문서 for the source formats, 윈도우 / 맥 in running prose (Windows / macOS in UI paths and
  version-specific notes), Chrome always in Latin letters (Google's Korean UI does the same).
- **Do not add:** HWP/한글 (Hancom) files — the tool does not read them and the English source does not mention
  them. No competitor or third-party app names (full list in `seo-workspace/qa.py` → FORBIDDEN).

## 2. Keyword plan (home + 7 articles)

Main keywords are chosen so that QA's check (exact string, or all space-separated parts) survives Korean
particles: put the parts in title, H1, first sentence of `.lead` and at least two H2s, and the exact phrase about
5+ times in the body.

| Page (en-slug) | Local main keyword | Slug | Title |
|---|---|---|---|
| home (`/ko/`) | PDF 스캔한 것처럼 만들기 | — | PDF 스캔한 것처럼 만들기 – 무료·업로드 없음 |
| how-to-make-a-pdf-look-scanned | pdf 스캔한 것처럼 | how-to-make-a-pdf-look-scanned | PDF 스캔한 것처럼 만드는 방법 6가지 (2026) |
| make-a-document-look-scanned | 문서 스캔한 것처럼 | make-a-document-look-scanned | 문서 스캔한 것처럼 만들기: 워드·구글 문서·사진 |
| pdf-to-scanned-pdf | pdf 스캔본 변환 | pdf-to-scanned-pdf | PDF 스캔본 변환: 평탄화부터 해상도·용량까지 |
| what-is-a-scanned-pdf | 스캔 pdf | what-is-a-scanned-pdf | 스캔 PDF란? 스캔본과 디지털 PDF의 차이 |
| image-to-scanned-pdf | 이미지 스캔본 pdf | image-to-scanned-pdf | 이미지를 스캔본 PDF로: JPG·휴대폰 사진 변환 |
| convert-color-pdf-to-black-and-white | pdf 흑백 변환 | convert-color-pdf-to-black-and-white | PDF 흑백 변환 방법 5가지: 윈도우·맥·온라인 |
| scan-effect | 스캔 효과 | scan-effect | 스캔 효과: 문서가 스캔본처럼 보이는 이유와 설정 |
| blog index | PDF 스캔한 것처럼 만들기 | — | PDF 스캔한 것처럼 만들기: 가이드·설정·방법 |

How the keywords are used in headings (examples for article translators):
- pdf 스캔한 것처럼 → "방법 1: 브라우저에서 PDF를 스캔한 것처럼 만들기", "PDF 스캔한 것처럼 만들기: 자주 묻는 질문".
- 문서 스캔한 것처럼 → "문서를 스캔한 것처럼 만드는 방법은?", "워드 문서를 스캔한 것처럼 만드는 방법".
- pdf 스캔본 변환 → "PDF 스캔본 변환은 무엇을 하나요?", "PDF 스캔본 변환 문제는 어떻게 해결하나요?".
- 스캔 pdf → "스캔 PDF란 정확히 무엇인가요?", "스캔 PDF는 디지털 PDF와 어떻게 다른가요?".
- 이미지 스캔본 pdf → "이미지를 스캔본 PDF로 바꾸는 가장 빠른 방법은?", "이미지 스캔본 PDF: 자주 묻는 질문".
- pdf 흑백 변환 → "방법 1: 브라우저에서 PDF 흑백 변환하기", "PDF 흑백 변환: 자주 묻는 질문".
- 스캔 효과 → "스캔 효과란 무엇인가요?", "스캔 효과 설정 5가지".

Internal link anchors (use these texts when linking the other guides):
`/blog/how-to-make-a-pdf-look-scanned/` PDF 스캔한 것처럼 만드는 방법 · `/blog/make-a-document-look-scanned/` 문서
스캔한 것처럼 만들기 · `/blog/pdf-to-scanned-pdf/` PDF 스캔본 변환 · `/blog/what-is-a-scanned-pdf/` 스캔 PDF란 ·
`/blog/image-to-scanned-pdf/` 이미지를 스캔본 PDF로 · `/blog/convert-color-pdf-to-black-and-white/` 컬러 PDF 흑백
변환 · `/blog/scan-effect/` 스캔 효과 설정 가이드 · `/scan` 무료 스캔 도구 / 스캐너 · `/scan/bulk` 일괄 스캔.

## 3. Recurring terms (EN → KO)

| English | Korean | Note |
|---|---|---|
| make a PDF look scanned / make it look scanned | PDF를 스캔한 것처럼 만들다 / 스캔본처럼 만들다 | keyword form: PDF 스캔한 것처럼 만들기 |
| scan effect | 스캔 효과 | |
| scanned look / scan look | 스캔한 느낌 | "스캔 느낌" also fine in headings |
| scanned PDF | 스캔 PDF | "스캔한 PDF" when it is a verb phrase |
| scanned copy | 스캔본 | as asked for by landlords, HR, schools |
| scanned document | 스캔 문서 | |
| scanned-looking PDF | 스캔본 같은 PDF | or 스캔한 것처럼 보이는 PDF |
| digital PDF / born-digital PDF | 디지털 PDF | |
| image-only PDF / image-based PDF | 이미지로만 된 PDF / 이미지 기반 PDF | |
| searchable PDF | 검색 가능한 PDF | |
| text layer | 텍스트 레이어 | hidden OCR text: 숨은 텍스트 레이어 |
| OCR | OCR(광학 문자 인식) | spell out on first use per page |
| flatten | 평탄화하다 (평탄화) | "flat pixels" → 평평한 픽셀 / 한 장의 이미지 |
| rasterize | 래스터화하다 (래스터화) | |
| render / page image | 렌더링하다 / 페이지 이미지 | |
| grayscale | 회색조 | first mention may add (그레이스케일); UI value is 회색조 |
| black and white (general) | 흑백 | |
| pure black and white / bitonal / 1-bit | 순수 흑백(이진) / 1비트 | 2 levels vs 회색조 256단계 |
| color (mode) | 컬러 | |
| colorspace | 색 공간 | UI label |
| bit depth | 비트 심도 | |
| tilt / skew | 기울기 (기울어짐) | "slight tilt" → 살짝 기울어진 각도 |
| rotation / rotate | 회전 | UI label 회전 |
| rotation variance | 회전 편차 | UI label |
| deskew / perspective correction / crop | 기울기 보정 / 원근 보정 / 자르기 | not tool features |
| noise | 노이즈 | UI label |
| grain / scanner grain | 입자감 / 스캐너 입자감 | |
| blur / soft focus | 흐림 / 부드럽게 흐려진 초점 | UI label 흐림 |
| brightness | 밝기 | UI label |
| contrast | 대비 | UI label |
| paper tone | 종이 색감 | cream paper → 미색 종이 |
| yellowish / aged paper | 누런 톤 / 누렇게 바랜 종이 | UI label 누런 톤 |
| border / scanner-edge line | 테두리 / 스캐너 가장자리 선 | UI label 테두리 |
| edge shadows / creases, folds, stains | 가장자리 그림자 / 구김, 접힌 자국, 얼룩 | not tool features |
| moiré | 모아레 | |
| halftone | 하프톤(망점) | |
| JPEG compression / artifacts | JPEG 압축 / 압축 아티팩트 | JPEG 블록 for "JPEG blocks" |
| resolution | 해상도 | UI label |
| dpi / ppi / scale factor | dpi / ppi / 배율 | "2× resolution" → 해상도 2×; 72 dpi × 배율 |
| file size | 파일 용량 | |
| photocopy look / photocopier | 복사본 느낌 / 복사기 | |
| fax look | 팩스 느낌 | |
| office scan | 사무실 스캔 | |
| flatbed scanner / sheet feeder (ADF) | 평판 스캐너 / 자동 급지 장치(ADF) | |
| print dialog | 인쇄 대화상자 | macOS menu says 프린트 (see §5) |
| print and scan / phone photo of a printout | 인쇄 후 스캔 / 인쇄물을 휴대폰으로 촬영 | |
| phone scanner app | 휴대폰 스캐너 앱 | never a brand |
| raster image editor | 래스터 이미지 편집기 | never a brand |
| desktop PDF software | 데스크톱 PDF 프로그램 | never a brand |
| bulk scan | 일괄 스캔 | UI label |
| ZIP archive | ZIP 파일 | |
| live preview | 실시간 미리보기 | |
| processed locally in your browser | 브라우저에서 로컬로 처리 | |
| not uploaded to a server | 서버에 업로드되지 않음 | |
| works offline / PWA | 오프라인에서 작동 / 프로그레시브 웹 앱(PWA) | |
| free, no signup | 무료, 회원가입 없음 | |
| Chrome extension | Chrome 확장 프로그램 | |
| side panel | 측면 패널 | Chrome UI term |
| Chrome Web Store | Chrome 웹 스토어 | |
| trust badge "rated 5 stars in the Chrome Web Store" | Chrome 웹 스토어 별점 5점 | in text: Chrome 웹 스토어에서 별점 5점을 받은 |
| web tool / the scanner (/scan) | 웹 도구 / 스캐너 | |
| watermark | 워터마크 | |
| stamp or signature / e-signature | 도장 또는 서명 / 전자 서명 | UI label 도장 또는 서명 |
| metadata / form fields / layers | 메타데이터 / 양식 필드 / 레이어 | |
| screen reader / accessibility | 스크린 리더 / 접근성 | |
| court filing / agency submission / long-term archiving (PDF/A) | 법원 제출 서류 / 기관 제출 / 장기 보존 (PDF/A) | |
| honest use (ethics callout) | 스캔 효과는 정직하게 사용하세요 | |
| preset / recipe / method, way / step | 프리셋 / 설정 조합 / 방법 / 단계 | "Way 1", "Method 1" → 방법 1 |
| FAQ / Table of Contents | 자주 묻는 질문 / 목차 | heading "… 자주 묻는 질문" or "… FAQ" |
| The Make PDF look scanned team | Make PDF look scanned 팀 | expert-quote cite: "웹 도구와 Chrome 확장 프로그램 개발팀" |

Sources and organizations: 미국 국립문서기록관리청(NARA) · FADGI(미국 연방기관 디지털화 가이드라인) ·
미국 의회도서관 · W3C · WCAG(웹 콘텐츠 접근성 지침) · 미국 시민이민서비스국(USCIS) · 미국 국세청(IRS) ·
CM/ECF(미국 연방법원 전자 제출 시스템) · GOV.UK · BBC 뉴스 · ISO 32000 · ISO 19005(PDF/A).

## 4. Interface labels (exactly as in ko.json)

| English UI | Korean UI (ko.json) | key |
|---|---|---|
| Scan | 스캔 | base.nav.scan / base.scanTitle |
| Bulk Scan | 일괄 스캔 | base.nav.bulk / base.bulkTitle |
| Home | 홈 | base.nav.home |
| Guides | 가이드 | base.nav.guides |
| Chrome Extension | Chrome 확장 프로그램 | base.chrome.label |
| FREE | 무료 | base.chrome.free |
| Convert to Scanned PDF | 스캔 PDF로 변환하기 | base.landing.cta |
| Start scanning | 스캔 시작하기 | actions.navigateToScan |
| Preview | 미리보기 | actions.preview |
| Save | 저장 | actions.save |
| Generate Scanned PDF | 스캔 PDF 생성 | actions.generateScannedPDF |
| Generating... | 생성 중... | actions.generating |
| Download Scanned PDF | 스캔 PDF 다운로드 | actions.downloadScannedPDF |
| Add files | 파일 추가 | actions.addFiles |
| Generate scanned PDFs | 스캔 PDF 모두 생성 | actions.processAll |
| Download all as ZIP | ZIP으로 모두 다운로드 | actions.downloadZip |
| Queued / Done / Failed | 대기 중 / 완료 / 실패 | actions.* |
| Scan Settings | 스캔 설정 | settings.settings |
| Noise | 노이즈 | settings.noise |
| Blur | 흐림 | settings.blur |
| Border (Yes / No) | 테두리 (예 / 아니요) | settings.border |
| Colorspace | 색 공간 | settings.colorspace.label |
| Colorful | 컬러 | settings.colorspace.colorful |
| Gray | 회색조 | settings.colorspace.grayscale |
| Rotate | 회전 | settings.rotate |
| Rotate Variance | 회전 편차 | settings.rotateVariance |
| Resolution | 해상도 | settings.scale |
| Yellowish | 누런 톤 | settings.yellowish |
| Brightness | 밝기 | settings.brightness |
| Contrast | 대비 | settings.contrast |
| Select or drop your file here | 파일을 선택하거나 여기에 끌어다 놓으세요 | settings.pdfSelectLabel |
| Watermark | 워터마크 | settings.extras.watermark |
| Watermark text / Watermark image | 워터마크 텍스트 / 워터마크 이미지 | settings.extras.* |
| Stamp or signature | 도장 또는 서명 | settings.extras.stamp |
| Add stamp or signature | 도장 또는 서명 추가 | settings.extras.stampImage |
| Horizontal position / Vertical position / Size | 가로 위치 / 세로 위치 / 크기 | settings.extras.stampX/Y/Scale |
| PDF metadata | PDF 메타데이터 | settings.extras.metadata |
| Title / Author / Subject / Keywords | 제목 / 작성자 / 주제 / 키워드 | settings.extras.* |
| Producer / Creator | 제작 프로그램 / 작성 프로그램 | settings.extras.producer/creator |
| Remove (image) | 제거 | settings.extras.clearImage |
| Drop your file here / Drop your files here | 파일을 여기에 끌어다 놓으세요 / 여러 파일을 여기에 끌어다 놓으세요 | upload.dropTitle* |
| Choose file / Choose files | 파일 선택 / 여러 파일 선택 | upload.choose* |
| Choose another file | 다른 파일 선택 | upload.replace |
| Add more files | 파일 더 추가 | upload.addMore |
| Processed in your browser — nothing is uploaded | 브라우저에서 처리 — 업로드되는 파일 없음 | upload.privacy |
| Create scanned PDF | 스캔 PDF 만들기 | save.create |
| Download again | 다시 다운로드 | save.downloadAgain |
| Download this scanned PDF | 이 스캔 PDF 다운로드 | files.downloadOne |
| Remove file | 파일 삭제 | files.remove |
| Show in preview | 미리보기에 표시 | files.preview |
| Steps: Upload / Adjust / Download | 업로드 / 조정 / 다운로드 | steps.* |
| Upload your files | 파일 업로드 | steps.uploadTitle |
| Adjust the scan look | 스캔 효과 조정 | steps.adjustTitle |
| Get your scanned PDF | 스캔 PDF 받기 | steps.downloadTitle |
| Original / Scanned preview | 원본 / 스캔 미리보기 | preview.* |

In running text write button and slider names as plain text without quotes, e.g. "스캔 PDF 생성을 클릭합니다",
"ZIP으로 모두 다운로드를 누르세요", "색 공간을 회색조로 두세요", "회전 편차를 0.5°로 설정합니다".

## 5. OS and app built-ins as named in the Korean UI

| English | Korean UI |
|---|---|
| macOS Preview | 미리보기 (앱) |
| Preview: File → Export… / Export as PDF… | 파일 > 내보내기… / 파일 > PDF로 내보내기… |
| Preview: Quartz Filter (Black & White, Gray Tone, Reduce File Size) | Quartz 필터 (흑백, 회색 톤, 파일 크기 줄이기) |
| macOS File → Print… / PDF → Save as PDF | 파일 > 프린트… / PDF > PDF로 저장 |
| macOS Photos | 사진 (앱) |
| Windows "Microsoft Print to PDF" | Microsoft Print to PDF (name unchanged) |
| Windows print dialog: Print / Printer properties / Color: Black and white | 인쇄 / 프린터 속성(기본 설정) / 색: 흑백 |
| Windows Photos → Print | 사진 앱 > 인쇄 |
| File Explorer / Downloads folder | 파일 탐색기 / 다운로드 폴더 |
| Word: File → Save As → PDF | 파일 > 다른 이름으로 저장 > 파일 형식: PDF (*.pdf) |
| Word: File → Export → Create PDF/XPS | 파일 > 내보내기 > PDF/XPS 문서 만들기 |
| Google Docs: File → Download → PDF document (.pdf) | 파일 > 다운로드 > PDF 문서(.pdf) |
| Chrome print (Ctrl+P): Destination → Save as PDF; Color → Black and white; More settings | 인쇄: 대상 > PDF로 저장; 색상 > 흑백; 설정 더보기 |
| Microsoft Edge print: Save as PDF; Color → Black and white | 인쇄: PDF로 저장; 색 > 흑백 |
| Chrome side panel / Extensions | 측면 패널 / 확장 프로그램 |
| Developer tools → Network tab | 개발자 도구 > 네트워크 탭 |
| iPhone Notes → Scan Documents | 메모 앱 > 문서 스캔 |
| iPhone Files → Scan Documents | 파일 앱 > 문서 스캔 |
| iPhone Settings → Camera → Formats → Most Compatible | 설정 > 카메라 > 포맷 > 높은 호환성 |
| Android camera | 카메라 앱 |
| Shortcuts Ctrl+P / Cmd+P | Ctrl+P / Cmd+P |

Menu paths use " > " between steps in Korean text (the English "→" is also acceptable inside step lists, but be
consistent within one article).
