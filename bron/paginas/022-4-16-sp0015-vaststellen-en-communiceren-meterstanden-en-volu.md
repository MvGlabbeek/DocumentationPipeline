# 4.16 SP0015 Vaststellen en communiceren meterstanden en volume(s) KA


Het subproces Vaststellen en communiceren meterstanden en volumes voor kleine aansluitingen bestaat uit de volgende onderdelen voor zowel event- als periodieke meterstanden: 

1. Vaststellen en communiceren vastgestelde meterstanden door leverancier 

2. Ontvangen vastgestelde meterstand door systeembeheerder 

3. Vaststellen en berekenen meterstanden door systeembeheerder 

4. SJ bepalen, respectievelijk SJA, SJI en SJV bepalen 

5. Distributie meetgegevens 

## 4.16.1 Procesafspraken Vaststellen en communiceren meterstanden en volumes KA

   - a. Indien de vastgestelde meterstand behoort bij een mutatiedatum wordt het veld ‘opnamedatum’ gevuld met de mutatiedatum. Betreft het een periodieke meterstand dan wordt de werkelijke opnamedatum gebruikt. 

   - b. Het kenmerk ‘periodiek’ wordt gebruikt voor het kenmerken van alle vastgestelde meterstanden die niet zijn vastgesteld in het kader van de processen Leverancierswitch, Inhuizing, Uithuizing, Einde levering, Balanceringsverantwoordelijkeswitch, Mutatie van de meetinrichting of de Driejaarlijkse fysieke opname. 

### In geval van een meetinrichting met handopname:

- c. Om te bepalen of een meterstand gecollecteerd kan worden door de leverancier, kan de actuele leverancier gebruik maken van het kenmerk ‘type meetinrichting’, ‘administratieve status van de meetinrichting’ en ‘uitleesbaarheid meetinrichting met communicatiefunctionaliteit’ uit de stamgegevens. Indien sprake is van een meetinrichting zonder communicatiefunctionaliteit of van een meetinrichting met communicatiefunctionaliteit waarvan de status administratief uit is of wanneer de meter technisch niet op afstand uitleesbaar is, verzamelt de leverancier de meterstanden voor de uitvoering van zijn wettelijke taken. 

- d. De bij een mutatie horende vastgestelde meterstand moet op de mutatiedatum op de meetinrichting staan, hebben gestaan of hebben kunnen staan. 

- e. De periodieke meterstand voor een allocatiepunt voor een meetinrichting met een handopname zal worden vastgesteld door de actuele leverancier. 

- f. De leverancier biedt geen periodieke meterstanden, met uitzondering van meterstanden uit het proces Dispuut over meterstanden, aan met een eerdere datum dan al aanwezig in het TMR. 

- g. De leverancier biedt geen meterstanden aan waar geen dispuut meer op mogelijk is. 

- h. Indien de vastgestelde meterstand behoort bij een mutatieproces is de leverancier verplicht om het transactiedossiernummer, ontvangen in het GAIN/LOSS-bericht, te vermelden bij de vastgestelde meterstand. 

- i. Bij een meetinrichting met handopname zal de actuele leverancier de klant om een meterstand verzoeken. Indien de leverancier geen meterstand heeft kunnen collecteren dan kan hij een meterstand vaststellen op basis van berekening. 

### In geval van een meetinrichting met communicatiefunctionaliteit:

- j. Indien een allocatiepunt is voorzien van een meetinrichting met communicatiefunctionaliteit, leest de distributiesysteembeheerder de meterstanden uit, valideert de uitgelezen meterstanden en stelt meterstanden vast op basis van een geëffectueerde wijziging van de allocatiemethode (zowel bij de wijziging naar SMA als de wijziging naar PRF), uithuizing, inhuizing, switch van een leverancier, einde levering of een switch van een balanceringsverantwoordelijke. 

- k. Indien een allocatiepunt is voorzien van een op afstand uitleesbare meter, leest de systeembeheerder maandovergang meterstanden uit, valideert de uitgelezen meterstanden en stelt de meterstanden vast. 

- l. Indien een allocatiepunt is voorzien van een meetinrichting met communicatiefunctionaliteit en de systeembeheerder heeft een verzoek voor vastgestelde meterstanden en volumes ten behoeve van de facturatie van een leverancier ontvangen, leest systeembeheerder de meterstanden uit, valideert de uitgelezen meterstanden en stelt de meterstanden vast. 

- m. De systeembeheerder probeert bij een allocatiepunt met een meetinrichting met communicatiefunctionaliteit waarvoor geen meterstand uitgelezen kan worden de volgende dag/dagen nogmaals de op afstand uitleesbare meter uit te lezen. Indien op de uiterlijke datum waarop de meterstand vastgesteld dient te zijn nog geen meterstanden uitgelezen zijn, berekent de systeembeheerder een meterstand. Indien de uitgelezen meterstand niet valide is, berekent de systeembeheerder direct een meterstand. 

- n. In een situatie waarin de systeembeheerder de meterstanden berekend heeft, heeft de leverancier de mogelijkheid om meterstanden aan te bieden conform het proces Melding vastgestelde meterstand KA. Deze meterstanden moeten de herkomstindicatie ‘overeengekomen’ of ‘klantstand’ hebben. Voor deze situatie mag het proces Dispuut over meterstanden niet gebruikt worden door de desbetreffende leverancier. Bij een uithuizing gevolgd door leegstand of een einde levering betreft het de oude leverancier. In alle andere gevallen de actuele/nieuwe leverancier. 

### Volumeberekening:

- o. De systeembeheerder berekent op basis van vastgestelde meterstanden volumes ten behoeve van de reconciliatie. De meterstanden en volumes worden ter beschikking gesteld aan de betreffende leverancier waarbij het herkenbaar is dat het een mutatie of een maandovergang betreft of naar aanleiding van een verzoek is. 

- p. Indien voor een voorafgaande periode nog meterstanden vastgesteld dienen te worden, vindt de vaststelling en berekening van het volume pas plaats zodra de voorliggende meterstanden zijn vastgesteld. 

### Verschil van inzicht:

- q. Een klant kan altijd bij de leverancier aangeven dat hij het niet eens is met een meterstand. De leverancier kan een vastgestelde meterstand van een meetinrichting met handopname corrigeren tot het einde van de dispuuttermijn. Dit doet de leverancier door voor dezelfde opnamedatum een nieuwe meterstand aan te bieden. 

- r. De systeembeheerder kan (als wederpartij) tegen vastgestelde meterstanden in dispuut treden conform het proces Dispuut over meterstanden. 

- s. De leverancier kan (als wederpartij) tegen vastgestelde meterstanden in dispuut treden conform het proces Dispuut over meterstanden. 

## 4.16.2 Procesbeschrijvingen KA

### Vaststellen en communiceren vastgestelde meterstanden KA door leverancier

Bijlage B1114: Subprocesplaat SP0015 KA – Vaststellen en communiceren vastgestelde meterstanden KA door leverancier

1. De leverancier bepaalt op basis van het type meetinrichting, administratieve status en uitleesbaarheid van de meetinrichting met communicatiefunctionaliteit of hij het collectieproces moet opstarten. 

2. In geval van een meetinrichting met handopname zal de verantwoordelijke leverancier de klant verzoeken een meterstand door te geven. 

3. De leverancier valideert de meterstand conform de validatieregels, zoals vastgelegd in de Energiewet en lagere regelgeving. 

4. Indien de leverancier geen meterstand heeft kunnen collecteren dan berekent hij een meterstand, conform de algoritmen vastgelegd in de Energiewet en lagere regelgeving. 

5. Wanneer de gecollecteerde meterstand bij validatie niet valide blijkt te zijn, verwerkt de leverancier de uitval uiterlijk binnen 15 werkdagen na de mutatiedatum. Hij doet dit als volgt: 

   - a. Hij neemt contact op met de klant om de meterstand te verifiëren dan wel een alternatieve meterstand vast te stellen. 

   - b. Indien contact met de klant niet mogelijk is wordt de meterstand conform de werkwijze in subproces ‘Vaststellen en berekenen meterstanden door systeembeheerder KA’ berekend. 

