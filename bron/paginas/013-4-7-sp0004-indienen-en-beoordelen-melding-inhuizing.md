# 4.7 SP0004 Indienen en beoordelen ‘melding inhuizing’


## 4.7.1 Procesafspraken KA

- a. De initiërende leverancier draagt er zorg voor dat hij een leveringsovereenkomst heeft op grond waarvan hij gerechtigd is om de inhuizing voor de klant uit te voeren. 

- b. De initiërende leverancier draagt er zorg voor dat hij van de klant minimaal die gegevens verkrijgt die nodig zijn om de EAN-code van het allocatiepunt te achterhalen. 

- c. Het is verplicht om de naam van de aangeslotene op te nemen in de ‘melding inhuizing’ bij een primair allocatiepunt. Indien het een zakelijke aangeslotene betreft wordt de bedrijfs- of instellingsnaam daartoe ingevuld in het veld achternaam. De systeembeheerder zal de ‘melding inhuizing’ afwijzen als de naam in de melding ontbreekt. In het geval van een inhuizing op een additioneel allocatiepunt, wordt het betreffende veld door de initiërende leverancier niet gevuld. Indien dit veld wel gevuld is, wordt dit veld door de systeembeheerder genegeerd. Het al dan niet aanwezig zijn van de naam van de aangeslotene bij een ‘melding inhuizing’ is geen reden voor het afwijzen van de ‘melding inhuizing’ op een additioneel allocatiepunt. 

- d. De initiërende leverancier spant zich ervoor in om bij een inhuizing op een primair allocatiepunt bij een natuurlijk persoon tevens de geboortedatum te verkrijgen. Indien de initiërende leverancier beschikt over de geboortedatum is het verplicht deze in te vullen in de ‘melding inhuizing’. In geval van een additioneel allocatiepunt wordt de geboortedatum niet gevuld in de ‘melding inhuizing’. Indien dit veld wel gevuld is, wordt dit veld door de systeembeheerder genegeerd. 

- e. De initiërende leverancier spant zich ervoor in om bij een inhuizing op een primair allocatiepunt bij een rechtspersoon tevens het KvK-nummer te verkrijgen. Indien de initiërende leverancier beschikt over een KvK-nummer is het verplicht dit in te vullen in de ‘melding inhuizing’. In geval van een additioneel allocatiepunt wordt het KvK-nummer niet gevuld in de ‘melding inhuizing’. Indien dit veld wel gevuld is, wordt dit veld door de systeembeheerder genegeerd. 

- f. Bij een meetinrichting zonder communicatiefunctionaliteit, meetinrichting met communicatiefunctionaliteit die administratief ‘uit’ staat of technisch op afstand niet uitleesbaar is, zal de initiërende leverancier de klant om een meterstand vragen ten behoeve van het subproces ‘Vaststellen en communiceren meterstanden’. Bij een meetinrichting met communicatiefunctionaliteit, die administratief op ‘aan’ staat en technisch op afstand uitleesbaar is, zal de leverancier een meterstand opvragen conform het subproces ‘Collecteren meterstand P4’ uit de P4. 

- g. Wanneer een ‘melding inhuizing’ wordt ingediend voor een allocatiepunt dat op de mutatiedatum de Fysieke status ‘In aanleg’ of ‘uit bedrijf’ heeft waarbij de meetinrichting is weggenomen, wordt er voor de mutatiedatum geen meterstand vastgesteld. 

- h. Indien de aansluiting fysiek is afgesloten, dient de aangeslotene contact op te nemen met de systeembeheerder om heraansluiting aan te vragen. 

- i. Wanneer op een allocatiepunt met een administratief uitgeschakelde meetinrichting een inhuizing of een uithuizing plaatsvindt, wordt de betreffende meetinrichting met communicatiefunctionaliteit op de mutatiedatum op administratief ‘aan’ gezet, tenzij de nieuwe aangeslotene al heeft aangegeven dat de meetinrichting administratief ‘uit’ dient te staan. De systeembeheerder verwerkt deze wijziging in zijn aansluitingenregister en zorgt ervoor dat de meetinrichting met communicatiefunctionaliteit via de P4 benaderbaar is bij administratief ‘aan’ en niet benaderbaar via de P4 bij administratief ‘uit’ overeenkomstig het subproces ‘Administratief aanen uitzetten van een meetinrichting met communicatiefunctionaliteit’. Bij een inhuizing op een additioneel allocatiepunt verandert de administratieve status van de meetinrichting met communicatiefunctionaliteit niet. 

