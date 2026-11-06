# Methode: van MSP-figuur naar de juiste Horizzon-view

*Pilot MSP Retail v13.0 · Het Normo · november 2026 · werkdocument*

## 1. Het probleem

Het MSP is een Word-document met 193 afbeeldingen zonder bijschrift of nummer. Dezelfde procesplaten bestaan (deels) als views in BizzDesign Horizzon, maar niets in het MSP zegt *welke* view bij *welke* afbeelding hoort. Een los volgnummer (B0001, B0002, …) lost dat niet op: het nummer moet dan aan beide kanten handmatig worden bijgehouden en zegt inhoudelijk niets.

## 2. Principe: de sleutel komt uit het MSP zelf

Elke figuur krijgt een **figuursleutel** die je afleidt uit de plek in het MSP: het paragraafnummer of de SP-code plus de variant (KA/GA). Die sleutel bestaat al aan beide kanten. In het MSP staat hij in de kop, in Horizzon in de viewnaam (impliciet nu, expliciet in het doelbeeld). De sleutel is het *ankerpunt*. Het bijlagenummer (B1001, …) blijft de *bestandsidentiteit* voor de publicatiepipeline, zodat die ongewijzigd blijft werken.

| Soort figuur | Sleutel | Afgeleid uit | Horizzon-bron |
|---|---|---|---|
| Marktprocesplaat (H3) | `MP-3.2.1` | MSP §3.2.1 | ArchiMate-view `02.1 Inhuizing KA` in *03A Views Markt- en subprocessen Retail* |
| Tijdlijn (H3) | `TL-3.2.1`, `TL-3.2.1-2` | idem, 2e, 3e… afbeelding in de paragraaf | nu als plaatje *ín* de marktprocesview |
| Subprocesplaat (H4) | `SP0004-KA`, `SP0015-GA-3` | SP-code + variant + volgnummer | BPMN-collaboration-view `SP0004 …` |
| Subproces zonder code | `PB-4.20-KA` | paragraafnummer | geen; eerst SP-code toekennen |
| Legenda / toelichting | `LEG-3`, `FIG-<§>-n` | paragraaf of bijlage | geen |

De sleutel is reproduceerbaar: dezelfde MSP-versie levert dezelfde sleutels op. Komt er in een nieuwe MSP-versie een paragraaf bij, dan krijgen alleen de nieuwe figuren een nieuwe sleutel en een nieuw bijlagenummer.

## 3. Koppelregels

`scripts/koppel.py` past de regels in deze volgorde toe. De eerste regel die raakt, telt.

| Regel | Wanneer | Uitkomst |
|---|---|---|
| **R0 (doelbeeld)** | viewnaam of eigenschap *MSP-sleutel* = sleutel | `gekoppeld`, deterministisch |
| **R1** | `MP-3.N.M` en er is een view met nummer `NN.M` | `gekoppeld` als nummer, KA/GA en naam (≥ 0,3 overlap) kloppen, anders `voorstel` |
| **R2** | `SPxxxx-…` en er is een BPMN-view die met `SPxxxx` begint | `gekoppeld` (of `voorstel` als het MSP meerdere platen voor die code heeft) |
| **R2b** | wel een ArchiMate-procesobject `SPxxxx`, geen BPMN-view | `view ontbreekt` + link naar het procesobject |
| **R3** | tijdlijn, legenda, toelichting | `geen Horizzon-bron`: tijdelijk de uitsnede uit de PDF |
| **Handmatig** | regel in `beoordeling.yml` | gaat altijd voor; met reden |

`voorstel` betekent dat een mens moet bevestigen. Dat gebeurt met een regel in `beoordeling.yml` (`view_id` + `reden`), niet door het register met de hand te wijzigen. Zo blijft elke keuze herleidbaar.

## 4. Resultaat van de pilot

| Soort | Gekoppeld | Voorstel | View ontbreekt | Geen bron | Totaal |
|---|---:|---:|---:|---:|---:|
| Marktprocesplaten | 28 | 5 | 6 | – | 39 |
| Subprocesplaten (BPMN) | 3 | – | 84 | – | 87 |
| Tijdlijnen | – | – | – | 43 | 43 |
| Overig (legenda, bijlagen) | – | – | – | 24 | 24 |
| **Totaal** | **31** | **5** | **90** | **67** | **193** |

- **Marktprocessen zijn vrijwel sluitend.** De nummering van de views volgt het MSP (§3.N.M = view NN.M). Er zijn vijf voorstellen, alle vijf door terminologieverschuiving sinds MSP v6. Voorbeelden: §3.17 *Wijzigen gegevens aangeslotene* tegenover view *17. Wijzigen naam Kleine aansluiting*, en §3.15 *Mutatie van de meetinrichting* tegenover *15. Metermutatie*. Voor §3.28 en §3.30–3.34 bestaat nog geen view.
- **Subprocessen zijn het eigenlijke gat.** Alleen SP0011, SP0043 en SP0048 hebben een BPMN-view. Voor 53 van de 84 ontbrekende platen staat het SP-procesobject wel in Horizzon. Daar is dus alleen de view nog nodig.
- **Tijdlijnen** zitten nu als plaatje (*ViewGraphic*) in de marktprocesviews. Een export van de view levert procesplaat en tijdlijn samen, terwijl het MSP ze als aparte figuren toont.