6. De leverancier stelt uiterlijk binnen 15 werkdagen na mutatiedatum de gevalideerde of berekende meterstand vast. 

7. De leverancier verstuurt de vastgestelde meterstand uiterlijk één werkdag na vaststelling naar de systeembeheerder. 

8. De systeembeheerder ontvangt de vastgestelde meterstand. 

### Ontvangen vastgestelde meterstand KA door systeembeheerder

Bijlage B1115: Subprocesplaat SP0015 KA – Ontvangen vastgestelde meterstand KA door systeembeheerder

1. De systeembeheerder ontvangt de ‘melding vastgestelde meterstand’ van een leverancier en beoordeelt deze op de volgende punten en waar relevant met betrekking tot de datum waarop de meterstand betrekking heeft: 

   - a. Is de melding ‘vastgestelde meterstand’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is het allocatiepunt voorzien van een meetinrichting? 

   - d. Is de leverancier, die de vastgestelde meterstand heeft ingediend, geregistreerd als actuele leverancier op het allocatiepunt dan wel, de leverancier die de mutatie heeft geïnitieerd? 

   - e. Is de ontvangen periodieke meterstand de meest recent vastgestelde meterstand? 

   - f. Is er voor de vastgestelde meterstand nog een dispuut mogelijk? 

   - g. Komt het aantal aangeboden meterstanden overeen met het aantal actieve telwerken van de meetinrichting? 

   - h. Is het aantal posities van de aangeboden meterstanden niet groter dan het aantal posities (telwielen) van de telwerken van de meetinrichting? 

   - i. _Indien de ingediende meterstand door de leverancier is gekoppeld aan een mutatieproces:_ Is een mutatieproces voor het betreffende allocatiepunt en datum bekend? 

   - j. Is de meterstand ingediend voor een allocatiepunt op een kleine aansluiting? k. Betreft de herkomstindicatie van de meterstand ‘berekend’, ‘klantstand’ of ‘overeengekomen’? 

   - l. Indien het allocatiepunt is voorzien van een meetinrichting met communicatiefunctionaliteit en de reeds eerder vastgestelde meterstand voor de betreffende datum 'berekend' is door de systeembeheerder of de herkomstindicatie 'klantstand' of 'overeengekomen' heeft: Heeft de door de leverancier aangeboden meterstand de herkomstindicatie 'klantstand' of 'overeengekomen'? 

   - m. Indien het allocatiepunt is voorzien van een meetinrichting met communicatiefunctionaliteit en er is al een meterstand vastgesteld voor de betreffende datum: Heeft deze vastgestelde meterstand een herkomstindicatie ongelijk aan 'P4-stand' of 'fysieke opname'? 

   - n. Indien het allocatiepunt is voorzien van een meetinrichting met communicatiefunctionaliteit: Is er al een meterstand vastgesteld voor de betreffende datum? 

2. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding vastgestelde meterstand’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst van de ‘melding vastgestelde meterstand’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. Het allocatiepunt is niet voorzien van een meetinrichting. 

   - d. De leverancier was op de betreffende datum niet als actuele leverancier geregistreerd op het allocatiepunt of is niet bekend als initiator van het mutatieproces. 

   - e. Er is reeds een vastgestelde meterstand bekend met een recentere datum. 

   - f. De vastgestelde meterstand is te laat ingediend en kan hierdoor niet meer door een wederpartij in dispuut worden getrokken. 

   - g. Het aantal aangeboden meterstanden komt niet overeen met het aantal actieve telwerken van de meetinrichting. 

   - h. Het aantal posities van de aangeboden meterstanden is groter dan het aantal posities (telwielen) van de telwerken van de meetinrichting. 

   - i. Er is geen mutatieproces bekend voor het betreffende allocatiepunt en datum. 

   - j. De meterstand is niet ingediend voor een allocatiepunt op een kleine aansluiting. 

   - k. De meterstand is ingediend met een niet passende herkomstindicatie. 

   - l. De meterstand is ingediend voor een allocatiepunt met een op afstand uitleesbare meter waarvoor nog geen meterstand is vastgesteld. 

3. De leverancier verwerkt de afwijzing. 

4. Indien de systeembeheerder geen vastgestelde meterstand van de leverancier heeft ontvangen binnen de gestelde termijnen, bepaalt de systeembeheerder binnen de gestelde termijnen namens de leverancier een meterstand (zie voor termijnen de paragraaf ‘Termijnen’). 

5. De systeembeheerder start de verwerking van de meterstand, ongeacht een mogelijke start van het proces Dispuut over meterstanden. 

### Vaststellen en berekenen meterstanden KA door systeembeheerder

Bijlage B1116: Subprocesplaat SP0015 KA – Vaststellen en berekenen meterstanden KA door systeembeheerder

1. De systeembeheerder bepaalt op basis van het type meetinrichting, administratieve status en uitleesbaarheid van de meetinrichting met communicatiefunctionaliteit of hij het collectieproces moet opstarten met betrekking tot de meterstanddatum. 

2. In geval van een meetinrichting met communicatiefunctionaliteit leest de systeembeheerder de meterstanden op afstand uit. 

3. De systeembeheerder valideert de meterstand op basis van de volgende criteria: 

   - a. De meterstand is gelijk aan of hoger dan de voorgaande vastgestelde uitgelezen meterstand op dezelfde meetinrichting en telwerk; 

   - b. De waarde van het berekende verschil tussen de uitgelezen en vorige vastgestelde uitgelezen meterstand van een telwerk is niet groter dan fysiek mogelijk zou zijn volgens de fysieke capaciteit van het allocatiepunt in het aansluitingenregister. 

4. De systeembeheerder berekent de meterstanden op basis van de beschikbare laatste meterstanden van dezelfde meter en telwerk indien: 

   - a. De gecollecteerde meterstand(en) bij validatie niet valide blijkt(en) te zijn; 

   - b. Uiterlijk 15 werkdagen na de mutatiedatum of de maandovergang geen meterstanden uitgelezen konden worden; 

   - c. De leverancier in gebreke is gebleven en niet tijdig meterstanden heeft aangeleverd voor een meetinrichting met handopname. 

5. De systeembeheerder stelt de valide meterstanden en de berekende meterstanden vast. 

## 4.16.3 Termijnen KA

### Voor meetinrichtingen met handopname:

- a. De leverancier verstuurt de vastgestelde meterstand op de mutatiedatum doch uiterlijk de 15<sup>e</sup> werkdag na de mutatiedatum, ingeval van een periodieke meterstand uiterlijk de eerste werkdag na vaststelling, naar de systeembeheerder. 

- b. De leverancier zal gecollecteerde meterstanden valideren en vaststellen en de meterstand uiterlijk één werkdag na vaststellen versturen naar de systeembeheerder. 

- c. De leverancier dient minimaal eenmaal per twaalf maanden een meterstand vast te stellen en deze te versturen naar de systeembeheerder. 

- d. Wanneer de gecollecteerde meterstand bij validatie niet valide blijkt te zijn dan verwerkt de leverancier de uitval uiterlijk binnen 15 werkdagen na de mutatiedatum 

- e. Indien de systeembeheerder geen vastgestelde meterstand van de leverancier heeft ontvangen binnen de gestelde termijnen, op uiterlijk de 15<sup>e</sup> werkdag na de mutatiedatum of uiterlijk 14 maanden na de laatste vastgestelde meterstand, stelt de systeembeheerder binnen de gestelde termijnen namens de leverancier een meterstand vast. 

   - i. Voor een meterstand behorende bij een mutatie communiceert de systeembeheerder de meterstand uiterlijk de 21<sup>e</sup> werkdag na de mutatiedatum; 

   - ii. Voor een periodieke meterstand communiceert de systeembeheerder een meterstand met opnamedatum 12 maanden na de laatste vastgestelde meterstand, uiterlijk 14 maanden plus vijf werkdagen na de laatste vastgestelde meterstand. 

### Voor op afstand uitleesbare meetinrichtingen:

- f. De systeembeheerder leest uiterlijk 5 werkdagen na mutatiedatum, na de datum uit het verzoek vaststellen meterstand of na de maandovergang de meterstanden uit in geval van een op afstand uitleesbare meetinrichting. 

