# 4.6 SP0022, SP0092, SP0095, SP0024, SP0053: Contracteindegegevens


Het Contracteindegegevensregister (CER) ondersteunt leveranciers bij het bepalen van de switchdatum ter voorkoming van ongewenste dubbele contractering, een periode van contractloosheid of het onbedoeld opleggen van opzegvergoedingen in verband met contractbreuk bij een allocatiepunt op een kleine aansluiting, (met uitzondering van allocatiepunten waarvoor beroep gedaan wordt op artikel 2.17, tweede lid, onderdeel c van de Energiewet). 

Het CER is een register dat leveranciers in staat stelt om te voldoen aan de op basis van de Energiewet en lagere regelgeving verplichte vastlegging van contracteindegegevens. De inhoud van deze gegevens zijn te vinden onder de procesbeschrijving ‘Aanleveren bronbestand’. Leveranciers stellen de contactgegevens van de contactpersonen belast met het proces CER beschikbaar in het Contactpersonenregister. 

In het proces CER levert de leverancier wekelijks, middels het bronbestand, zijn contracteindegegevens aan voor de vulling van het CER. De leverancier is verantwoordelijk voor het aanleveren van zijn contracten aan het CER, de systeembeheerder is verantwoordelijk voor het beheer van het CER, waaronder het vullen van het CER met de aangeleverde contracten. Tevens is het mogelijk om contracten separaat aan te melden buiten de wekelijkse aanlevering. Deze melding blijft een maand actief en na een jaar wordt deze verwijderd uit het CER. Bij de eerstvolgende aanlevering van het bronbestand dient het contract mee opgeleverd te worden. 

De leverancier kan, ten behoeve van het bepalen van de juiste contractingangsdatum van zijn leveringscontract, de contracteindegegevens uit het CER opvragen. Tevens wordt er dagelijks vanuit het CER, per leverancier (bedrijfs-EAN-code), een signalering verhuizingen verstuurd. Hierin staan de voor deze leverancier van toepassing zijnde goedgekeurde (geforceerde) uithuizingen. Hierdoor wordt een leverancier geïnformeerd over verhuizingen op een allocatiepunt waar de leverancier volgens het aansluitingenregister nog niet verantwoordelijk voor is, maar volgens het CER wel een contract (in de toekomst) mee heeft afgesloten. Dit ter voorkoming van onterechte leverancierswitches. 

## 4.6.1 SP0022 Procesafspraken Aanleveren bronbestand CER KA

- a. De leverancier levert wekelijks, middels het bronbestand, zijn contracteindegegevens voor zijn allocatiepunten op een kleine aansluiting (met uitzondering van allocatiepunten waarvoor een beroep gedaan wordt op artikel 2.17, tweede lid, onderdeel c van de Energiewet) aan voor de vulling van het CER. 

- b. Indien in het bronbestand allocatiepunten zijn opgenomen waarvoor een beroep gedaan wordt op artikel 2.17, tweede lid, onderdeel c van de Energiewet worden deze allocatiepunten wel opgenomen in het CER. 

- c. Het CER wordt door de systeembeheerder wekelijks opnieuw opgebouwd. 

- d. Indien het bronbestand volledig wordt afgewezen en de termijn voor aanlevering is nog niet verlopen, dan is het mogelijk om opnieuw een bestand aan te leveren. 

- e. Indien een bronbestand niet binnen de daarvoor geldende termijn wordt opgeleverd, dan zal het meest recent aangeleverde en correct verwerkte bronbestand worden verwerkt. De contactpersoon van de leverancier wordt hierover geïnformeerd. 

- f. Indien het bronbestand langer dan vier weken niet wordt aangeleverd, dan wordt er geen bronbestand ingelezen. Dit betekent dat er vanaf dit moment voor deze leverancier geen contracten staan geregistreerd. 

- g. Het is mogelijk voor een leverancier om een bronbestand aan te leveren zonder contracten (een leeg bronbestand). Hierdoor zijn er voor deze leverancier geen contracten meer aanwezig in het CER en zijn de contracten van deze leverancier niet meer beschermd. Dit zou bijvoorbeeld kunnen in het geval van een afroep van de Procedure Leveringszekerheid. 

