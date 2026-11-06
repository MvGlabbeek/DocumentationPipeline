# 4.9 SP0005 Indienen en beoordelen ‘melding uithuizing’


## 4.9.1 Procesafspraken KA

- a. De leverancier draagt er zorg voor dat hij een machtiging van de aangeslotene heeft op grond waarvan hij gerechtigd is om de uithuizing voor de klant uit te voeren. 

- b. Een ingediende ‘melding uithuizing’ die nog niet is geëffectueerd, kan worden doorkruist door een inhuizing, leverancierswitch of uithuizing met een eerdere of dezelfde mutatiedatum. Deze inhuizing, leverancierswitch of uithuizing prevaleert dan boven de uithuizing (uithuizing wordt geannuleerd). De leverancier die de uithuismelding deed, is in een dergelijke situatie niet langer de leverancier en is niet verantwoordelijk voor het vaststellen van een meterstand. 

- c. De systeembeheerder verwerkt de ‘melding uithuizing’ nadat alle meldingen voor inhuizing en leverancierswitch voor de desbetreffende mutatiedatum zijn verwerkt. 

- d. Wanneer op een primair allocatiepunt met een meetinrichting met communicatiefunctionaliteit die administratief op ‘uit’ staat, een uithuizing is geëffectueerd in het aansluitingenregister, dan wordt de administratieve status van de betreffende meetinrichting op ‘aan’ gezet. Indien de uithuizing een primair allocatiepunt betreft, wordt voor eventueel bijbehorende additionele allocatiepunten met een meetinrichting met communicatiefunctionaliteit de administratieve status van de desbetreffende meetinrichting niet aangepast. De systeembeheerder verwerkt deze wijziging in het aansluitingenregister en zorgt ervoor dat de meetinrichting met communicatiefunctionaliteit via de P4 benaderbaar is overeenkomstig het subproces ‘Administratief aan- en uitzetten van een meetinrichting met communicatiefunctionaliteit’. Indien de uithuizing een additioneel allocatiepunt met een meetinrichting met communicatiefunctionaliteit betreft, wordt de administratieve status van de desbetreffende meetinrichting niet aangepast. 

- e. Een leverancier die zowel de uithuizing van de oude klant als de inhuizing van de nieuwe klant doorgeeft, is zelf verantwoordelijk voor het voorkomen van een uithuizing van de nieuwe klant door een melding uithuizing. 

- f. Wanneer een uithuizing wordt gemeld voor een allocatiepunt met de fysiek status ‘in aanleg’ of ‘uit bedrijf’ wordt er voor de mutatiedatum geen meterstand vastgesteld. 

- g. Bij een niet op afstand uitleesbare meetinrichting zal de leverancier de klant om een meterstand vragen ten behoeve van het deelproces ‘Vaststellen meterstand’. Bij een meetinrichting met communicatiefunctionaliteit zal de leverancier een meterstand opvragen conform het subproces ‘Collecteren meterstand P4’ uit de P4. 

## 4.9.2 Procesbeschrijving KA

Bijlage B1100: Subprocesplaat SP0005 KA

1. De leverancier verstuurt een ‘melding uithuizing’, één werkdag voor de mutatiedatum, naar de systeembeheerder. 

Een uitzondering wordt gemaakt voor allocatiepunten waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet waar een ‘melding uithuizing’ tenminste één werkdag voor de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum kan worden ingediend. 

2. De systeembeheerder beoordeelt de ‘melding uithuizing’ op de volgende punten: 

   - a. Is de ‘melding uithuizing’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt de datum van indienen tenminste één werkdag voor en maximaal 20 werkdagen voor de mutatiedatum? 

   - d. Is er geen andere nog niet geëffectueerde leverancierswitch-, inhuizing-, uithuizing- of einde leveringsmelding ontvangen met een eerdere mutatiedatum? 

   - e. Is de melding uithuizing ingediend door: 

      - i. de in het aansluitingenregister vermelde leverancier, of; 

      - ii. bij een allocatiepunt zonder geregistreerde leverancier: de leverancier van een bevestigde inhuizing met dezelfde mutatiedatum? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding uithuizing’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst van de ‘melding uithuizing’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De gewenste mutatiedatum ligt buiten het venster van tenminste één werkdag en maximaal 20 werkdagen in de toekomst. 

   - d. Er is reeds een andere nog niet geëffectueerde melding van een leverancierswitch, inhuizing, uithuizing of einde levering ontvangen waarvan de mutatiedatum voor de mutatiedatum van de uithuizing ligt (kruisend proces). De leverancier staat niet als actieve leverancier geregistreerd op het allocatiepunt. 

   - e. De melding uithuizing is niet ingediend door: 

      - i. de in het aansluitingenregister vermelde leverancier, of; 

      - ii. bij een allocatiepunt zonder geregistreerde leverancier; de leverancier van een bevestigde inhuizing met dezelfde mutatiedatum. 