- g. Indien een uitgelezen meterstand niet valide is, berekent de systeembeheerder de meterstanden en stelt de berekende vastgestelde meterstanden en evt. bijbehorende volumes uiterlijk de 6e werkdag na mutatiedatum of na de maandovergang voor elektriciteit ter beschikking aan de leverancier. Volumes voor maandovergang meterstanden van gas worden berekend nadat de maandgemiddelde calorische omrekenfactor beschikbaar is. De meterstanden en volumes voor maandovergangmeterstanden voor gas worden zo spoedig mogelijk nadat de maandgemiddelde calorische omrekenfactor beschikbaar is doch uiterlijk 15 werkdagen na de maandovergang ter beschikking gesteld aan de leverancier. 

- h. De systeembeheerder berekent voor allocatiepunten met een op afstand uitleesbare meetinrichting de meterstanden en stelt deze uiterlijk 15 werkdagen na de mutatiedatum, na de datum uit het verzoek vaststellen meterstand of na de maandovergang vast indien er geen meterstanden uitgelezen konden worden. 

## 4.16.4 Gegevensuitwisseling

### Melding vastgestelde meterstand KA

|**Melding vastgestelde meterstand**|**KA**|||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Transactiedossiernummer|A|Ja|Ja|1|Transactiedossiernummer is verplicht bij het indienen van een<br>vastgestelde meterstand behorend bijeen mutatieproces|
|Proces ID|V|Ja|Ja|1|Reden van aanlevering|
|Referentie|O|Ja|Ja|1||
|EAN-code leverancier|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|Ja|Ja|1||
|Productsoort|V|Ja|Ja|1|Elektriciteit of gas|
|**_Meetinrichting:_**||||**_1 per E_**|**_AN-code allocatiepunt_**|
|Meetinrichtingnummer|V|Ja|Ja|1||
|Aantal telwerken|V|Nee|Ja|1|Aantal actieve telwerken|
|**_Telwerk:_**||||**_n per m_**|**_eetinrichting_**|
|Registertype|V|Nee|Ja|1|Normaal<br>Laag<br>Teruglevering normaal<br>Terugleveringlaag|
|Meeteenheid|V|Ja|Ja|1||
|Aantal telwielen|V|Ja|Ja|1||
|**_Meterstand:_**||||**_1 per t_**|**_elwerk_**|
|Meterstand|V|Ja|Ja|1||
|Meterstanddatum|V|Ja|Ja|1||
|Herkomstindicatie|V|Ja|Ja|1|P4 is niet toegestaan als herkomstindicatie|

### Afwijzing vastgestelde meterstand KA

|**Afwijzing vastgestelde meterstan**|**d KA**|||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Proces ID|V|Ja|Ja|1|Reden van aanlevering van vastgestelde meterstand|
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Transactiedossiernummer|V|Ja|Ja|1|Gevuld vanuit de melding vastgestelde meterstand of gevuld door<br>nieuw transactiedossiernummer bijde verwerking|
|EAN-code systeembeheerder|V|Ja|Ja|1||
|EAN-code leverancier|V|Ja|Ja|1||
|Afwijsreden|V|Ja|Ja|n|Indicatie van de reden waarom de vastgestelde meterstand is<br>afgewezen:<br>Periodiek + events:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het allocatiepunt is onbekend in het aansluitingenregister van de<br>systeembeheerder.<br>•<br>Het allocatiepunt is niet voorzien van een meetinrichting.<br>•<br>De leverancier was op de betreffende datum niet geregistreerd<br>als actuele leverancier op het allocatiepunt of is niet bekend als<br>initiator van het mutatieproces.<br>•<br>Er is reeds een vastgestelde meterstand bekend met een<br>recentere datum.<br>•<br>De vastgestelde meterstand is te laat ingediend en kan hierdoor<br>niet meer door een wederpartij in dispuut worden getrokken;<br>•<br>Het aantal aangeboden meterstanden komt niet overeen met het<br>aantal actieve telwerken van de meetinrichting.<br>•<br>Het aantal posities van de aangeboden meterstanden is groter<br>dan het aantal posities (telwielen) van de telwerken van de<br>meetinrichting.<br>•<br>Er is geen mutatieproces bekend voor het betreffende<br>allocatiepunt en datum.|

|**Afwijzing vastgestelde metersta**|**nd KA**|||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
||||||•<br>De meterstand is niet ingediend voor een allocatiepunt op een<br>kleine aansluiting.<br>•<br>De<br>meterstand<br>is<br>ingediend<br>met<br>een<br>niet<br>passende<br>herkomstindicatie.<br>•<br>De meterstand is ingediend voor een op afstand uitleesbare<br>meetinrichtingwaarvoor nog geen meterstand is vastgesteld.|
|Toelichting afwijsreden|O|Ja|Ja|n||

## 4.16.5 Procesafspraken SJ en volume bepalen KA

- a. Standaardjaarvolume afname en invoeding elektriciteit (SJA/SJI) en standaardjaarverbruik gas (SJV): 

- i. Het SJ (SJV/SJA/SJI) wordt herberekend op basis van alle vastgestelde af- of uitgelezen meterstanden. 

- ii. De systeembeheerder berekent het SJ conform de regels zoals vastgelegd in de Energiewet en lagere regelgeving. 

- iii. Het SJ wordt bepaald op het niveau van het allocatiepunt. 

- iv. Bij een allocatiepunt met een profielcategorie waar slechts één SJ dient te worden vastgesteld wordt het SJ gekenmerkt als SJ Normaaluren. 

- v. Bij onbemeten allocatiepunten zoals bedoeld in Energiewet en lagere regelgeving, wordt een forfaitair SJ gebruikt. Bij onbemeten allocatiepunten kunnen geen additionele allocatiepunten aanwezig zijn. 

- vi. Als een meterstand naar aanleiding van een dispuut wordt herzien, blijft het op basis van deze meterstand berekende SJ geldig tot het moment dat de uit het dispuut resulterende herziene meterstand leidt tot een nieuwe bepaling van het SJ. 

- vii. Bij een meetinrichting mutatie die tot gevolg heeft dat een allocatiepunt elektriciteit van een enkel tarief profielcategorie naar een dubbel tarief profielcategorie gaat, zal de systeembeheerder het SJA/SJI in het aansluitingenregister wijzigen door het op het moment van het administratief verwerken van de wissel van de meetinrichting voor het allocatiepunt geldige SJA/SJI volgens een vaste verdeelsleutel voor de betreffende profielcategorie te verdelen over Normaaluren en Laaguren. 

- viii. De systeembeheerder draagt zorg dat de bepaling van SJ en plaatsing in het aansluitingenregister uiterlijk de 5<sup>e</sup> werkdag na ontvangst van een vastgestelde meterstand zijn uitgevoerd. 

- ix. Bij het herberekenen van het SJV gas dient de systeembeheerder ook het capaciteitstarief opnieuw te bepalen. 

- x. Wanneer de systeembeheerder aan de hand van een gemeten volume constateert dat er op een allocatiepunt voor het eerst binnen 345 dagen teruglevering plaatsvindt, moet hij de begindatum van deze volumeperiode gebruiken als begindatum voor het berekenen van het SJI en SJA zoals bedoeld in de Energiewet en lagere regelgeving. 

- b. Volumebepaling: 

- i. Voor alle ontvangen vastgestelde meterstanden, met uitzondering van de eerste (begin)stand op een nieuwe meetinrichting wordt een volume bepaald. 

- ii. Volumes worden bepaald conform het gestelde in de Energiewet en lagere regelgeving. 

- iii. De systeembeheerder draagt zorg dat de volumebepaling uiterlijk de 5<sup>e</sup> werkdag na het vaststellen van de meterstand is uitgevoerd en in het TMR is opgenomen en gecommuniceerd naar de betrokken marktpartijen. 

- iv. De systeembeheerder berekent de volumes naar aanleiding van vastgestelde maandovergangmeterstanden van allocatiepunten gas na publicatie van de maandgemiddelde calorische omrekenfactor van de betreffende maand. 

## 4.16.6 Procesbeschrijvingen KA