- h. De contracteindegegevens worden per bedrijfs-EAN-code van de leverancier aan het CER aangeleverd. 

- i. Leveranciers leveren middels het bronbestand aan het CER op: alle contracten, voor zowel elektriciteit als gas, waarvan de contract einddatum onbepaald is of in de toekomst ligt. 

   - Indien de bestaande leverancier het proces Einde levering heeft opgestart, dan wordt het contract niet meer aan het CER aangeleverd. 

- j. Het CER verwerkt het bronbestand per contract en eventuele functionele uitval wordt als afwijzing per contract teruggekoppeld. 

- k. De terugkoppeling van de afwijzing per contract gebeurt met de teruggave van het volledige record zoals aangeleverd in het bronbestand. 

## 4.6.2 Procesbeschrijving KA

Bijlage B1090: Subprocesplaat SP0022 KA

1. De leverancier stelt zijn bronbestand ten behoeve van het CER samen. Dit bronbestand bestaat uit de volgende contracteindegegevens: 

   - a. De EAN-code van het allocatiepunt 

   - b. De einddatum van de leveringsovereenkomst 

   - c. De opzegtermijn 

   - d. De EAN-code van de leverancier 

2. De leverancier verstuurt het bronbestand naar het CER. 

3. Het CER ontvangt het bronbestand. Hierbij wordt het bestand beoordeeld op de volgende punten: 

   - a. Is het bronbestand syntactisch correct? 

   - b. Is de EAN-code van de leverancier bekend in het leveranciersregister? 

4. Indien één van de controles een negatief resultaat oplevert, wijst het CER het bronbestand af, en verstuurt het CER een afwijsbericht naar de leverancier. De afwijsredenen die het CER kan hebben zijn: 

   - a. Het bestand is syntactisch fout. 

   - b. De EAN-code van de leverancier is onbekend. 

5. De leverancier verwerkt de afwijzing. 

6. Indien alle controles een positief resultaat opleveren, verwerkt het CER het bronbestand. Bij de verwerking van het bronbestand worden de volgende punten gecontroleerd door het CER: 

   - a. Is de EAN-code van de leverancier in het contracteindegegeven gelijk aan de EAN-code van de marktpartij in de bestandsnaam? 

   - b. Is de EAN-code van het allocatiepunt correct? 

   - c. Heeft de einddatum van het contract het juiste formaat? 

   - d. Ligt de einddatum van de leveringsovereenkomst in de toekomst? 

   - e. Heeft het contract een geldige opzegtermijn die groter of gelijk is aan 0 en kleiner of gelijk is aan 30 kalenderdagen? 

7. Indien, na verwerking van het bronbestand, één van de controles een negatief resultaat oplevert, verstuurt het CER een afwijsbericht per EAN-code van het allocatiepunt naar de leverancier. De afwijsredenen die per EAN-code kunnen worden gegeven zijn: 

   - a. De EAN-code van de leverancier in het contracteindegegeven is niet gelijk aan de EANcode van de marktpartij in de bestandsnaam. 

   - b. De EAN-code van het allocatiepunt is niet correct. 

   - c. Bestand is syntactisch onjuist (omdat de datumnotatie niet correct is). 

   - d. De einddatum van de leveringsovereenkomst ligt niet in de toekomst. 

   - e. Ongeldige opzegtermijn in het contract. 

8. De leverancier verwerkt de eventuele afwijzingen. 

## 4.6.3 Termijnen KA

- a. De bronbestanden voor de vulling van het CER worden wekelijks uiterlijk op de laatste werkdag van de week voor 12:00 aangeleverd. Daarbij geldt dat het laatst correct aangeleverde bestand zal worden gebruikt voor de vulling van het CER. Het CER verwerkt de aangeleverde bestanden op zaterdag tussen 00:00 en 07:00. 

- b. De leverancier ontvangt binnen een uur na versturen van het bronbestand de terugkoppeling of het bronbestand juist is ontvangen. 

- c. Zodra het bronbestand door het CER verwerkt is, worden uiterlijk de eerste werkdag na verwerking de afwijzingen aan de leverancier opgeleverd. 

## 4.6.4 Gegevensuitwisseling

### Aanlevering