## 5. Bevindingen die de methode raken

1. **Werkviews bevatten interne notities.** View *17. Wijzigen naam KA* bevat de notitie "In het MSP is het niet duidelijk of het alleen KV of ook GV betreft", en in het model staan meer vraag-notities over SP0004/SP0015. Een export publiceert die notities mee. Exporteer daarom niet uit werkviews.
2. **De MSP heeft dubbele en ontbrekende codes.** §4.36 en §4.37 hebben allebei SP0072. §4.20 en §4.39–4.43 hebben geen SP-code. Paragrafen §4.6, §4.10, §4.15 en §4.29 bundelen meerdere codes. De sleutel maakt dit zichtbaar; de MSP-redactie moet het oplossen.
3. **Eén view, meerdere figuren.** De BPMN-view SP0048 is één plaat, het MSP ook. SP0015 heeft in het MSP 11 deelplaten. Daar is één view per deelproces nodig (`SP0015-KA`, `SP0015-KA-2`, …), anders klopt de koppeling niet.
4. **De Doelbinding-matrix (bijlage, p. 271) is een tabel in afbeeldingsvorm.** De tekst ervan staat nu alleen in figuur B1186. Advies: omzetten naar een echte tabel in de tekst.

## 6. Afspraken om het sluitend te maken (doelbeeld)

**Horizzon-kant**

1. Maak een map **03P Publicatie MSP Retail**. Elke figuur die het MSP toont, krijgt daar een eigen *publicatieview*: geen werknotities, vaste stijl en legenda.
2. De viewnaam begint met de sleutel: `MP-3.2.1 Inhuizing KA`, `SP0004-KA Indienen en beoordelen melding inhuizing`. Zet daarnaast de eigenschappen **MSP-sleutel** en **Bijlagenummer** (B10xx) op de view. Daarmee werkt regel R0 en is de koppeling vanuit beide kanten vindbaar.
3. Een publicatieview mag werkviews hergebruiken (dezelfde objecten), maar verwijst nooit naar notities.
4. Tijdlijnen worden een eigen view (`TL-3.2.1 …`), of blijven bewust een bestand buiten Horizzon. Kies één van beide en leg dat vast.

**MSP-kant (Word/Confluence)**

5. Zet onder elke afbeelding een regel `Bijlage B10xx`. De pipeline herkent die regel al.
6. Elke paragraaf in H4 krijgt precies één SP-code. Gebundelde paragrafen splitsen of per plaat de code noemen.

**Proces**

7. Het register (`bijlagen.yml`) is de enige plek waar de koppeling staat. Het wordt gegenereerd en handmatige keuzes staan in `beoordeling.yml`.
8. Elke run levert `DEKKING.md`. Een publicatie is pas *vast te stellen* als er geen `voorstel` meer openstaat. `view ontbreekt` mag alleen als bewuste tussenoplossing met de PDF-uitsnede.
9. Bij een nieuwe MSP-versie draait de keten opnieuw. Gewijzigde paragrafen geven automatisch nieuwe of vervallen sleutels, en het rapport laat zien welke views bijgewerkt moeten worden. Zo blijven MSP-versie en view-versie in de pas.

## 7. Link naar de view

Elke figuur met een gekoppelde of voorgestelde view krijgt in `bijlagen.yml` het veld `horizzon` met de link naar de view (`https://mffbas.horizzon.cloud/sites/<site>/views/<view-id>`). De publicatiepipeline zet die link al in het onderschrift onder de plaat (*bron in BizzDesign Horizzon*), dus de pagina's in `bron/paginas` hoeven hem niet zelf te bevatten. In het doorlopende `MSP-volledig.md` staat de link direct onder de plaat. Bij een voorstel staat erbij dat de koppeling nog bevestigd moet worden.

Figuren zonder view krijgen geen `horizzon`-link. Als er wel een SP-procesobject is, staat die link in `horizzon_procesobject_link`; die wordt niet gepubliceerd. Zo staat "bron in Horizzon" nooit onder een PDF-uitsnede.

De link vraagt om een Horizzon-account, ook al staat de site op *publiek toegankelijk*. Voor externe lezers is de link dus alleen informatief, tenzij Het Normo de site echt anoniem openstelt.

## 8. Technische beperkingen in deze pilot

- De MCP-export geeft een download-URL die **24 uur geldig** is. Downloaden kan alleen vanaf een machine die `mcp.horizzon.cloud` kan bereiken. Voor de pilot gebeurt dat met `scripts/haal_exports.ps1` op een eigen machine. Voor een automatische GitHub-workflow is een Horizzon-API-token nodig in plaats van de MCP.
- Werkende route op 6 november: de ingebouwde browser van de Claude-desktopapp haalt alle exports op en downloadt ze als één bundel, waarna een script ze uitpakt tot losse SVG's. De SVG's zijn vectoren zonder externe afbeeldingen. In drie ervan (B1005, B1043, B1053) staan werknotities uit Horizzon; die moeten uit de view voordat ze gepubliceerd worden (zie bevinding 1).
- De MCP kan geen views of eigenschappen aanmaken. De publicatieviews (punt 6) maak je in Enterprise Studio.
- De conversie gebruikt de PDF. Opmaak blijft grotendeels behouden (332 van 332 genummerde koppen, 2.125 tabelregels). Onderstreping komt als `<u>`-HTML mee.
