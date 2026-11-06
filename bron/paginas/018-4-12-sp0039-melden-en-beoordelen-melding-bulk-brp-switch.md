# 4.12 SP0039 Melden en beoordelen ‘melding bulk BRP-switch’


## 4.12.1 Procesafspraken KA

- a. De richtlijn is dat wanneer voor meer dan 50.000 allocatiepunten van kleine aansluitingen een BRP-switch op dezelfde mutatiedatum doorgevoerd dient te worden, daarvoor het proces Bulk BRP-switch wordt toegepast. Indien een leverancier voor minder dan 50.000 allocatiepunten van kleine aansluitingen het proces Bulk BRP-switch wil toepassen, treedt de leverancier hierover in overleg met de systeembeheerder. 

- b. Het is per ‘melding bulk BRP-switch’ alleen mogelijk om allocatiepunten naar één nieuwe balanceringsverantwoordelijke te switchen. 

- c. De systeembeheerder beoordeelt alle individuele BRP-switches in de ‘melding bulk BRPswitch’. De systeembeheerder keurt de BRP-switch voor het betreffende allocatiepunt af als de leverancier die de ‘melding BRP-switch’ indient niet de actuele leverancier is van het betreffende allocatiepunt. Dit is ook het geval indien er geen leverancier in het aansluitingenregister is vermeld op het moment dat de systeembeheerder de ‘melding bulk BRP-switch’ verwerkt. 

- d. Als bij beoordeling van de inhuizing, leverancierswitch, uithuizing of einde levering voor een allocatiepunt dat opgenomen is in een ‘melding bulk BRP-switch’ met een mutatiedatum die gelijk is aan of later ligt dan de mutatiedatum van de inhuizing, leverancierswitch, uithuizing of einde levering, dan wordt de eerder goedgekeurde BRP-switch voor het betreffende allocatiepunt verwijderd en niet uitgevoerd. 

- e. Indien voor allocatiepunten, die opgenomen zijn in een ‘melding bulk BRP-switch’, het verzoek niet kan worden uitgevoerd als gevolg van kruisende berichten, dient de leverancier voor deze individuele allocatiepunten een nieuw verzoek in middels het sub proces melden en beoordelen ‘melding individuele BRP-switch’. 

- f. De leverancier mag bij de bulk BRP-switch een meterstand vaststellen voor het verdelen van het volume voor de reconciliatie; dit is echter niet verplicht. Indien een meterstand wordt vastgesteld bij een bulk BRP-switch dan wordt hiervoor het kenmerk (ProcesID) ‘PV-switch’ gebruikt. 

- g. De systeembeheerders en leveranciers dienen de contactgegevens bekend te maken van het organisatieonderdeel dat belast is met de afhandeling bulk BRP-switches namens de betreffende marktpartij. 

- h. Wanneer op de mutatiedatum van de bulk BRP-switch naast het veld EAN-code balanceringsverantwoordelijke ook één of meer andere velden van de stamgegevens wijzigen vanuit een ander proces, ontvangen de leverancier en de balanceringsverantwoordelijke een stamgegevensbericht. 

- i. De leverancier draagt er zorg voor dat hij een over een leveringsovereenkomst beschikt op grond waarvan hij gerechtigd is om de bulk BRP-switch uit te voeren. 

- j. Voor allocatiepunten van klanten waarvoor een vergunningsplicht geldt is dit reeds geregeld in de eisen van de leveringsvergunning. 

- k. De leverancier draagt er zorg voor dat hij zowel met de oude als de nieuwe balanceringsverantwoordelijke overeenstemming heeft bereikt over het indienen van de bulk BRP-switch en de wijze waarop informatie uitgewisseld wordt. 

- l. De stamgegevens worden in bulk door de systeembeheerder aan de betrokken partijen verzonden. 

## 4.12.2 Procesbeschrijving KA

Bijlage B1107: Subprocesplaat SP0039 KA

1. De leverancier verstuurt tussen 30 en 25 werkdagen voor de gewenste mutatiedatum een aankondiging bulk BRP-switch naar de uitvoeringsorganisatie via een melding dat een ‘melding bulk BRP-switch’ ingediend zal worden. 

2. De uitvoeringsorganisatie ontvangt en verwerkt de aankondiging. 

3. De leverancier verstuurt de ‘melding bulk BRP-switch’ tenminste vijf werkdagen en maximaal 20 werkdagen voor de mutatiedatum, naar de systeembeheerder. 

4. De systeembeheerder beoordeelt de ‘melding bulk BRP-switch’ op de volgende punten: 

   - a. Is de ‘melding bulk BRP-switch’ volledig en syntactisch correct? 

   - b. Ligt de datum van ontvangst tenminste vijf werkdagen en maximaal 20 werkdagen voor de mutatiedatum? 

   - c. Heeft de opgegeven balanceringsverantwoordelijke een volledige erkenning volgens het BRP-register van de betreffende de transmissiesysteembeheerder? 