|**Aanlevering bronbestand**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|Contract einddatum|O|1|Is optioneel indien onbepaalde tijd contract. Einddatum van het contract is een tot-<br>datum|
|Opzegtermijn|V|1|De opzegtermijn van het contract. Wordt weergegeven in kalenderdagen en is groter<br>ofgelijk aan 0 en kleiner ofgelijk aan 30.|
|EAN-code leverancier|V|1||

### Afwijzing op aanlevering

|**Afwijzing op aanlevering**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|Afwijsreden|V|1|•<br>Indicatie van de reden waarom de melding is afgewezen: Het bestand is|
||||syntactisch fout.|
||||•<br>De EAN-code van de leverancier is onbekend.|

### Afwijzing op detailrecord

|**Afwijzing op detailrecord**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|n|Indien afgewezen allocatiepunt|
|Contract einddatum|A|n|Afhankelijk van afgewezen allocatiepunt|
|Opzegtermijn|A|n|Afhankelijk van afgewezen allocatiepunt|

|**Afwijzing op detailrecord**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code leverancier|V|1||
|Afwijsreden|A|n|Afhankelijk van afgewezen allocatiepunt<br>Indicatie van de reden waarom de melding is afgewezen:<br>•<br>De EAN-code van de marktpartij in het contracteinde is niet gelijk aan de EAN-<br>code van de marktpartij in de bestandsnaam.<br>•<br>De EAN-code van het allocatiepunt is niet correct.<br>•<br>Bestand is syntactisch onjuist (omdat de datumnotatie niet correct is).<br>•<br>De einddatum van de leveringsovereenkomst ligt niet in de toekomst.<br>•<br>Ongeldige opzegtermijn in het contract.|

## 4.6.5 SP0053 Procesafspraken Realtime melden contract KA

- a. Om direct toegang tot de gegevens in het CER, TMR en/of het aansluitingenregister te krijgen kan de leverancier realtime de aanwezigheid van een contract melden. Deze melding wordt tijdelijk geregistreerd (1 jaar) in het CER en daarna verwijderd. 

- b. De aanwezigheid van een contract kan via een synchroon-kanaal gemeld worden aan het CER per EAN-code van de leverancier. 

## 4.6.6 Procesbeschrijving KA

Bijlage B1091: Subprocesplaat SP0053 KA

1. De leverancier stuurt de ‘melding contract’ naar het CER. 

2. Het CER verwerkt de melding. Hierbij wordt de melding beoordeeld door het CER op de volgende punten: 

   - a. Is de ‘melding contract’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de leverancier bekend in het leveranciersregister? 

3. Indien één van de controles een negatief resultaat oplevert, wijst het CER de ‘melding contract’ af, en verstuurt het CER direct een afwijsbericht naar de leverancier. De afwijsredenen die het CER kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De leverancier is onbekend in het leveranciersregister. 

4. De leverancier verwerkt de afwijzing van de melding. 

5. Indien alle controles een positief resultaat opleveren, accepteert het CER de ‘melding contract’ van de leverancier en verwerkt het CER de goedgekeurde melding. 

## 4.6.7 Termijnen KA

- a. Een leverancier die realtime een contract meldt ontvangt direct een afwijzing als het meldingsbericht niet correct is. 

- b. Gedurende één maand na aanlevering van de ‘melding contract’ krijgt de desbetreffende leverancier toegang tot het CER. 

c. De ‘melding contract’ wordt gedurende één jaar geregistreerd in het CER en daarna verwijderd. 

## 4.6.8 Gegevensuitwisseling

### Melding

|**Melding contract**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|EAN-code leverancier|V|1||
|Referentie|O|1||

### Afwijzing melding

|**Afwijzing melding contract**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|EAN-code leverancier|V|1||
|Referentie|A|1|Gevuld indien meegegeven in de melding|
|Afwijsreden|V|n|Indicatie van de reden waarom de melding is afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het allocatiepunt is onbekend in het aansluitingenregister van de<br>systeembeheerder.<br>•<br>De leverancier is onbekend in het leveranciersregister.|
|Toelichting afwijsreden|O|n||

## 4.6.9 SP0022 Procesafspraken Opvragen CER KA

