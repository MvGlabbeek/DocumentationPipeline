# 4.10 SP0036 & SP0006: Indienen ‘melding vooraankondiging einde levering’ (KA) & Indienen en beoordelen ‘melding einde levering’ (KA & GA)


## 4.10.1 Procesafspraken KA

   - a. Het beëindigen van de leveringsverantwoordelijkheid van een leverancier voor een allocatiepunt betekent dat de leverancier als verantwoordelijk leverancier wordt verwijderd uit het aansluitingenregister. De leverancier kan zijn leveringsverantwoordelijkheid beëindigen door de ‘melding einde levering’ aan de systeembeheerder te sturen en hiermee de systeembeheerder te vragen hem als verantwoordelijk leverancier uit het aansluitingenregister te halen. 

   - b. Middels het beëindigen van de leveringsovereenkomst worden de contractuele afspraken tussen de leverancier en klant betreffende de levering op het allocatiepunt beëindigd. 

   - c. Voorwaarden aan beëindiging leveringsverantwoordelijkheid: 

      - i. Indien een leverancier de leveringsverantwoordelijkheid wil beëindigen dan dient de leverancier de klant tijdig, zijnde 20 werkdagen voor de gewenste datum van de beëindiging van de leveringsverantwoordelijkheid te informeren. 

      - ii. Een ‘melding einde levering’ dient voorafgegaan te worden door een ‘melding vooraankondiging einde levering’ 10 werkdagen voor de voorgenomen einde leveringsdatum vanuit de leverancier aan de systeembeheerder. 

      - iii. Na ontvangst van de ‘melding vooraankondiging einde levering’ van de leverancier aan de systeembeheerder over het voornemen om de leveringsverantwoordelijkheid te beëindigen voor een allocatiepunt, informeert de systeembeheerder de aangeslotene dat de aangeslotene de keuze heeft om alsnog een leveringsovereenkomst aan te gaan ofwel in geval van een additioneel allocatiepunt om een opdracht te geven voor het verwijderen van het betreffende additionele allocatiepunt ofwel, indien hij geen keuze maakt het afsluiten van het primaire allocatiepunt en bijbehorende additionele allocatiepunten. 

   - d. Na de melding van de leverancier om de leveringsverantwoordelijkheid te beëindigen, zal binnen 10 werkdagen na de mutatiedatum een eerste poging worden gedaan om de allocatiepunt af te sluiten. 

   - e. Bij een ingediende ‘melding einde levering’ die nog niet geëffectueerd is, kan het zijn dat de initiërende leverancier door een inhuizing of leverancierswitch geforceerd een uithuizing krijgt. De door de initiërende leverancier ingediende ‘melding einde levering’ wordt geannuleerd en de leverancier is in deze situatie niet de initiërende leverancier, maar de oude leverancier binnen het proces Leverancierswitch of Inhuizing. De oude leverancier wordt hiervan middels een LOSS-bericht op de hoogte gesteld. 

   - f. Indien de systeembeheerder bij fysieke afsluiting een fysieke opname heeft kunnen verrichten, dan kan de systeembeheerder deze fysieke opname op twee manieren aan het proces ‘einde levering’ koppelen: 

      - i. Als de fysieke opname heeft plaatsgevonden voordat de leverancier een meterstand heeft vastgesteld, kan de systeembeheerder de fysieke opname via een meterstandenbericht naar de leverancier sturen. Deze fysieke opname wordt door de systeembeheerder op de mutatiedatum gezet. 

      - ii. Als de fysieke opname heeft plaatsgevonden nadat de leverancier een meterstand heeft vastgesteld, kan de systeembeheerder de fysieke opname via het proces Dispuut 

over meterstanden als alternatieve meterstand voor het proces ‘Einde levering’ naar de leverancier sturen. 

- g. De systeembeheerder verwerkt de ‘melding einde levering’ nadat alle verzoeken voor inhuizing en leverancierswitch voor de desbetreffende mutatiedatum zijn verwerkt. 

- h. Wanneer een ‘melding einde levering’ wordt ingediend voor een allocatiepunt met de fysieke status ‘in aanleg’ of ‘uit bedrijf’, wordt er voor de mutatiedatum geen meterstand vastgesteld. 

## 4.10.2 Procesbeschrijvingen KA

### Melding vooraankondiging einde levering

Bijlage B1102: Subprocesplaat SP0036 KA – Melding vooraankondiging einde levering

