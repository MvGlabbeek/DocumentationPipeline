# MSP Congestiebeheersing · pilot externe publicatie

Pilot voor het extern publiceren van architectuurdocumentatie van Het Normo die in Confluence wordt bijgehouden. Dezelfde inhoud wordt langs **twee paden** gepubliceerd, zodat we ze naast elkaar kunnen beoordelen en daarna één kiezen:

| Pad | Weergave | Adres (na eerste publicatie) |
|---|---|---|
| 1. **MkDocs** (Material) | Website met een pagina per Confluence-pagina, navigatie volgens de paginaboom, zoekfunctie | https://mvglabbeek.github.io/DocumentationPipeline/mkdocs/ |
| 2. **ReSpec** | Eén doorlopend document met genummerde hoofdstukken, inhoudsopgave en bijlagen | https://mvglabbeek.github.io/DocumentationPipeline/respec/ |

Startpagina met beide: https://mvglabbeek.github.io/DocumentationPipeline/

## Hoe het werkt

```
Confluence ── per pagina "Exporteren naar Markdown" ──► bron/paginas/*.md
BizzDesign Horizzon ── export met bijlagenummer ──────► bron/bijlagen/B0001 ….svg / .png / .xlsx
                                                            │
                                     scripts/inname.py      │  structuur afleiden → bron/structuur.yml
                                                            ▼
                                                   _build/paginas/ (genormaliseerd)
                                         ┌──────────────────┴──────────────────┐
                                         ▼                                     ▼
                                MkDocs → /mkdocs/                     ReSpec → /respec/
                                                            │
                                                            ▼
                                                      GitHub Pages
```

Elke commit op `main` die iets in `bron/` wijzigt, start de workflow **Publiceer site** (tabblad *Actions*). Het verslag van de inname (structuur, nog ontbrekende bijlagen, meldingen) staat in de samenvatting van de workflowrun.

## Pagina's aanleveren

1. Exporteer in Confluence elke pagina die gepubliceerd moet worden naar Markdown.
2. Upload de bestanden in `bron/paginas/` (op github.com: *Add file → Upload files*) en commit naar `main`.

- **Bestandsnamen maken niet uit.** De eerste kop (`# Titel`) van het bestand is de titel en de identiteit van de pagina.
- **Dezelfde pagina opnieuw exporteren?** Upload hem gewoon. Staat dezelfde titel er meerdere keren (`Pagina.md`, `Pagina-1.md`, `Pagina-2.md`), dan telt het bestand met het hoogste volgnummer (de laatste download). Oude versies mag je weggooien.
- **Niet publiceren** = niet uploaden. Een pagina verwijderen uit de publicatie = het bestand verwijderen.

### De paginaboom

Een Markdown-export bevat niet waar de pagina in Confluence hing. De structuur staat daarom in **`bron/structuur.yml`**:

```yaml
- "MSP Congestiebeheersing":
    - "Procesdomein: Muteren"  # nog geen bestand
    - "Procesdomein: Handelen"
    - "Procesdomein: Verrekenen":
        - "Valideren transport (grenswaarde)"  # nog geen bestand
```

Inspringing is subpagina, de volgorde is de volgorde in de publicatie. Je hoeft dit bestand niet zelf te maken: bij elke inname worden **nieuwe pagina's automatisch geplaatst** onder de pagina die ernaar verwijst, op de plek van die verwijzing. Een verwijzing is een Confluence-link naar de pagina, of een opsommingsitem met (het laatste deel van) de titel, zoals `3. Handelen` voor *Procesdomein: Handelen*. De workflow commit de aangevulde structuur terug.

- Klopt een plaatsing niet? Verplaats de regel in `structuur.yml`; wat erin staat, wordt niet meer verschoven.
- Pagina's waarnaar gelinkt wordt maar die nog niet zijn aangeleverd, staan erin met `# nog geen bestand`. Upload je ze later, dan landen ze vanzelf op de goede plek.
- Zet titels tussen aanhalingstekens; een pagina met subpagina's krijgt een dubbele punt.

### Wat de inname met de tekst doet

- De titelkop gaat naar de paginatitel; de koppen in de pagina schuiven een niveau op.
- Links naar Confluence-pagina's die ook gepubliceerd worden, worden links binnen de publicatie. Links naar Confluence-pagina's die niet gepubliceerd worden, worden gewone tekst (externe lezers kunnen Confluence niet in).
- Een opsommingsitem dat precies een gepubliceerde subpagina noemt, wordt een link naar die pagina.
- Overige links (bijv. naar energiedatawijzer.nl) blijven ongewijzigd.

## Bijlagen: diagrammen, afbeeldingen en tabellen

Afbeeldingen en tabellen komen niet uit Confluence maar worden **los aangeleverd met een vast nummer**: `B0001`, `B0002`, … Het nummer zegt niets over de plaats in de tekst en wordt nooit hergebruikt.

**Bestand:** exporteer uit BizzDesign Horizzon en zet het nummer vooraan in de bestandsnaam:

