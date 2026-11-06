# MSP Retail · pilot externe publicatie met Horizzon-figuren

Uitbreiding van de publicatiepipeline (MSP Congestiebeheersing) naar de *Markt- en subprocessen Retailprocessen v13.0*. De tekst komt als Markdown uit het MSP, zonder afbeeldingen. Elke afbeelding wordt een bijlageverwijzing die naar een export van de bijbehorende Horizzon-view wijst. Hoe die koppeling wordt bepaald, staat in **[METHODE.md](METHODE.md)**. Hoe ver de dekking is, staat in **[DEKKING.md](DEKKING.md)**.

## Inhoud

```
bron/paginas/            60 Markdown-pagina's (hoofdstukken; H4 per subproces; elke bijlage apart)
bron/structuur.yml       paginaboom
bron/bijlagen/           bijlagen.yml (register met sleutel, status, Horizzon-view) + PDF-uitsneden als tussenoplossing
exports/                 lijst met Horizzon-exports (SVG) van 6 november 2026, 24 uur geldig
beoordeling.yml          handmatige koppelkeuzes (gaan voor op de automatische regels)
werk/                    MSP-volledig.md (één doorlopend bestand), figuren.json, Horizzon-catalogus, ruwe conversie
scripts/                 bouw_pilot.py (hele keten), msp_naar_md.py, koppel.py, splits_paginas.py, dekking.py, haal_exports.*
```

`bron/` heeft dezelfde vorm als in de congestiebeheer-pilot en kan zo in de repository worden gezet. De bijlagenummers beginnen bij **B1001**, zodat ze niet botsen met B0001–B0999 van die pilot.

## Gebruik

```bash
pip install pymupdf pymupdf4llm pyyaml
python msp_retail/scripts/bouw_pilot.py msp.pdf   # conversie (schrijft naar bron/ in de repo), koppeling, pagina's, dekkingsrapport
```

Horizzon-exports ophalen. Dit moet op een machine die Horizzon kan bereiken, en binnen 24 uur na de export:

```powershell
.\scripts\haal_exports.ps1 .\exports\exports-2026-11-06.tsv
```

Zijn de URL's verlopen, vraag Claude dan opnieuw de views te exporteren via de BizzDesign-MCP. Claude maakt dan een nieuwe `exports-<datum>.tsv`.

Een voorstel bevestigen of een koppeling corrigeren doe je in `beoordeling.yml`:

```yaml
B1053:
  view_id: 50813046-1f91-ef11-8b28-088fc3766e18
  reden: "view toont wijzigen naam; dekt §3.17 voor KA, bevestigd door <naam>"
```

Draai daarna `bouw_pilot.py` opnieuw.
