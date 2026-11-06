# 4.8 SP0007 Indienen en beoordelen ‘melding leverancierswitch’


## 4.8.1 Procesafspraken KA

- a. De initiërende leverancier draagt er zorg voor dat hij een leveringsovereenkomst heeft op grond waarvan hij gerechtigd is om de leverancierswitch uit te voeren. 

- b. De initiërende leverancier draagt er zorg voor dat hij van de klant minimaal die gegevens verkrijgt die nodig zijn om de EAN-code van het allocatiepunt te achterhalen. 

- c. De initiërende leverancier spant zich ervoor in om bij een leverancierswitch op een allocatiepunt bij een natuurlijk persoon tevens de geboortedatum te verkrijgen. 

- d. De initiërende leverancier spant zich ervoor in om bij een leverancierswitch op een allocatiepunt bij een rechtspersoon tevens het KvK-nummer te verkrijgen. 

- e. Indien op de mutatiedatum geen actieve leverancier aanwezig is in het aansluitingenregister en de leverancierswitch een primair allocatiepunt betreft, wordt de ‘melding leverancierswitch’ door de systeembeheerder goedgekeurd, indien door de initiërende leverancier de naam van de aangeslotene in de ‘melding leverancierswitch’ is opgenomen. Indien het een rechtspersoon betreft wordt de bedrijfs- of instellingsnaam daartoe opgenomen in het veld ‘achternaam’. In dat geval is de leverancier verplicht de geboortedatum of KvK-nummer in te vullen indien hij daarover beschikt. 

- f. Indien op de mutatiedatum geen actieve leverancier aanwezig is in het aansluitingenregister en de leverancierswitch een additioneel allocatiepunt betreft, wordt de naam van de aangeslotene door de initiërende leverancier niet in de ‘melding leverancierswitch’ opgenomen. Indien dit wel gebeurt, wordt dit veld door de systeembeheerder genegeerd. Indien de geboortedatum of KvK-nummer gevuld zijn, worden deze eveneens genegeerd door de systeembeheerder. Het al dan niet aanwezig zijn van de naam van de aangeslotene bij een ‘melding leverancierswitch’ is geen reden voor het afwijzen van de ‘melding leverancierswitch’ op een additioneel allocatiepunt. 

- g. Wanneer een ‘melding leverancierswitch’ wordt ingediend voor een allocatiepunt die op de mutatiedatum de status ‘in aanleg’ of ‘uit bedrijf’ heeft waarbij de meetinrichting is verwijderd, wordt er voor de mutatiedatum geen meterstand vastgesteld. 

- h. Bij een meetinrichting zonder communicatiefunctionaliteit, meetinrichting met communicatiefunctionaliteit die administratief ‘uit’ staat of technisch op afstand niet uitleesbaar is, zal de initiërende leverancier de klant om een meterstand vragen ten behoeve van het subproces ‘Vaststellen en communiceren meterstanden’. Bij een meetinrichting met communicatiefunctionaliteit, die administratief op ‘aan’ staat en technisch op afstand 

uitleesbaar is, zal de leverancier een meterstand opvragen conform het subproces ‘Collecteren meterstand P4’ uit de P4. 

## 4.8.2 Procesbeschrijving KA

Bijlage B1098: Subprocesplaat SP0007 KA

1. De initiërende leverancier verstuurt de ‘melding leverancierswitch’ tenminste op de mutatiedatum en ten hoogste één werkdag voor de mutatiedatum naar de systeembeheerder. Een uitzondering wordt gemaakt voor allocatiepunten waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet, waar een ‘melding leverancierswitch’ tenminste één werkdag voor mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum kan worden ingediend. 

