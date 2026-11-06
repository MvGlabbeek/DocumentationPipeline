# 4.11 SP0008 Indienen en beoordelen ‘melding individuele BRP-switch’


## 4.11.1 Procesafspraken KA

- a. Het geautomatiseerd verwerken van zogenaamde bulk BRP-switches valt buiten scope van dit subproces en is beschreven in indienen en beoordelen ‘melding bulk BRP-switch’. 

- b. Indien voor meer dan 50.000 allocatiepunten van kleine aansluitingen (ongeacht het aantal systeembeheerders in het verzoek) een BRP-switch op dezelfde mutatiedatum doorgevoerd dient te worden, dient daarvoor het subproces Indienen en beoordelen ‘melding bulk BRPswitch’ te worden toegepast. Indien een leverancier voor minder dan 50.000 allocatiepunten van kleine aansluitingen een bulk BRP-switch wil toepassen, treedt de leverancier hierover in overleg met de systeembeheerder. 

- c. Voor allocatiepunten op kleine aansluitingen mag een ‘melding individuele BRP-switch’ alleen worden ingediend door de actuele leverancier op het allocatiepunt. ‘Meldingen individuele BRP-switch’ van niet-actuele leveranciers worden door de systeembeheerder afgewezen (dit is ook het geval indien geen leverancier in het aansluitingenregister is vermeld op het moment van indienen van de individuele BRP-switch). 

- d. De leverancier draagt er zorg voor dat hij over een leveringsovereenkomst beschikt op grond waarvan hij gerechtigd is om de BRP-switch uit te voeren. Voor allocatiepunten van klanten waarvoor een vergunningsplicht geldt, is dit reeds geregeld in de eisen van de leveringsvergunning. 

- e. Een ingeplande individuele BRP-switch wordt niet geeffectueerd als een inhuizing, leverancierswitch, uithuizing of einde levering wordt ingediend met een eerdere of gelijke mutatiedatum. 

- f. De leverancier mag bij de individuele BRP-switch een meterstand vaststellen voor het verdelen van het volume voor de reconciliatie; dit is echter niet verplicht. Indien een meterstand wordt vastgesteld bij een individuele BRP-switch dan wordt hiervoor het kenmerk ’PV-switch’ gebruikt. 

## 4.11.2 Procesbeschrijving KA

Bijlage B1105: Subprocesplaat SP0008 KA

1. De leverancier verstuurt de ‘melding individuele BRP-switch’, één werkdag voor de mutatiedatum, naar de systeembeheerder. 

Een uitzondering wordt gemaakt voor allocatiepunten van kleine aansluitingen die vallen onder artikel 2.17, tweede lid, onderdeel c van de Energiewet, waarvoor een ‘melding individuele BRP-switch’ kan worden ingediend in de periode van 20 werkdagen tot en met één werkdag voor de gewenste mutatiedatum. 

2. De systeembeheerder beoordeelt de ‘melding individuele BRP-switch’ op de volgende punten: 

   - a. Is de ‘melding individuele BRP-switch’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de leverancier de actuele leverancier op het allocatiepunt? 

   - d. Ligt datum van indienen tenminste één werkdag en maximaal 20 werkdagen voor de mutatiedatum? 

   - e. Heeft de opgegeven balanceringsverantwoordelijke een erkenning volgens het BRPregister van de betreffende transmissiesysteembeheerder. 

   - f. Is er geen andere nog niet geëffectueerde melding leverancierswitch, inhuizing, uithuizing of einde levering ingediend voor een eerdere of dezelfde mutatiedatum? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding individuele BRP-switch’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst ‘melding individuele BRP-switch’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De leverancier staat niet als actuele leverancier geregistreerd op het allocatiepunt. 

   - d. De gewenste mutatiedatum ligt buiten het venster van tenminste één werkdag en maximaal 20 werkdagen in de toekomst. 

   - e. De opgegeven balanceringsverantwoordelijke heeft geen erkenning volgens het BRPregister van de betreffende transmissiesysteembeheerder. 

   - f. Er is reeds een andere nog niet geëffectueerde melding van een leverancierswitch, inhuizing, uithuizing of einde levering ingediend voor een eerdere of dezelfde mutatiedatum. 

4. De leverancier verwerkt de afwijzing. 

5. Als alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding individuele BRP-switch’ van de leverancier en verstuurt de systeembeheerder het bericht GAIN naar de leverancier en de nieuwe balanceringsverantwoordelijke, de Stamgegevens na GAIN naar de nieuwe balanceringsverantwoordelijke en het bericht LOSS naar de oude balanceringsverantwoordelijke. De GAIN-, Stamgegevens na GAIN- en LOSSberichten worden uiterlijk de werkdag na ontvangst van de ‘melding individuele BRP-switch’ verstuurt. 

6. De leverancier ontvangt en verwerkt het bericht GAIN. 

7. De nieuwe balanceringsverantwoordelijke ontvangt en verwerkt het bericht GAIN. 

8. De oude balanceringsverantwoordelijke ontvangt en verwerkt het bericht LOSS. 