- a. Het opvragen van de gegevens van een contract uit het CER is alleen mogelijk indien voor het betreffende allocatiepunt: 

   - i. de desbetreffende leverancier beschikt over een toestemming van de klant; 

   - ii. een realtime melding contract door de desbetreffende leverancier is gedaan: gedurende een maand na de realtime melding van het contract; 

   - iii. door de desbetreffende leverancier een contract is opgeleverd via het wekelijkse bronbestand. 

- b. Indien de nieuwe leverancier bij de opvraag geen contractgegevens uit het CER heeft ontvangen, dan zal de nieuwe leverancier de klant voor vragen of klachten over contractbreuk doorverwijzen naar de oude leverancier. De nieuwe leverancier kan middels de opbouw van het transactiedossier aantonen wat het resultaat van de opvraag is geweest. 

- c. Het opvragen van gegevens wordt alleen uitgevoerd op de, via het wekelijkse bronbestand, aangeleverde contracten. 

- d. Bij het opvragen van de contract einddatum voor een allocatiepunt wordt altijd één contract als resultaat teruggegeven. Dit zijn de gegevens van het contract waarvan de contract einddatum het verst in de toekomst ligt. Indien bij het opvragen van de contract einddatum voor een allocatiepunt meerdere contracten aanwezig zijn met dezelfde contract einddatum (kan ook leeg zijn), dan wordt het contract met de langste opzegtermijn geselecteerd. 

- e. Indien bij een opvraag van een contract een lege contract einddatum wordt opgeleverd, dan dient de leverancier rekening te houden met de opzegtermijn voor het bepalen van de einddatum van het op te zeggen contract. De leverancier berekent de (vroegste) einddatum van het opgevraagde contract dan als volgt: einddatum = de actuele datum + de opzegtermijn. 

## 4.6.10 Procesbeschrijving KA

Bijlage B1092: Subprocesplaat SP0022 KA

1. De leverancier stuurt de ‘opvraag’ naar het CER. Deze bevat onder andere: 

   - a. EAN-code van de leverancier 

   - b. EAN-code allocatiepunt 

2. Het CER verwerkt de opvraag. Hierbij wordt de opvraag beoordeeld door het CER op de volgende punten: 

   - a. Is de opvraag volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het CER? 

   - c. Is de leverancier bekend in het leveranciersregister? 

3. Indien één van de controles een negatief resultaat oplevert, wijst het CER de ‘opvraag’ af, en verstuurt het CER direct een afwijsbericht naar de leverancier. De afwijsredenen die het CER kan hebben zijn: 

   - a. Onvolledige opvraag of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het CER. 

   - c. De opvragende leverancier is onbekend in het leveranciersregister. 

   - d. Er is geen contract aanwezig in het CER van de opvragende leverancier. 

4. De leverancier verwerkt de afwijzing van de opvraag. 

5. Indien alle controles een positief resultaat opleveren, accepteert het CER de ‘opvraag’ van leverancier en verstuurt het CER het resultaat van de ‘opvraag’ naar de leverancier. 

6. De leverancier verwerkt het resultaat. 

## 4.6.11 Termijnen KA

Alle opvragingen ontvangen door het CER worden direct verwerkt door het CER en resultaten worden direct ter beschikking gesteld. 

## 4.6.12 Gegevensuitwisseling

|**Opvraag CER**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|Referentie|O|1||
|EAN-code leverancier|V|1||

### Resultaat

|**Resultaat opvraag CER**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|Referentie|O|1|Gevuld indien meegegeven in de raadpleging|
|Transactiedossiernummer|V|1||
|Contract einddatum|O|1|Optioneel indien onbepaalde tijd contract|

|**Resultaat opvraag CER**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|Opzegtermijn|V|1||

### Afwijzing

|**Afwijzing opvraag CER**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|Referentie|O|1|Gevuld indien meegegeven in de raadpleging|
|Transactiedossiernummer|V|1||
|Afwijsreden|V|n|De indicatie van de reden waarom de melding is afgewezen:<br>•<br>Onvolledige opvraag of syntactische fout.<br>•<br>Het allocatiepunt is onbekend in het CER.<br>•<br>De opvragende leverancier is onbekend in het leveranciersregister.<br>•<br>Er isgeen contract aanwezigin het CER van de opvragende leverancier|
|Toelichting afwijsreden|O|n||

