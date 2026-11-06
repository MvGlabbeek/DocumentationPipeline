# 4.41 Verzoeken vaststellen meterstand KA


## 4.41.1 Procesafspraken KA

- a. Ten behoeve van de facturatie van de klant heeft leverancier de mogelijkheid om voor een allocatiepunt met een op afstand uitleesbare meetinrichting, meterstanden en volumes te laten vaststellen. Hiervoor dient een leverancier een verzoek in bij de systeembeheerder. Indien het verzoek voldoet, worden voor de gewenste datum meterstanden en volumes vastgesteld voor het betreffende allocatiepunt door de systeembeheerder. De vastgestelde volumes worden gehanteerd in de reconciliatie. 

   - Verzoeken mogen alleen plaatsvinden door de actuele leverancier op het allocatiepunt. 

   - Er dient sprake te zijn van een allocatiepunt met een op afstand uitleesbare meetinrichting van een kleine aansluiting. 

   - Uiterlijk drie keer per maand mag voor een allocatiepunt een verzoek voor vastgestelde meterstanden ingediend worden. 

   - Een verzoek wordt afgewezen indien: 

      - de datum in het verzoek in de toekomst ligt; of, 

      - de datum in het verzoek ligt voor of op een datum waarvoor meterstanden vastgesteld zijn of moeten worden vastgesteld ten gevolge van een mutatieproces, een maandovergang of een ander proces voor vastgestelde meterstanden. 

## 4.41.2 Procesbeschrijving KA

Bijlage B1169: Subprocesplaat zonder SP-code (§4.41.2) KA

1. De leverancier verstuurt het verzoek vaststellen meterstand. 

2. De systeembeheerder ontvangt het ‘verzoek vaststellen meterstand’ van de leverancier en beoordeelt het verzoek op de volgende punten: 

   - a. Is het verzoek volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is het verzoek ingediend voor allocatiepunt op een kleine aansluiting? 

   - d. Is het allocatiepunt voorzien van een op afstand uitleesbare meetinrichting? 

   - e. Is de leverancier geregistreerd als actuele leverancier op het allocatiepunt? 

   - f. Is de datum in het verzoek gelijk aan vandaag of eerder, en ligt deze datum na een datum waarvoor meterstanden vastgesteld zijn of moeten worden? 

   - g. Is het aantal eerdere verzoeken voor vastgestelde meterstanden voor de betreffende maand kleiner dan drie? 

Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder het ‘verzoek vaststellen meterstand’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst van het ‘verzoek vaststellen meterstand’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is niet bekend in het aansluitingenregister van de systeembeheerder. 

   - c. Het allocatiepunt betreft geen allocatiepunt op een kleine aansluiting. 

   - d. Het allocatiepunt is niet voorzien van een op afstand uitleesbare meetinrichting. 

   - e. De marktpartij is op de betreffende datum niet als actuele leverancier geregistreerd op het allocatiepunt. 

   - f. De datum in het verzoek ligt in de toekomst, of ligt voor of op de datum waarop meterstanden vastgesteld zijn of moeten worden. 

   - g. Het maximaal aantal verzoeken is overschreden. 

3. De leverancier ontvangt en verwerkt de afwijzing. 

4. De systeembeheerder stelt de meterstanden en volumes vast en communiceert deze naar de leverancier. 

## 4.41.3 Termijnen KA

- a. Indien de systeembeheerder het verzoek afwijst, wordt het afwijsbericht uiterlijk één werkdag na het verzoek verstuurd. 

## 4.41.4 Gegevensuitwisseling

Het verzoek van de opvragende leverancier naar de systeembeheerder ten behoeve van vastgestelde meterstanden bevat minimaal de volgende gegevens. 

### Verzoek vaststellen meterstand van opvragende leverancier naar systeembeheerder

|**Gegeven**|**Toelichting**|
|---|---|
|Leverancier|Unieke identificatie van de leverancier|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Datum meterstand(en)||
|Referentie|Referentie van de opvragende marktpartij|

**Afwijzing vanuit systeembeheerder naar opvragende leverancier** 

|**Gegeven**|**Toelichting**|
|---|---|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Afwijsreden|Indicatie van de reden waarom de melding is afgewezen:<br>• Onvolledige melding of syntactische fout.<br>• Het allocatiepunt is niet bekend in het aansluitingenregister van de systeembeheerder.<br>• Het betreft geen allocatiepunt op een kleine aansluiting.<br>• Het allocatiepunt is niet voorzien van een op afstand uitleesbare meetinrichting.<br>• De opvragende leverancier is op de betreffende datum niet als actuele leverancier<br>geregistreerd op het allocatiepunt.<br>• De gewenste datum voldoet niet aan de criteria.<br>• Het maximaal aantal verzoeken is bereikt.|
|Referentie|De door de opvragende leverancier in het verzoek meegegeven referentie.|
|Transactiedossiernummer|Het bij de afhandeling van de transactie nieuw toegekende unieke nummer|