## 4.7.2 Procesbeschrijving KA

Bijlage B1096: Subprocesplaat SP0004 KA

1. De initiërende leverancier verstuurt de ‘melding inhuizing’ tenminste op de mutatiedatum en ten hoogste twee werkdagen voor de mutatiedatum naar de systeembeheerder. Een uitzondering wordt gemaakt voor allocatiepunten waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet, waar een ‘melding inhuizing’ tenminste op de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum kan worden ingediend. 

2. De systeembeheerder beoordeelt de ‘melding inhuizing’ op de volgende punten: 

   - a. Is de ‘melding inhuizing’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt de datum van ontvangst tenminste op de mutatiedatum en maximaal 20 werkdagen voor de mutatiedatum? 

   - d. Is de initiërende leverancier als onderneming bekend bij de systeembeheerder (en is het vanuit de toezichthouder toegestaan om aanvragen van deze leverancier in behandeling te nemen)? 

   - e. Heeft de opgegeven balanceringsverantwoordelijke een erkenning volgens het BRPregister (elektriciteit of gas)? 

   - f. Is er geen andere melding leverancierswitch of inhuizing met een latere mutatiedatum ontvangen? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding inhuizing’ af, en verstuurt de systeembeheerder een afwijsbericht naar de initiërende leverancier uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De gewenste mutatiedatum ligt buiten het venster van de ontvangstdatum en maximaal 20 werkdagen in de toekomst. 

   - d. De initiërende leverancier is niet als onderneming bekend bij de systeembeheerder (of het is vanuit de toezichthouder niet toegestaan om aanvragen van deze leverancier in behandeling te nemen). 

   - e. De opgegeven balanceringsverantwoordelijke heeft geen volledige erkenning volgens het BRP-register. 

   - f. Er is reeds een andere melding van een inhuizing of leverancierswitch met een latere mutatiedatum ontvangen (kruisend proces). 

4. De initiërende leverancier verwerkt de afwijzing. 

5. Als alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding inhuizing’, van de initiërende leverancier en verstuurt hij het bericht GAIN naar de initiërende leverancier en de nieuwe balanceringsverantwoordelijke, het bericht Stamgegevens na GAIN naar de nieuwe balanceringsverantwoordelijke en, als deze partijen aanwezig zijn, het bericht LOSS naar de oude leverancier en de oude balanceringsverantwoordelijke. De GAIN-, Stamgegevens na GAIN- en LOSS-berichten worden uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’ verstuurd. 

6. De initiërende leverancier ontvangt en verwerkt het bericht GAIN. 

7. Na het verwerken van het bericht GAIN wordt door de initiërende leverancier het versturen van het bericht ’Melding wijzigen gegevens aangeslotene’ ingepland op de datum van de effectuering van de inhuizing. 

8. De oude leverancier (indien aanwezig) ontvangt en verwerkt het bericht LOSS. 

9. De nieuwe balanceringsverantwoordelijke ontvangt en verwerkt het bericht GAIN en stamgegevens. 

10. De oude balanceringsverantwoordelijke (indien aanwezig) ontvangt en verwerkt het bericht LOSS. 

11. De systeembeheerder: 

   - a. Plant de melding van de initiërende leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

   - b. Verwijdert eerder ontvangen maar nog niet geëffectueerde meldingen voor uithuizing, einde levering of BRP-switch met dezelfde of een latere mutatiedatum dan de inhuizing. 

   - c. Als een inhuizing is ingediend met dezelfde mutatiedatum als een reeds ontvangen leverancierswitch of inhuizing dan zal de eerder ontvangen leverancierswitch of inhuizing worden geannuleerd/overschreven. Voor de geannuleerde/overschreven leverancierswitch of inhuizing wordt een LOSS verstuurd. 

## 4.7.3 Termijnen KA

- a. Een ‘melding inhuizing’ kan in de periode twee werkdagen voor de mutatiedatum tot en met de mutatiedatum worden ingediend. 

- b. Een uitzondering wordt gemaakt voor aansluitingen waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet, waar een ‘melding inhuizing’ kan worden ingediend in de periode 20 werkdagen voor de mutatiedatum tot en met de mutatiedatum. 