## 4.6.13 SP0092 Procesafspraken Vooraankondiging leverancierswitch

   - a. Uiterlijk één werkdag na het sluiten van een overeenkomst met een aangeslotene die de beschikking heeft over een allocatiepunt op een kleine aansluiting stuurt de initiërende leverancier een ‘vooraankondiging leverancierswitch’ aan het CER. 

   - b. Voor zover er contracten met een einddatum na de beoogde switchdatum op het allocatiepunt in het CER geregistreerd staan, brengt de systeembeheerder de reeds gecontracteerde leverancier(s) (dit kunnen er meerdere zijn) hiervan middels een bericht op de hoogte. 

   - c. Indien een leverancier (huidige of toekomstige, dit kunnen er meerdere zijn) een ‘melding vooraankondiging leverancierswitch’ vanuit het CER ontvangt, dan verstrekt deze uiterlijk de volgende werkdag indien van toepassing de voorlopige hoogte van de opzegvergoeding aan de klant. 

   - d. De ‘melding vooraankondiging leverancierswitch’ wordt alleen uitgevoerd voor de door de wekelijkse aanlevering (bronbestand) geregistreerde contracten. 

## 4.6.14 Procesbeschrijving KA

Bijlage B1093: Subprocesplaat SP0092 KA

1. Na het sluiten van een overeenkomst stuurt de initiërende leverancier de ‘vooraankondiging leverancierswitch’ aan de systeembeheerder. 

2. De systeembeheerder verwerkt de vooraankondiging. Hierbij wordt de vooraankondiging beoordeeld door de systeembeheerder op de volgende punten: 

   - a. Is de ‘vooraankondiging leverancierswitch’ volledig en syntactisch correct? 

   - b. Is de EAN-code correct? 

   - c. Heeft de beoogde switchdatum in de ‘vooraankondiging leverancierswitch’ het juiste formaat? 

   - d. Ligt de beoogde switchdatum in de ‘vooraankondiging leverancierswitch’ in de toekomst? 

   - e. Is er een contract met de aangegeven EAN-code van het allocatiepunt bekend in het CER? 

   - f. Is de initiërende leverancier bekend in het leveranciersregister? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘vooraankondiging leverancierswitch’ af, en verstuurt de systeembeheerder een afwijsbericht naar de initiërende leverancier. De afwijsredenen die het CER kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. De EAN-code is onjuist. 

   - c. De beoogde switchdatum in de ‘vooraankondiging leverancierswitch’ heeft niet het juiste formaat. 

   - d. De beoogde switchdatum in de ‘vooraankondiging leverancierswitch’ ligt niet in de toekomst. 

   - e. De aangegeven EAN-code van het allocatiepunt is onbekend in het CER. 

   - f. De leverancier is onbekend in het leveranciersregister. 

4. De initiërende leverancier verwerkt de afwijzing van de vooraankondiging leverancierswitch: a. In het geval van afwijsredenen a. t/m d. of f. verwerkt de initiërende leverancier de afwijzing en start de initiërende leverancier indien noodzakelijk het proces opnieuw. 

   - b. In het geval van afwijsreden e. kan de initiërende leverancier de afwijzing functioneel beschouwen als een resultaat zoals bedoeld in punt 6. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘vooraankondiging leverancierswitch’ van de initiërende leverancier en verstuurt de systeembeheerder het resultaat van de vooraankondiging leverancierswitch naar de initiërende leverancier. Tevens verstuurt de systeembeheerder de ‘melding vooraankondiging leverancierswitch’ <mark>voor zover er contracten op het allocatiepunt in het CER geregistreerd staan met een einddatum die later ligt dan de in de vooraankondiging gecommuniceerde beoogde switchdatum, naar de oude leverancier(s).</mark> 

6. De initiërende leverancier verwerkt het resultaat van de ‘vooraankondiging leverancierswitch’. 7. De oude leverancier(s) die de ‘melding vooraankondiging leverancierswitch’ ontvangt/ontvangen, dit kunnen er meerdere zijn, verwerkt deze en stuurt waar nodig een indicatie van de voorlopige hoogte van de opzegvergoeding naar de desbetreffende klant. 

