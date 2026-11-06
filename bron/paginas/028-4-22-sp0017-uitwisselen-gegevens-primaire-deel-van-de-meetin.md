# 4.22 SP0017 Uitwisselen gegevens primaire deel van de meetinrichting


## 4.22.1 Procesafspraken GA

- a. Het subproces ‘Uitwisselen gegevens primaire deel van de meetinrichting’ is bedoeld voor de meetverantwoordelijke partij in het kader van een meetverantwoordelijke partij switch, die als zodanig beschikt over een machtiging van de aangeslotene. Het proces kan ook gebruikt worden door de actuele meetverantwoordelijke partij ter controle of aanvulling van de eigen gegevens. 

- b. Het subproces ‘Uitwisselen gegevens primaire deel van de meetinrichting’ is bedoeld om de meetverantwoordelijke partij op de hoogte te stellen omtrent fysieke plaatsing, wijziging en verwijdering van het primaire deel van de meetinrichting en in geval van administratieve wijzigingen omtrent de kenmerken. 

- c. Het proces geldt voor het primaire deel van de meetinrichting voor allocatiepunten op een grote aansluiting elektriciteit en grote aansluiting gas. 

## 4.22.2 Procesbeschrijvingen GA

### Opleveren gegevens primaire deel van de meetinrichting

Bijlage B1139: Subprocesplaat SP0017 GA – Opleveren gegevens primaire deel van de meetinrichting

1. De systeembeheerder verwerkt de nieuwe of gewijzigde gegevens van het primaire deel van de meetinrichting uiterlijk de werkdag na de fysieke werkzaamheden. 

2. De systeembeheerder verstuurt de gegevens van het primaire deel van de meetinrichting uiterlijk de werkdag na de verwerking naar de meetverantwoordelijke partij, indien aanwezig. 

3. De meetverantwoordelijke partij (indien aanwezig) ontvangt en beoordeelt de gegevens van het primaire deel van de meetinrichting. 

4. Indien de meetverantwoordelijke partij, conform de specificaties, niet geldige domeinwaardes aantreft in de ontvangen gegevens van het primaire deel van de meetinrichting, verstuurt hij een afwijzing. 

5. De systeembeheerder levert in het geval hij een afwijzing ontvangt een nieuw responsebericht op. 

### Opvragen gegevens primaire deel van de meetinrichting

Bijlage B1140: Subprocesplaat SP0017 GA – Opvragen gegevens primaire deel van de meetinrichting

1. De meetverantwoordelijke partij verstuurt de ‘melding opvraag gegevens primaire deel van de meetinrichting’ naar de systeembeheerder. 

2. De systeembeheerder beoordeelt de ‘melding opvraag gegevens primaire deel van de meetinrichting’ op de volgende punten: 

   - a. Is de ‘melding opvraag gegevens primaire deel van de meetinrichting’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Heeft de opgeven meetverantwoordelijke partij een volledige erkenning volgens het MV-register? 

   - d. Heeft de opgegeven EAN-code betrekking op een additioneel allocatiepunt? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding opvraag gegevens primaire deel van de meetinrichting’ af, en verstuurt de systeembeheerder een afwijsbericht naar de meetverantwoordelijke partij uiterlijk de werkdag na ontvangst van de ‘melding opvraag gegevens primaire deel van de meetinrichting’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De opgegeven meetverantwoordelijke partij heeft geen volledige erkenning volgens het MV-register. 

   - d. De opgegeven EAN-code heeft betrekking op een additioneel allocatiepunt. 

4. De meetverantwoordelijke partij verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding opvraag gegevens primaire deel van de meetinrichting’, van de meetverantwoordelijke partij en verstuurt hij de ‘Gegevens primaire deel van de meetinrichting’ voor elektriciteit en voor gas het bericht ‘Technische gegevens van de gasaansluiting’ uiterlijk vijf werkdagen na ontvangst van de ‘melding opvraag gegevens primaire deel van de meetinrichting’. De gegevens betreffende elektriciteit worden verstuurd middels het berichtenverkeer. 

6. De meetverantwoordelijke partij ontvangt en verwerkt de gegevens van het primaire deel van de meetinrichting. 

## 4.22.3 Termijnen GA

- a. De systeembeheerder verwerkt mutaties in de gegevens van het primaire deel van de meetinrichting uiterlijk de volgende werkdag in zijn administratie. 

- b. De systeembeheerder verstuurt de gegevens primaire deel van de meetinrichting uiterlijk de werkdag na aanpassing in het aansluitingenregister naar de meetverantwoordelijke partij die in het aansluitingenregister staat geregistreerd. 

## 4.22.4 Gegevensuitwisseling

|**Opvraag gegevens primaire deel va**|**n de meet**|**inrichting**||||
|---|---|---|---|---|---|
|**Gegeven**|**GA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|O|Ja|Ja|1||
|EAN-code meetverantwoordelijke<br>partij|V|Ja|Ja|1|Opvragende marktpartij|
|EAN-code systeembeheerder|V|Ja|Ja|1||

|**Afwijzing opvraag primaire deel van**|**de meet**|**inrichting**||||
|---|---|---|---|---|---|
|**Gegeven**|**GA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Transactiedossiernummer|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens technische redenen is<br>afgewezen|
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag|
|EAN-code meetverantwoordelijke<br>partij|V|Ja|Ja|1|Opvragende marktpartij|
|Afwijsreden|V|Ja|Ja|n|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het allocatiepunt is onbekend in het aansluitingenregister van de<br>systeembeheerder.<br>•<br>De opgegeven meetverantwoordelijke partij heeft geen volledige<br>erkenning volgens het MV-register.<br>•<br>De opgegeven EAN-code heeft betrekking op een additioneel<br>allocatiepunt.|
|Toelichting afwijsreden|O|Ja|Ja|n||