1. De initiërende leverancier informeert de klant tenminste 20 werkdagen vooraf over zijn voornemen om het contract met de klant te beëindigen. De leverancier volgt hierbij de voorwaarden van de Energieregeling, afdeling 2.4. Aan de klant worden de volgende zaken gecommuniceerd: 

   - a. De leverancier geeft aan dat hij het voornemen heeft om het contract met de klant op de mutatiedatum te ontbinden. 

   - b. De leverancier geeft aan dat de systeembeheerder het allocatiepunt zal afsluiten. In geval van een additioneel allocatiepunt geeft hij daarnaast ook aan dat de aangeslotene in plaats hiervan ook kan kiezen voor het aan de systeembeheerder geven van een opdracht voor het verwijderen van het betreffende additionele allocatiepunt. 

#### Melding einde levering

Bijlage B1103: Subprocesplaat SP0006 KA – Melding einde levering

1. De leverancier verstuurt de ‘melding einde levering’, één werkdag voor de mutatiedatum, naar de systeembeheerder. 

Een uitzondering wordt gemaakt voor allocatiepunten waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet, waar een ‘melding einde levering’ tenminste op de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum kan worden ingediend. 

2. De systeembeheerder beoordeelt de melding op de volgende punten: 

   - a. Is de ‘melding einde levering’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt de datum van indienen tenminste één werkdag voor en maximaal 20 werkdagen voor de gewenste mutatiedatum? 

   - d. Is er geen andere nog niet geëffectueerde melding leverancierswitch, inhuizing, uithuizing of einde levering ontvangen voor een eerdere of dezelfde mutatiedatum? 

   - e. Is de leverancier geregistreerd als actuele leverancier op het allocatiepunt? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding einde levering’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst van de ‘melding einde levering’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De gewenste mutatiedatum ligt buiten het venster van tenminste één werkdag en maximaal 20 werkdagen in de toekomst; 

   - d. Er is reeds een nog niet geëffectueerde melding van een leverancierswitch, inhuizing, uithuizing of einde levering ontvangen, waarvan de mutatiedatum op of voor de mutatiedatum van de einde levering ligt. 

   - e. De leverancier staat niet als actuele leverancier geregistreerd op het allocatiepunt. 

4. De leverancier verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding einde levering’, van de leverancier en verstuurt hij het bericht LOSS naar de leverancier en de balanceringsverantwoordelijke. De LOSS berichten worden uiterlijk de werkdag na ontvangst van de ‘melding einde levering verstuurd. 

6. De leverancier ontvangt en verwerkt het bericht LOSS. 

7. De balanceringsverantwoordelijke ontvangt en verwerkt het bericht LOSS. 

8. De systeembeheerder: 

   - a. Plant de melding van de leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

   - b. Verwijdert de door de leverancier ingediende maar nog niet geëffectueerde meldingen voor BRP-switch met dezelfde of een latere mutatiedatum dan de einde levering; 

   - c. Plant activiteiten in om de aansluiting fysiek af te sluiten respectievelijk het additionele allocatiepunt te verwijderen. 

## 4.10.3 Termijnen KA

- a. De leverancier zorgt ervoor dat de klant minimaal 20 werkdagen voor de datum van beëindiging van de leveringsovereenkomst hierover geïnformeerd is, en dat de ‘melding einde levering’ voorafgegaan is door een ‘melding vooraankondiging einde levering’. 

- b. Een ‘melding vooraankondiging einde levering’ wordt 10 werkdagen voor de mutatiedatum ingediend. 

- c. Een ‘melding einde levering’ kan in de periode één werkdag voor de mutatiedatum worden ingediend. 

- d. Een uitzondering wordt gemaakt voor allocatiepunten waarvoor een beroep wordt gedaan op artikel 2.17, tweede lid, onderdeel c van de Energiewet waar een ‘melding einde levering’ kan worden ingediend in de periode 20 werkdagen voor de mutatiedatum tot en met één werkdag voor de mutatiedatum. 

- e. Bij verwerking van de ‘melding einde levering’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de ‘melding einde levering’ over het resultaat door middel van een LOSS. Bij afwijzing van de ‘melding einde levering’ ontvangt alleen de leverancier een afwijzing van de systeembeheerder. 

- f. De ‘melding einde levering’ een impliciete opdracht van de leverancier aan de systeembeheerder om het allocatiepunt binnen 10 werkdagen na de mutatiedatum fysiek af 

te sluiten. De systeembeheerder moet binnen 10 werkdagen na mutatiedatum minimaal een eerste poging hebben gedaan om het allocatiepunt fysiek af te sluiten. Aanvullend hierop kan de aangeslotene bij een additioneel allocatiepunt in plaats hiervan ook kiezen voor het geven van een opdracht voor het verwijderen van het betreffende additionele allocatiepunt. 

## 4.10.4 Procesafspraken GA

- a. Het beëindigen van de leveringsverantwoordelijkheid van een leverancier voor een allocatiepunt betekent dat de leverancier als verantwoordelijk leverancier wordt verwijderd uit het aansluitingenregister. De leverancier kan zijn leveringsverantwoordelijkheid beëindigen door een ‘melding einde levering’ aan de systeembeheerder te sturen en hiermee de systeembeheerder te vragen hem als verantwoordelijk leverancier uit het aansluitingenregister te halen. 