## 4.6.15 Termijnen Vooraankondiging leverancierswitch

- a. De initiërende leverancier verstuurt de ‘vooraankondiging leverancierswitch’ uiterlijk de eerste werkdag na het sluiten van de overeenkomst met de klant; 

- b. De ‘vooraankondiging leverancierswitch’ wordt uiterlijk één werkdag na ontvangst door het CER verwerkt en het resultaat wordt direct na verwerking ter beschikking gesteld aan de initiërende leverancier. 

- c. Direct na verwerking van de ‘vooraankondiging leverancierswitch’ verstuurt het CER de ‘melding vooraankondiging leverancierwitch’ aan de oude leverancier(s) voor zover het contract een einddatum heeft die na de beoogde switchdatum ligt. 

## 4.6.16 Gegevensuitwisseling

### Vooraankondiging leverancierswitch

|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|---|---|---|---|
|EAN-code allocatiepunt|V|1||
|Referentie|O|1|Referentie ter routering van het antwoord van de systeembeheerder|
|Transactiedossiernummer|O|1|De leverancier dient dit veld leeg te laten. Het CER kent het<br>transactiedossiernummer toe.|
|Beoogde switchdatum|V|1|De datum per wanneer de leverancier voornemens is een leverancierswitch in te<br>dienen|

### Resultaat

|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|---|---|---|---|
|EAN-code allocatiepunt|V|1||
|Referentie|O|1|De door de contracterende leverancier in de vooraankondiging leverancierswitch|
||||meegegeven referentie|
|Transactiedossiernummer|V|1|Het bij de afhandeling van de transactie nieuw toegekende unieke nummer.|
|Beoogde switchdatum|V|1|Datum waarop de leverancier voornemens is de leverancierswitch te effectueren|

### Melding vooraankondiging leverancierswitch

|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|---|---|---|---|
|EAN-code allocatiepunt|V|1||
|Transactiedossiernummer|V|1|Het bij de afhandeling van de transactie nieuw toegekende unieke nummer.|
|Beoogde switchdatum|V|1|Datum waarop de leverancier voornemens is de leverancierswitch te effectueren|

### Afwijzing

|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|---|---|---|---|
|EAN-code allocatiepunt|V|1||
|Referentie|O|1|Gevuld indien door de leverancier meegegeven in de vooraankondiging<br>leverancierswitch KA|
|Afwijsreden|V|1|Verplichting indien er een afwijzing wordt geretourneerd.<br>De indicatie van de reden waarom de melding is afgewezen:<br>•<br>Onvolledige vooraankondiging of syntactische fout.<br>•<br>De EAN-code is onjuist.<br>•<br>De beoogde switchdatum in de ‘vooraankondiging leverancierswitch’ heeft<br>niet het juiste formaat.<br>•<br>De beoogde switchdatum ligt niet in de toekomst.<br>•<br>Voor het allocatiepunt met de aangegeven EAN-code zijn geen contracten<br>bekend in het CER.<br>•<br>De leverancier is onbekend in het leveranciersregister.|
|Toelichting afwijsreden|O|n||
|Transactiedossiernummer|O|1||

## 4.6.17 SP0095 Procesafspraken Opvragen contracterende leverancier bij systeembeheerder

Wanneer een klant met een kleine aansluiting na ontvangst van de voorlopige opzegvergoeding bij de reeds gecontracteerde leverancier aangeeft niet te weten dat hij/zij een contract heeft afgesloten en/of met welke leverancier dit dan is, en dus niet weet bij welke leverancier hij zich moet melden om dit op te helderen, kan de reeds gecontracteerde leverancier de EAN-code van de contracterende leverancier opvragen bij de systeembeheerder. Deze verzoeken vinden plaats buiten het afgesproken gestandaardiseerde berichtenverkeer om. 

De reeds gecontracteerde leverancier kan deze verzoeken op één van de volgende manieren indienen: 

- a. Voorkeurskanaal van de systeembeheerder is het indienen van deze verzoeken via Partners in Energie (PiE). Hierdoor kan de systeembeheerder makkelijker sturen waar een vraag terecht komt en kunnen de tijdslijnen beter gewaarborgd worden. 