2. De systeembeheerder beoordeelt de melding op de volgende punten: 

   - a. Is de ‘melding leverancierswitch’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt de datum van ontvangst tenminste één werkdag en maximaal 20 werkdagen voor de mutatiedatum? 

   - d. Is de initiërende leverancier als onderneming bekend bij de systeembeheerder (en is het vanuit de toezichthouder toegestaan om aanvragen van deze leverancier in behandeling te nemen)? 

   - e. Heeft de opgegeven balanceringsverantwoordelijke een erkenning volgens het BRPregister (elektriciteit of gas)? 

   - f. Is er geen andere melding leverancierswitch of inhuizing met een latere mutatiedatum ontvangen? 

   - g. Is de naam van de aangeslotene ingevuld in de ‘melding leverancierswitch’ indien de ‘melding leverancierswitch’ is ingediend: 

      - i. voor een primair allocatiepunt, en 

      - ii. met een mutatiedatum waarop geen actieve leverancier aanwezig is in het aansluitingenregister? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding leverancierswitch’ af, en verstuurt de systeembeheerder een afwijsbericht naar de 

initiërende leverancier uiterlijk de werkdag na ontvangst van de ‘melding leverancierswitch’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De gewenste mutatiedatum ligt buiten het venster van tenminste één werkdag en maximaal 20 werkdagen in de toekomst. 

   - d. De initiërende leverancier is niet als onderneming bekend bij de systeembeheerder (of het is vanuit de toezichthouder toegestaan om aanvragen van deze leverancier in behandeling te nemen). 

   - e. De opgegeven balanceringsverantwoordelijke heeft geen erkenning volgens het BRPregister. 

   - f. Er is reeds een andere melding van een inhuizing of leverancierswitch met een latere mutatiedatum ontvangen (kruisend proces). 

   - g. De naam van de aangeslotene is niet gevuld in de ‘melding leverancierswitch’ van een primair allocatiepunt terwijl er geen actieve leverancier in het aansluitingenregister aanwezig is op de gewenste mutatiedatum (gebruik ‘melding inhuizing’ in plaats van ‘melding leverancierswitch’). 

4. De initiërende leverancier verwerkt de afwijzing. 

5. Als alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding leverancierswitch’ van de initiërende leverancier en verstuurt hij het bericht GAIN naar de initiërende leverancier en de nieuwe balanceringsverantwoordelijke, de Stamgegevens na GAIN naar de nieuwe balanceringsverantwoordelijke en, als deze partijen aanwezig zijn, het bericht LOSS naar de oude leverancier en de oude balanceringsverantwoordelijke. De GAIN-, Stamgegevens na GAIN- en LOSS-berichten worden uiterlijk de werkdag na ontvangst van de ‘melding leveranciersswitch’ verstuurd. 

6. De initiërende leverancier ontvangt en verwerkt het bericht GAIN. 

7. Na het verwerken van het bericht GAIN wordt door de leverancier het versturen van het bericht ’Melding wijzigen gegevens aangeslotene’ ingepland op de datum van de effectuering van de leverancierswitch. 

8. De oude leverancier (indien aanwezig) ontvangt en verwerkt het bericht LOSS. 

9. De nieuwe balanceringsverantwoordelijke ontvangt en verwerkt het bericht GAIN en stamgegevens. 

10. De oude balanceringsverantwoordelijke (indien aanwezig) ontvangt en verwerkt het bericht LOSS. 

11. De systeembeheerder: 

   - a. Plant de melding van de initiërende leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

   - b. Verwijdert eerder ontvangen maar nog niet geëffectueerde meldingen voor uithuizing, einde levering of BRP-switch met dezelfde of een latere mutatiedatum dan de leverancierswitch. 

   - c. Als een leverancierswitch is ingediend met dezelfde mutatiedatum als een reeds ontvangen leverancierswitch of inhuizing, zal de eerder ontvangen leverancierswitch of inhuizing worden geannuleerd/overschreven. Voor de geannuleerde/overschreven leverancierswitch of inhuizing wordt een LOSS verstuurd. 

## 4.8.3 Termijnen KA

- a. Een ‘melding leverancierswitch’ kan in de periode één werkdag voor de mutatiedatum tot en met de mutatiedatum worden ingediend. 