### SJ (SJV/SJA/SJI) bepalen

Bijlage B1117: Subprocesplaat SP0015 KA – SJ (SJV/SJA/SJI) bepalen

1. De systeembeheerder bepaalt het SJ, behalve bij een berekende meterstand, conform de rekenregels in de Energiewet en lagere regelgeving. 

2. De systeembeheerder verwerkt het SJ in het aansluitingenregister. 

### Volume bepalen voor reconciliatie

Bijlage B1118: Subprocesplaat SP0015 KA – Volume bepalen voor reconciliatie

1. De systeembeheerder bepaalt na de vaststelling van de meterstand het volume voor reconciliatie conform de rekenregels in de Energiewet en lagere regelgeving. 

Elektriciteit: 

   - a. Bij een reguliere meetinrichting elektriciteit<sup>4</sup> met een telwerk voor hoog en een telwerk voor laag: 

      - i. LAAG: Het verschil tussen de eindstand en de beginstand van het telwerk laag vermenigvuldigd met de omrekenfactor. 

      - ii. NORMAAL: Het verschil tussen de eindstand en de beginstand van het telwerk hoog vermenigvuldigd met de omrekenfactor. 

   - b. Bij een meetinrichting elektriciteit met een telwerk voor totaal en een telwerk voor laag (Amsterdamse meetinrichting ): 

      - i. LAAG: Het verschil tussen de eindstand en de beginstand van het telwerk laag vermenigvuldigd met de omrekenfactor. 

      - ii. NORMAAL: Het verschil tussen de eindstand en de beginstand van het telwerk totaal vermenigvuldigd met de omrekenfactor verminderd met het LAAG volume. 

   - c. Bij een meetinrichting elektriciteit met een enkel telwerk: i. LAAG: n.v.t. 

      - ii. NORMAAL: Het verschil tussen de eindstand en de beginstand van het telwerk vermenigvuldigd met de omrekenfactor. 

Bij bemeten allocatiepunten gas is het onderscheid tussen NORMAAL en LAAG niet van toepassing. 

> 4 Ook bij teruglevering is er sprake van een volume NORMAAL/LAAG. De wijze van berekening is identiek aan de wijze van berekening van het volume bij levering. 

### Distributie meetgegevens en opnemen in TMR

Bijlage B1119: Subprocesplaat SP0015 KA – Distributie meetgegevens en opnemen in TMR

1. De systeembeheerder verstuurt, conform de afgesproken termijnen, de vastgestelde meterstand (en volume) aan (indien aanwezig): 

   - a. de actuele leverancier: de vastgestelde meterstand en het volume in geval van een periodieke of fysieke meteropname wegens de driejaarlijkse meteropname of meetinrichting mutatie. 

   - b. de oude leverancier: de vastgestelde meterstand en het volume in geval van een leveranciersswitch, uithuizing, einde levering of inhuizing met geforceerde uithuizing. 

   - c. de nieuwe leverancier: de vastgestelde meterstand in geval van een leverancierswitch of inhuizing. 

2. De nieuwe leverancier ontvangt en verwerkt de meterstand.. 

3. De huidige leverancier ontvangt en verwerkt de meterstand en het volume. 

4. De oude leverancier ontvangt en verwerkt de meterstand en het volume. 

5. De systeembeheerder stelt, conform de afgesproken termijnen, na de ontvangst van de vastgestelde meterstand de meterstanden en volumes beschikbaar via het TMR. 

## 4.16.7 Termijnen KA

### In geval van een meetinrichting met handopname:

- a. De systeembeheerder bepaalt zo spoedig mogelijk, doch uiterlijk de vijfde werkdag na de ontvangst van de vastgestelde meterstand of uiterlijk de vijfde werkdag nadat de systeembeheerder namens de leverancier een meterstand heeft vastgesteld het SJ, behalve bij een berekende meterstand. 

- b. De systeembeheerder bepaalt zo spoedig mogelijk, doch uiterlijk de vijfde werkdag na de ontvangst van de vastgestelde meterstand of uiterlijk de vijfde werkdag nadat de systeembeheerder namens de leverancier een meterstand heeft vastgesteld het volume. 

- c. De systeembeheerder verstuurt zo spoedig mogelijk, doch uiterlijk vijf werkdagen na de ontvangst van de vastgestelde meterstand of uiterlijk vijf werkdagen nadat de systeembeheerder namens de leverancier een meterstand heeft vastgesteld aan (indien aanwezig): 

   - i. de actuele leverancier: de vastgestelde meterstand en het volume in geval van een periodieke of fysieke meteropname wegens de driejaarlijkse meteropname of meetinrichting mutatie. 

   - ii. de oude leverancier: de vastgestelde meterstand en het volume in geval van een leverancierswitch, uithuizing, einde levering of inhuizing met geforceerde uithuizing. 

   - iii. de nieuwe leverancier: de vastgestelde meterstand in geval van een leverancierswitch of inhuizing. 

- d. De systeembeheerder stelt zo spoedig mogelijk, doch uiterlijk vijf werkdagen na de ontvangst van de vastgestelde meterstand de gegevens beschikbaar via het TMR. 

### In gevalvan een op afstand uitleesbare meetinrichting:

- e. De systeembeheerder bepaalt voor op afstand uitleesbare meetinrichtingen uiterlijk één werkdag na het vaststellen van de meterstanden de volumes. Indien voor een voorafgaande periode nog meterstanden vastgesteld dienen te worden, vindt de vaststelling en berekening van het volume pas plaats zodra de voorliggende meterstanden zijn vastgesteld. 

- f. De systeembeheerder verstuurt zo spoedig mogelijk, doch uiterlijk één werkdag na vaststelling van de meterstanden en berekening van volumes (indien aanwezig): 

   - i. aan de leverancier: de vastgestelde meterstanden en de volumes in geval van een mutatie van de meetinrichting, fysieke opname, balanceringsverantwoordelijkeswitch of een verzoek vaststellen meterstanden en volumes. 

   - ii. aan de leverancier: de vastgestelde meterstanden en de volumes in geval van een leverancierswitch, uithuizing, einde levering of inhuizing met geforceerde uithuizing. 

   - iii. de nieuwe leverancier: de vastgestelde meterstanden in geval van een leverancierswitch of inhuizing. 

- g. De systeembeheerder verstuurt zo spoedig mogelijk voor elektriciteit de maandovergangmeterstanden doch uiterlijk 15 werkdagen na de eerste kalenderdag van de maand de vastgestelde maandovergangmeterstanden en de volumes aan de actuele leverancier. 

- h. In afwijking van e. berekent de systeembeheerder het volume voor gas voor maandovergangmeterstanden van allocatiepunten met een op afstand uitleesbare meetinrichting nadat de maandgemiddelde calorische omrekenfactoren zijn gepubliceerd. De vastgestelde meterstanden en volumes worden zo spoedig mogelijk, doch uiterlijk 15 werkdagen na de eerste kalenderdag van de maand aan de actuele leverancier verstuurd. 

## 4.16.8 Gegevensuitwisseling

### Meterstand en volume KA

|**Meterstand en volume KA**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Transactiedossiernummer|A|Ja|Ja|1|Niet door de systeembeheerder, maar door het Portaal gevuld bij<br>communicatie van fysieke opname. In alle overige gevallen verplicht<br>gevuld.|
|Proces ID|V|Ja|Ja|1|Reden van aanlevering|
|Referentie|O|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|EAN-code systeembeheerder|V|Ja|Ja|1|Systeembeheerder|
|EAN-code leverancier|V|Ja|Ja|1||
|Productsoort|V|Ja|Ja|1|Elektriciteit of gas|
|**_Meetinrichting_**:||||**_1 per E_**|**_AN-code allocatiepunt_**|
|Meetinrichtingnummer|V|Ja|Ja|1||
|Aantal telwerken|V|Nee|Ja|1|Aantal actieve telwerken|
|**_Telwerk_**:||||**_n per m_**|**_eetinrichting_**|
|Registertype|V|Nee|Ja|1|1 per telwerk:<br>•<br>Normaal<br>•<br>Laag<br>•<br>Teruglevering normaal<br>•<br>Terugleveringlaag|
|Meeteenheid|V|Ja|Ja|1||
|Aantal telwielen|V|Ja|Ja|1||
|**_Volume:_**||||**_1 per te_**|**_lwerk_**|
|Hoeveelheid|A|Ja|Ja|1|Indien alleen één meterstand wordt gecommuniceerd (o.a. een<br>inhuisstand),isgeen volumegevuld.|