- b. Middels het beëindigen van de leveringsovereenkomst worden de contractuele afspraken tussen de leverancier en klant betreffende de levering op het allocatiepunt beëindigd. 

- c. Voorwaarden voor beëindiging leveringsverantwoordelijkheid: 

   - i. Indien een leverancier de leveringsverantwoordelijkheid wil beëindigen dan dient de leverancier de klant tijdig (minimaal 20 werkdagen voor de gewenste datum van de beëindiging van de leveringsverantwoordelijkheid) te informeren over de beëindiging van het contract, en te informeren over de afsluiting door de systeembeheerder. 

   - ii. De systeembeheerder informeert de aangeslotene de werkdag na ontvangst van de ‘melding einde levering’ per brief over de ontstane situatie. De systeembeheerder geeft aan dat er na de mutatiedatum fysiek wordt afgesloten indien er zich geen leverancier heeft gemeld en indien (in geval van een additioneel allocatiepunt) de aangeslotene geen opdracht heeft gegeven voor het verwijderen van het betreffende additionele allocatiepunt. De systeembeheerder plant de fysieke afsluiting in en de geplande datum voor fysieke afsluiting wordt naar de aangeslotene gecommuniceerd. 

- d. Na de melding van de leverancier om de leveringsverantwoordelijkheid te beëindigen, zal binnen 10 werkdagen na de mutatiedatum een eerste poging worden gedaan om het allocatiepunt af te sluiten. 

- e. Bij een ingediende ‘melding einde levering’ die nog niet geëffectueerd is, kan het zijn dat de initiërende leverancier door een inhuizing of leverancierswitch geforceerd een uithuizing krijgt. De door de initiërende leverancier ingediende ‘melding einde levering’ wordt geannuleerd en de leverancier is in deze situatie niet de initiërende leverancier, maar de oude leverancier binnen het proces Leverancierswitch of inhuizing. De oude leverancier wordt hiervan middels een LOSS-bericht op de hoogte gesteld. 

- f. Wanneer een ‘melding einde levering’ wordt ingediend voor een allocatiepunt dat, op de mutatiedatum de fysieke status ‘in aanleg’ of ‘uit bedrijf’ heeft, wordt er voor de mutatiedatum geen meterstand vastgesteld. 

- g. Bij het verwerken van de ‘melding einde levering’ in het aansluitingenregister wordt de meetverantwoordelijke partij op het allocatiepunt niet uit het aansluitingenregister verwijderd. 

- h. De meetverantwoordelijke partij stelt bij een einde levering een meterstand vast voor de mutatiedatum en berekent het bijbehorende volume. 

## 4.10.5 Procesbeschrijving GA

Bijlage B1104: Subprocesplaat SP0006 GA

1. De leverancier verstuurt de ‘melding einde levering’, tenminste 12 werkdagen voor de mutatiedatum en ten hoogste 20 werkdagen voor de mutatiedatum, naar de systeembeheerder. 

2. De systeembeheerder beoordeelt de melding op de volgende punten: 

   - a. Is de ‘melding einde levering’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Ligt datum van indienen tenminste 12 werkdagen voor en maximaal 20 werkdagen voor de gewenste mutatiedatum? 

   - d. Is er geen nog niet geëffectueerde melding voor leverancierswitch, inhuizing, uithuizing of einde levering ontvangen voor een eerdere of dezelfde mutatiedatum? 

   - e. Is de leverancier geregistreerd als actuele leverancier op het allocatiepunt? 

   - f. Is het allocatiepunt niet geblokkeerd voor geautomatiseerde mutaties? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding einde levering’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst van de ‘melding einde levering’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De gewenste mutatiedatum ligt buiten het venster van tenminste 12 werkdagen en maximaal 20 werkdagen in de toekomst. 

   - d. Er is reeds een nog niet geëffectueerde melding van een leverancierswitch, inhuizing, uithuizing of einde levering ontvangen, waarvan de mutatiedatum op of voor de mutatiedatum van de einde levering ligt (kruisend bericht). 

   - e. De leverancier staat niet als actuele leverancier geregistreerd op het allocatiepunt. 

   - f. Het allocatiepunt is geblokkeerd voor geautomatiseerde mutaties. 

4. De leverancier verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding einde levering’ van de leverancier en verstuurt de systeembeheerder het bericht LOSS naar de leverancier, de balanceringsverantwoordelijke en de meetverantwoordelijke partij. De LOSS berichten worden uiterlijk de werkdag na ontvangst van de ‘melding einde levering’ verstuurd. 

6. De leverancier ontvangt en verwerkt het bericht LOSS. 