- b. Een uitzondering wordt gemaakt voor allocatiepunten waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet, waar een ‘melding leverancierswitch’ kan worden ingediend in de periode 20 werkdagen voor de mutatiedatum tot en met één werkdag voor mutatiedatum. 

- c. Bij verwerking van de ‘melding leverancierswitch’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de ‘melding leverancierswitch’ 

over het resultaat door middel van een GAIN/LOSS. Bij afwijzing van de ‘melding leverancierswitch’ ontvangt alleen de initiërende leverancier een afwijzing van de systeembeheerder. 

- d. Na acceptatie van de ‘melding leverancierswitch’ voorziet de systeembeheerder de nieuwe balanceringsverantwoordelijke uiterlijk de werkdag na ontvangst van de ‘melding leverancierswitch’ van de gegevens die deze balanceringsverantwoordelijke nodig heeft voor het opstellen van zijn prognoses. Dit doet de systeembeheerder door middel van het bericht Stamgegevens na GAIN. 

## 4.8.4 Procesafspraken GA

- a. De initiërende leverancier draagt er zorg voor dat hij een machtiging heeft voor het uitvoeren van de leverancierswitch. 

- b. De initiërende leverancier draagt er zorg voor dat hij van de klant minimaal die gegevens verkrijgt die nodig zijn voor het achterhalen van de EAN-code van het allocatiepunt. 

- c. Indien de aansluiting fysiek is afgesloten, dan dient de aangeslotene contact op te nemen met de systeembeheerder om heraansluiting aan te vragen. 

- d. Indien op de mutatiedatum geen actieve leverancier aanwezig is in het aansluitingenregister, dan wordt de ‘melding leverancierswitch’ door de systeembeheerder goedgekeurd indien door de initiërende leverancier de naam van de aangeslotene in de ‘melding leverancierswitch’ is opgenomen; indien het een zakelijke klant betreft wordt de bedrijfs- of instellingsnaam daartoe opgenomen in het veld achternaam. 

- e. Indien op de mutatiedatum geen actieve leverancier aanwezig is in het aansluitingenregister, en de initiërende leverancier beschikt over een KvK-nummer van de aangeslotene dan is het verplicht dit in te vullen in de ‘melding leverancierswitch’. 

- f. Indien op de mutatiedatum geen actieve leverancier aanwezig is in het aansluitingenregister en de leverancierswitch een additioneel allocatiepunt betreft, dan worden de naam van de aangeslotene en het KvK-nummer door de initiërende leverancier niet in de ‘melding leverancierswitch’ opgenomen. Indien dit wel gebeurt, worden deze velden door de systeembeheerder genegeerd bij de verwerking van de melding leverancierswitch. 

- g. Wanneer een leverancierswitch wordt ingediend voor een allocatiepunt dat op de mutatiedatum de fysieke status ‘in aanleg’ heeft, of de fysieke status is ‘uit bedrijf’ waarbij de meetinrichting is verwijderd, wordt er voor de mutatiedatum geen meterstand vastgesteld. 

## 4.8.5 Procesbeschrijving GA

Bijlage B1099: Subprocesplaat SP0007 GA

1. De initiërende leverancier verstuurt de ‘melding leverancierswitch’, tenminste vijf werkdagen voor de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum, naar de systeembeheerder. 

