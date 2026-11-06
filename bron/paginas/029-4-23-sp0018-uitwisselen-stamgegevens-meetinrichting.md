# 4.23 SP0018 Uitwisselen stamgegevens meetinrichting


## 4.23.1 Procesafspraken GA

- a. Zowel marktpartijen die beschikken over een machtiging van de aangeslotene als de systeembeheerder kunnen stamgegevens van de meetinrichting opvragen bij de meetverantwoordelijke partij. 

- b. In het subproces Uitwisselen stamgegevens meetinrichting worden zij de opvragende marktpartij genoemd. 

- c. De opvragende marktpartij (uitgezonderd de systeembeheerder) dient de machtiging op verzoek te kunnen overleggen indien dit niet reeds de actuele marktpartij op de aansluiting is. 

## 4.23.2 Procesbeschrijvingen GA

### Melden en beoordelen opvraag stamgegevens meetinrichting

Bijlage B1141: Subprocesplaat SP0018 GA – Melden en beoordelen opvraag stamgegevens meetinrichting

1. De opvragende marktpartij verstuurt de ‘melding opleveren stamgegevens meetinrichting’ naar de meetverantwoordelijke partij. 

2. De meetverantwoordelijke partij beoordeelt de opvraag op de volgende punten: 

   - a. Is de ‘melding opleveren stamgegevens meetinrichting’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het register van de betreffende meetverantwoordelijke partij? 

   - c. Is de opvragende marktpartij als onderneming bekend bij de meetverantwoordelijke partij en is het vanuit de toezichthouder toegestaan om aanvragen van deze partij in behandeling te nemen? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de meetverantwoordelijke partij de ‘melding opleveren stamgegevens meetinrichting’ af, en verstuurt de meetverantwoordelijke partij een afwijsbericht van de ‘melding opleveren stamgegevens meetinrichting’ naar de opvragende. De afwijsredenen die de meetverantwoordelijke partij kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het register van de meetverantwoordelijke partij. 

   - c. De aanvragende marktpartij is niet als onderneming bekend bij de meetverantwoordelijke partij of het is vanuit de toezichthouder niet toegestaan om aanvragen van deze marktpartij in behandeling te nemen. 

4. De opvragende marktpartij verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de meetverantwoordelijke partij de ‘melding opleveren stamgegevens meetinrichting’ van de opvragende marktpartij en verstuurt de meetverantwoordelijke partij de stamgegevens van de meetinrichting. 

6. De opvragende marktpartij verwerkt de stamgegevens van de meetinrichting. 

### Opleveren stamgegevens meetinrichting

Bijlage B1142: Subprocesplaat SP0018 GA – Opleveren stamgegevens meetinrichting

1. De meetverantwoordelijke partij verzamelt de stamgegevens van de meetinrichting. 

2. De meetverantwoordelijke partij verstuurt de ‘stamgegevens meetinrichting’ aan de opvragende marktpartij. 

3. De opvragende marktpartij ontvangt en beoordeelt de stamgegevens meetinrichting. 

4. Indien de opvragende marktpartij, conform de specificaties, niet geldige domeinwaardes aantreft in de ontvangen stamgegevens, verstuurt hij een afwijzing. 

5. De meetverantwoordelijke partij levert in dat geval een nieuw responsebericht op. 

## 4.23.3 Termijnen GA

Voor dit proces zijn geen termijnen vastgesteld. 

## 4.23.4 Gegevensuitwisseling GA

### Opvraag

|**Melding Opvraag stamgegevens mee**|**tinricht**|**ing**|||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Referentie|O|O|Ja|Ja|1||
|EAN-code<br>meetverantwoordelijke|V|V|Ja|Ja|1||
|partij|||||||
|EAN-code opvragende marktpartij|V|V|Ja|Ja|1||

### Afwijzing response

Indien in het responsebericht een domeinwaarde wordt gehanteerd die niet voorkomt in de specificatie (kolom opmerking) kan het onderstaande afkeurbericht worden verzonden. De meetverantwoordelijke partij levert in dat geval een nieuw bericht op. 

|**Afwijzing**|||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Afwijsreden|V|V|Ja|Ja|1|Indicatie van de reden waarom het responsebericht wordt<br>afgewezen:<br>•<br>Ongeldige domeinwaarde|
|Toelichting afwijsreden|O|O|Ja|Ja|1||

### Afwijzing

|**Afwijzing opvraag stamgegevens me**|**etinrichti**|**ng**|||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens technische redenen<br>is afgewezen|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag|
|EAN-code opvragende marktpartij|V|V|Ja|Ja|1||
|EAN-code meetverantwoordelijke<br>partij|V|V|Ja|Ja|1||
|Afwijsreden|V|V|Ja|Ja|n|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het allocatiepunt is onbekend in het register van de<br>meetverantwoordelijke partij.<br>•<br>De aanvragende partij is niet als onderneming bekend bij<br>de meetverantwoordelijke partij of het is vanuit de<br>toezichthouder niet toegestaan om aanvragen van deze<br>partijin behandelingte nemen.|
|Toelichting afwijsreden|O|O|Ja|Ja|n||

### Response

|**Stamgegevens meetinrichting**|||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|A|A|Ja|Ja|1|Verplicht bij antwoord op aanvraag|
|Referentie|A|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag.|
|EAN-code meetverantwoordelijke<br>partij|V|V|Ja|Ja|1||
|EAN-code opvragende marktpartij|V|V|Ja|Ja|1||
|Ingangsdatum|V|V|Ja|Ja|1||
|Productsoort|V|V|Ja|Ja|1|Elektriciteit of gas|
|Redencode<sup>8</sup>|V|V|Ja|Ja|1|Verwijdering, plaatsing, wijziging van de meetinrichting of op<br>verzoek|
|EAN-code allocatiepunt|V|V|Ja|Ja|1||
|Meetveld / Meetstraat|V|A|Ja|Ja|n|Meetveld bij elektriciteit, Meetstraat bij gas<br>n >= 1|
|Identificatie van het meetveld /<br>de meetstraat|V|A|Ja|Ja|1||
|Meetinrichtingnummer|V|V|Ja|Ja|1||
|Capaciteit|A|A|Ja|Nee|n||
|_Per register_|A|A|||_n_|_n registers per meetinrichting_|
|Register ID|A|A|Ja|Ja|n||
|Aantal Telwielen|A|A|Ja|Ja|1||
|Registertype|A|A|Nee|Ja|1|Normaal / laag|
|Meetrichting|A|A|Nee|Ja|1|Indicatie van de richting waarin de meting wordt uitgevoerd:<br>•<br>Levering<br>•<br>Teruglevering|

> 8 Als de redencode voor het bericht ‘Verwijdering van de meetinrichting’ is, worden de gegevens van de verwijderde meetinrichting(en) niet nogmaals in het bericht opgenomen. 

|**Stamgegevens meetinrichting**|||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Indicatie herleiding|A|A|Ja|Nee|n|Niet genormaliseerd|
|||||||Genormaliseerd 0°C en 1013,25 mbar|
|Vermenigvuldigingsfactor|V|V|Ja|Ja|1||
|Meetsoort|O|O|Nee|Ja|1||