7. De balanceringsverantwoordelijke ontvangt en verwerkt het bericht LOSS. 

8. De meetverantwoordelijke partij ontvangt en verwerkt het bericht LOSS. 

9. De systeembeheerder: 

   - a. Plant de melding van de leverancier in voor effectuering op de in de melding aangegeven datum in het aansluitingenregister. 

   - b. Verwijdert de door de initiërende leverancier ingediende maar nog niet geëffectueerde aanvragen voor BRP-switch met dezelfde of een latere mutatiedatum dan de einde levering; 

   - c. Informeert de werkdag na ontvangst van het verzoek per aangetekende brief de aangeslotene over het voornemen tot fysieke afsluiting over te gaan. In geval van een additioneel allocatiepunt geeft hij daarnaast ook aan dat de aangeslotene in plaats hiervan ook kan kiezen voor het verstrekken van een opdracht voor het verwijderen van het betreffende additionele allocatiepunt. 

   - d. Plant activiteiten in om het allocatiepunt fysiek af te sluiten respectievelijk het additionele allocatiepunt te verwijderen. 

## 4.10.6 Termijnen GA

- a. Een ‘melding einde levering’ kan in de periode 20 tot en met 12 werkdagen voor de gewenste mutatiedatum worden ingediend. 

- b. Bij verwerking van de ‘melding einde levering’ informeert de systeembeheerder alle betrokken marktpartijen uiterlijk de werkdag na ontvangst van de ‘melding einde levering’ over het resultaat door middel van een LOSS. Bij afwijzing van de ‘melding einde levering’ ontvangt alleen de leverancier een afwijzing van de systeembeheerder. 

## 4.10.7 Gegevensuitwisseling

### Vooraankondiging einde leveringsmelding

|**Vooraankondiging einde leveringsme**|**lding do**|**or levera**|**ncier**|||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|O|Ja|Ja|1||
|EAN-code systeembeheerder|V|Ja|Ja|1||
|EAN-code leverancier|V|Ja|Ja|1||
|Mutatiedatum|V|Ja|Ja|1|Voorgenomen mutatiedatum|
|Contactgegevens aangeslotene|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt<br>De leverancier hoeft deze contactgegevens niet op te leveren, het is geheel<br>optioneel. Het is aan de leverancier om te beoordelen of hij deze gegevens<br>wil en mag (in het kader vanprivacy)verstrekken.|
|Achternaam|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Tussenvoegsel|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Voorletters|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Straatnaam|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Huisnummer|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Huisnummer toevoeging|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Postcode|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Plaatsnaam|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Landcode|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|Telefoonnummer|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|
|E-mailadres|O|Ja|A|1|Ja in geval van primair allocatiepunt, nee in geval van additioneel<br>allocatiepunt|

### Melding einde levering

|**Melding einde levering door lever**|**ancier**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Referentie|O|O|O|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|Mutatiedatum|V|V|V|Ja|Ja|1|Voorgenomen mutatiedatum|

### Afwijzing

|**Afwijzing naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens technische<br>redenen is afgewezen|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||
|Mutatiedatum|V|V|V|Ja|Ja|1||
|Afwijsreden|V|V|V|Ja|Ja|n|Indicatie van de reden waarom de melding is<br>afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister van de systeembeheerder.<br>•<br>De gewenste mutatiedatum ligt buiten het<br>indienvenster.<br>•<br>Er is reeds een nog niet geëffectueerde melding<br>van een leverancierswitch, inhuizing, uithuizing<br>of einde levering ontvangen, waarvan de<br>mutatiedatum op of voor de mutatiedatum van<br>de einde levering ligt.<br>•<br>De leverancier staat niet als actuele leverancier<br>geregistreerd op het allocatiepunt.<br>•<br>Het<br>allocatiepunt<br>is<br>geblokkeerd<br>voor<br>geautomatiseerde mutaties.|
|Toelichtingafwijsreden|O|O|O|Ja|Ja|n||

### LOSS

|**LOSS naar leverancier**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Einde levering|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|V|Ja|Ja|1||

|**LOSS naar balanceringsverantwoor**|**delijke**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|V|V|V|Ja|Ja|1||
|Proces ID|V|V|V|Ja|Ja|1|Einde levering|
|Mutatiedatum|V|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|V|V|Ja|Ja|1||

|**LOSS naar meetverantwoordelijke partij**||||||
|---|---|---|---|---|---|
|**Gegeven**<br>**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt<br>V|V|Ja|Ja|1||

|**LOSS naar meetverantwoordelijke**|**partij**||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|V|V|Ja|Ja|1||
|Proces ID|V|V|Ja|Ja|1|Einde levering|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Mutatiedatum|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|EAN-code leverancier|V|V|Ja|Ja|1||