4. De leverancier verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding uithuizing’ van de leverancier en verstuurt hij het bericht LOSS naar de leverancier en de balanceringsverantwoordelijke. De LOSS berichten worden uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’ verstuurd. 

6. De leverancier ontvangt en verwerkt het bericht LOSS. 

7. De balanceringsverantwoordelijke ontvangt en verwerkt het bericht LOSS. 

8. De systeembeheerder: 

   - a. Plant de melding van de leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

   - b. Verwijdert eerder ontvangen maar nog niet geëffectueerde meldingen voor BRPswitch met dezelfde of een latere mutatiedatum dan de uithuizing, die door de leverancier zijn ingediend. 

## 4.9.3 Termijnen KA

- a. Een ‘melding uithuizing’ kan één werkdag voor de mutatiedatum worden ingediend. 

- b. Een uitzondering wordt gemaakt voor allocatiepunten waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet waar een ‘melding uithuizing’ kan worden ingediend in de periode 20 werkdagen voor de mutatiedatum tot en met één werkdag voor de mutatiedatum. 

- c. Bij verwerking van de uithuismelding informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de uithuismelding over het resultaat door middel van een LOSS. Bij afwijzing van de uithuismelding ontvangt alleen de leverancier een afwijzing van de systeembeheerder. 

## 4.9.4 Procesafspraken GA

- a. De leverancier draagt er zorg voor dat hij een machtiging van de klant heeft voor het uitvoeren van de uithuizing. 

- b. Een leverancier die zowel de inhuizing van de oude klant als de inhuizing van de nieuwe klant doorgeeft, is zelf verantwoordelijk voor het voorkomen van een uithuizing van de nieuwe klant door een melding uithuizing. 

- c. Wanneer een ‘melding uithuizing’ wordt ingediend voor een allocatiepunt, die op de mutatiedatum de Fysieke status ‘In aanleg’ of ‘Uit bedrijf’ heeft, wordt er voor de mutatiedatum geen stand vastgesteld. 

- d. De meetverantwoordelijke partij bepaalt bij een uithuizing de meterstand en het bijbehorende volume, de systeembeheerder neemt deze over en distribueert de meterstand en het volume naar de leverancier. 

- e. Een ingediende ‘melding uithuizing’ die nog niet is geëffectueerd, kan worden gekruist door een inhuizing, leverancierswitch, uithuizing of einde levering met een eerdere of dezelfde mutatiedatum. De leverancier die de uithuizing heeft ingediend ontvangt een tweede LOSSbericht met een eerdere mutatiedatum. De meetverantwoordelijke partij ontvangt een GAINbericht (in het kader van de inhuizing of leverancierswitch) naast het reeds ontvangen LOSSbericht (in het kader van de uithuizing). 

## 4.9.5 Procesbeschrijving GA

Bijlage B1101: Subprocesplaat SP0005 GA

1. De leverancier verstuurt de ‘melding uithuizing’, tenminste vijf werkdagen voor de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum, naar de systeembeheerder. 