De systeembeheerder beoordeelt de ‘melding bulk BRP-switch’ voor ieder allocatiepunt in de melding op de volgende punten: 

   - d. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - e. Is de leverancier geregistreerd als actuele leverancier op het allocatiepunt? 

   - f. Is er geen andere nog niet geëffectueerde melding leverancierswitch, inhuizing, uithuizing of einde levering ingediend voor een eerdere of dezelfde mutatiedatum? 

   - g. Is het een allocatiepunt van een kleine aansluiting? 

5. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding bulk BRP-switch’ af, en verstuurt een afwijsbericht naar de leverancier uiterlijk drie werkdagen na ontvangst ‘melding bulk BRP-switch’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. De gewenste mutatiedatum ligt buiten het venster van tenminste vijf werkdagen en maximaal 20 werkdagen in de toekomst. 

   - c. De opgegeven balanceringsverantwoordelijke heeft geen volledige erkenning volgens het BRP-register van de betreffende transmissiesysteembeheerder. 

   - d. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - e. De leverancier staat niet als actuele leverancier geregistreerd op het allocatiepunt. Er is reeds een nog niet geëffectueerde leverancierswitch, inhuizing, uithuizing of einde levering op het allocatiepunt ingediend. 

   - f. Het allocatiepunt is geen allocatiepunt van een kleine aansluiting. 

6. De leverancier ontvangt en verwerkt de afwijzing. 

7. Als alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding bulk BRP-switch’ van de leverancier en verstuurt de systeembeheerder in bulkvorm het bericht GAIN naar de leverancier en nieuwe balanceringsverantwoordelijke, de Stamgegevens na GAIN naar de nieuwe balanceringsverantwoordelijke en het bericht LOSS naar de oude balanceringsverantwoordelijke. De GAIN-, Stamgegevens na GAIN- en LOSSberichten worden uiterlijk 3 werkdagen na ontvangt van de ‘melding bulk BRP-switch’ verstuurd. 

8. De leverancier ontvangt en verwerkt de bulk GAIN-berichten. 

9. De nieuwe balanceringsverantwoordelijke ontvangt en verwerkt de bulk GAIN-berichten en stamgegevens. 

10. De oude balanceringsverantwoordelijke ontvangt en verwerkt de bulk LOSS-berichten. 

11. Voor de allocatiepunten waarvoor de ‘melding bulk BRP-switch’ is goedgekeurd, plant de systeembeheerder de mutatie in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

## 4.12.3 Termijnen KA

- a. De aankondiging dat een ‘melding bulk BRP-switch’ zal worden ingediend bij de systeembeheerder, wordt tussen 30 en 25 werkdagen voor de mutatiedatum door de leverancier gedaan bij de uitvoeringsorganisatie via een melding. 

- b. Een ‘melding bulk BRP-switch’ kan tussen de 20 tot en met vijf werkdagen voor de mutatiedatum door de leverancier worden ingediend. 

- c. Een ‘melding bulk BRP-switch’ wordt uiterlijk drie werkdagen na indienen door de systeembeheerder beoordeeld, waarbij uiterlijk drie werkdagen na ontvangst van de ‘melding bulk BRP-switch’ de betrokken marktpartijen in bulkvorm over het resultaat van de beoordeling geïnformeerd worden (mits er één leverancier op dat moment een bulk BRPswitch heeft ingediend) en waarbij uiterlijk drie werkdagen na ontvangst van de ‘melding bulk BRP-switch’ de nieuwe balanceringsverantwoordelijke in bulkvorm voorzien wordt van de gegevens die deze nodig heeft voor het opstellen van zijn prognoses (mits er één leverancier op dat moment een bulk BRP-switch heeft ingediend). 

## 4.12.4 Gegevensuitwisseling

### Vooraankondiging bulk BRP-switch

De vooraankondiging bulk BRP-switch verloopt via een melding aan de uitvoeringsorganisatie. De vooraankondiging wordt hier verder niet beschreven. 

### Melding bulk BRP-switch

|**Melding bulk BRP-switch**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Mutatiedatum|V|Ja|Ja|1||
|Referentie|O|Ja|Ja|1||
|Proces ID|V|Ja|Ja|1|BRP-switch|
|EAN-code systeembeheerder|V|Ja|Ja|1||
|EAN-code leverancier|V|Ja|Ja|1||
|EAN-code|V|Ja|Ja|1|EAN-code nieuwe balanceringsverantwoordelijke|
|balanceringsverantwoordelijke||||||
|EAN-code allocatiepunt|V|Ja|Ja|n||

### Afwijzing

|**Afwijzing naar leverancier (op**|**het totaal van**|**de bulk BR**|**P-switch**|**melding)**||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|EAN-code leverancier|V|Ja|Ja|1||
|Afwijsreden|V|Ja|Ja|n|Indicatie van de reden waarom de melding is afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>De gewenste mutatiedatum ligt buiten het venster van tenminste<br>vijf werkdagen en maximaal 20 werkdagen in de toekomst.<br>•<br>De opgegeven balanceringsverantwoordelijke heeft geen volledige<br>erkenning<br>volgens<br>het<br>BRP-register<br>van<br>de<br>transmissiesysteembeheerder.|
|Toelichtingafwijsreden|O|Ja|Ja|n||