2. De systeembeheerder beoordeelt de ‘melding leverancierswitch’ op de volgende punten: 

   - a. Is de ‘melding leverancierswitch’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt datum van indienen tenminste vijf werkdagen en maximaal 20 werkdagen voor de mutatiedatum? 

   - d. Is de naam van de aangeslotene ingevuld indien de ‘melding leverancierswitch’ voor een allocatiepunt is ingediend in geval van leegstand? 

   - e. Is de initiërende leverancier als onderneming bekend bij de systeembeheerder (en is het vanuit de toezichthouder toegestaan om aanvragen van deze leverancier in behandeling te nemen)? 

   - f. Heeft de opgegeven balanceringsverantwoordelijke een erkenning volgens het BRPregister (elektriciteit of gas)? 

   - g. Is er geen andere melding leverancierswitch of inhuizing met een latere mutatiedatum ontvangen? 

   - h. Is het allocatiepunt niet geblokkeerd voor geautomatiseerde mutaties? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding leverancierswitch’ af, en verstuurt de systeembeheerder een afwijsbericht naar de initiërende leverancier uiterlijk de werkdag na ontvangst van de ‘melding leverancierswitch’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De gewenste mutatiedatum ligt buiten het venster van tenminste vijf werkdagen en maximaal 20 werkdagen in de toekomst. 

   - d. De naam van de aangeslotene is niet ingevuld terwijl leegstand bestaat op de gewenste mutatiedatum in de ‘melding leverancierswitch’ van een primair allocatiepunt. 

   - e. De initiërende leverancier is niet als onderneming bekend bij de systeembeheerder (of het is vanuit de toezichthouder niet toegestaan om aanvragen van deze leverancier in behandeling te nemen). 

   - f. De opgegeven balanceringsverantwoordelijke heeft geen erkenning volgens het BRPregister. 

   - g. Er is reeds een andere melding van een inhuizing of leverancierswitch met een latere mutatiedatum ontvangen (kruisend proces). 

   - h. Het allocatiepunt is geblokkeerd voor geautomatiseerde mutaties. 

4. De initiërende leverancier verwerkt de afwijzing. 

5. Als alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding leverancierswitch’ van de initiërende leverancier en verstuurt de systeembeheerder het bericht GAIN naar de initiërende leverancier, de nieuwe balanceringsverantwoordelijke en de meetverantwoordelijke partij, de Stamgegevens na GAIN naar de balanceringsverantwoordelijke en, als deze partijen aanwezig zijn, het bericht LOSS naar de oude leverancier en de oude balanceringsverantwoordelijke. De GAIN-, Stamgegevens na GAIN- en LOSS-berichten worden uiterlijk de werkdag na ontvangst van de ‘melding leverancierswitch’ verstuurd. 

6. De initiërende leverancier ontvangt en verwerkt het bericht GAIN. 

7. De oude leverancier, indien aanwezig, ontvangt en verwerkt het bericht LOSS. 

8. De nieuwe balanceringsverantwoordelijke ontvangt en verwerkt het bericht GAIN en stamgegevens. 

9. De oude balanceringsverantwoordelijke, indien aanwezig, ontvangt en verwerkt het bericht LOSS. 

10. De meetverantwoordelijke partij, indien aanwezig, ontvangt en verwerkt het bericht GAIN. 

11. De systeembeheerder: 

   - a. Plant de melding van de initiërende leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

   - b. Verwijdert eerder ontvangen maar nog niet geëffectueerde meldingen voor uithuizing, einde levering of BRP-switch met dezelfde of een latere mutatiedatum dan de leverancierswitch. 

   - c. Als een leverancierswitch is ingediend met dezelfde mutatiedatum als een reeds ontvangen leverancierswitch of inhuizing, zal de eerder ontvangen leverancierswitch of inhuizing worden geannuleerd/overschreven. Voor de geannuleerde/overschreven leverancierswitch of inhuizing wordt een LOSS verstuurd. 

## 4.8.6 Termijnen GA

- a. Een ‘melding leverancierswitch’ kan in de periode 20 werkdagen tot en met vijf werkdagen voor mutatiedatum worden ingediend. 

- b. Bij verwerking van de ‘melding leverancierswitch’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de ‘melding leverancierswitch’ over het resultaat door middel van een GAIN/LOSS. Bij afwijzing van de ‘melding leverancierswitch’ ontvangt alleen de initiërende leverancier een afwijzing van de systeembeheerder. 