- b. Een tweede manier om deze verzoeken in te dienen is om in het Contactpersonenregister in de bestaande contactgroep ‘Onterecht klantproces’ op te zoeken welk emailadres of telefoonnummer bij de systeembeheerder voor dit doeleinde gebruikt kan worden en vervolgens te e-mailen of te bellen. 

## 4.6.18 Procesbeschrijving KA

Bijlage B1094: Subprocesplaat SP0095 KA

1. De reeds gecontracteerde leverancier dient een opvraag contracterende leverancier in bij de systeembeheerder. 

2. De systeembeheerder zoekt de EAN-code van de contracterende leverancier op in het transactiedossier en deelt deze met de opvragende reeds gecontracteerde leverancier. 

3. De reeds gecontracteerde leverancier faciliteert de klant met een kleine aansluiting bij het ophelderen van de situatie. 

## 4.6.19 Termijnen Opvragen contracterende leverancier bij systeembeheerder

De systeembeheerder beantwoordt verzoeken van de reeds gecontracteerde leverancier binnen één werkdag. 

## 4.6.20 Gegevensuitwisseling

De reeds gecontracteerde leverancier vermeldt in de opvraag in ieder geval de EAN-code van het allocatiepunt en waar mogelijk ook het transactiedossiernummer van de ontvangen vooraankondiging leverancierswitch. 

De systeembeheerder vermeldt in de terugkoppeling: 

- De EAN-code van het allocatiepunt; 

- De EAN-code van de contracterende leverancier; 

- De naam van de contracterende leverancier. 

## 4.6.21 SP0024 Procesafspraken signaleren verhuizingen KA

- a. Dagelijks wordt vanuit het CER, per leverancier (bedrijfs-EAN-code), een signalering verhuizingen verstuurd. Hierin staan de voor deze leverancier van toepassing zijnde goedgekeurde (geforceerde) uithuizingen. 

- b. Middels de signalering verhuizingen wordt een leverancier geïnformeerd over verhuizingen op een allocatiepunt waar de leverancier volgens het aansluitingenregister nog niet verantwoordelijk voor is, maar volgens het CER wel een contract (in de toekomst) mee heeft afgesloten. Dit dient ter voorkoming van onterechte switches. Deze functionaliteiten worden uitgevoerd op de contracten die via het wekelijkse bronbestand zijn opgeleverd, dus niet op de realtime gemelde contracten. 

## 4.6.22 Procesbeschrijving KA

Bijlage B1095: Subprocesplaat SP0024 KA

1. De systeembeheerder levert de goedgekeurde (geforceerde) uithuizingen op van de vorige kalenderdag aan het CER. Deze gegevens betreffen: 

   - a. De EAN-code van het allocatiepunt. 

   - b. De bedrijfs-EAN-code van de uithuizende leverancier. 

- c. De mutatiedatum van de uithuizing. 

- 2. Het CER splitst de uithuizingen op in delen per bedrijfs-EAN-code van de leverancier, op basis van de registraties van contracten in CER. 

3. Het CER stelt per bedrijfs-EAN-code van de leverancier een signalering verhuizing beschikbaar. 

4. De leveranciers vragen de verhuizingen op. 

5. De leveranciers verwerken de signalering verhuizingen. 

## 4.6.23 Termijnen KA

- a. Dagelijks na 00:00 stelt de systeembeheerder alle goedgekeurde (geforceerde) uithuizingen van de kalenderdag ervoor ter beschikking aan het CER. 

- b. Het CER stelt dagelijks, uiterlijk om 08:00, de signalering verhuizingen beschikbaar aan leveranciers die een contract hebben opgeleverd via het wekelijkse bronbestand. 

## 4.6.24 Gegevensuitwisseling

### Overzicht verhuizing

|**Overzicht verhuizing**||||
|---|---|---|---|
|**Gegevens**|**Kenmerk**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|A|n|Verplicht indien signalering verhuizingen geretourneerd kan worden|
|Transactiedossiernummer|V|n||
|Mutatiedatum|V|n|De datum waarop de uithuizing zal worden geëffectueerd<br>door de<br>systeembeheerder|
|EAN-code leverancier|V|n|EAN-code van de uithuizende leverancier|
