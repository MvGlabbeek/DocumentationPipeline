# 4.5 SP0055 Raadplegen Toegankelijk Meetregister door (actuele) leverancier


## 4.5.1 Procesafspraken KA

Een doelstelling van het TMR is om het kunnen valideren en vaststellen van meterstanden door de (actuele) leverancier te faciliteren, met het kunnen opvragen van vastgestelde meterstanden en volumes. 

Alle (conform de Energiewet en lagere regelgeving) vastgestelde meterstanden en volumes worden in het TMR opgeslagen en ter beschikking gesteld aan een opvragende leverancier. 

De leverancier kan voor controledoeleinden meetgegevens opvragen uit het TMR. Het opvragen van meetgegevens uit het TMR is beperkt tot de periode dat de leverancier als actuele leverancier geregistreerd is (geweest) op het allocatiepunt en de meterstanden tot vier maanden na het einde van de periode van levering. Voor de actuele leverancier op het allocatiepunt worden de meetgegevens tevens aangevuld met de laatst genoteerde P4/klant/fysieke meterstand van vóór de leveringsperiode waarvoor de leverancier geregistreerd is geweest op het allocatiepunt en de eventuele tussenliggende berekende meterstanden. 

- a. Het TMR beperkt zich tot de meetgegevens behorende bij een allocatiepunt op een kleine aansluiting. 

- b. Indien voor onbemeten allocatiepunten volumes beschikbaar zijn, worden die ook via het TMR ontsloten. 

- c. Meetgegevens worden per specifiek opgegeven allocatiepunt opgevraagd en opgeleverd. 

- d. Indien correcties plaats vinden op reeds opgevraagde meetgegevens dan wordt de opvragende marktpartij niet gewaarschuwd dat er correcties hebben plaats gevonden. De marktpartij dient zelf tot deze conclusie te komen bij een eventuele volgende opvraag van de historie voor het betreffende allocatiepunt. 

- e. De systeembeheerders dragen er zorg voor dat alle vastgestelde meetgegevens binnen 24 uur beschikbaar zijn via het TMR. 

- f. De herkomstindicatie van meterstanden wordt éénduidig vastgelegd via de codes: 

   - i. Berekend 005 

   - ii. Overeengekomen 102 

   - iii. Klantstand/P1-stand 22 iv. Fysieke opname 003 v. P4-stand 004 

- g. Via het TMR worden meterstanden en volumes voor zowel levering als teruglevering gecommuniceerd. 

- h. Alle vastgestelde meterstanden en volumes die in het TMR beschikbaar zijn en voldoen aan de voorwaarden zoals genoemd in de procesafspraken beschreven in deze paragraaf worden opgeleverd. 

- i. Meetgegevens zijn uitsluitend opvraagbaar per gespecificeerd allocatiepunt. 

- j. Hierbij is het niet van belang wie de klant is. Het is dus mogelijk dat de informatie, die wordt geleverd, het gevolg is van volumes door, in de tijd gezien, verschillende contracten. 

- k. Negatieve volumes zijn mogelijk en zullen dan ook als een negatief volume worden aangegeven. 

- l. Indien de laatste meterstand lager is dan de vorige meterstand en er een positief volume wordt vermeld, dan moet er worden geconcludeerd dat de meetinrichting (of eigenlijk het 

telwerk) ‘over de kop’ is gegaan. ‘Meetinrichting over de kop’ is geen aparte indicatie bij meterstanden of volumes. 

- m. Het TMR is toegankelijk voor de marktrollen leverancier en systeembeheerder. 

- n. De portal behandelt slechts enkelvoudige opvragingen. Met andere woorden, indien een opvrager voor een postcode/huisnummer zowel gegevens van elektriciteit als gegevens van gas wil opvragen dan zal de opvrager dit via twee afzonderlijke opvragingen (per allocatiepunt) dienen te doen. 

- o. Energetische volumes zijn verplicht op te leveren. 

- p. Gemeten volumes zijn optioneel op te leveren. 

- q. Volumes worden met periode gepresenteerd. 

- r. Meterstanden worden met een datum gepresenteerd. 

- s. Wisselingen van meetinrichtingen zijn zichtbaar doordat meetinrichtingnummers bij meterstanden verplicht zijn. 

- t. Bij onbemeten allocatiepunten kennen we wel volumes, maar geen meterstanden. Deze worden gepresenteerd door alleen volumes te communiceren en bij het meetinrichtingnummer ‘ONBEMETERD’ te vermelden. 

## 4.5.2 Procesbeschrijving KA

Bijlage B1089: Subprocesplaat SP0055 KA

1. De opvragende marktpartij vraagt de meetgegevens uit het TMR op van het allocatiepunt. 

2. De systeembeheerder ontvangt de ‘opvraag raadplegen TMR’ van de opvragende marktpartij. De systeembeheerder beoordeelt de opvraag op de volgende punten: 

   - a. Is de opvraag volledig en syntactisch correct? 

   - b. Komt het allocatiepunt voor in het TMR? 

   - c. Is de opvragende leverancier als leverancier in het aansluitingenregister op het allocatiepunt geregistreerd of geregistreerd geweest? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘opvraag raadplegen TMR’ af, en verstuurt de systeembeheerder een afwijsbericht naar de marktpartij direct na ontvangst van de ‘opvraag raadplegen TMR’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige opvraag of syntactische fout. 

   - b. Het allocatiepunt komt niet voor in het TMR. 

   - c. De opvragende leverancier is niet geregistreerd of geregistreerd geweest op het allocatiepunt. 