- c. Bij verwerking van de ‘melding inhuizing’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’ over het resultaat door middel van een GAIN / LOSS. Bij afwijzing van de ‘melding inhuizing’ ontvangt alleen de initiërende leverancier een afwijzing van de systeembeheerder. 

- d. Na acceptatie van de ‘melding inhuizing’ voorziet de systeembeheerder de nieuwe balanceringsverantwoordelijke uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’ van de gegevens die deze balanceringsverantwoordelijke nodig heeft voor het opstellen van zijn prognoses. Dit doet de systeembeheerder door middel van het bericht Stamgegevens na GAIN. 

## 4.7.4 Procesafspraken GA

- a. De initiërende leverancier draagt er zorg voor dat hij een machtiging van de klant heeft voor het uitvoeren van de inhuizing. 

- b. De initiërende leverancier draagt er zorg voor dat hij van de klant minimaal die gegevens verkrijgt die nodig zijn om de EAN-code van het allocatiepunt te achterhalen. 

- c. Indien de aansluiting fysiek is afgesloten, dan dient de aangeslotene contact op te nemen met de systeembeheerder om heraansluiting aan te vragen. 

- d. Het is verplicht om de naam van de aangeslotene op te nemen in de ‘melding inhuizing’ bij een primair allocatiepunt; indien het een zakelijke aangeslotene betreft wordt de bedrijfs- of instellingsnaam daartoe ingevuld in het veld achternaam. De systeembeheerder wijst af als de naam in het verzoek ontbreekt. In het geval van een inhuizing op een additioneel allocatiepunt, wordt het betreffende veld door de initiërende leverancier niet gevuld. Indien dit veld wel gevuld is, wordt dit veld door de systeembeheerder genegeerd. 

- e. Indien de initiërende leverancier beschikt over een KvK-nummer bij een inhuizing op een primair allocatiepunt is het verplicht dit in te vullen in de ‘melding inhuizing’. In geval van een additioneel allocatiepunt wordt het KvK-nummer niet gevuld in de ‘melding inhuizing’. Indien dit veld wel gevuld is, wordt dit veld door de systeembeheerder genegeerd. 

- f. Het verwerken van een inhuizing in het geval dat meerdere balanceringsverantwoordelijken verantwoordelijk zijn voor een allocatiepunt gas, wordt niet in het berichtenverkeer ondersteund en valt buiten de scope van dit subproces. Bij een allocatiepunt elektriciteit is het niet mogelijk om gelijktijdig meerdere balanceringsverantwoordelijken te hebben. 

- g. Wanneer een ‘melding inhuizing’ wordt ingediend voor een allocatiepunt, die op de mutatiedatum de fysieke status ‘In aanleg’ heeft, of ‘Uit bedrijf’ waarbij de meetinrichting is verwijderd, wordt er voor de mutatiedatum geen meterstand vastgesteld. 

## 4.7.5 Procesbeschrijving GA

Bijlage B1097: Subprocesplaat SP0004 GA

1. De initiërende leverancier verstuurt de ‘melding inhuizing’, tenminste vijf werkdagen voor de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum, naar de systeembeheerder. 

Een uitzondering bestaat voor aansluitingen met leegstand, hiervoor kan tenminste op de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum een ‘melding inhuizing’ worden ingediend. 

2. De systeembeheerder beoordeelt de ‘melding inhuizing’ op de volgende punten: 

   - a. Is de ‘melding inhuizing’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt datum van ontvangst tenminste vijf en maximaal 20 werkdagen voor de mutatiedatum of in geval van leegstand tenminste nul en maximaal 20 werkdagen voor de mutatiedatum? 

   - d. Is de leverancier als onderneming bekend bij de systeembeheerder (en is het vanuit de toezichthouder toegestaan om aanvragen van deze leverancier in behandeling te nemen)? 

   - e. Heeft de opgegeven balanceringsverantwoordelijke een volledige erkenning volgens het BRP-register (elektriciteit of gas)? 

   - f. Is er geen andere melding leverancierswitch of inhuizing met een latere mutatiedatum ontvangen? 

   - g. Is het allocatiepunt niet geblokkeerd voor geautomatiseerde mutaties? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding inhuizing’ af, en verstuurt de systeembeheerder een afwijsbericht naar de initiërende leverancier uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. c. De gewenste mutatiedatum ligt buiten het venster van tenminste vijf en maximaal 20 werkdagen in de toekomst of in geval van leegstand buiten het venster van tenminste nul en maximaal 20 werkdagen in de toekomst. 

   - d. De leverancier is niet als onderneming bekend bij de systeembeheerder (of het is vanuit de toezichthouder niet toegestaan om aanvragen van deze leverancier in behandeling te nemen). 

   - e. De opgegeven balanceringsverantwoordelijke heeft geen volledige erkenning volgens het BRP-register. 

   - f. Er is reeds een andere melding van een inhuizing of leverancierswitch met een latere mutatiedatum ontvangen (kruisend proces). 

   - g. Het allocatiepunt is geblokkeerd voor geautomatiseerde mutaties. 

