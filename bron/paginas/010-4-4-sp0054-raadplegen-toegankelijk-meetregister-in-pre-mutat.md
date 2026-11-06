# 4.4 SP0054 Raadplegen Toegankelijk Meetregister in pre-mutatiefase


## 4.4.1 Procesafspraken KA

Een doelstelling van het Toegankelijk Meetregister (TMR) is het faciliteren van het kunnen valideren en vaststellen van meterstanden door de leverancier, middels het opvragen van vastgestelde meterstanden en volumes. 

Alle (conform de Energiewet en lagere regelgeving) vastgestelde meterstanden en volumes worden in het TMR opgeslagen en onder voorwaarden op een eenduidige manier ter beschikking gesteld aan een opvragende leverancier. 

Het opvragen van meetgegevens uit het TMR in de pre-mutatiefase mag alleen wanneer een toekomstige leverancier zijn contract heeft geregistreerd in het Contracteinderegister en het een meetinrichting zonder communicatiefunctionaliteit betreft. Deze ontvangt de laatst genoteerde klant of fysieke meterstand van vóór het moment van raadplegen en de eventueel tussenliggende, berekende of overeengekomen, meterstanden. Indien er geen laatst genoteerde P4/klant/fysieke meterstand wordt gevonden wordt de laatste berekende of overeengekomen meterstand teruggekoppeld. 

- a. Het TMR beperkt zich tot de meetgegevens behorende bij allocatiepunten op een kleine aansluiting. 

- b. Indien voor onbemeten allocatiepunten volumes beschikbaar zijn, worden die ook via het TMR ontsloten. 

- c. Meetgegevens worden per specifiek opgegeven allocatiepunt opgevraagd en opgeleverd. 

- d. Indien correcties plaatsvinden op reeds opgevraagde meetgegevens dan wordt de opvragende marktpartij niet gewaarschuwd dat er correcties hebben plaats gevonden. De partij dient zelf tot deze conclusie te komen bij een eventuele volgende opvraag van de historie voor het betreffende allocatiepunt. 

- e. De systeembeheerders dragen er zorg voor dat alle vastgestelde meetgegevens binnen 24 uur beschikbaar zijn via het TMR. 

- f. De herkomstindicatie van meterstanden wordt éénduidig vastgelegd via de codes: 

   - i. Berekend 005 

   - ii. Overeengekomen 102 

   - iii. Klantstand/P1-stand 22 iv. Fysieke opname 003 v. P4-stand 004 

- g. Via het TMR worden meterstanden en volumes voor zowel levering als teruglevering gecommuniceerd. 

- h. Alle vastgestelde meterstanden en volumes die in het TMR beschikbaar zijn en voldoen aan de voorwaarden zoals genoemd in deze paragraaf worden opgeleverd. 

- i. Meetgegevens zijn uitsluitend opvraagbaar per gespecificeerd allocatiepunt. 

- j. Hierbij is het niet van belang wie de klant is. Het is dus mogelijk dat de informatie, die wordt geleverd, het gevolg is van volumes door, in de tijd gezien, verschillende contracten. 

- k. Negatieve volumes zijn mogelijk en zullen dan ook als een negatief volume worden aangegeven. 

- l. Indien de laatste meterstand lager is dan de vorige meterstand en er een positief volume wordt vermeld, dan moet er worden geconcludeerd dat de meetinrichting (of eigenlijk het telwerk) ‘over de kop’ is gegaan. ‘Meetinrichting over de kop’ is geen aparte indicatie bij meterstanden of volumes. 

- m. Het TMR is toegankelijk voor de rollen leverancier en systeembeheerder. 

- n. De portal behandelt slechts enkelvoudige opvragingen; met andere woorden: indien een opvrager voor een postcode/huisnummer zowel gegevens van elektriciteit als gegevens van gas wil opvragen dan zal de opvrager dit via twee afzonderlijke opvragingen (per allocatiepunt) dienen te doen. 

- o. Energetische volumes zijn verplicht op te leveren. 

- p. Gemeten volumes zijn optioneel op te leveren. 