9. De systeembeheerder plant de ‘melding BRP-switch’ van de leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

## 4.11.3 Termijnen KA

- a. De termijn voor het indienen van een BRP-switch voor een allocatiepunt op een kleine aansluiting is één werkdag voor de mutatiedatum. Een uitzondering wordt gemaakt voor allocatiepunten op kleine aansluitingen die vallen onder artikel 2.17, tweede lid, onderdeel c van de Energiewet, waarvoor een BRP-switch kan worden ingediend in de periode van 20 werkdagen tot en met één werkdag voor de gewenste mutatiedatum. 

- b. Een ‘melding BRP-switch’ wordt uiterlijk één werkdag na ontvangst door de systeembeheerder beoordeeld en de betrokken marktpartijen worden uiterlijk één werkdag na ontvangst van de melding over het resultaat van de beoordeling geïnformeerd. 

- c. Na acceptatie van de ‘melding BRP-switch’ voorziet de systeembeheerder de nieuwe balanceringsverantwoordelijke uiterlijk de werkdag na ontvangst van de ‘melding BRP-switch’ van de gegevens die deze balanceringsverantwoordelijke nodig heeft voor het opstellen van zijn prognoses. Dit doet de systeembeheerder door middel van het bericht Stamgegevens na GAIN. 

## 4.11.4 Procesafspraken GA

- a. Het verwerken van een BRP-switch in het geval dat meerdere balanceringsverantwoordelijken gelijktijdig verantwoordelijk zijn voor één allocatiepunt gas, wordt niet in het (geautomatiseerde) berichtenverkeer ondersteund en valt buiten de scope van dit subproces. Voor een allocatiepunt elektriciteit is het niet mogelijk om gelijktijdig meerdere balanceringsverantwoordelijken te hebben op het betreffende allocatiepunt. 

- b. Voor allocatiepunten op grote aansluitingen mag een ‘melding individuele BRP-switch’ alleen worden ingediend door de actuele leverancier op het allocatiepunt. ‘Meldingen individuele BRP-switch’ van niet-actuele leveranciers worden door de systeembeheerder afgewezen (dit is ook het geval indien geen leverancier in het aansluitingenregister is vermeld op het moment van indienen van de individuele BRP-switch). 

- c. Een ingeplande BRP-switch wordt niet geeffectueerd als een inhuizing, leverancierswitch, uithuizing of einde levering wordt ingediend met een eerdere of gelijke mutatiedatum. 

- d. De leverancier die de individuele BRP-switch heeft geïnitieerd is verantwoordelijk om de beoogde nieuwe balanceringsverantwoordelijke te informeren indien een goedgekeurde individuele BRP-switch niet doorgaat wegens een leverancierswitch, inhuizing, uithuizing of einde levering waarvan de mutatiedatum eerder dan of gelijk is aan de mutatiedatum van de individuele BRP-switch. 

- e. Een positieve uitkomst van het subproces Indienen en beoordelen ‘melding individuele BRPswitch’ is voor de systeembeheerder een opdracht tot mutatie van het aansluitingenregister op de mutatiedatum. 

## 4.11.5 Procesbeschrijving GA

Bijlage B1106: Subprocesplaat SP0008 GA

1. De leverancier verstuurt de ‘melding individuele BRP-switch’, tenminste vijf werkdagen en maximaal 20 werkdagen voor de mutatiedatum, naar de systeembeheerder. 

2. De systeembeheerder beoordeelt de ‘melding individuele BRP-switch’ op de volgende punten: a. Is de ‘melding BRP-switch’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de leverancier geregistreerd als actuele leverancier op het allocatiepunt? 

   - d. Ligt datum van indienen tenminste vijf werkdagen en maximaal 20 werkdagen voor de mutatiedatum? 

   - e. Heeft de opgegeven balanceringsverantwoordelijke een volledige erkenning volgens het BRP-register van de betreffende transmissiesysteembeheerder? 

   - f. Is er geen andere nog niet geëffectueerde melding leverancierswitch, inhuizing, uithuizing of einde levering ingediend voor een eerdere of dezelfde mutatiedatum? 

   - g. Is het allocatiepunt niet geblokkeerd voor geautomatiseerde mutaties? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding individuele BRP-switch’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst ‘melding individuele BRP-switch’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De leverancier staat niet als actuele leverancier geregistreerd op de allocatiepunt. 

   - d. De gewenste mutatiedatum ligt buiten het venster van tenminste vijf werkdagen en maximaal 20 werkdagen in de toekomst. 

   - e. De opgegeven balanceringsverantwoordelijke heeft geen volledige erkenning volgens het BRP-register van de betreffende transmissiesysteembeheerder. 

   - f. Er is reeds een andere nog niet geëffectueerde melding voor een leverancierswitch, inhuizing, uithuizing of einde levering ingediend voor een eerdere of dezelfde mutatiedatum. 

   - g. Het allocatiepunt is geblokkeerd voor geautomatiseerde mutaties. 

4. De leverancier verwerkt de afwijzing. 