4. De initiërende leverancier verwerkt de afwijzing. 

5. Als alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding inhuizing’ van de initiërende leverancier en verstuurt de systeembeheerder het bericht GAIN naar de initiërende leverancier, de nieuwe balanceringsverantwoordelijke en de meetverantwoordelijke partij (indien aanwezig), de Stamgegevens na GAIN naar de nieuwe balanceringsverantwoordelijke en, als deze partijen aanwezig zijn, het bericht LOSS naar de oude leverancier en de oude balanceringsverantwoordelijke. De GAIN-, Stamgegevens na GAIN- en LOSS-berichten worden uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’ verstuurd. 

6. De initiërende leverancier ontvangt en verwerkt het bericht GAIN. 

7. Indien aanwezig ontvangt en verwerkt de oude leverancier het bericht LOSS. 

8. De nieuwe balanceringsverantwoordelijke ontvangt en verwerkt het bericht GAIN en stamgegevens. 

9. Indien aanwezig ontvangt en verwerkt de oude balanceringsverantwoordelijke het bericht LOSS. 

10. De meetverantwoordelijke partij (indien aanwezig) ontvangt en verwerkt het bericht GAIN. 

11. De systeembeheerder: 

   - a. Plant de melding van de initiërende leverancier in voor effectuering op de in de melding aangeven datum in het aansluitingenregister. 

- b. Verwijdert eerder ontvangen maar nog niet geëffectueerde meldingen voor inhuizing, uithuizing, einde levering of BRP-switch met dezelfde of een latere mutatiedatum dan de inhuizing. 

- c. Als een inhuizing is ingediend met dezelfde mutatiedatum als een reeds ontvangen leverancierswitch of inhuizing dan zal de eerder ontvangen leverancierswitch of inhuizing worden geannuleerd/overschreven. Voor de geannuleerde/overschreven leverancierswitch of inhuizing wordt een LOSS verstuurd. 

## 4.7.6 Termijnen GA

- a. Een ‘melding inhuizing’ kan in de periode 20 werkdagen tot en met vijf werkdagen voor de mutatiedatum worden ingediend. 

- b. Een ‘melding inhuizing’ voor allocatiepunt met leegstand kan in de periode 20 werkdagen tot en met de mutatiedatum ingediend. 

- c. Bij verwerking van de ‘melding inhuizing’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’ over het resultaat door middel van een GAIN / LOSS. Bij afwijzing van de ‘melding inhuizing’ ontvangt alleen de initiërende leverancier een afwijzing van de systeembeheerder. 

- d. Na acceptatie van de ‘melding inhuizing’ voorziet de systeembeheerder de nieuwe balanceringsverantwoordelijke uiterlijk de werkdag na ontvangst van de ‘melding inhuizing’ van de gegevens die deze balanceringsverantwoordelijke nodig heeft voor het opstellen van zijn prognoses. Dit doet de systeembeheerder door middel van het bericht Stamgegevens na GAIN. 

## 4.7.7 Gegevensuitwisseling

### Melding inhuizing