|**Afwijzing naar leverancier (voor**|**de individue**|**le BRP-swit**|**chmeldi**|**ngen in de**|**bulk BRP-switch)**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|V|Ja|Ja|1||
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|EAN-code leverancier|V|Ja|Ja|1||
|**_Allocatiepunt_**||**_Per EAN_**|**_-code all_**|**_ocatiepun_**|**_t_**|
|EAN-code allocatiepunt|V|Ja|Ja|n||
|Afwijsreden|V|Ja|Ja|n|Indicatie van de reden waarom de melding is afgewezen:<br>•<br>Het allocatiepunt is onbekend in het aansluitingenregister van de<br>systeembeheerder.<br>•<br>De leverancier staat niet als actuele leverancier geregistreerd op de<br>allocatiepunt.<br>•<br>Er is reeds een nog niet geëffectueerde leverancierswitch, inhuizing,<br>uithuizing of einde levering op het allocatiepunt ingediend.<br>•<br>Het allocatiepunt isgeen allocatiepunt van een kleine aansluiting.|
|Toelichting afwijsreden|O|Ja|Ja|n||

### GAIN

|**GAIN naar leverancier**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|V|Ja|Ja|1||
|Proces ID|V|Ja|Ja|1|BRP-switch|
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|Ja|Ja|1||
|EAN-code leverancier|V|Ja|Ja|1||
|EAN-code|V|Ja|Ja|1||
|balanceringsverantwoordelijke||||||
|EAN-code allocatiepunt|V|Ja|Ja|n||

|**GAIN naar nieuwe balanceringsver**|**antwoord**|**elijke**||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|V|Ja|Ja|1||
|Proces ID|V|Ja|Ja|1|BRP-switch|
|Mutatiedatum|V|Ja|Ja|1||
|EAN-code leverancier|V|Ja|Ja|1||
|EAN-code|V|Ja|Ja|1||
|balanceringsverantwoordelijke||||||
|EAN-code allocatiepunt|V|Ja|Ja|n||

### Stamgegevens na GAIN

|**Stamgegevens na GAIN naar nieuwe**|**balanceri**|**ngsvera**|**ntwoord**|**elijke**||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Individuele BRP-switch|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code balanceringsverantwoordelijke|
|Productsoort|V|V|V|Ja|Ja|1|Elektriciteit of gas|
|Systeemgebied|A|A|A|Ja|Ja|1||
|Leveringsrichting|A|A|A|Ja|Ja|1|Alleen verplicht als het allocatiepunt in bedrijf<br>genomen is|
|Wijze van bemeting|V|V|V|Ja|Ja|1|De verschillende manieren van bemeten:<br>•<br>Onbemeten<br>•<br>Jaarlijks<br>•<br>Maandelijks<br>•<br>Telemetrie<br>•<br>Niet continu<br>•<br>Anders bemeten<br>•<br>Onbekend|
|Profielcategorie|A|A|A|Ja|Ja|1|Een in bedrijf zijnde allocatiepunt heeft verplicht een<br>profiel/afnamecategorie, tenzij het een telemetrisch<br>gealloceerde allocatiepunt op een grote aansluiting<br>elektriciteit betreft:<br>•<br>Elektriciteit: E1A, E1B, E1C, E2A, E2B, E3, E4A,<br>OPC<br>•<br>Gas: G1A,G2A,G2C,GGV,GXX,GIS,GIN|
|Fysieke status|V|V|V|Ja|Ja|1|Een indicatie van de fysieke status van een<br>allocatiepunt:<br>•<br>In aanleg<br>•<br>In bedrijf<br>•<br>Uit bedrijf<br>•<br>Verwijderd|
|Leveringsstatus|V|V|V|Ja|Ja|1|Een indicatie van de leveringsstatus van een<br>allocatiepunt, afhankelijk of een leverancier en<br>balanceringsverantwoordelijke zijn geregistreerd op<br>een allocatiepunt, zijnde:<br>•<br>Actief<br>•<br>Inactief|
|Verbruikssegment|V|V|V|Ja|Ja|1|Specificatie<br>van<br>het<br>segment<br>waartoe<br>het<br>allocatiepunt behoort(GA,KA,A1)|
|SJI laag tarief|O|O|O|Nee|Ja|1||
|SJI normaal tarief|O|O|O|Nee|Ja|1||
|SJA laag tarief|O|O|O|Nee|Ja|1||
|SJA normaal tarief|O|O|O|Nee|Ja|1||
|SJV|O|O|Nvt|Ja|Nee|1|Wordt gecommuniceerd middels het veld SJA<br>normaal tarief|
|Allocatiemethode|V|V|V|Ja|Ja|1|Telemetrie, slimmemeterallocatie of geprofileerd|

### LOSS

|**LOSS naar oude balanceringsveran**|**twoordeli**|**jke**||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|V|Ja|Ja|1||
|Proces ID|V|Ja|Ja|1|BRP-switch|
|Mutatiedatum|V|Ja|Ja|1||
|EAN-code|V|Ja|Ja|1||
|balanceringsverantwoordelijke||||||
|EAN-code allocatiepunt|V|Ja|Ja|n||