2. De systeembeheerder boordeelt de ‘melding uithuizing’ op de volgende punten: 

   - a. Is de ‘melding uithuizing’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt datum van ontvangst tenminste vijf werkdagen voor en maximaal 20 werkdagen voor de mutatiedatum? 

   - d. Is er geen andere nog niet geëffectueerde leverancierswitch-, inhuizing-, uithuizing- of einde leveringsmelding’ ontvangen met een eerdere mutatiedatum? 

   - e. Is de melding uithuizing ingediend door: 

      - i. de in het aansluitingenregister vermelde leverancier, of; 

      - ii. bij een allocatiepunt zonder geregistreerde leverancier: de leverancier van een bevestigde inhuizing met dezelfde mutatiedatum? 

   - f. Is het allocatiepunt niet geblokkeerd voor geautomatiseerde mutaties? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding uithuizing’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst van de ‘melding uithuizing’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledig melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De gewenste mutatiedatum ligt buiten het venster van tenminste vijf werkdagen en maximaal 20 werkdagen in de toekomst. 

   - d. Er is reeds een andere nog niet geëffectueerde melding van een leverancierswitch, inhuizing, uithuizing of einde levering ontvangen waarvan de mutatiedatum voor de mutatiedatum van de uithuizing ligt (zie Bijlage Uniforme procedure Kruisende processen.). 

   - e. De melding uithuizing is niet ingediend door: 

      - i. de in het aansluitingenregister vermelde leverancier, of; 

      - ii. bij een allocatiepunt zonder geregistreerde leverancier: de leverancier van een bevestigde inhuizing met dezelfde mutatiedatum. 

   - f. Het allocatiepunt is geblokkeerd voor geautomatiseerde mutaties. 

4. De leverancier verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding uithuizing’ van de leverancier en verstuurt de systeembeheerder het bericht LOSS naar de leverancier, de meetverantwoordelijke partij en de balanceringsverantwoordelijke. De LOSS berichten worden uiterlijk de werkdag na ontvangst van de ‘melding uithuizing’ verstuurd. 

6. De leverancier ontvangt en verwerkt het bericht LOSS. 

7. De balanceringsverantwoordelijke ontvangt en verwerkt het bericht LOSS. 

8. De meetverantwoordelijke partij ontvangt en verwerkt het bericht LOSS. 

9. De systeembeheerder: 

   - a. Plant de melding van de leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

   - b. Verwijdert eerder ontvangen maar nog niet geëffectueerde aanvragen voor uithuizing, einde levering of BRP-switch met dezelfde of een latere mutatiedatum dan de uithuizing, die door de initiërende leverancier zijn ingediend. 

## 4.9.6 Termijnen GA

- a. Een ‘melding uithuizing’ kan in de periode 20 werkdagen tot en met vijf werkdagen voor mutatiedatum worden ingediend. 

- b. Bij verwerking van de ‘melding uithuizing’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de uithuismelding over het resultaat door middel van een LOSS. Bij afwijzing van de ‘melding uithuizing’ ontvangt alleen de leverancier een afwijzing van de systeembeheerder. 

## 4.9.7 Gegevensuitwisseling

### Melding uithuizing

|**Melding uithuizing door leveran**|**cier**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Referentie|O|O|O|Ja|Ja|1||

|**Melding uithuizing door leveranci**|**er**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||

### Afwijzing

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de melding wegens technische<br>redenen is afgewezen|
|Proces ID|V|V|V|Ja|Ja|1|Uithuizing|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|Afwijsreden|V|V|V|Ja|Ja|n|Indicatie van de reden waarom de melding is<br>afgewezen:<br>•<br>Onvolledig melding of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister van de systeembeheerder.<br>•<br>De gewenste mutatiedatum ligt buiten het<br>venster van tenminste vijf werkdagen en<br>maximaal 20 werkdagen in de toekomst.<br>•<br>Er is reeds een andere nog niet geëffectueerde<br>melding van een leverancierswitch, inhuizing,<br>uithuizing of einde levering ontvangen waarvan<br>de mutatiedatum op of voor de mutatiedatum<br>van de uithuizing ligt.<br>•<br>De uithuismelding is niet ingediend door: de in<br>het aansluitingenregister vermelde leverancier,<br>of; bij een allocatiepunt zonder geregistreerde<br>leverancier; de leverancier van een bevestigde<br>inhuizing met dezelfde mutatiedatum.<br>•<br>Het<br>allocatiepunt<br>is<br>geblokkeerd<br>voor<br>geautomatiseerde mutaties.|
|Toelichtingafwijsreden|O|O|O|Ja|Ja|n||

### LOSS

|**LOSS naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Uithuizing|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||

|**LOSS naar balanceringsverantwoo**|**rdelijke**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Uithuizing|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1||

|**LOSS naar meetverantwoordelijk**|**e partij**||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|Ja|Ja|1||
|Proces ID|V|V|Ja|Ja|1|Uithuizing|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|Ja|Ja|1||
