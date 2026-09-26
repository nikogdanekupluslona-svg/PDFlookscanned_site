# Glossaire français (fr) — pdflookscanned.com

Marché : France, Belgique, Suisse, Canada — français standard (pas de régionalismes, pas de « québécismes » ni de
belgicismes). Ce fichier fait foi pour tous les textes français : interface (`messages/fr.json`), guide de l'accueil
(`home-guide/fr.html`), habillage du blog (`translations/fr/chrome.json`) et les 7 articles.

## 1. Adresse et style

- **Vouvoiement** partout (« vous », « votre », impératif en « -ez » : « Déposez », « Réglez », « Téléchargez »).
  Jamais de tutoiement, jamais de « on » pour s'adresser au lecteur (« on » reste possible pour une vérité générale :
  « On donne un effet scanné à un PDF quand… »).
- Phrases courtes, style direct, réponse d'abord. Chaque H2 s'ouvre sur un paragraphe de 40–60 mots qui répond seul
  à la question, en nommant le sujet (pas de « Cela… », « Il… » en ouverture).
- Pas de calques de l'anglais : « faire ressembler », « donner un aspect », pas « faire regarder scanné » ;
  « régler » / « ajuster » plutôt que « tuner » ; « aperçu en direct » plutôt que « preview live ».
- **Titres et intertitres en casse de phrase** : seule la première lettre (et les noms propres) en majuscule.
  L'anglais « What Is a Scanned PDF? » devient « Qu'est-ce qu'un PDF scanné ? », jamais « Qu'est-Ce Qu'un PDF Scanné ».
- Les intertitres qui sont des questions en anglais restent des questions en français (≤ 70 caractères).
- Pas de mots creux (« révolutionnaire », « ultime », « incroyable »), pas d'emoji.
- Le nom du produit **Make PDF look scanned** reste en anglais (nom propre, sans guillemets, sans article
  obligatoire) : « l'outil gratuit Make PDF look scanned », « l'équipe Make PDF look scanned ». Ne jamais le traduire.
- Ne jamais écrire « lookscanned » ni nommer un concurrent ou un logiciel tiers (liste `seo-workspace/qa.py` →
  `FORBIDDEN`). Dire « un éditeur d'images matricielles », « une application de scan pour téléphone »,
  « un logiciel PDF de bureau ». Le contrôle QA travaille sur des mots entiers : « canevas » est accepté, mais
  évitez tout mot qui contiendrait exactement un nom interdit.

## 2. Typographie