### Response

#### Elektriciteit

|**Gegevens primaire deel van de mee**|**tinrichting elektriciteit**|||
|---|---|---|---|
|**Gegeven**|**GA**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|Transactiedossiernummer|A|1|Alleen verplicht indien response op een opvraag.|
|Referentie|A|1|Gevuld indien meegegeven in de opvraag|
|EAN-code meetverantwoordelijke<br>partij|V|1|Opvragende marktpartij indien het bericht het antwoord is op een opvraag.<br>Actuele meetverantwoordelijkepartijin de overigegevallen|
|EAN-code systeembeheerder|V|1||
|Productsoort|V|1|Elektriciteit|
|Weekmax|O|1|Alleen indien bedrijfstijd < 600 uur. ‘Ja’ of ‘Nee’|
|Zekeringswaarde|V|1||
|Reden verstrekking|V|1|Op verzoek / Update|
|Toegang vereist|V|1||
|Ingangsdatum-tijd|V|1||
|**_Meetveld_**||n|n is maximaal 5|
|Meetveld identificatie|V|1|één per meetveld|
|Verliesfactor|V|1|Opgeven als percentage|
|Situatie|V|1|Bestaand / te realiseren|
|**_Spanningstrafo_**||_1_|_Eén spanningstrafo (optioneel)_<br>_Onderliggendegegevens zijn verplicht indien een trafo aanwezig is._|
|Apparaatnummer|A|n|n is maximaal 3|
|U-primair|A|1||
|U-secundair|A|1||
|Nauwkeurigheidsklasse|A|1|Onbekend; 0,1; 0,2S; 0,2; 0,3; 0,5S; 0,5; 1,0; 2,0; 3; 5|
|Nominaal vermogen|A|1|Uitgedrukt in VA|
|Type schakeling|A|1|Onbekend / YY sec. geaard / Yyd /dzY|
|Soort smeltveiligheid|A|1|Onbekend / Diazed / mespatroon|
|Waarde smeltveiligheid|A|1|Uitgedrukt in Ampère|
|**_Stroomtrafo_**||_1_|_Eén trafo per meetveld (optioneel)_|
|Apparaatnummer|V|n|n is minimaal 2 en maximaal 6|
|I-primair|V|1||
|I-secundair|V|1||
|Nauwkeurigheidsklasse|V|1|Onbekend; 0,1; 0,2S; 0,2; 0,3; 0,5S; 0,5; 1,0; 2,0; 3; 5|
|Nominaal vermogen VA|V|1||
|Instr. Veiligheidsfactor|V|1||
|Type schakeling|V|1|Toegestane waarden: Onbekend / Drieleider / Vierleider|

#### Gas

|**Gegevens primaire deel van de meetinrichting**|**gas**|||
|---|---|---|---|
|**Gegeven**|**GA**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|1||
|Datum verzending|V||Datum waarop het bericht verzonden is DD:MM:YYYY|
|EAN-code meetverantwoordelijke partij|V|1|Opvragende marktpartij indien het bericht het antwoord is op een aanvraag.<br>Actuele meetverantwoordelijkepartijin de overigegevallen|
|EAN-code systeembeheerder|V|1||
|**_Meetstraat_**||n|N per meetstraat|
|Meetstraat|A|1|Indien er sprake is van meerdere meetstraten per allocatiepunt identificatie<br>meetstraat,éénper meetstraat|
|Situatie|V|1|Bestaand / te realiseren|
|Schroefdraadaansluiting|O|1|“1”, ”1,5” of ”2” (er is sprake van een schroefdraadaansluiting of een<br>flensaansluiting)|
|Flensaanduiding|O|1|DN40, DN50, DN80, DN100, DN150, DN200, DN250, DN300, DN400 (er is sprake<br>van een schroefdraadaansluitingof een flensaansluiting)|
|Drukklasse van de flenzen|A|1|PN6, PN10, PN12, PN16 (indien er sprake is van een flensaansluiting)|
|Inbouwmaat|O|1|Maat die tussen de flenzen beschikbaar is in mm|
|Geregelde meetdruk?|V|1|Bevindt de meter zich in de geregelde druk? j/n|
|Meetdruk|A|1|Indien de meter zich in de geregelde druk bevindt meetdruk in mBar, indien<br>ongeregeld nvt|
|Minimale of gegarandeerde netdruk|A|1|Indien meter voor de regelaar: druk waarop minimaal teruggevallen kan worden<br>in mBar|

|**Gegevens primaire deel van de meetinrichting gas**||||
|---|---|---|---|
|**Gegeven**|**GA**|**1/n**|**Opmerking**|
|Netdruk|V|1|Netdruk in mBar|

### Afwijzing response

Indien in het responsebericht een domeinwaarde wordt gehanteerd die niet voorkomt in de specificatie (kolom opmerking) kan het onderstaande afkeurbericht worden verzonden. De zendende partij levert in dat geval een nieuw responsebericht op. 

|**Afwijzing**|||||||
|---|---|---|---|---|---|---|
|**Gegeven**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Afwijsreden|V|V|Ja|Ja|1|Indicatie van de reden waarom het responsebericht wordt<br>afgewezen:|
|||||||•<br>Ongeldige domeinwaarde|
|Toelichting afwijsreden|O|O|Ja|Ja|1||