|**Melding door nieuwe leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Referentie|O|O|O|Ja|Ja|1||
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1||
|KvK-nummer|O|O|O|Ja|Ja|1|Verplicht indien leverancier beschikt over het KvK-<br>nummer|
|Voorletters aangeslotene|O|O|O|Ja|Ja|1||
|Tussenvoegsel aangeslotene|O|O|O|Ja|Ja|1||
|(Achter-) Naam aangeslotene|V|V|V|Ja|Ja|1|Bij een zakelijke aangeslotene wordt de bedrijfs- of<br>instellingsnaam hier ingevuld|
|Geboortedatum|O|O|O|Ja|Ja|1|Verplicht indien de leverancier beschikt over de<br>geboortedatum|
|_Correspondentieadres:_||||||||
|Straatnaam / Postbus|A|O|O|Ja|Ja|1|Verplicht bij KA indien dit afwijkt van het|
|Huisnummer / Postbusnummer|A|O|O|Ja|Ja|1|aansluitadres.|
|Huisnummer-toevoeging|A|O|O|Ja|Ja|1||
|Postcode|A|O|O|Ja|Ja|1||
|Woonplaats|A|O|O|Ja|Ja|1||
|Land|A|O|O|Ja|Ja|1||

### Afwijzing naar leverancier

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens<br>technische redenen is afgewezen.|

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Proces ID|V|V|V|Ja|Ja|1|Inhuizing|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|Mutatiedatum|V|V|V|Ja|Ja|1||
|Afwijsreden|V|V|V|Ja|Ja|n|•<br>Onvolledige melding of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister<br>van<br>de<br>systeembeheerder.<br>•<br>De gewenste mutatiedatum ligt buiten het<br>venster van tenminste vijf en maximaal 20<br>werkdagen in de toekomst of in geval van<br>leegstand buiten het venster van tenminste nul<br>en maximaal 20 werkdagen in de toekomst.<br>•<br>De<br>initiërende<br>leverancier<br>is<br>niet<br>als<br>onderneming bekend bij de systeembeheerder<br>(of het is vanuit de toezichthouder niet<br>toegestaan om aanvragen van deze leverancier<br>in behandeling te nemen).<br>•<br>De opgegeven balanceringsverantwoordelijke<br>heeft geen volledige erkenning volgens het<br>BRP-register.<br>•<br>Er is reeds een andere melding van een<br>inhuizing of leverancierswitch met een latere<br>mutatiedatum ontvangen.<br>•<br>Het<br>allocatiepunt<br>is<br>geblokkeerd<br>voor<br>geautomatiseerde mutaties.|
|Toelichting afwijsreden|O|O|O|Ja|Ja|n||

### GAIN naar nieuwe leverancier en balanceringsverantwoordelijke

|**GAIN naar nieuwe leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Inhuizing|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code nieuwe balanceringsverantwoordelijke|
|EAN-code leverancier|A|A|A|Ja|Ja|1|EAN-code oude leverancier. Alleen gevuld als een<br>leverancier<br>geregistreerd<br>was<br>in<br>het<br>aansluitingenregister tot de mutatiedatum.|

|**GAIN naar nieuwe balanceringsvera**|**ntwoordel**|**ijke**||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Inhuizing|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code nieuwe balanceringsverantwoordelijke|

### Stamgegevens na GAIN naar balanceringsverantwoordelijke

|**Stamgegevens na GAIN naar nieuw**|**e balanceri**|**ngsvera**|**ntwoord**|**elijke**||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n **|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Inhuizing|

|**Stamgegevens na GAIN naar nieuwe**|**balanceri**|**ngsvera**|**ntwoord**|**elijke**||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n **|**Opmerking**|
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
|SJV|O|O|nvt|Ja|Nee|1|Wordt gecommuniceerd middels het veld SJA<br>normaal tarief|
|Allocatiemethode|V|V|V|Ja|Ja|1|Telemetrie, slimmemeterallocatie of geprofileerd|

### GAIN naar meetverantwoordelijke partij

|**GAIN naar meetverantwoordelijke p**|**artij**||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|Ja|Ja|1||
|Proces ID|V|V|Ja|Ja|1|Inhuizing|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code<br>balanceringsverantwoordelijke|V|V|Ja|Ja|1|EAN-code nieuwe balanceringsverantwoordelijke|
|EAN-code leverancier|A|A|Ja|Ja|1|EAN-code oude leverancier. Alleen gevuld als een<br>leverancier geregistreerd was in het aansluitingenregister<br>tot de mutatiedatum.|

### LOSS naar oude leverancier en balanceringsverantwoordelijke

|**LOSS naar oude leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Inhuizing|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code oude leverancier|

|**LOSS naar oude balanceringsverant**|**woordelijk**|**e**||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Inhuizing|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code oude balanceringsverantwoordelijke|