4. De marktpartij ontvangt en verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘opvraag raadplegen TMR’ van de marktpartij en verstuurt de systeembeheerder de meetgegevens direct naar de marktpartij. 

6. De marktpartij ontvangt en verwerkt de meetgegevens van het allocatiepunt. 

## 4.5.3 Termijnen KA

De ‘opvraag raadplegen TMR’ wordt direct beantwoord. 

## 4.5.4 Gegevensuitwisseling

### Opvraag

|**Opvraag uit het Toegankelijk Meetre**|**gister d**|**oor levera**|**ncier met**|**periode v**|**an levering**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code opvragende marktpartij|V|Ja|Ja|1||
|Account_id|V|Ja|Ja|1|ID van hetgebruikersaccount,waaronder de opvraagwordtgedaan|
|Referentie|O|Ja|Ja|1|Door de opvrager te bepalen uniek kenmerk, aan de hand waarvan<br>opvraagen antwoord aan elkaargerelateerd kunnen worden|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|EAN-code van de opleverende<br>marktpartij|O|Ja|Ja|1|EAN--code van de marktpartij die verantwoordelijk geacht wordt voor<br>opleveringvan de meetgegevens voor dit allocatiepunt|

### Response

|**Meetgegevens uit het Toegankelijk Meetre**|**gister**|||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1|EAN-code van het allocatiepunt waarvoor meetgegevens worden<br>opgevraagd en opgeleverd|
|EAN-code systeembeheerder|V|Ja|Ja|1||
|EAN-code van de opleverende marktpartij|V|Ja|Ja|1|EAN-code van de partij die de meetgegevens voor dit allocatiepunt<br>oplevert|
|Referentie|O|Ja|Ja|1|Door de opvrager te bepalen uniek kenmerk, aan de hand waarvan<br>opvraagen antwoord aan elkaargerelateerd kunnen worden|
|Meetinrichtingnummer|O|Ja|Ja|1||
|**_Telwerk_**||||**_n_**|**_n per meetinrichting_**|
|Telwerkidentificatie|V|Ja|Ja|1|•<br>Meetinrichting<br>met<br>communicatiefunctionaliteit:<br>telwerkidentificatie door middel van de OBIS-code zonder<br>interpunctie<br>•<br>Meetinrichting<br>zonder<br>communicatiefunctionaliteit:<br>telwerkidentificatie door middel van een numerieke<br>aanduiding|
|Registertype|V|Nee|Ja|1|Indicatie van het volume dat op het telwerk wordt geregistreerd:<br>•<br>Normaal<br>•<br>Laag<br>•<br>Teruglevering normaal|
||||||•<br>Terugleveringlaag|
|**_Volume_**||||**_1_**|**_1 per telwerk_**|
|Begindatum volumeperiode|V|Ja|Ja|1||
|Einddatum volumeperiode|V|Ja|Ja|1|Voor periodemarkeringen worden ‘tot datums’ gebruikt, zo wordt<br>de maand maart 2025 aangeduid van 01-03-25 tot 01-04-25.|
|Hoeveelheid|V|Ja|Ja|1||
|Meeteenheid hoeveelheid|V|Ja|Ja|1||
|Herkomstindicatie volume|O|Ja|Ja|1|Indicatie die aangeeft hoe het volume is verkregen. Indien gevuld<br>moet voldaan worden aan het domein|
|Gecorrigeerde hoeveelheid|O|Ja|Nee|1||
|Meeteenheid gecorrigeerd volume|V|Ja|Nee|1||
|EAN-code vaststellende partij|O|Ja|Ja|1|De EAN-code van de partij die het volume heeft vastgesteld|
|**_Meterstand_**||||**_n_**|**_n per allocatiepunt, meterstanden worden in TMR direct op het_**<br>**_allocatiepuntgecommuniceerd._**|
|Meetinrichtingnummer|V|Ja|Ja|1||
|Telwerkidentificatie|V|Ja|Ja|1|•<br>Meetinrichting<br>met<br>communicatiefunctionaliteit:<br>telwerkidentificatie door middel van de OBIS-code zonder<br>interpunctie<br>•<br>Meetinrichting<br>zonder<br>communicatiefunctionaliteit:<br>telwerkidentificatie door middel van een numerieke<br>aanduiding|
|Registertype/Tariefzone|A|Nee|Ja|1|Indicatie van het volume dat op het telwerk wordt geregistreerd:<br>•<br>Normaal<br>•<br>Laag<br>•<br>Teruglevering normaal|
||||||•<br>Terugleveringlaag|
|Meterstand|V|Ja|Ja|1||
|Meterstanddatum|V|Ja|Ja|1||
|Herkomstindicatie|V|Ja|Ja|1||

|**Meetgegevens uit het Toegankelijk Meetreg**|**ister**|||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code van de vaststellende<br>marktpartij|O|Ja|Ja|1|De EAN-code van de marktpartij die het volume heeft vastgesteld|

### Afwijzing

|**Afwijzing opvraag Toegankelijk Mee**|**tregiste**|**r**||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code opvragende marktpartij|V|Ja|Ja|1||
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag.|
|EAN-code systeembeheerder|V|Ja|Ja|1||
|Afwijsreden|V|Ja|Ja|n|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledig opvraag of syntactische fout<br>•<br>Het allocatiepunt komt niet voor in het TMR<br>•<br>De opvragende leverancier is niet vermeld of vermeld geweest op het<br>allocatiepunt|