- c. Na acceptatie van de ‘melding leverancierswitch’ voorziet de systeembeheerder de nieuwe balanceringsverantwoordelijke uiterlijk de werkdag na ontvangst van de ‘melding leverancierswitch’ van de gegevens die deze balanceringsverantwoordelijke nodig heeft voor het opstellen van zijn prognoses. Dit doet de systeembeheerder door middel van het bericht Stamgegevens na GAIN. 

## 4.8.7 Gegevensuitwisseling

### Melding leverancierswitch

|**Melding leverancierswitch door nieu**|**we leve**|**rancier**||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Referentie|O|O|O|Ja|Ja|1||
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1||
|Voorletters aangeslotene|O|O|O|Ja|Ja|1||
|Tussenvoegsel aangeslotene|O|O|O|Ja|Ja|1||
|Achternaam aangeslotene|O|O|O|Ja|A|1|Van toepassing indien er sprake is van een primair<br>allocatiepunt. Bij een zakelijke aangeslotene wordt de<br>bedrijfs- of instellingsnaam hier ingevuld.|
|Geboortedatum|O|O|O|Ja|A|1|Verplicht indien de leverancier beschikt over de<br>geboortedatum en er sprake is van een primair<br>allocatiepunt.|
|KvK-nummer|O|O|O|Ja|A|1|Verplicht indien de leverancier beschikt over het KvK-<br>nummer en er sprake is van eenprimair allocatiepunt.|
|_Correspondentieadres:_||||||||
|Straatnaam / Postbus|A|O|O|Ja|A|1|Verplicht bij KA indien dit afwijkt van het aansluitadres en|
|Huisnummer / Postbusnummer|A|O|O|Ja|A|1|er sprake is van een primair allocatiepunt .|
|Huisnummer-toevoeging|A|O|O|Ja|A|1||
|Postcode|A|O|O|Ja|A|1||
|Woonplaats|A|O|O|Ja|A|1||
|Land|A|O|O|Ja|A|1||

### Afwijzing naar de leverancier

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GV**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens<br>technische redenen is afgewezen|
|Proces ID|V|V|V|Ja|Ja|1|Leverancierswitch|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|Afwijsreden|V|V|V|Ja|Ja|n|Indicatie van de reden waarom de melding is<br>afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister<br>van<br>de<br>systeembeheerder.<br>•<br>De gewenste mutatiedatum ligt buiten het<br>venster van tenminste vijf werkdagen en<br>maximaal 20 werkdagen in de toekomst.<br>•<br>De naam van de aangeslotene is niet ingevuld<br>terwijl leegstand bestaat op de gewenste<br>mutatiedatum<br>in<br>de<br>‘melding<br>leverancierswitch’<br>van<br>een<br>primair<br>allocatiepunt.<br>•<br>De<br>initiërende<br>leverancier<br>is<br>niet<br>als<br>onderneming bekend bij de systeembeheerder<br>(of het is vanuit de toezichthouder niet<br>toegestaan<br>om<br>aanvragen<br>van<br>deze<br>leverancier in behandeling te nemen).<br>•<br>De opgegeven balanceringsverantwoordelijke<br>heeft geen volledige erkenning volgens het<br>BRP-register.|

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GV**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
||||||||•<br>Er is reeds een andere melding van een<br>inhuizing of leverancierswitch met een latere<br>mutatiedatum ontvangen.<br>•<br>Het<br>allocatiepunt<br>is<br>geblokkeerd<br>voor<br>geautomatiseerde mutaties.|
|Toelichtingafwijsreden|O|O|O|Ja|Ja|n||

### GAIN naar de nieuwe leverancier en balanceringsverantwoordelijke

|**GAIN naar nieuwe leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Leverancierswitch|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code nieuwe balanceringsverantwoordelijke|
|EAN-code leverancier|A|A|A|Ja|Ja|1|EAN-code oude leverancier. Alleen gevuld als een<br>leverancier geregistreerd was in het aansluitingenregister<br>tot de mutatiedatum.|