|**Meterstand en volume KA**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Gecorrigeerde hoeveelheid|A|Ja|nvt|1|Indien alleen één meterstand wordt gecommuniceerd (o.a. een<br>inhuisstand),isgeen volumegevuld.|
|**_Meterstand:_**||||**_Per vol_**<br>**_Indieng_**|**_ume (2 meterstanden: beginstand en eindstand)_**<br>**_een volume(1 meterstand)_**|
|Meterstand|V|Ja|Ja|1||
|Meterstanddatum|V|Ja|Ja|1||
|Herkomstindicatie|V|Ja|Ja|1|•<br>P4-stand|

## 4.16.9 Procesafspraken GA Collecteren, volume bepalen en versturen vastgestelde meterstand en volume

   - a. De meetverantwoordelijke partij stelt alle meterstanden en volumes voor bemeten allocatiepunten op grote aansluitingen vast. 

   - b. Binnen de definitie van periodieke meterstanden en volumes, zoals deze gehanteerd wordt vallen de volgende meterstanden en volumes: 

      - i. gas: periodieke opname van niet op afstand uitleesbare allocatiepunten op grote aansluitingen; 

      - ii. elektriciteit: jaarlijks bemeten indien artikel 1.3 lid 1 of 2 van de Energiewet met een doorlaatwaarde kleiner dan of gelijk aan 3x80A; 

      - iii. elektriciteit: maandelijkse tellerstanden en volumes van continu bemeten allocatiepunten. 

   - c. De periodieke meterstand voor een niet op afstand uitleesbaar allocatiepunt op een grote aansluiting gas wordt minimaal jaarlijks vastgesteld door de meetverantwoordelijke partij en verstuurd naar de systeembeheerder. 

   - d. Voor continu bemeten allocatiepunten gas worden geen periodieke meetgegevens uitgewisseld; deze informatie wordt via de telemetrieketen uitgewisseld. De volumecorrecties die volgen uit de halfjaarlijkse opname van continu bemeten allocatiepunten gas, worden als correctie-energie middels de allocatie aan de leverancier beschikbaar gesteld. 

   - e. Om te bepalen met welke frequentie (maandelijks, jaarlijks) een meterstand gecollecteerd dient te worden, kan de meetverantwoordelijke partij gebruik maken van het kenmerk ‘meetmethode’ uit het stamgegevensbericht. 

## 4.16.10 Procesbeschrijvingen GA

### Collecteren meterstand GA

Bijlage B1120: Subprocesplaat SP0015 GA – Collecteren meterstand GA

1. Voor welke populatie allocatiepunten een periodieke meterstand gecollecteerd dient te worden, wordt bepaald door (een combinatie van): 

   - a. de meetmethode; 

   - b. de afrekenmaand (genoemd in het aansluitingenregister); 

   - c. de capaciteit van het allocatiepunt (elektriciteit, maandopname); 

   - d. de tijd verstreken sinds de activering van de meetinrichting of de vorige uit- of aflezing (continue bemeten, halfjaarlijkse opname). 

In geval van een niet op afstand uitleesbare meetinrichting zal de meetverantwoordelijke partij een meterstand uit- of aflezen of de klant verzoeken om een meterstand door te geven (via een meterstandenkaart, internet, telefoonservice). 

In geval van een jaarlijkse opname bij aansluitingen elektriciteit, dient de opname in de zes weken voorafgaande aan de afrekenmaand (genoemd in het aansluitingenregister) plaats te vinden. 

2. De meetverantwoordelijke partij zal de gecollecteerde meterstanden valideren, conform het gestelde in de Energiewet en lagere regelgeving). 

3. Indien de meetverantwoordelijke partij redelijkerwijs niet in staat is de tellerstand uit of af te lezen of de klant heeft geen meterstand aangeleverd, berekent de meetverantwoordelijke partij een meterstand conform de rekenregels zoals gesteld in de Energiewet en lagere regelgeving. 

4. Indien de meterstanden niet voldoen aan de validatieregels worden de gegevens door de meetverantwoordelijke partij (opnieuw) afgelezen en/of wordt in overleg met de klant vastgesteld dat het gemeten volume overeenkomt met het volume dat zou mogen worden verwacht. 

5. Indien de meterstanden voldoen aan de validatieregels, stelt de meetverantwoordelijke partij de meterstanden vast, uiterlijk één werkdag na datacollectie. 

### Berekenen volume en versturen vastgestelde meterstand en volume

Bijlage B1121: Subprocesplaat SP0015 GA – Berekenen volume en versturen vastgestelde meterstand en volume

1. De meetverantwoordelijke partij berekent het volume met behulp van de vastgestelde meterstand, de voorlaatste vastgestelde meterstand en de (technische) meetinrichting gegevens conform het gestelde in de Energiewet en lagere regelgeving. 

2. De meetverantwoordelijke partij verstuurt de vastgestelde meterstanden en het volume aan de systeembeheerder en zorgt ervoor dat de systeembeheerder de meetgegevens ontvangt binnen de volgende termijnen: 

   - a. jaarlijkse opname van aansluitingen elektriciteit: uiterlijk 10<sup>e</sup> werkdag na de dag van vaststelling; 

   - b. maandelijkse meterstanden en volumes van continue bemeten allocatiepunten elektriciteit: uiterlijk de 10<sup>e</sup> werkdag van de maand na de maand waarop de meterstanden en volumes betrekking hebben. 

3. De systeembeheerder ontvangt en verwerkt de meterstanden en volumes van de meetverantwoordelijke partij. 

## 4.16.11 Termijnen GA

- a. De meetverantwoordelijke partij levert de meterstand en het bijbehorende volume uiterlijk de 10<sup>e</sup> werkdag van de maand na de mutatiedatum aan bij de systeembeheerder. 

- b. Voor allocatiepunten op een grote aansluitingen elektriciteit die niet continue bemeten zijn, neemt de meetverantwoordelijke partij tenminste één keer per jaar de meterstand op, in de zes weken voorafgaande aan de afrekenmaand (genoemd in het aansluitingenregister). 

- c. De meetverantwoordelijke partij zal de vastgestelde meterstanden en volumes aanleveren aan de systeembeheerder en zorgt ervoor dat de systeembeheerder deze binnen de volgende termijnen ontvangen heeft: 

   - i. periodieke opname van niet op afstand uitleesbare allocatiepunten op grote aansluitingen elektriciteit: uiterlijk de 10<sup>e</sup> werkdag na de dag van vaststelling; 

   - ii. maandelijkse meterstanden en volumes van continue bemeten allocatiepunten elektriciteit: uiterlijk de 10<sup>e</sup> werkdag van de maand na de maand waarop de meterstanden en volumes betrekking hebben. 

## 4.16.12 Gegevensuitwisseling

De onderstaande tabel bevat de benodigde informatie-uitwisseling m.b.t. periodes langer of gelijk aan één allocatiedag. Deze informatie-uitwisseling kan de volgende informatie bevatten<sup>5</sup> : 

- Volumes per OVP (gas en elektriciteit) 

- Volumes per periode langer of gelijk aan één dag (gas en elektriciteit) 

- Meterstanden (gas en elektriciteit) 

- Diverse andere gegevens, zoals kWMax (elektriciteit) 