- Espace avant `:` `;` `?` `!` (une espace simple suffit dans le HTML et le JSON ; pas d'espace avant `.` et `,`).
- Guillemets français avec espaces : « copie scannée ». Guillemets anglais seulement dans les citations imbriquées.
- Apostrophe droite `'` partout (cohérence avec `fr.json` et avec ce que les gens tapent dans la recherche).
- Tiret cadratin `—` comme dans la source pour les incises ; tiret demi-cadratin `–` pour les plages (0,2–0,4).
- Mois en minuscules : « 18 septembre 2026 ». Format de date : jour mois année.
- Chemins de menus : garder la flèche de la source → « Fichier → Exporter ».
- Majuscules : « Chrome Web Store », « Microsoft Print to PDF », « Aperçu » (app macOS), mais « l'extension Chrome »,
  « le navigateur », « l'outil web ».

## 3. Nombres et unités

| Règle | Exemple anglais | Français |
|---|---|---|
| Virgule décimale | 0.3, 0.5°, 1.1 | 0,3 · 0,5° · 1,1 |
| Plages | 0.2–0.4, 0.5°–2° | 0,2–0,4 · 0,5°–2° (ou « de 0,2 à 0,4 ») |
| Séparateur de milliers : espace | 2,200 px | 2 200 px |
| Pourcentage : espace avant % | 300–400% | 300–400 % |
| Degré collé au nombre | 1° | 1° |
| Multiplicateur de résolution inchangé | 2×, 3× | 2×, 3× |
| Résolution | 144 dpi | 144 dpi (on peut préciser une fois « points par pouce » ; « ppp » accepté, mais restez sur **dpi**) |
| Densité de pixels | 300 ppi | 300 ppi (pixels par pouce) |
| Tailles de fichier | 2 MB, 500 KB, 1 GB | 2 Mo, 500 Ko, 1 Go |
| Durées | 10–20 minutes | 10 à 20 minutes |
| Formats de papier | A4, Letter | A4 (par défaut en Europe) ; Letter = « format Lettre US » |
| Bits | 1-bit, 8-bit | 1 bit, 8 bits (« image 1 bit », « niveaux de gris 8 bits ») |
| Raccourcis | Ctrl+P, Cmd+P | Ctrl+P, Cmd+P (inchangés) |

Les valeurs restent exactement celles de la source ; seule la notation change.

## 4. Termes récurrents EN → FR

| Anglais | Français (à utiliser) | Remarques |
|---|---|---|
| scan effect | effet scanné | terme général dans tous les textes |
| scanner effect / scan effect (article `scan-effect`) | effet scanner | mot-clé principal de l'article `scan-effect` ; y alterner avec « effet scanné » |
| scan look / scanned look | aspect scanné, rendu scanné | |
| make a PDF look scanned | donner un effet scanné à un PDF ; faire ressembler un PDF à un scan | 1re forme = accueil ; 2e = article pilier |
| make a document look scanned | donner un aspect scanné à un document | |
| scanned-looking PDF | PDF d'aspect scanné | |
| scanned PDF | PDF scanné | synonyme occasionnel : PDF numérisé |
| scanned copy | copie scannée | |
| scanned document | document scanné (document numérisé) | |
| scan (noun) / to scan / scanning | un scan / scanner / numérisation | « numériser » en synonyme soutenu |
| scanner (device) | scanner | « numériseur » seulement pour l'entité Wikipédia |
| flatbed scanner / office scanner | scanner à plat / scanner de bureau | « scan de bureau » pour le rendu |
| sheet-fed scanner / document feeder (ADF) | scanner à défilement / chargeur automatique de documents | |
| digital PDF / born-digital PDF | PDF natif | « PDF numérique » en synonyme |
| image-only PDF | PDF image (PDF composé uniquement d'images) | |
| searchable PDF / text-searchable | PDF interrogeable / texte interrogeable | |
| text layer | couche de texte | « couche de texte invisible » pour l'OCR |
| OCR | OCR (reconnaissance optique de caractères) | développer une fois par article |
| flatten / flattening | aplatir / aplatissement | « aplatir un PDF » |
| rasterize / rasterization | rastériser / rastérisation | ou « convertir en image » |
| page image | image de page | |
| vector (text, shapes) | vectoriel (texte vectoriel, contours vectoriels) | |
| raster image editor | éditeur d'images matricielles | jamais de nom de logiciel |
| grayscale | niveaux de gris | « un PDF en niveaux de gris » |
| black and white (pure, 1-bit) / bitonal | noir et blanc pur / bitonal | expliquer une fois : 1 bit, deux valeurs |
| color (mode) / color space | couleur / espace colorimétrique | dans l'interface : « Mode couleur » |
| bit depth | profondeur de couleur (profondeur de bits) | |
| threshold / halftone | seuil / trame (similigravure) | |
| skew / tilt / tilted / deskew | inclinaison / inclinaison / incliné / redresser | « légère inclinaison » |
| rotation | rotation | |
| noise / grain | bruit / grain | « grain du scanner » |
| blur / soft focus / sharpness | flou / léger flou / netteté | |
| moiré | moiré | |
| paper tone / yellowed, aged paper | teinte du papier / papier jauni, papier vieilli | |
| brightness / contrast | luminosité / contraste | |
| JPEG compression / JPEG blocks / artifacts | compression JPEG / blocs JPEG / défauts, artefacts | « artefacts de compression » |
| edge shadows / creases, folds / coffee stains | ombres de bord / plis, pliures / taches de café | l'outil n'en produit aucun |
| border (scanner edge line) | bordure (fine ligne de bord de scanner) | |
| perspective (phone photo) / crop | perspective (déformation de perspective) / recadrer, recadrage | |
| photocopy look / fax look | effet photocopie / effet fax (rendu télécopie) | photocopier = photocopieur |
| preset / recipe / cheat sheet | préréglage / recette / aide-mémoire | |
| resolution | résolution | |
| file size | taille du fichier | « plus léger » / « plus lourd » |
| live preview | aperçu en direct | « aperçu en temps réel » dans l'interface |
| web tool / browser tool / browser | outil web, outil en ligne / outil dans le navigateur / navigateur | |
| bulk scan / batch | Scan par lots / par lots, plusieurs fichiers à la fois | « Scan par lots » = nom de la fonction |
| Chrome extension / Chrome Web Store | extension Chrome / Chrome Web Store | le store garde son nom anglais |
| side panel | panneau latéral | |
| trust badge "rated 5 stars in the Chrome Web Store" | « noté 5 étoiles sur le Chrome Web Store » | sens obligatoire, ne pas modifier |
| free, no signup | gratuit, sans inscription | |
| processed locally / in your browser | traité localement / dans votre navigateur | |
| upload (to a server) / add a file in the UI | envoyer (à un serveur) / importer | « rien n'est envoyé » |
| download / drop a file | télécharger / déposer un fichier (glisser-déposer) | |
| offline / PWA | hors ligne / application web progressive (PWA) | |
| watermark / stamp / signature | filigrane / tampon / signature | |
| e-signature / wet signature | signature électronique / signature manuscrite | |
| metadata | métadonnées | |
| print dialog / print to PDF | boîte de dialogue d'impression / imprimer en PDF | |
| printer / toner | imprimante / toner | |
| phone scanner app | application de scan pour téléphone | sans nom de marque |
| screen reader / accessibility | lecteur d'écran / accessibilité | |
| archive / archiving | archive / archivage | PDF/A inchangé |
| court / agency / e-filing | tribunal / administration (organisme public) / dépôt électronique | les institutions américaines citées gardent leur nom |
| ID documents | pièces d'identité | |
| landlord / HR team / mockup / zine | propriétaire (bailleur) / service RH / maquette / fanzine | |
| spreadsheet | feuille de calcul (tableur) | |
| honest use | usage honnête | encadré d'avertissement |

## 5. Libellés de l'interface (exactement comme dans `messages/fr.json`)

Quand un texte cite un bouton, un curseur ou une option, écrivez-le **exactement** ainsi (même casse), sans
guillemets ou entre « » si la phrase l'exige : « cliquez sur Générer le PDF scanné ».

| Anglais (en.json) | Français (fr.json) | Clé |
|---|---|---|
| Make PDF look scanned | Make PDF look scanned | base.title (marque, non traduite) |
| Make PDF look scanned (H1 d'accueil) | Donner un effet scanné à un PDF | base.landing.headline |
| Scan | Scanner | base.scanTitle, base.nav.scan |
| Bulk Scan | Scan par lots | base.bulkTitle, base.nav.bulk |
| Home | Accueil | base.nav.home |
| Guides | Guides | base.nav.guides |
| Chrome Extension | Extension Chrome | base.chrome.label |
| FREE | GRATUIT | base.chrome.free |
| Convert to Scanned PDF | Convertir en PDF scanné | base.landing.cta |
| Three steps to a scanned PDF | Un PDF scanné en trois étapes | base.landing.stepsTitle |
| Choose a file | Choisissez un fichier | base.landing.step1Title |
| Adjust the scan effect | Réglez l'effet scanné | base.landing.step2Title |
| Export the PDF | Exportez le PDF | base.landing.step3Title |
| Key features | Fonctionnalités clés | base.landing.featuresTitle |
| Language | Langue | base.language |
| Start scanning | Commencer à scanner | actions.navigateToScan |
| Back | Retour | actions.backToIndex |
| Preview | Aperçu | actions.preview |
| Save | Enregistrer | actions.save |
| Generate Scanned PDF | Générer le PDF scanné | actions.generateScannedPDF |
| Generating... | Génération… | actions.generating |
| Download Scanned PDF | Télécharger le PDF scanné | actions.downloadScannedPDF |
| Successfully generated | PDF généré avec succès | actions.generateSuccess |
| Failed to generate: | Échec de la génération : | actions.generateError |
| Add files | Ajouter des fichiers | actions.addFiles |
| Generate scanned PDFs | Générer les PDF scannés | actions.processAll |
| Download all as ZIP | Tout télécharger en ZIP | actions.downloadZip |
| Preparing file… | Préparation du fichier… | actions.converting |
| Queued / Done / Failed | En attente / Terminé / Échec | actions.queued / done / failed |
| Scan Settings | Réglages du scan | settings.settings |
| Noise | Bruit | settings.noise (et settings.attenuate) |
| Blur | Flou | settings.blur |
| Border | Bordure | settings.border.label |
| Yes / No (Border) | Oui / Non | settings.border.true / false |
| Colorspace | Mode couleur | settings.colorspace.label |
| Colorful | Couleur | settings.colorspace.colorful |
| Gray | Niveaux de gris | settings.colorspace.grayscale |
| Rotate | Rotation | settings.rotate |
| Rotate Variance | Variation de rotation | settings.rotateVariance |
| Resolution | Résolution | settings.scale |
| Yellowish | Jaunissement | settings.yellowish (= teinte du papier) |
| Brightness | Luminosité | settings.brightness |
| Contrast | Contraste | settings.contrast |
| Select or drop your file here | Sélectionnez ou déposez votre fichier ici | settings.pdfSelectLabel |
| No file selected | Aucun fichier sélectionné | settings.pdfNoSelectMessage |
| Watermark | Filigrane | settings.extras.watermark |
| Watermark text | Texte du filigrane | settings.extras.watermarkText |
| Watermark image | Image du filigrane | settings.extras.watermarkImage |
| Stamp or signature | Tampon ou signature | settings.extras.stamp |
| Add stamp or signature | Ajouter un tampon ou une signature | settings.extras.stampImage |
| Horizontal position / Vertical position | Position horizontale / Position verticale | settings.extras.stampX / stampY |
| Size | Taille | settings.extras.stampScale |
| PDF metadata | Métadonnées PDF | settings.extras.metadata |
| Title / Author / Subject / Keywords | Titre / Auteur / Objet / Mots-clés | settings.extras.* |
| Producer / Creator | Producteur / Créateur | settings.extras.producer / creator |
| Remove (image) | Supprimer | settings.extras.clearImage |
| Drop your file here / Drop your files here | Déposez votre fichier ici / Déposez vos fichiers ici | upload.dropTitle / dropTitleMany |
| or | ou | upload.or |
| Choose file / Choose files | Choisir un fichier / Choisir des fichiers | upload.choose / chooseMany |
| Choose another file | Choisir un autre fichier | upload.replace |
| Add more files | Ajouter d'autres fichiers | upload.addMore |
| Processed in your browser — nothing is uploaded | Traité dans votre navigateur — rien n'est envoyé | upload.privacy |
| Loaded | Chargé | upload.ready |
| {n} page / {n} pages | {n} page / {n} pages | upload.pages |
| Create scanned PDF / Create {n} scanned PDFs | Créer le PDF scanné / Créer {n} PDF scannés | save.create |
| Your scanned PDF is ready | Votre PDF scanné est prêt | save.readyTitle |
| Download again | Télécharger à nouveau | save.downloadAgain |
| Done — the download has started | Terminé — le téléchargement a commencé | save.downloadStarted |
| Show in preview | Afficher l'aperçu | files.preview |
| Download this scanned PDF | Télécharger ce PDF scanné | files.downloadOne |
| Remove file | Retirer le fichier | files.remove |
| Preparing… / Ready / Scanning… / Scanned | Préparation… / Prêt / Scan en cours… / Scanné | files.status.* |
| Upload / Adjust / Download (steps) | Importer / Régler / Télécharger | steps.upload / adjust / download |
| Upload your files | Importez vos fichiers | steps.uploadTitle |
| Adjust the scan look | Réglez l'aspect scanné | steps.adjustTitle |
| Get your scanned PDF | Récupérez votre PDF scanné | steps.downloadTitle |
| Original / Scanned preview | Original / Aperçu scanné | preview.original / scanned |

Dans le texte courant, on peut écrire les réglages en minuscules quand on parle de la notion (« un peu de bruit
et de flou »), mais avec la majuscule du libellé quand on désigne le contrôle (« le curseur Bruit »,
« passez le Mode couleur sur Niveaux de gris »).

Blog (chrome.json) : « Ouvrir l'outil gratuit → », « Ajouter à Chrome — gratuit → », « Plus de guides → »,
« Guides associés », « Mis à jour : », « {n} min de lecture », « L'équipe {brand} ».

## 6. Fonctions intégrées de macOS / Windows / iOS / Chrome (libellés de l'interface française)

| Anglais | Français |
|---|---|
| macOS Preview | Aperçu |
| Open With → Preview | Ouvrir avec → Aperçu |
| File → Export | Fichier → Exporter… |
| Export as PDF | Exporter au format PDF… |
| Quartz Filter (pop-up menu) | menu local Filtre Quartz |
| Black & White / Gray Tone / Reduce File Size (Quartz filters) | Noir & blanc / Ton de gris / Réduire la taille du fichier |
| File → Print → PDF → Save as PDF (macOS) | Fichier → Imprimer → menu PDF (en bas à gauche) → Enregistrer au format PDF |
| Microsoft Print to PDF | Microsoft Print to PDF (nom inchangé) |
| Printer Properties / Printing preferences (Windows) | Propriétés de l'imprimante / Options d'impression |
| Windows Photos app → Print | application Photos → Imprimer |
| Full page photo (layout) | Photo pleine page |
| Chrome / Edge print: Destination → Save as PDF | Destination → Enregistrer au format PDF |
| Color → Black and white (Chrome/Edge print dialog) | Couleur → Noir et blanc |
| More settings | Plus de paramètres |
| Developer tools → Network tab | Outils de développement → onglet Réseau |
| Downloads folder | dossier Téléchargements |
| Microsoft Word: File → Save As → PDF | Fichier → Enregistrer sous → PDF (*.pdf) |
| Microsoft Word: File → Export | Fichier → Exporter → Créer un document PDF/XPS |
| Google Docs: File → Download → PDF document (.pdf) | Fichier → Télécharger → Document PDF (.pdf) |
| Excel: Page setup | Mise en page |
| iPhone: Settings → Camera → Formats → Most Compatible | Réglages → Appareil photo → Formats → Le plus compatible |
| iPhone Notes → Scan Documents | Notes → Scanner des documents |
| iPhone Files app → Scan Documents | app Fichiers → Scanner des documents |
| Android camera | Appareil photo (Android) |

## 7. Mots-clés et slugs par page

| en-slug | Mot-clé principal FR | Slug localisé | Title |
|---|---|---|---|
| (accueil `/`) | donner un effet scanné à un pdf | — | Donner un effet scanné à un PDF en ligne – gratuit et privé |
| (index du blog) | donner un effet scanné à un pdf | — | Donner un effet scanné à un PDF : guides et réglages |
| how-to-make-a-pdf-look-scanned | faire ressembler un pdf à un scan | faire-ressembler-pdf-a-un-scan | Faire ressembler un PDF à un scan : 6 méthodes gratuites |
| make-a-document-look-scanned | donner un aspect scanné à un document | donner-aspect-scanne-document | Donner un aspect scanné à un document : Word, Docs, photo |
| pdf-to-scanned-pdf | convertir un pdf en pdf scanné | convertir-pdf-en-pdf-scanne | Convertir un PDF en PDF scanné : aplatir et rester lisible |
| what-is-a-scanned-pdf | pdf scanné | pdf-scanne-definition | PDF scanné : définition et différence avec un PDF natif |
| image-to-scanned-pdf | image en pdf scanné | image-en-pdf-scanne | Image en PDF scanné : transformer un JPG ou une photo |
| convert-color-pdf-to-black-and-white | convertir un pdf en noir et blanc | convertir-pdf-en-noir-et-blanc | Convertir un PDF couleur en noir et blanc : 5 méthodes |
| scan-effect | effet scanner | effet-scanner | Effet scanner : ce qui donne à un document l'air scanné |

Variantes secondaires utiles (à répartir naturellement, sans bourrage) : « PDF effet scanné », « effet scanner PDF »,
« rendre un PDF scanné », « simuler un scan », « PDF aspect scanné », « faux scan » (seulement comme expression de
recherche, jamais comme incitation à tromper), « PDF numérisé », « copie scannée », « PDF en niveaux de gris ».

Rappel pour les articles : le mot-clé principal doit figurer au début du `title`, dans le `h1`, dans la première
phrase du `.lead` (tous ses mots doivent y apparaître), dans au moins deux H2, et environ 5 fois dans le corps.
Les liens internes restent en chemins anglais (`/blog/scan-effect/`) ; seul le texte d'ancre est traduit — par
exemple « guide des réglages de l'effet scanner », « image en PDF scanné », « convertir un PDF en PDF scanné »,
« comment convertir un PDF couleur en noir et blanc », « comment faire ressembler un PDF à un scan »,
« qu'est-ce qu'un PDF scanné », « donner un aspect scanné à un document ».