5. Als alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding individuele BRP-switch’ van de leverancier en verstuurt de systeembeheerder het 

bericht GAIN naar de leverancier, de nieuwe balanceringsverantwoordelijke en de meetverantwoordelijke partij, de Stamgegevens na GAIN naar de nieuwe balanceringsverantwoordelijke en het bericht LOSS naar de oude balanceringsverantwoordelijke. De GAIN-, Stamgegevens na GAIN- en LOSS-berichten worden uiterlijk de werkdag na ontvangst van de ‘melding individuele BRP-switch’ verstuurt. 

6. De leverancier ontvangt en verwerkt het bericht GAIN. 

7. De nieuwe balanceringsverantwoordelijke ontvangt en verwerkt het bericht GAIN. 

8. De oude balanceringsverantwoordelijke ontvangt en verwerkt het bericht LOSS. 

9. De meetverantwoordelijke partij ontvangt en verwerkt het bericht GAIN. 

10. De systeembeheerder plant de ‘melding BRP-switch’ van de leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

## 4.11.6 Termijnen GA

- a. De indientermijn voor een BRP-switch is de periode 20 werkdagen tot en met vijf werkdagen voor mutatiedatum. 

- b. Bij verwerking van de ‘melding BRP-switch’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de ‘melding BRP-switch’ over het resultaat door middel van een GAIN / LOSS. Bij afwijzing van de ‘melding BRP-switch’ ontvangt alleen de leverancier een afwijzing van de systeembeheerder. 

- c. Na acceptatie van de ‘melding BRP-switch’ voorziet de systeembeheerder de nieuwe balanceringsverantwoordelijke uiterlijk de werkdag na ontvangst van de ‘melding BRP-switch’ van de gegevens die deze balanceringsverantwoordelijke nodig heeft voor het opstellen van zijn prognoses. Dit doet de systeembeheerder door middel van het bericht Stamgegevens na GAIN. 

## 4.11.7 Gegevensuitwisseling

### Melding individuele BRP-switch

|**Melding individuele BRP-switch door leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Referentie|O|O|O|Ja|Ja|1||
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|Leverancier EAN|V|V|V|Ja|Ja|1||
||V|V|V|Ja|Ja|1|De EAN-code van de nieuwe|
|EAN-code balanceringsverantwoordelijke|||||||balanceringsverantwoordelijke|

### Afwijzing

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|A|Ja|Ja|1|Verplicht<br>gevuld,<br>tenzij<br>de<br>opvraag<br>wegens<br>technische redenen is afgewezen|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|De EAN-code van de nieuwe<br>balanceringsverantwoordelijke|

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Afwijsreden|V|V|V|Ja|Ja|n|Indicatie van de reden waarom de melding is<br>afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister<br>van<br>de<br>systeembeheerder.<br>•<br>De leverancier staat niet als actuele leverancier<br>geregistreerd op het allocatiepunt.<br>•<br>De gewenste mutatiedatum ligt buiten het<br>venster van tenminste 1 werkdag en maximaal<br>20 werkdagen in de toekomst.<br>•<br>De opgegeven balanceringsverantwoordelijke<br>heeft geen volledige erkenning volgens het<br>BRP-register van de betreffende<br>transmissiesysteembeheerder.<br>•<br>Er is reeds een andere nog niet geëffectueerde<br>melding van een leverancierswitch, inhuizing,<br>uithuizing of einde levering ingediend voor een<br>eerdere of dezelfde mutatiedatum.<br>•<br>Het<br>allocatiepunt<br>is<br>geblokkeerd<br>voor<br>geautomatiseerde mutaties(alleen GA)|
|Toelichtingafwijsreden|O|O|O|Ja|Ja|n||

### GAIN

|**GAIN naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|BRP-switch|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|De EAN-code van de nieuwe<br>balanceringsverantwoordelijke|

|**GAIN naar nieuwe balanceringsver**|**antwoord**|**elijke**||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|BRP-switch|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|EAN-code|V|V|V|Ja|Ja|1|De EAN-code van de nieuwe|
|balanceringsverantwoordelijke|||||||balanceringsverantwoordelijke|

|**GAIN naar meetverantwoordelijke p**|**artij**||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|Ja|Ja|1||
|Proces ID|V|V|Ja|Ja|1|BRP-switch|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|Ja|Ja|1||
|EAN-code systeembeheerder EAN|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|Ja|Ja|1||

### Stamgegevens na GAIN

|**Stamgegevens na GAIN naar nieuw**|**e balanceri**|**ngsvera**|**ntwoord**|**elijke**||||
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
|SJV|O|O|nvt|Ja|Nee|1|Wordt gecommuniceerd middels het veld SJA normaal<br>tarief|
|Allocatiemethode|V|V|V|Ja|Ja|1|Telemetrie, slimmemeterallocatie of geprofileerd|

### LOSS

|**LOSS naar oude balanceringsveran**|**twoordeli**|**jke**||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|BRP-switch|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code|V|V|V|Ja|Ja|1|De EAN-code van de oude|
|balanceringsverantwoordelijke|||||||balanceringsverantwoordelijke|