| Soort | Voorbeeld | Formaten |
|---|---|---|
| diagram/afbeelding | `B0002 Hoofdprocesmodel.svg` of `B0002.png` | `.svg` (voorkeur, scherp op elk formaat), `.png`, `.webp`, `.jpg` |
| tabel | `B0010 Processen per domein.xlsx` | `.xlsx` (eerste tabblad), `.csv` (`;` of `,`), `.md` |
| document | `B0020.pdf` | `.pdf`, `.docx`, `.pptx` |

Upload in `bron/bijlagen/` en commit. Wat na het nummer in de bestandsnaam staat, wordt de titel (tenzij het register een titel geeft). Vervangen = een nieuw bestand met hetzelfde nummer uploaden. Op de site heet het bestand altijd `B0002.svg`, dus spaties in de naam zijn geen probleem.

**Plaats in de tekst:** kies per bijlage een van twee manieren.

1. **In Confluence** een eigen regel onder of boven de afbeelding: `Bijlage B0002` of `Bijlage B0002: Hoofdprocesmodel`. Na de export wordt die regel de bijlage. In een zin wordt *bijlage B0002* een verwijzing.
2. **In het register** `bron/bijlagen/bijlagen.yml`, zonder iets in Confluence te veranderen:

   ```yaml
   B0002:
     titel: Hoofdprocesmodel congestiebeheersing
     pagina: MSP Congestiebeheersing        # titel van de pagina
     na: Onderstaand hoofdprocesmodel maakt  # stukje tekst uit de alinea waarna de bijlage komt
     horizzon: https://…                     # optioneel: link naar de view in Horizzon
   ```

Zolang het bestand er nog niet is, toont de publicatie *"Bijlage B0002 volgt"* en noemt het workflowverslag welke bijlagen ontbreken. Beide publicaties hebben een **Overzicht bijlagen** met alle bijlagen en waar ze gebruikt worden.

Tip: zet het bijlagenummer ook in de naam of een eigenschap van de view in BizzDesign (bijv. *B0002 Hoofdprocesmodel*). Dan is de koppeling vanuit beide kanten te vinden en weet iedereen bij een volgende export welk nummer erbij hoort.

> De exportmogelijkheden (SVG, PNG, Excel) en de menu-namen verschillen per Horizzon-versie en licentie; controleer ze in jullie omgeving.

## Eenmalige instellingen

1. *Settings → Pages → Build and deployment → Source:* **GitHub Actions**.
2. *Settings → Actions → General → Workflow permissions:* **Read and write permissions**, zodat de workflow de aangevulde `structuur.yml` kan terugcommitten. Kan dat niet (organisatiebeleid), dan werkt de publicatie wel, maar moet je nieuwe pagina's zelf in `structuur.yml` zetten.

## Lokaal bekijken

```bash
pip install -r requirements.txt
python scripts/bouw_site.py              # inname + beide paden in _site/
python -m http.server -d _site 8000      # http://localhost:8000
```

`python scripts/inname.py --controle` toont de afgeleide structuur en meldingen zonder `structuur.yml` te wijzigen.

## Vergelijking voor het besluit

| | MkDocs (Material) | ReSpec |
|---|---|---|
| Vorm | website, pagina per onderwerp | één document, genummerd |
| Navigatie | menu volgens paginaboom, zoekfunctie, vorige/volgende | inhoudsopgave, ankers, printbaar als één geheel |
| Past bij | naslag, lezers die gericht zoeken | vastgestelde versies, citeren ("zie 3.2"), standaarden-achtige publicaties |
| Versies | per publicatie; versiebeheer apart in te richten | datum en versie in de kop; *latest version*-link |
| Verwijzen naar bijlagen | link naar Overzicht bijlagen | anker binnen het document |
| Techniek | wordt bij het bouwen omgezet naar HTML | wordt in de browser opgemaakt (JavaScript van w3.org) |
| Aandachtspunt | Material for MkDocs waarschuwt dat het aangekondigde MkDocs 2.0 niet compatibel is; deze pilot gebruikt bewust MkDocs 1.x | beperkte huisstijl; voor Nederlandse publicaties bestaat een NL-profiel van ReSpec (Geonovum/Logius) |

Na het besluit: haal het andere pad weg onder `paden:` in `publicatie.yml`.

## Mappen

```
bron/paginas/             Markdown-exports uit Confluence (één bestand per pagina)
bron/structuur.yml        paginaboom (wordt automatisch aangevuld)
bron/bijlagen/            B0001 ….* uit BizzDesign en bijlagen.yml (optioneel register)
publicatie.yml            titel, redacteuren, status, te bouwen paden
mkdocs.base.yml           basisinstellingen MkDocs
respec/                   ReSpec-sjabloon
site_root/                sjabloon startpagina
scripts/                  inname.py, build_mkdocs.py, build_respec.py, bouw_site.py, gemeen.py
.github/workflows/        publiceer.yml
```