- q. Volumes worden met periode gepresenteerd. 

- r. Meterstanden worden met een datum gepresenteerd. 

- s. De wisselingen van meetinrichtingen zijn zichtbaar doordat meetinrichtingnummers bij meterstanden verplicht zijn. 

- t. Bij onbemeten allocatiepunten kennen we wel volumes, maar geen meterstanden. Deze worden gepresenteerd door alleen volumes te communiceren en bij het meetinrichtingnummer ‘ONBEMETERD’ te vermelden. 

## 4.4.2 Procesbeschrijving KA

Bijlage B1088: Subprocesplaat SP0054 KA

1. De leverancier vraagt de meetgegevens van de aansluiting op uit het TMR. 

2. De systeembeheerder ontvangt de opvraag ‘raadplegen TMR in pre-mutatiefase’ van de leverancier. De systeembeheerder beoordeelt de opvraag op de volgende punten: 

   - a. Is de opvraag volledig en syntactisch correct? 

   - b. Komt het allocatiepunt voor in het TMR? 

   - c. Is de EAN-code van de opvragende leverancier bekend in het leveranciersregister? 

   - d. Heeft de opvragende leverancier een contract voor het betreffende allocatiepunt in het Contracteinderegister geregistreerd? 

   - e. Betreft het een meetinrichting zonder communicatiefunctionaliteit of een meetinrichting die niet uitgelezen mag worden (meetinrichtingen met communicatiefunctionaliteit met de status ‘technisch niet op afstand uitleesbaar’ of administratief ‘uit’). 

3. Indien de systeembeheerder de opvraag ‘meetgegevens TMR in pre-mutatiefase’ niet kan verwerken, verstuurt de systeembeheerder een afwijzing naar de opvragende marktpartij direct na ontvangst van de opvraag ‘meetgegevens TMR in pre-mutatiefase’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige aanvraag of syntactische fout. 

   - b. EAN-code allocatiepunt komt niet voor in het TMR. 

   - c. EAN-code opvragende leverancier komt niet voor in het leveranciersregister. 

   - d. Geen contract van de opvragende leverancier voor het betreffende allocatiepunt geregistreerd in het Contracteinderegister. 

   - e. Het betreft geen meetinrichting zonder communicatiefunctionaliteit of een meetinrichting met communicatiefunctionaliteit die niet uitgelezen mag worden. 

4. De leverancier ontvangt en verwerkt de afwijzing. 

5. Indien de systeembeheerder de opvraag kan verwerken dan verstuurt de systeembeheerder de meetgegevens direct aan de leverancier. 

6. De leverancier ontvangt en verwerkt de meetgegevens van het allocatiepunt. 

## 4.4.3 Termijnen KA

De opvraag ‘Raadplegen TMR in pre-mutatiefase’ wordt direct beantwoord. 

## 4.4.4 Gegevensuitwisseling

### Opvraag

|**Opvraag uit het Toegankelijk Meetre**|**gister d**|**oor de toe**|**komstige**|**leverancie**|**r**|
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code opvragende marktpartij|V|Ja|Ja|1||
|Account_id|V|Ja|Ja|1|ID van hetgebruikersaccount,waaronder de opvraagwordtgedaan|
|Referentie|O|Ja|Ja|1|Door de opvrager te bepalen uniek kenmerk, aan de hand waarvan<br>opvraagen antwoord aan elkaargerelateerd kunnen worden|
|EAN-code allocatiepunt|V|Ja|Ja|1||

|**Opvraag uit het Toegankelijk Meetre**|**gister d**|**oor de to**|**ekomstige**|**leverancie**|**r**|
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code van de opleverende partij|O|Ja|Ja|1|EAN-code van de partij die verantwoordelijk geacht wordt voor<br>opleveringvan de meetgegevens voor dit allocatiepunt.|

### Response

