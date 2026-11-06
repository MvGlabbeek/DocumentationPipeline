# 4.25 SP0026 Opvragen gegevens ten behoeve van compensatievergoedingen


## 4.25.1 Procesafspraken KA

   - a. De systeembeheerder bepaalt de populatie van allocatiepunten die door een storing getroffen is. 

   - b. Dit proces wordt alleen toegepast voor primaire allocatiepunten. 

   - c. De systeembeheerder vraagt de gegevens van de allocatiepunten behorend bij een kleine aansluiting waarbij een storing is geconstateerd op, bij de leverancier die (op de storingsdatum) verantwoordelijk was voor het allocatiepunt. 

   - d. Wanneer de leverancier niet beschikt over het bankrekeningnummer van de klant, levert de leverancier alleen de contactgegevens aan zoals deze bij hem beschikbaar zijn. Bij velden waarvoor geen gegevens beschikbaar zijn hanteert de leverancier de domeinwaarde ‘LEEG’. 

   - e. Indien de leverancier over meerdere bankrekeningnummers van een klant beschikt, levert hij in de terugkoppeling naar de systeembeheerder het bankrekeningnummer dat voor betalingsdoeleinden wordt gebruikt. 

   - f. Indien de systeembeheerder bij een leverancier voor een allocatiepunt waarmee de leverancier geen leveringsovereenkomst heeft op het moment van de storing, gegevens opvraagt, meldt de leverancier dit in het door hem aangeleverde bericht. 

   - g. De systeembeheerder is verantwoordelijk voor een juiste en tijdige uitbetaling van de compensatievergoeding en betaalt de vergoeding zelf aan de door storing getroffen aangeslotene. 

   - h. De systeembeheerder is verantwoordelijk voor het verkrijgen van de bank- en contactgegevens van de getroffen aangeslotene. Indien de systeembeheerder deze gegevens niet bij een leverancier kan verkrijgen, zal hij deze gegevens via een andere weg moeten verkrijgen. 

   - i. In de Algemene Voorwaarden van de leverancier is opgenomen dat de leverancier op diens verzoek aan de systeembeheerder de contact- en bankgegevens van de getroffen aangeslotene verstrekt ten behoeve van compensatie na ernstige storing. 

## 4.25.2 Procesbeschrijvingen KA

### Opvragen gegevens getroffen allocatiepunten

Bijlage B1144: Subprocesplaat SP0026 KA – Opvragen gegevens getroffen allocatiepunten

1. Na een storing inventariseert de systeembeheerder welke allocatiepunten getroffen zijn door storing en recht hebben op een compensatie. Voor de allocatiepunten op kleine aansluitingen verzamelt de systeembeheerder de bijbehorende EAN-codes ten behoeve van het opvragen van de klantgegevens bij de leverancier. 

2. De systeembeheerder bepaalt welke leverancier voor de getroffen allocatiepunten op kleine aansluitingen verantwoordelijk was op de storingsdatum. De systeembeheerder stelt per leverancier een bericht samen met daarin de allocatiepunten waarvan hij de gegevens wil hebben. 

3. De systeembeheerder verstuurt het bericht aan de leverancier. 

4. De leverancier ontvangt het bericht. 

### Aanleveren gevraagde gegevens

Bijlage B1145: Subprocesplaat SP0026 KA – Aanleveren gevraagde gegevens

1. Wanneer het bericht verwerkt kan worden, verzamelt de leverancier per EAN-code de contacten bankgegevens geldig op de door de systeembeheerder gevraagde datum van de aangeslotenen op de allocatiepunten waarvoor de systeembeheerder dit aan hem heeft verzocht. 

2. Indien de leverancier niet beschikt over de bankgegevens van een aangeslotene, levert de leverancier alleen de contactgegevens aan bij de systeembeheerder. Indien de leverancier voor de datum waarop de storing heeft plaatsgevonden voor een allocatiepunt geen leverancier was, wordt voor dat allocatiepunt de waarde ‘nee’ teruggegeven. De leverancier stelt één bericht samen met de verzamelde contact- en bankgegevens. 

3. De leverancier verzendt uiterlijk de 10<sup>e</sup> werkdag na ontvangst van het verzoek van de systeembeheerder, het bericht met de contact- en bankgegevens van de aangeslotenen op de getroffen allocatiepunten naar de systeembeheerder. 

4. De systeembeheerder ontvangt het bericht met de contact- en bankgegevens van de aangeslotenen op de getroffen allocatiepunten van de leverancier. 

## 4.25.3 Termijnen KA

De leverancier verstuurt uiterlijk 10 werkdagen na ontvangst van het verzoek tot het aanleveren van de gegevens van de aangeslotenen op de getroffen allocatiepunten op kleine aansluitingen, de contact- en bankgegevens van de aangeslotenen op de getroffen allocatiepunten op kleine aansluitingen aan de systeembeheerder. 

## 4.25.4 Gegevensuitwisseling

### Opvraag

|**Opvragen gegevens m.b.t. compe**|**nsatievergo**|**edingen**||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Referentie|O|Ja|A|1||
|EAN-code systeembeheerder|V|Ja|A|1||
|EAN-code leverancier|V|Ja|A|1||
|Storingsdatum|V|Ja|A|1||
|EAN-code allocatiepunt|V|Ja|A|n||

### Response

|**Aanleveren gegevens t.b.v. compensat**|**ievergoedi**|**ngen**||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|V|Ja|A|1||
|Referentie|A|Ja|A|1|Gevuld indien meegegeven in de opvraag|
|EAN-code systeembeheerder|V|Ja|A|1||
|EAN-code leverancier|V|Ja|A|1||
|Storingsdatum|V|Ja|A|1||
|EAN-code allocatiepunt|V|Ja|A|n||
||||||**1 per allocatiepunt**|
|Contract|V|Ja|A|1|**Ja**(dan worden de volgende velden, voor zover bekend, gevuld)<br>**Nee**(dan worden de volgende velden niet gevuld; allocatiepunt<br>niet bekend bij deze leverancier op storingsdatum)<br>Indien sprake is van een additioneel allocatiepunt dan wordt de<br>opvraagdoor de leveranciergenegeerd.|
|Voorletters aangeslotene|O|Ja|A|1||
|Tussenvoegsel aangeslotene|O|Ja|A|1||
|(Achter-) Naam aangeslotene|V|Ja|A|1||
|_Correspondentieadres:_||||||
|Straatnaam / Postbus|A|Ja|A|1|Alleen indien dit afwijkt van het aansluitadres|
|Huisnummer / Postbusnummer|A|Ja|A|1|Alleen indien dit afwijkt van het aansluitadres|
|Huisnummertoevoeging|A|Ja|A|1|Alleen indien dit afwijkt van het aansluitadres|
|Postcode|A|Ja|A|1|Alleen indien dit afwijkt van het aansluitadres|
|Woonplaats|A|Ja|A|1|Alleen indien dit afwijkt van het aansluitadres|
|Land|A|Ja|A|1|Alleen indien dit afwijkt van het aansluitadres|
|Bankrekeningnummer|A|Ja|A|1|Bankrekeningnummer van de aangeslotene|
