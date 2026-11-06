# 4.19 SP0016 Uitwisselen historische meetgegevens


## 4.19.1 Procesafspraken GA

- a. Marktpartijen die beschikken over een machtiging van de aangeslotene kunnen historische meetgegevens opvragen bij de systeembeheerder. Voor allocatiepunten kunnen de leverancier of de balanceringsverantwoordelijke historische meetgegevens opvragen. In het subproces ‘uitwisselen historische meetgegevens’ worden zij de opvragende marktpartij genoemd. De opvragende marktpartij dient de machtiging op verzoek te kunnen overleggen indien dit niet reeds de actieve marktpartij is op dat allocatiepunt. 

- b. Bij opvraag historische meetgegevens wordt de historische meetgegevens alleen verstuurd naar de marktpartij die de gegevens opvraagt. 

- c. Het subproces ‘Uitwisselen historische meetgegevens’ is van toepassing op het opleveren van historische meterstanden en volumes. Onder historische meterstanden en volumes worden verstaan de meterstanden en volumes die de systeembeheerder beschikbaar heeft als gevolg van een periodieke opname, inhuizing, uithuizing, leverancierswitch, einde levering of mutatie van de meetinrichting. 

- d. De opvragende marktpartij draagt zorg dat hij van de klant minimaal die klantgegevens verkrijgt die nodig zijn voor het achterhalen van de EAN-code van het allocatiepunt. 

- e. De output van het subproces indienen en beoordelen ‘melding opleveren historische meetgegevens op verzoek’ is voor de systeembeheerder de opdracht voor het opleveren van historische meetgegevens. 

- f. Het opvragen van uur- of kwartierwaarden is buiten scope van dit subproces. 

- g. Het opvragen van historische meetgegevens door de klant is buiten scope van dit subproces. 

## 4.19.2 Procesbeschrijving GA

Bijlage B1132: Subprocesplaat SP0016 GA

1. De opvragende marktpartij verstuurt de ‘aanvraag historische meetgegevens’ naar de systeembeheerder. 

2. De systeembeheerder beoordeelt het verzoek op de volgende punten: 

   - a. Is het de ‘aanvraag historische meetgegevens’’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de opvragende marktpartij als onderneming bekend bij de systeembeheerder en is het vanuit de toezichthouder toegestaan om aanvragen van deze partij in behandeling te nemen? 

   - d. Is voor in de opvraag aangegeven periode historische meetgegevens voor het desbetreffende allocatiepunt beschikbaar? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘aanvraag historische meetgegevens’ af, en verstuurt de systeembeheerder een afwijsbericht naar de opvragende marktpartij binnen vijf werkdagen na ontvangst van de ‘aanvraag historische meetgegevens’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledig melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De aanvragende partij is niet als onderneming bekend bij de systeembeheerder of het is vanuit de toezichthouder niet toegestaan om aanvragen van deze marktpartij in behandeling te nemen. 

   - d. Er zijn geen historische meetgegevens beschikbaar. 

4. De opvragende marktpartij verwerkt de afwijzing. 

5. Indien de systeembeheerder het ‘verzoek historische meetgegevens’ van de opvragende marktpartij kan verwerken, dan plant de systeembeheerder het opleveren van de gevraagde meetgegevens in. 

6. De systeembeheerder distribueert binnen vijf werkdagen na ontvangst van het ‘verzoek historische meetgegevens’ de gevraagde meetgegevens aan de opvragende marktpartij. 

7. De opvragende marktpartij ontvangt en verwerkt de historische meetgegevens. 

## 4.19.3 Termijnen GA

De systeembeheerder beoordeelt het ‘verzoek historische meetgegevens’ binnen vijf werkdagen. 

## 4.19.4 Gegevensuitwisseling

### Opvraag

|**Opvraag historische meetgegevens**|||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Proces ID|V|V|Ja|Ja|1|Opvraag historische meetgegevens|
|Referentie|O|O|Ja|Ja|1||
|EAN-code opvragende marktpartij|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|Begindatum|V|V|Ja|Ja|1|Startdatum van de periode waarvan historische meetgegevens<br>wordt opgevraagd.|
|Einddatum|V|V|Ja|Ja|1|Einddatum van de periode waarvan historische meetgegevens<br>wordt opgevraagd.|

### Afwijzing

|**Afwijzing opvraag historische meetg**|**egevens**||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens technische redenen is<br>afgewezen|
|Proces ID|V|V|Ja|Ja|1|Opvraag historische meetgegevens|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag|
|EAN-code opvragende marktpartij|V|V|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|Afwijsreden|V|V|Ja|Ja|n|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledig melding of syntactische fout.<br>•<br>Het allocatiepunt is onbekend in het aansluitingenregister van<br>de systeembeheerder.<br>•<br>De aanvragende partij is niet als onderneming bekend bij de<br>systeembeheerder of het is vanuit de toezichthouder niet<br>toegestaan om aanvragen van deze partij in behandeling te<br>nemen.<br>•<br>Er zijngeen historische meetgegevens beschikbaar.|
|Toelichting afwijsreden|O|O|Ja|Ja|n||

### Response

|**Meterstand en volume**|||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|Ja|Ja|1|Alleen verplicht indien respons op opvraag|
|Proces ID|V|V|Ja|Ja|1|Opvraag historische meetgegevens|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag|
|EAN-code systeembeheerder|V|V|Ja|Ja|1||
|EAN-code opvragende marktpartij|V|V|Ja|Ja|1||
|Volumeperiode|V|V|Ja|Ja|1|Volumeperiode op allocatiepunt|
|**_Volume_**|||||**_Per EA_**|**_N-code_**|
|Volumeperiode|V|V|Ja|Ja|1|Voor periodemarkeringen worden ‘tot datums’ gebruikt, zo<br>wordt de maand maart aangeduid van 01-03 tot 01-04.|
|Registertype|V|V|Ja|Ja|n||
|Hoeveelheid|V|V|Ja|Ja|n|Afhankelijk van mogelijke levering, teruglevering, normaal, laag.|
|Gecorrigeerde hoeveelheid|V|V|Ja|Nee|1||
|**_Meterstand_**|||||**_2 per v_**|**_erbruik_**|
|Meterstand|O|V|Ja|Ja|1|Verplicht voor A1|
|Meterstanddatum|O|V|Ja|Ja|1|Verplicht voor A1|
|Herkomstindicatie|O|V|Ja|Ja|1|Verplicht voor A1|
