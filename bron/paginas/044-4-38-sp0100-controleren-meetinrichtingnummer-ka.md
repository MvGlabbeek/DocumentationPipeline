# 4.38 SP0100 Controleren meetinrichtingnummer KA


## 4.38.1 Procesafspraken

- a. Een systeembeheerder, leverancier en overige dienstenaanbieder kunnen een aanvraag voor het controleren van het meetinrichtingnummer KA doen. 

   - Een leverancier kan, ook indien deze niet in het aansluitingenregister geregistreerd staat op een aansluiting, een meetinrichtingnummer controle laten uitvoeren door de systeembeheerder om te laten controleren of het meetinrichtingnummer hoort bij de actueel geregistreerde meetinrichting op een allocatiepunt op een kleine aansluiting. 

   - Een overige dienstenaanbieder kan, ook zonder klantmandaat, een meetinrichtingnummer controle laten uitvoeren door de systeembeheerder om te laten controleren of het meetinrichtingnummer hoort bij de actueel geregistreerde meetinrichting op een allocatiepunt op een kleine aansluiting. 

## 4.38.2 Procesbeschrijving

Bijlage B1166: Subprocesplaat SP0100 KA

1. De opvragende marktpartij vraagt de controle van het meetinrichtingnummer aan. 

2. De systeembeheerder beoordeelt de opvraag op de volgende punten: 

   - a. Is de aanvraag compleet en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de opvragende marktpartij bekend als systeembeheerder, als leverancier in het Leveranciersregister of als overige diensten aanbieder? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder het verzoek af, en verstuurt een afwijzing naar de opvragende marktpartij. De afwijsredenen die de systeembeheerder kan gebruiken zijn: 

- a. Onvolledige opvraag of syntactische fout; 

b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

c. De opvragende marktpartij is onbekend als systeembeheerder, leverancier of overige diensten aanbieder. 

De opvragende marktpartij verwerkt de afwijzing. 

4. Indien alle controles een positief resultaat opleveren, voert de systeembeheerder de controle van het meetinrichtingnummer uit en verstuurt het resultaat naar de opvragende marktpartij. 

5. De opvragende marktpartij ontvangt en verwerkt het resultaat. 

## 4.38.3 Termijnen

a. De controle van het meetinrichtingnummer wordt via een synchroon-kanaal aangevraagd door de aanvragende partij. 

## 4.38.4 Gegevensuitwisseling

### Aanvraag

|**Gegeven**|**Toelichting**|
|---|---|
|Identificatie aanvragende partij|Identificatie van de leverancier, de overige dienstenaanbieder of de systeembeheerder|
|Identificatie systeembeheerder van het<br>allocatiepunt|Identificatie van de systeembeheerder van het allocatiepunt|
|Identificatie van het allocatiepunt|Identificatie van het allocatiepunt|
|Identificatie meetinrichting|De laatste 6 cijfers van het nummer van de meetinrichting|

### Antwoord

|**Gegeven**|**Toelichting**|
|---|---|
|Identificatie aanvragende partij|Identificatie aanvragende partij|
|Identificatie systeembeheerder van het<br>allocatiepunt|Identificatie van de systeembeheerder van het allocatiepunt|
|Identificatie van het allocatiepunt|Identificatie van het allocatiepunt|
|Resultaat|Het resultaat van de controle van hetmeetinrichtingnummer:<br>- meetinrichtingnummer hoort bij de actueel geregistreerde meetinrichting op de het<br>allocatiepunt;<br>- meetinrichtingnummer hoort niet bij de actueel geregistreerde meetinrichting op het<br>allocatiepunt.|

### Afwijzing

|**Gegeven**|**Toelichting**|
|---|---|
|Identificatie aanvragende partij|Identificatie aanvragende partij|
|Identificatie systeembeheerder van het<br>allocatiepunt|Identificatie van de systeembeheerder van het allocatiepunt|
|Identificatie van het allocatiepunt|Identificatie van het allocatiepunt|
|Afwijsreden|Identificatie van de reden waarom de aanvraag is afgewezen:<br>- onvolledige aanvraag of syntactische fout;<br>- het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder;<br>- de aanvragende marktpartij is onbekend als leverancier, overige dienstenaanbieder of<br>systeembeheerder.|