|**GAIN naar nieuwe balanceringsver**|**antwoord**|**elijke**||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Leverancierswitch|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|Nieuwe leverancier|V|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code nieuwe balanceringsverantwoordelijke|

### Stamgegevens na GAIN

|**Stamgegevens na GAIN naar nieuw**|**e balanceri**|**ngsvera**|**ntwoord**|**elijke**||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Leverancierswitch|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code balanceringsverantwoordelijke|
|Productsoort|V|V|V|Ja|Ja|1|Elektriciteit of gas|
|Systeemgebied|A|A|A|Ja|Ja|1||
|Leveringsrichting|A|A|A|Ja|Ja|1|Alleen verplicht als de aansluiting in bedrijf genomen is|
|Wijze van bemeting|V|V|V|Ja|Ja|1|De verschillende manieren van bemeten:<br>•<br>Onbemeten<br>•<br>Jaarlijks<br>•<br>Maandelijks<br>•<br>Telemetrie<br>•<br>Niet continu<br>•<br>Anders bemeten<br>•<br>Onbekend|
|Profielcategorie|A|A|A|Ja|Ja|1|Een in bedrijf zijnde allocatiepunt heeft verplicht een<br>profiel/afnamecategorie, tenzij het een telemetrisch<br>gealloceerde allocatiepunt op een grote aansluiting<br>elektriciteit betreft:<br>•<br>Elektriciteit: E1A, E1B, E1C, E2A, E2B, E3, E4A, OPC<br>•<br>Gas: G1A,G2A,G2C,GGV,GXX,GIS,GIN|

|**Stamgegevens na GAIN naar nieuw**|**e balanceri**|**ngsvera**|**ntwoorde**|**lijke**|||
|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**<br>**Opmerking**|
|Fysieke status|V|V|V|Ja|Ja|1<br>Een indicatie van de fysieke status van een allocatiepunt:<br>•<br>In aanleg<br>•<br>In bedrijf<br>•<br>Uit bedrijf<br>•<br>Verwijderd|
|Leveringsstatus|V|V|V|Ja|Ja|1<br>Een<br>indicatie<br>van<br>de<br>leveringsstatus<br>van<br>een<br>allocatiepunt, afhankelijk of een leverancier en<br>balanceringsverantwoordelijke zijn geregistreerd op een<br>aansluiting, zijnde:<br>•<br>Actief<br>•<br>Inactief|
|Verbruikssegment|V|V|V|Ja|Ja|1|
|SJI laag tarief|O|O|O|Nee|Ja|1|
|SJI normaal tarief|O|O|O|Nee|Ja|1|
|SJA laag tarief|O|O|O|Nee|Ja|1|
|SJA normaal tarief|O|O|O|Nee|Ja|1|
|SJV|O|O|nvt|Ja|Nee|1<br>Wordt gecommuniceerd middels het veld SJA normaal<br>tarief|
|Allocatiemethode|V|V|V|Ja|Ja|1<br>Telemetrie, slimmemeterallocatie of geprofileerd|
|**GAIN naar meetverantwoordelijke**|**partij**||||||
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|Ja|Ja|1||
|Proces ID|V|V|Ja|Ja|1|Leverancierswitch|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code<br>balanceringsverantwoordelijke|V|V|Ja|Ja|1|EAN-code nieuwe balanceringsverantwoordelijke|
|EAN-code leverancier|A|A|Ja|Ja|1|EAN-code oude leverancier. Alleen gevuld als een leverancier<br>geregistreerd was in het aansluitingenregister tot de<br>mutatiedatum.|

### LOSS naar de oude leverancier en balanceringsverantwoordelijke

|**LOSS naar oude leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Leverancierswitch|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code nieuwe leverancier|
|EAN-code leverancier|V|V|V|Ja|Ja|1|EAN-code oude leverancier|

|**LOSS naar oude balanceringsveran**|**twoordelij**|**ke**||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GV**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Leverancierswitch|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1|EAN-code oude balanceringsverantwoordelijke|