|**Meetgegevens uit het Toegankelijk**|**Meetreg**|**ister**||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1|EAN-code van het allocatiepunt waarvoor meetgegevens wordt<br>opgevraagd en opgeleverd|
|Systeemgebied|V|Ja|Ja|1||
|EAN-code van de opleverende partij|V|Ja|Ja|1|EAN-code van de partij die de meetgegevens voor dit allocatiepunt<br>oplevert|
|Referentie|O|Ja|Ja|1|Door de opvrager te bepalen uniek kenmerk, aan de hand waarvan<br>opvraagen antwoord aan elkaargerelateerd kunnen worden|
|**Volume**||||**n**|**n per allocatiepunt, volumes worden in TMR direct op het allocatiepunt**<br>**gecommuniceerd.**|
|Meetinrichtingnummer|O|Ja|Ja|1||
|Registertype|A|Nee|Ja|1|Indicatie van het verbruik dat op het telwerk wordt geregistreerd:<br>•<br>Normaal<br>•<br>Laag<br>•<br>Teruglevering normaal<br>•<br>Terugleveringlaag|
|Begindatum volumeperiode|V|Ja|Ja|1||
|Einddatum volumeperiode|V|Ja|Ja|1|Voor periodemarkeringen worden ‘tot datums’ gebruikt, zo wordt de<br>maand maart 2025 aangeduid van 01-03-25 tot 01-04-25.|
|Hoeveelheid|V|Ja|Ja|1||
|Meeteenheid hoeveelheid|V|Ja|Ja|1||
|Herkomstindicatie volume|O|Ja|Ja|1|Indicatie die aangeeft hoe het volume is verkregen. Indien gevuld moet<br>voldaan worden aan het domein|
|Gecorrigeerde hoeveelheid|O|Ja|Nee|1||
|Meeteenheid<br>gecorrigeerd<br>volume|O|Ja|Nee|1||
|EAN-code vaststellende partij|O|Ja|Ja|1|De EAN-code van de partij die het volume heeft vastgesteld|
|**_Meterstand_**||||**_n_**|**n per allocatiepunt, meterstanden worden in TMR direct op het**<br>**allocatiepuntgecommuniceerd.**|
|Meetinrichtingnummer|V|Ja|Ja|1||
|Telwerkidentificatie|V|Ja|Ja|1|•<br>Meetinrichting<br>met<br>communicatiefunctionaliteit:<br>telwerkidentificatie door middel van de OBIS-code zonder<br>interpunctie<br>•<br>Meetinrichting<br>zonder<br>communicatiefunctionaliteit:<br>telwerkidentificatie door middel van een numerieke aanduiding|
|Registertype/Tariefzone|A|Nee|Ja|1|Indicatie van het verbruik dat op het telwerk wordt geregistreerd:<br>•<br>Normaal<br>•<br>Laag<br>•<br>Teruglevering normaal<br>•<br>Terugleveringlaag|
|Meterstand|V|Ja|Ja|1||
|Meterstanddatum|V|Ja|Ja|1||
|Herkomstindicatie|V|Ja|Ja|1||
|EAN-code vaststellende partij|O|Ja|Ja|1|De EAN-code van de partij die de meterstand heeft vastgesteld|

### Afwijzing

|**Afwijzing opvraag Toegankelijk Mee**|**tregiste**|**r**||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n **|**Opmerking**|
|EAN-code opvragende marktpartij|V|Ja|Ja|1||
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag.|
|**Foutmelding**||||**n**|**_nperfoutmelding_**|
|Volgnummer|V|Ja|Ja|1|Volgnummer van de foutmeldingbinnen de afwijzing|
|Afwijsreden|V|Ja|Ja|N|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Aanvraag niet volledig of syntactisch onjuist<br>•<br>EAN-code allocatiepunt onbekend<br>•<br>EAN-code opvragende marktpartijonbekend|

|**Afwijzing opvraag Toegankelijk Mee**|**tregiste**|**r**||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n **|**Opmerking**|
|EAN-code opvragende marktpartij|V|Ja|Ja|1||
||||||•<br>De opvragende leverancier heeft geen contract voor het<br>betreffende<br>allocatiepunt<br>in<br>het<br>Contracteinderegister<br>geregistreerd;<br>•<br>Het betreft een meetinrichtingmet communicatiefunctionaliteit..|
