# MSP CB-architectuur · pilot externe publicatie

Pilot voor het extern publiceren van de architectuurdocumentatie van Het Normo, die in Confluence wordt bijgehouden. Dezelfde inhoud wordt langs **twee paden** gepubliceerd, zodat we ze naast elkaar kunnen beoordelen en daarna één kiezen:

| Pad | Weergave | Adres (na eerste publicatie) |
|---|---|---|
| 1. **MkDocs** (Material) | Website met een pagina per Confluence-pagina, navigatie volgens de paginaboom, zoekfunctie | https://hetnormo.github.io/MSP_CB_Pilot/mkdocs/ |
| 2. **ReSpec** | Eén doorlopend document met genummerde secties, inhoudsopgave en bijlagen | https://hetnormo.github.io/MSP_CB_Pilot/respec/ |

Startpagina met beide: https://hetnormo.github.io/MSP_CB_Pilot/

De opzet volgt de pipeline van de [DT Verkenner](https://github.com/MvGlabbeek/dtverkenner): bronbestanden in `bron/`, één workflow die bouwt en via GitHub Pages publiceert.

## Hoe het werkt

```
Confluence-space ──export (HTML, zip)──► bron/confluence-export/
                                              │  scripts/confluence_naar_md.py
                                              ▼
                       bron/paginas/   Markdown, één bestand per pagina, mappen volgen de paginaboom
                       bron/bijlagen/  B0001.svg, B0002.png, B0003.csv ... + bijlagen.yml (register)
                                              │  scripts/bouw_site.py
                          ┌───────────────────┴───────────────────┐
                          ▼                                       ▼
                MkDocs  → _site/mkdocs/                 ReSpec → _site/respec/
                                              │
                                              ▼
                                       GitHub Pages
```

**Confluence blijft tijdens de pilot de bron.** Pas de tekst daar aan en exporteer opnieuw; `bron/paginas/` wordt bij elke conversie opnieuw opgebouwd. De bijlagen en hun nummers blijven wel bewaard (zie hieronder). Kiezen we later voor Markdown als bron, dan stoppen we met converteren en wordt `bron/paginas/` het werkdocument.

## Bijlagen: diagrammen, afbeeldingen en tabellen

Alles wat geen lopende tekst is, wordt een **losse, uniek genummerde bijlage**: `B0001`, `B0002`, ... In de tekst staat alleen een verwijzing:

| In de Markdown | Betekenis |
|---|---|
| `[[bijlage:B0007]]` (alleen op een regel) | toon bijlage B0007 hier, met onderschrift en links |
| `[[zie:B0007]]` (in een zin) | verwijzing naar bijlage B0007 |

Regels:

- Het bestand heet naar het nummer en staat in `bron/bijlagen/`: `B0007.svg`, `B0012.csv`. Het nummer zegt niets over de plaats in de tekst. Een nieuwe bijlage krijgt het eerstvolgende vrije nummer; een nummer wordt nooit hergebruikt.
- Toegestane formaten: diagram/afbeelding `.svg` (voorkeur) `.png` `.webp` `.jpg`; tabel `.csv` `.xlsx` (eerste tabblad) `.md`; document `.pdf` `.docx` `.pptx`. Staan er meerdere bestanden met hetzelfde nummer, dan wint de eerste in deze volgorde.
- Het register `bron/bijlagen/bijlagen.yml` bevat per nummer `titel`, `soort` (diagram, afbeelding, tabel, document), `bron` (confluence, bizzdesign, handmatig), `horizzon` (link naar de view) en optioneel `toelichting`. `sleutel` en `confluence` beheert de converter.
- Beide publicaties hebben een **Overzicht bijlagen** met alle bijlagen, waar ze gebruikt worden en de link naar BizzDesign Horizzon.

Wat de converter van Confluence-inhoud maakt:

| In Confluence | Wordt |
|---|---|
| Ingevoegde afbeelding (ook draw.io/Gliffy, als png in de export) | bijlage, bestand uit de export overgenomen |
| Tabel | bijlage als `.csv` (eenvoudige tabel) of `.md` (samengevoegde cellen, lijsten, links) |
| Iframe/macro of losse link naar BizzDesign Horizzon | bijlage van soort *diagram* met de Horizzon-link, **nog te exporteren** |
| Link naar Horizzon midden in een zin | linktekst + `[[zie:...]]` |
| Bijlage-bestand (pdf, xlsx ...) waarnaar gelinkt wordt | bijlage van soort *document* of *tabel* |
| Link naar andere pagina in de space (ook naar een kop) | relatieve Markdown-link |
| Info/let op/waarschuwing-macro | citaatblok met label |

Nummers zijn stabiel: bij een volgende export herkent de converter elke bijlage aan haar sleutel (Confluence-bijlage-id, Horizzon-URL of tabelkop) en hergebruikt het nummer.

### Werkinstructie: diagram of tabel uit BizzDesign Horizzon

1. Na een conversie toont de workflow (en de site, met een gele melding) welke diagrammen **nog te exporteren** zijn, met hun nummer en Horizzon-link.
2. Open de view in Horizzon en exporteer het diagram als afbeelding, bij voorkeur **SVG** (scherp op elk formaat), anders PNG.
3. Noem het bestand naar het bijlagenummer, bijv. `B0003.svg`. Tip: zet het nummer ook in de naam of een eigenschap van de view in BizzDesign (bijv. *B0003 Capabilitykaart*), dan is de koppeling vanuit beide kanten vindbaar.
4. Tabellen (catalogi, matrices) exporteer je naar Excel of CSV en noem je `B0012.xlsx` of `B0012.csv`.
5. Upload in `bron/bijlagen/` (op github.com: *Add file → Upload files*) en commit naar `main`. De site wordt opnieuw gebouwd.
6. Vervangen gaat hetzelfde: upload een nieuw bestand met hetzelfde nummer. Een andere beeldverhouding is geen probleem.

Een bestand dat uit BizzDesign komt wordt door een nieuwe conversie **niet overschreven**: de converter vernieuwt een bestand alleen als het register `bron: confluence` aangeeft en de extensie gelijk is. Een afbeelding uit Confluence vervangen door een BizzDesign-export kan dus door `B0002.svg` te uploaden (en `B0002.png` te verwijderen), of door `bron: bizzdesign` te zetten.

> De exportmogelijkheden (SVG, PNG, Excel) en de naam van de menu-opties verschillen per Horizzon-versie en licentie; controleer ze in jullie omgeving. Automatisch exporteren via de Horizzon-API is een mogelijke vervolgstap.

## Publiceren

### Eenmalig

1. *Settings → Pages → Build and deployment → Source:* **GitHub Actions**.
2. *Settings → Actions → General → Workflow permissions*: de conversieworkflow moet kunnen committen. Staat dit op alleen-lezen en kan dat niet anders (organisatiebeleid), gebruik dan route B.

### Confluence exporteren

In de space: *Space-instellingen → Exporteer space → HTML* (Engelse interface: *Space settings → Export space → HTML*). Kies *Aangepast* om alleen de te publiceren pagina's mee te nemen. Download de zip.

Pagina's met een van de labels uit `publicatie.yml` (`intern`, `niet-publiceren`, `concept`) worden samen met hun subpagina's **niet omgezet**; ze komen dus ook niet in de repository. Links ernaartoe worden gewone tekst.

### Route A: via github.com

Upload de zip in `bron/confluence-export/` en commit naar `main`. De workflow *Converteer Confluence-export* zet hem om, commit `bron/paginas/` en `bron/bijlagen/`, haalt de zip weer weg en start *Publiceer site*. Het verslag (aantal pagina's, nog te exporteren diagrammen, waarschuwingen) staat in de samenvatting van de workflowrun.

Let op: is de repository openbaar, dan blijft de zip in de git-geschiedenis zichtbaar. Gebruik route A alleen met een export die geen interne pagina's bevat (kies *Aangepast* bij exporteren), of gebruik route B.

### Route B: lokaal

```bash
pip install -r requirements.txt          # en pandoc installeren
python scripts/confluence_naar_md.py ~/Downloads/Confluence-space-export.zip
python scripts/bouw_site.py              # bouwt _site/ met beide paden
python -m http.server -d _site 8000      # bekijk op http://localhost:8000
git add bron && git commit -m "Nieuwe export" && git push
```

Proberen zonder eigen export: `voorbeeld/confluence-export-voorbeeld.zip` is een kleine nagebootste export met alle situaties (Horizzon-iframe en -links, afbeeldingen, tabellen, pdf, interne links, een pagina met label *intern*).

## Vergelijking voor het besluit

| | MkDocs (Material) | ReSpec |
|---|---|---|
| Vorm | website, pagina per onderwerp | één document, genummerd |
| Navigatie | menu volgens paginaboom, zoekfunctie, vorige/volgende | inhoudsopgave, ankers, printbaar als één geheel |
| Past bij | naslag, lezers die gericht zoeken | vastgestelde versies, citeren ("zie 3.2"), standaarden-achtige publicaties |
| Versies | per publicatie; versiebeheer apart in te richten | datum en versie in de kop; *latest version*-link |
| Verwijzen naar bijlagen | link naar Overzicht bijlagen | anker binnen het document |
| Techniek | wordt bij het bouwen omgezet naar HTML | wordt in de browser opgemaakt (JavaScript van w3.org) |
| Aandachtspunt | Material-for-MkDocs waarschuwt dat het aangekondigde MkDocs 2.0 niet compatibel is; deze pilot gebruikt bewust MkDocs 1.x | huisstijl beperkt; voor Nederlandse publicaties bestaat een NL-profiel van ReSpec (Geonovum/Logius) |

## Bekende beperkingen

- De converter is gebouwd voor de standaard HTML-export van Confluence en getest op een nagebootste export. Controleer de eerste echte export goed; de workflow meldt afbeeldingen die niet gevonden worden en links die verdwijnen.
- Dynamische macro's (Jira, paginaboom, 'onlangs bijgewerkt') hebben geen statische inhoud en vallen weg; draw.io- en Gliffy-diagrammen komen als afbeelding mee.
- Links naar pagina's in andere spaces worden gewone tekst; links naar Confluence zelf blijven staan maar zijn voor externe lezers niet bereikbaar (de workflow meldt ze).
- Diagrammen uit Horizzon zijn pas zichtbaar na export; tot die tijd toont de site een melding met de link (die alleen werkt met Horizzon-toegang).

## Mappen

```
bron/confluence-export/   zip van de Confluence-export (tijdelijk)
bron/paginas/             Markdown-pagina's (gegenereerd tijdens de pilot)
bron/bijlagen/            B0001.* ... en bijlagen.yml
publicatie.yml            titel, redacteuren, status, te bouwen paden, labels, tabeldrempel
mkdocs.base.yml           basisinstellingen MkDocs
respec/                   ReSpec-sjabloon
site_root/                sjabloon startpagina
scripts/                  converter en bouwscripts
voorbeeld/                voorbeeld-export en het script dat hem maakt
.github/workflows/        converteer.yml, publiceer.yml
```

Na het besluit: haal het andere pad weg onder `paden:` in `publicatie.yml`.