|**Meterstand en volume GA (verzond**|**en door**|**meetver**|**antwoor**|**delijke part**|**ij)**|||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**6|**Gas**|**Elek**<br>**aan-**<br>**sluiting**|**Elek**<br>**allocatie**<br>**punt**|**1/**<br>**n**|**Opmerking**|
|EAN-code aansluiting/<br>allocatiepunt/overdrachtspunt|V|V|Ja|Ja|Ja|1|Aansluiting en primair allocatiepunt hebben dezelfde<br>EAN-code|
|Indicatie type EAN-code<sup>7</sup>|O|O|Nee|Ja|Ja||Indicatie of de gegevens verstrekt een allocatiepunt of<br>overdrachtspunt betreffen|
|Generator ID / Verbruikers ID|A|A|Nee|Nee|Ja|n|Indien het een productie volume betreft, alleen in<br>maandbericht. Deze wordt ook in andere processen<br>gebruikt als mFRRda(Noodvermogen).|
|EAN-code meetverantwoordelijke<br>partij|V|V|Ja|Ja|Ja|1||
|EAN-code systeembeheerder of<br>balanceringsverantwoordelijke|V|V|Ja|Ja|Ja|1|De<br>EAN-code<br>van<br>de<br>systeembeheerder<br>of<br>balanceringsverantwoordelijke (alleen elektriciteit) die<br>het bericht ontvangt|
|EAN-code systeemgebied source|O||Ja|Ja|Ja|1|De EAN-code van het systeemgebied dat bij een<br>systeemkoppelingals source isgedefinieerd.|
|EAN-code systeemgebied sink|O||Ja|Ja|Ja|1|De EAN-code van het systeemgebied dat bij een<br>systeemkoppeling als sink is gedefinieerd. Verplicht bij<br>systeemkoppeling.|
|Berichtsoort|V|V|Ja|Ja|Ja|1|Origineel of update (een versienummer kan ook). Bij de<br>technische uitwerking van de berichten moet bepaald<br>worden of dit veld noodzakelijk is.|
|Productsoort|V|V|Ja|Ja|Ja|1|Elektriciteit of gas|
|Startdatum/tijd volumeperiode|V|V|Ja|Ja|Ja|1|DD:MM:YYYY HH:MM Startdatum en tijd van de periode<br>waar het bericht betrekkingopheeft.|
|Einddatum/tijd volumeperiode|A|A|Ja|Ja|Ja|1|DD:MM:YYYY HH:MM Einddatum en tijd van de periode<br>waar het bericht betrekking op heeft.|
|**_Volume per OVP_**||||||**_n p_**|**_er allocatiepunt_**|
|Startdatum OVP|V|V|Ja|Ja|Ja|1|DD:MM:YYYY HH:MM Startdatum en tijd van de periode<br>waar het volume betrekking op heeft. Dit kan ook<br>weergegeven worden door een nummer (OVP<br>Sequence). Afhankelijk van de standaard van het<br>nieuwe bericht.|
|Einddatum OVP|V|V|Ja|Ja|Ja|1|DD:MM:YYYY HH:MM Einddatum en tijd van de periode<br>waar het volume betrekking op heeft. Dit kan ook<br>weergegeven worden door een nummer (OVP<br>Sequence). Afhankelijk van de standaard van het<br>nieuwe bericht.|
|Hoeveelheid|V|V|Ja|Ja|Ja|1|Eén per volume (zonder decimalen)|

> 5 Deze informatie hoeft niet noodzakelijkerwijs via één bericht uitgewisseld worden. Dit kan via verschillende berichten. 

> 6 Exclusief onbemeten. 

> 7 Voor elektriciteit worden OVP waarden voor het type allocatiepunt uitgewisseld. Voor het type overdrachtspunt niet. Dit kan dezelfde EAN-code zijn. 

|**Meterstand en volume GA (verzo**<br>**Gegeven**|**nden door**<br>**GA**|**meetver**<br>**A1**6|**antwoor**<br>**Gas**|**delijke par**<br>**Elek**<br>**aan-**<br>**sluiting**|**tij)**<br>**Elek**<br>**allocatie**<br>**punt**|**1/**<br>**n**<br>**Opmerking**|
|---|---|---|---|---|---|---|
|Energiesoort|V|V|Nee|Ja|<br>Ja|1<br>Volume, blindverbruik, calorische waarde<sup>[1]</sup>|
|Energierichting|V|V|Nee|Ja|Ja|1<br>Levering, teruglevering|
|||||||LVR of TLV (levering of teruglevering). Voor gas geldt: Dit<br>is<br>al<br>in<br>aansluitingenregister<br>bepaald<br>qua<br>afnamecategorie. Hoeft niet per sé in het bericht.<br>Advies: niet in bericht.|
|Herkomstindicatie|V|V|?|Ja|Ja|1<br>Gemeten, Berekend, Gemeten Update|
|Validatiestatus|O|O|?|O|O|1|
|Reparatiemethodiek|O|O|O|O|O|1|
|Register type|A|A|Nee|Ja|Ja|1<br>één per volume<br>Alleen in maandberichtnormaal of laag|
|**_Restvolume_**||||||, <br>**_1 per allocatiepunt (gas)_**|
|Restvolume|A|A|Nee|Nee|Nee|1<br>Geregistreerde<br>hoeveelheid<br>restvolume<br>in<br>volumeperiode, let op teken!<br>Positief is teruglevering in systeemgebied<br>Negatief is levering door systeemgebied<br>Indien geen restvolume dan 0<br>In (XML) bericht geen negatieve waarden. In bericht<br>oplossen door dit aan te duiden met een<br>extra veld "leveringsrichting".|
|Energierichting|V|Nee|Ja|Nee|Nee|1<br>**Levering, teruglevering**|
|**_kW Max_**||||||**_n per overdrachtspunt (elektriciteit)_**<sup>**[2]**</sup>|
|Startdatum/tijd periode|A|A|Nee|Ja|Nee|1<br>DD:MM:YYYY HH:MM Startdatum en tijd van de periode<br>waar hetgegeven betrekkingopheeft.|
|Einddatum/tijd periode|A|A|Nee|Ja|Nee|<br>1<br>DD:MM:YYYY HH:MM Einddatum en tijd van de periode<br>waar hetgegeven betrekkingopheeft.|
|**kW Max**||||||<br>**_n per overdrachtspunt elektriciteit)_**|
|kW Max<br>Energie-eenheid|A<br>V|nvt<br>V|Nee<br>Ja|Ja<br>Ja|Nee<br>Ja|1<br>kW<br>1<br>kWh|
|<br>Energierichting|V|V|Nee|Ja|Ja|1<br>Levering, teruglevering|
|**_Meterstand_**||||||**_n per EAN-code_**allocatiepunt|
|Meetinrichting ID|A|A|O|O|O|1<br>Eén<br>per<br>meterstand:<br>Bij<br>een<br>correctievolume<br>(berichtsoort = update) worden geen meterstanden<br>|
|Meterstand|A|V|O|O|O|gecommuniceerd<br>1<br>Eén<br>per<br>meterstand:<br>Bij<br>een<br>correctievolume<br>(berichtsoort = update) worden geen meterstanden<br>gecommuniceerd|
|Eenheid|A|A|O|O|O|<br>1<br>kVar, kWh, Nm<sup>3</sup>|
|Energierichting register|A|A|O|O|Ja|2|
|Register ID|A|V|Ja|O|Ja|n<br>Eén<br>per<br>meterstand:<br>Bij<br>een<br>correctievolume<br>(berichtsoort = update) worden geen meterstanden<br>|
|Vermenigvuldigingsfactor|A|A|n.v.t|Ja|Ja|gecommuniceerd<br>1<br>Conform de Energiewet en lagere regelgeving|
|Opnamedatum|A|A|A|O|Ja|n<br>Eén<br>per<br>meterstand:<br>Bij<br>een<br>correctievolume<br>(berichtsoort = update) worden geen meterstanden<br>|
|Herkomstindicatie|A|A|A|Ja|Ja|gecommuniceerd,alleen in maandbericht.<br>n<br>Opgenomen<br>door<br>meetverantwoordelijke<br>partij,<br>Opgenomen<br>door<br>klant,<br>Berekend<br>door<br>meetverantwoordelijkepartij|
|Soort|A|A||||<br>Herleid volume, actieve energie, reactieve energie,<br>brutoproductieeigenverbruik)|
|Tariefzone|A|A|n.v.t.|Ja|Ja|, <br>1<br>Hoog of laag tarief|
|**Volumes (>= 1 dag)**||||||n per allocatiepunt/Productie-eenheid|
|<br>Startdatum/tijd periode|V|V|Ja|Ja|Ja|<br>1<br>DD:MM:YYYY HH:MM Startdatum en tijd van de periode<br>waar het volume betrekkingopheeft|
|Einddatum/tijd periode|V|V|Ja|Ja|Ja|.<br>1<br>DD:MM:YYYY HH:MM Einddatum en tijd van de periode<br>waar het volume betrekkingopheeft.|
|Soort|A|A||||<br>Herleid volume, actieve energie, reactieve energie,<br>brutoproductie,eigenverbruik)|

> [1] Alleen voor GIS/GIN en alleen indien gemeten door meetverantwoordelijke partij. 

> [2] De kWMax kan betrekking hebben op een maand of een week. 

|**Meterstand en volume GA (ver**|**zonden door**|**meetvera**|**ntwoor**|**delijke part**|**ij)**|||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**6|**Gas**|**Elek**<br>**aan-**<br>**sluiting**|**Elek**<br>**allocatie**<br>**punt**|**1/**<br>**n**|**Opmerking**|
|Hoeveelheid|V|V|Ja|Ja|Ja|1|Eén per volume (zonder decimalen)|
|Eenheid|A|A|O|O|O|1|kVarh, kWh, Nm<sup>3</sup>|
|Energierichting|A|A|O|O|Ja|1|Teruglevering, levering|
|Tariefzone|A|A|n.v.t.|Ja|Ja|1|Hoog of laag tarief|
|Herkomstindicatie|V|V|?|Ja|Ja|1|Gemeten, Berekend, Gemeten Update|
|Validatiestatus|O|O|?|O|O|1||
|Reparatiemethodiek|O|O|O|O|O|1||
|Herkomstindicatie|A|A|A|Ja|Ja|n|Opgenomen<br>door<br>meetverantwoordelijke<br>partij,<br>Opgenomen<br>door<br>klant,<br>Berekend<br>door<br>meetverantwoordelijkepartij|

## 4.16.13 Procesafspraken GA SJ (SJV/SJA/SJI)-bepaling en distributie meetgegevens

   - a. De systeembeheerder bepaalt zo spoedig mogelijk, doch uiterlijk de 5<sup>e</sup> werkdag na de ontvangst van de vastgestelde meterstand het SJ conform het gestelde in de Energiewet en lagere regelgeving. 

   - b. De systeembeheerder dient het bepalen van het SJ uit te voeren voor: 

      - Profielallocatiepunten gas- en elektriciteit (SJ) 

      - Telemetrie allocatiepunten op grote aansluitingen gas (JV) 

## 4.16.14 Procesbeschrijvingen GA

### SJ (SJV/SJA/SJI)-bepaling

Bijlage B1122: Subprocesplaat SP0015 GA – SJ (SJV/SJA/SJI)-bepaling

1. De systeembeheerder bepaalt zo spoedig mogelijk, doch uiterlijk de vijfde werkdag na de ontvangst van de vastgestelde meterstand het SJ conform het gestelde in de Energiewet en lagere regelgeving. De systeembeheerder bepaalt het jaarvolume conform het gestelde in de Energiewet en lagere regelgeving. 

2. De systeembeheerder verwerkt het SJ en jaarvolume in het aansluitingenregister en verstuurt de stamgegevens naar de marktpartijen op het allocatiepunt. 

### Distributie meetgegevens

Bijlage B1123: Subprocesplaat SP0015 GA – Distributie meetgegevens

1. De systeembeheerder bewaakt dat hij tijdig meterstanden en volumes van de meetverantwoordelijke partij ontvangt in het kader van mutatieprocessen en periodieke volumebepaling. 

2. Wanneer niet tijdig meterstanden en volumes aangeleverd worden en bij geconstateerde tekortkomingen in de meetgegevens informeert de systeembeheerder de meetverantwoordelijke partij en stelt deze zo nodig in gebreke. 

3. Indien noodzakelijk bepaalt de systeembeheerder een volume conform het gestelde in de Energiewet en lagere regelgeving. 

Voor onbemeten allocatiepunten elektriciteit zal de systeembeheerder geen meetgegevens ontvangen van een meetverantwoordelijke partij. Bij deze allocatiepunten bepaalt de systeembeheerder het volume op basis van lichturen, branduren, vermogen, bedrijfstijd of andere gegevens waarover de systeembeheerder kan beschikken om een volume vast te stellen. 

4. Voor volumes van allocatiepunten gas voert de systeembeheerder de calorische correctie uit. Dit geldt zowel voor de volumes die door de meetverantwoordelijke partij zijn aangeleverd als voor de volumes die de systeembeheerder zelf heeft berekend. 

5. De systeembeheerder verstuurt het volume (en de meterstanden indien aangeleverd door de meetverantwoordelijke partij) naar de actuele leverancier, uiterlijk de werkdag na ontvangst indien de meetverantwoordelijke partij meetgegevens aangeleverd heeft en uiterlijk de 15<sup>e</sup> werkdag van de afrekenmaand (genoemd in het aansluitingenregister) voor jaarlijks opgenomen allocatiepunten op aansluitingen elektriciteit en uiterlijk de 20<sup>e</sup> werkdag van de afrekenmaand voor jaarlijks opgenomen allocatiepunten op aansluitingen gas. De systeembeheerder maakt gebruik van de gegevens in zijn aansluitingenregister, om te bepalen wie de verantwoordelijke leverancier is gedurende de verbruiksperiode. Indien de systeembeheerder zelf een volume bepaald heeft (behoudens voor onbemeten allocatiepunten elektriciteit), distribueert de systeembeheerder het volume (ook) naar de meetverantwoordelijke partij. De systeembeheerder maakt gebruik van de gegevens in zijn aansluitingenregister, om te bepalen wie de meetverantwoordelijke partij is gedurende de verbruiksperiode. 

6. De leverancier ontvangt de vastgestelde meterstanden en volumes van de systeembeheerder. 

7. Indien het volume is bepaald door de systeembeheerder (behoudens voor onbemeten allocatiepunten elektriciteit): de meetverantwoordelijke partij ontvangt het door de systeembeheerder bepaalde volume. 

### Reclameren volumes en meterstanden elektriciteit

### Procesafspraken

- a. Een reclamatie met betrekking tot een bericht Volumes en meterstanden elektriciteit (zie par. 4.19.12 en par. 4.19.16) mag ingediend worden (de systeembeheerder doet dit met inachtneming van par. 4.19.16). 

   - a. bij het niet tijdig ontvangen hebben van deze meetgegevens; 

   - b. als de ontvangen meetgegevens volgens de ontvanger onjuist en/of onvolledig zijn; 

   - c. met betrekking tot alle meetpunten die conform de Systeemcode elektriciteit 2026 art. 2.4 voorzien zijn van een unieke EAN-code en waarvoor de meetverantwoordelijke partij meetgegevens moet versturen naar de systeembeheerder en eventueel ook de balanceringsverantwoordelijke zonder; 

   - d. specifiek voor een allocatiepunt elektriciteit met allocatiemethode TMT: als de ontvangen meetgegevens volgens de ontvanger onjuist en/of onvolledig zijn en de ontvangen meetgegevens ongelijk zijn aan de meest recente, geaccepteerde versies van de meetgegevens TMT over één kalenderdag (zie MSP-WE par. 4.1.4) waarop het betreffende reclamatieproces is toegepast of toegepast had kunnen worden (zie MSPWE par. 4.2.3 of par. 4.2.5). 

- b. Bij twijfel omtrent de juistheid en/of volledigheid van de meetgegevens elektriciteit dient de balanceringsverantwoordelijke en/of de systeembeheerder het herzieningsverzoek in bij de meetverantwoordelijke partij. 

- c. Een herzieningsverzoek bevat altijd een onderbouwing van de reclamatie. 

- d. Er mag maximaal eenmaal een herzieningsverzoek worden ingediend met betrekking tot een specifiek bericht Volumes en meterstanden of een niet ontvangen bericht Volumes en meterstanden. 

- e. Het antwoord van de meetverantwoordelijke partij is een acceptatie of een afwijzing van het herzieningsverzoek. Indien de meetverantwoordelijke partij het herzieningsverzoek niet honoreert, bevat het antwoord ook een motivatie. 

### Procesbeschrijving

Bijlage B1124: Subprocesplaat SP0015 GA – Procesbeschrijving

1. Indien de meetgegevens elektriciteit niet tijdig zijn ontvangen of niet voldoen aan de volledigheid en juistheid stuurt de reclamerende partij een herzieningsverzoek aan de meetverantwoordelijke partij om de meetgegevens aan te passen of alsnog aan te leveren. 

2. De meetverantwoordelijke partij beoordeelt het herzieningsverzoek op volledigheid, het voldoen aan de procesafspraken en vervolgens op inhoud. 

3. De meetverantwoordelijke partij beantwoordt het herzieningsverzoek. Indien het herzieningsverzoek wordt gehonoreerd, stelt de meetverantwoordelijke partij (nieuwe) maandmeetgegevens vast en stuurt separaat de (nieuwe) maandmeetgegevens en indien van toepassing een meetcorrectierapport (beschreven in par. 3.27 Informeren over meetcorrectie GA). 

4. De reclamerende partij ontvangt en verwerkt het antwoord van de meetverantwoordelijke partij. 

## 4.16.15 Termijnen GA

- a. De systeembeheerder stelt de vastgestelde volumes (en eventueel vastgestelde meterstanden) voor niet op afstand uitleesbare allocatiepunten op grote aansluitingen gas, uiterlijk de 20<sup>e</sup> werkdag van de afrekenmaand (genoemd in het aansluitingenregister) beschikbaar aan de actuele leverancier. 

- b. In geval van een maandelijks opgenomen allocatiepunten op grote aansluitingen gas stelt de systeembeheerder de vastgestelde volumes (en eventueel de meterstanden) uiterlijk de 20<sup>e</sup> werkdag van de maand na de maand waarop de gegevens betrekking hebben, beschikbaar aan de actuele leverancier. 

- c. De systeembeheerder stelt de vastgestelde volumes (en eventuele meterstanden) voor niet op afstand uitleesbare allocatiepunten op grote aansluitingen elektriciteit, uiterlijk de 15<sup>e</sup> werkdag van de afrekenmaand (genoemd in het aansluitingenregister) beschikbaar aan de leverancier. 

- d. In geval van telemetrisch bemeten allocatiepunten op grote aansluitingen elektriciteit stelt de systeembeheerder de vastgestelde volumes uiterlijk op de 15<sup>e</sup> werkdag na de maand waarop de gegevens betrekking hebben beschikbaar aan de leverancier. 

- e. De systeembeheerder bepaalt het SJV/SJA/SJI en verstuurt de stamgegevens uiterlijk vijf werkdagen na ontvangst van de meetgegevens van de meetverantwoordelijke partij naar de actuele marktpartijen in het aansluitingenregister. 

- f. De systeembeheerder bepaalt het jaarvolume en verstuurt de stamgegevens conform de termijnen in de Informatiecode elektriciteit en gas. 

- g. Bij mutatieprocessen worden volume (en eventuele meterstand) uiterlijk de 10<sup>e</sup> werkdag van de maand volgend op de mutatiedatum door de meetverantwoordelijke partij bepaald en aan de systeembeheerder aangeleverd. 

- h. De systeembeheerder verstuurt het volume (en de eventuele meterstand) in de maand na afloop van de betreffende verbruiksperiode respectievelijk aan (indien aanwezig) de oude en de initiërende leverancier. 

   - i. De systeembeheerder levert de meterstand en het volume uiterlijk de 15<sup>e</sup> werkdag van de maand na de mutatiedatum aan bij (indien aanwezig) de oude leverancier. 

   - ii. De systeembeheerder levert de meterstand en het volume uiterlijk de 15<sup>e</sup> werkdag van de maand na de mutatiedatum aan bij de initiërende leverancier. 

- i. De balanceringsverantwoordelijke partij en de systeembeheerder sturen een herzieningsverzoek zo snel mogelijk na constatering naar de meetverantwoordelijke partij. 

- j. De meetverantwoordelijke partij beantwoordt een herzieningsverzoek zo spoedig mogelijk doch uiterlijk de 10<sup>e</sup> werkdag na ontvangst van het herzieningsverzoek. 

- k. Indien het herzieningsverzoek wordt gehonoreerd, wijzigt de meetverantwoordelijke partij de meetgegevens, stuurt indien van toepassing een meetcorrectierapport en stuurt (een) nieuw(e) bericht(en) Meetgegevens volgens de daarvoor geldende termijnen na vaststelling. (beschreven in par. 3.27 Informeren over meetcorrectie GA). 

## 4.16.16 Gegevensuitwisseling

### Stand en volume GA (verzonden door systeembeheerder)

|**Stand en volume GA (verzonden**|**door systee**|**mbeheerd**|**er)**||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|Ja|Ja|1||

|**Stand en volume GA (verzonden do**|**or systee**|**mbeheerd**|**er)**||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Proces ID|V|V|Ja|Ja|1||
|Referentie|A|A|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|EAN-code leverancier|A|A|Ja|Ja|1||
|Productsoort|V|V|Ja|Ja|1|Elektriciteit of gas|
|Volumeperiode|V|V|Ja|Ja|1|Volumeperiode per allocatiepunt|
|**_Volume_**|||||**_Per EA_**|**_N allocatiepunt_**|
|Volumeperiode|V|V|Ja|Ja|n|Voor periodemarkeringen worden ‘tot datums’ gebruikt, zo<br>wordt de maand maart 2012 aangeduid van 01-03-12 tot 01-04-<br>12.|
|Registertype|V|V|Nee|Ja|n|Afhankelijk van mogelijke levering, teruglevering, normaal, laag.|
|Hoeveelheid|V|V|Ja|Ja|n|Afhankelijk van mogelijke levering, teruglevering, normaal, laag.|
|Gecorrigeerde hoeveelheid|V|V|Ja|Nee|1||
|**_Meterstand_**|||||**_2 per v_**|**_olume_**|
|Meterstand|O|V|Ja|Ja|1|Verplicht voor A1|
|Meterstanddatum|O|V|Ja|Ja|1|Verplicht voor A1|
|Herkomstindicatie|O|V|Ja|Ja|1|Verplicht voor A1|

### Herzieningsverzoek

|**Herzieningsverzoek door systeembe**|**heerder**|**of balanceringsverantwoordelijke partij bij de meetverantwoordelijke partij**|
|---|---|---|
|**Gegeven**|**GA**|**Toelichting**|
|Kenmerk herzieningsverzoek|V|De unieke identificatie van het herzieningsverzoek|
|Referentie naar de meetgegevens|O|De unieke identificatie van het/de bericht(en) meetgegevens waar de reclamatie betrekking op<br>heeft/hebben(optioneel;niet verplicht ingeval van niet ontvangen meetgegevens).|
|Identificatie allocatiepunt|V|De unieke identificatie van het allocatiepunt of de allocatiepunten waar de reclamatie betrekking op<br>heeft/hebben. Bij een reclamatie met betrekking tot niet tijdig ontvangen meetgegevens mogen<br>meerdere allocatiepunten in één herzieningsverzoek opgenomen worden. Bij overige reclamaties geldt<br>dat een herzieningsverzoek slechts één allocatiepunt bevat.|
|Periode|V|De periode waar het/de (ontbrekende) bericht(en) meetgegevens betrekking op heeft/hebben.|
|Reclamatiereden|V|Omschrijving van de reden van reclamatie.|
|Toelichting|O|Een toelichting op de reclamatie|

### Antwoord op herzieningsverzoek

|**Antwoord op herzieningsverzoek**|**door meet**|**verantwoordelijke partij aan systeembeheerder of balanceringsverantwoordelijke partij**|
|---|---|---|
|**Gegeven**|**GA**|**Toelichting**|
|Kenmerk herzieningsverzoek|V|De unieke identificatie van het herzieningsverzoek|
|Antwoord|V|•<br>Verzoek gehonoreerd<br>•<br>Verzoek nietgehonoreerd|
|Toelichting|O|Een toelichting op het besluit van de meetverantwoordelijke partij (verplicht indien het<br>herzieningsverzoek niet isgehonoreerd).|
