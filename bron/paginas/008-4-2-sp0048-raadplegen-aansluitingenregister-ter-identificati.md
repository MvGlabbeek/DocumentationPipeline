# 4.2 SP0048 Raadplegen aansluitingenregister ter identificatie van het allocatiepunt


## 4.2.1 Procesafspraken KA en GA

Voor het identificeren van een allocatiepunt heeft de leverancier de beschikking over een zoekmogelijkheid op het aansluitingenregister. Hieronder worden de procesafspraken en procesbeschrijving voor KA en GA beschreven. 

Het aantal zoekmogelijkheden is beperkt zoals beschreven in de paragraaf Gegevensuitwisseling. De zoekparameters zijn zo gekozen dat wordt voorkomen dat onnodig gegevens van meerdere allocatiepunten opgeleverd worden. 

## 4.2.2 Procesbeschrijving KA en GA

Bijlage B1086: Subprocesplaat SP0048 KA-GA

1. De leverancier vraagt de allocatiepuntgegevens ten behoeve van het identificeren van het allocatiepunt op als onderdeel van het proces Inhuizing of proces Leverancierswitch. 

2. De systeembeheerder ontvangt de opvraag ‘allocatiepuntgegevens ten behoeve van het identificeren van het allocatiepunt’ van de leverancier. De systeembeheerder beoordeelt de opvraag op de volgende punten: 

   - a. Is de opvraag volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de opvragende leverancier bekend in het leveranciersregister? 

   - d. In geval van een grote aansluiting: Is het allocatiepunt dat de opvragende leverancier wil raadplegen een allocatiepunt op een grote aansluiting? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de opvraag ‘allocatiepuntgegevens ten behoeve van het identificeren van het allocatiepunt’ af, en verstuurt de systeembeheerder een afwijsbericht naar de opvragende leverancier direct na ontvangst van de opvraag ‘allocatiepuntgegevens ten behoeve van het identificeren van het allocatiepunt’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige opvraag of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De opvragende leverancier is onbekend in het leveranciersregister. 

   - d. Het allocatiepunt is geen allocatiepunt op een grote aansluiting. 

4. De opvragende leverancier ontvangt en verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de opvraag ‘allocatiepuntgegevens ten behoeve van het identificeren van het allocatiepunt’ van de opvragende leverancier en verstuurt de systeembeheerder de allocatiepuntgegevens direct naar de opvragende leverancier. 

6. De opvragende leverancier ontvangt en verwerkt de gegevens van het allocatiepunt als onderdeel van het proces Inhuizing of proces Leverancierswitch. 

## 4.2.3 Termijnen KA en GA

De opvraag ‘allocatiepuntgegevens ten behoeve van het identificeren van het allocatiepunt’ wordt direct beantwoord. 

## 4.2.4 Gegevensuitwisseling

### Opvraag

|**Opvraag allocatiepuntgegeven**|**s ten behoeve**|**van ide**|**ntificere**|**n van he**|**t allocat**|**iepunt**||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Productsoort|O|O|O|Ja|Ja|1|Elektriciteit of gas|
|Zoekcriteria|V|V|V|Ja|Ja|1|Zoekopdracht mogelijk middels:<br>•<br>Zoekparameters voor identificatie van het allocatiepunt|

### Zoekparameters voor identificatie allocatiepunt

|**Attribuut**|**Gebruik**|**1/n**|**Opmerking**|
|---|---|---|---|
|_Zoekcriteria_||||
|EAN-code allocatiepunt|Afhankelijk|1|Niet in combinatie met andere attributen (geen wildcards).|
|Postcode|Optioneel|1|Alleen in combinatie met huisnummer (geen wildcards; als huisnummer wordt<br>leeggelaten krijg je alleen allocatiepunten waargeen huisnummer vermeld staat).|
|Huisnummer<sup>3</sup>|Afhankelijk|1|Alleen in combinatie met straatnaam en woonplaats, of met postcode (geen<br>wildcards).|
|Huisnummertoevoeging|Afhankelijk|1|Alleen in combinatie met huisnummer, straatnaam en woonplaats, of huisnummer<br>enpostcode(geen wildcards).|
|Straatnaam|Afhankelijk|1|Alleen in combinatie met woonplaats en huisnummer (geen wildcards; als<br>huisnummer wordt leeggelaten krijg je alleen allocatiepunten waar geen<br>huisnummer vermeld staat)|

> 3 Bij het zoeken op adres (straatnaam en woonplaats of postcode) inclusief huisnummer, wordt als zoekresultaat alle allocatiepunten op dat adres en alle allocatiepunten op dat adres met een huisnummertoevoeging getoond. 

|**Attribuut**|**Gebruik**|**1/n**|**Opmerking**|
|---|---|---|---|
|Woonplaats|Afhankelijk|1|Alleen in combinatie met straatnaam en huisnummer (geen wildcards; als<br>huisnummer wordt leeggelaten krijg je alleen allocatiepunten waar geen<br>huisnummer vermeld staat)|
|Landcode|Afhankelijk|1|Alleen in combinatie met woonplaats, straatnaam en huisnummer (geen wildcards;<br>als huisnummer wordt leeggelaten krijg je alleen allocatiepunten waar geen<br>huisnummer vermeld staat)|
|BAG nummeridentificatie|Afhankelijk|1|Niet in combinatie met andere zoekcriteria (geen wildcards).|
|Locatieomschrijving|Afhankelijk|1|Alleen in combinatie met straatnaam en woonplaats (geen wildcards).|
|_Filtercriteria_||||
|Productsoort|Optioneel|1|Deze criteria kunnen alleen worden gebruikt in combinatie met minimaal één van|
|Verbruikssegment|Optioneel|1|bovenstaande zoekcriteria.|

### Response

|**Response opvraag aansluitingenr**|**egister ten**|**behoeve**|**van ide**|**ntificere**|**n van h**|**et allocat**|**iepunt**|
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Straatnaam|O|O|O|Ja|Ja|1||
|Huisnummer|O|O|O|Ja|Ja|1||
|Huisnummertoevoeging|O|O|O|Ja|Ja|1||
|Woonplaats|V|A|A|Ja|Ja|1|Een allocatiepunt in Nederland heeft verplicht een<br>woonplaats|
|Postcode|O|O|O|Ja|Ja|1||
|Landcode|V|V|V|Ja|Ja|1||
|Locatieomschrijving|O|O|O|Ja|Ja|1|Via locatieomschrijving wordt ook gecommuniceerd of het<br>eengelijkspanningsaansluitingbetreft|
|BAG nummeridentificatie|O|O|O|Ja|Ja|1||
|Productsoort|V|V|V|Ja|Ja|1|Elektriciteit of gas|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|Systeemgebied|A|A|A|Ja|Ja|1||
|Allocatiemethode|Nee|V|V|Ja|Ja|1|Aanduiding of het allocatiepunt al dan niet geprofileerd is:<br>•<br>Geprofileerd<br>•<br>Telemetrie<br>•<br>Slimmemeterallocatie|
|Wijze van bemeting|Nee|V|V|Ja|Ja|1|De verschillende manieren van bemeten:<br>•<br>Onbemeten<br>•<br>Jaarlijks<br>•<br>Maandelijks<br>•<br>Telemetrie<br>•<br>Niet continue<br>•<br>Anders bemeten<br>•<br>Onbekend|
|Afrekenmaand|nvt|A|A|Ja|Ja|1|Allocatiepunten die jaarlijks worden afgerekend moeten<br>worden ingevuldoverige niet.|
|Contractcapaciteit|nvt|A|nvt|Ja|Ja|1|,  <br>Vermogen voor de aansluiting. Voor een additioneel<br>allocatiepunt zal hier de waarde 0 worden vermeld.|
|Profielcategorie|Nee|A|A|Ja|Ja|1|Een in bedrijf zijnde allocatiepunt heeft verplicht een<br>profiel/afnamecategorie,<br>tenzij<br>het<br>een<br>telemetrisch<br>bemeten allocatiepunt op een grote aansluiting elektriciteit<br>betreft:<br>•<br>Elektriciteit: E1A, E1B, E1C, E2A, E2B, E3, E4A, OPC<br>•<br>Gas: G1A,G2A,G2C,GGV,GXX,GIS,GIN|
|Leveringsrichting|Nee|A|A|Ja|Ja|1|Indicatie van de leveringsrichting op het allocatiepunt:<br>•<br>Levering<br>•<br>Teruglevering<br>•<br>Combi|
|Fysieke capaciteit|Nee|O|O|Ja|Ja|1|<br>Een in bedrijf zijnde allocatiepunt op een grote aansluiting<br>heeft verplicht een fysieke capaciteit.<br>Elektriciteit:<br>•<br>Voor allocatiepunten op grote aansluitingen kleiner of<br>gelijk 3x80A; 1x6A, 1x10A, 1x25A, 1x35A, 1x50A, 1x63A,<br>1x80A, 3x25A, 3x35A, 3x50A, 3x63A, 3x80A, OBK<br>•<br>Voor allocatiepunten op grote aansluitingen groter dan<br>3x80A; in kVA (leeg indien onbekend)<br>Gas: in m<sup>3</sup>(n)/uur(leegindien onbekend)|

|**Response opvraag aansluitingenreg**|**ister ten**|**behoeve**|**van ide**|**ntificere**|**n van h**|**et allocat**|**iepunt**|
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Verbruikssegment|V|V|V|Ja|Ja|1|Een specificatie van het segment van de aansluiting waar het<br>allocatiepunt zich opbevindt(GA,KA of A1)|
|EAN-code primair allocatiepunt|A|A|A|Nee|A|1|Indien het een additioneel allocatiepunt betreft dan verplicht<br>te vullen met de EAN-code van het bijbehorende primaire<br>allocatiepunt.<br>Dient leeg te worden gelaten indien het een primair<br>allocatiepunt betreft.|
|Laatste 4 cijfers<br>meetinrichtingnummer|A|nvt|nvt|Ja|Ja|1|Verplicht bij een allocatiepunt op een kleine aansluiting met<br>de fysieke status in bedrijf met wijze van bemeting ongelijk<br>aan:_onbemeten, anders bemeten_of_onbekend_|

### Afwijzing

|**Afwijzing opvraag aansluitingen**|**register ten**|**behoeve**|**van ide**|**ntificeren**|**van het**|**allocatie**|**punt**|
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n **|**Opmerking**|
|Afwijsreden|V|V|Ja|Ja|Ja|1|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledige opvraag of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister<br>van<br>de<br>betreffende<br>systeembeheerder.<br>•<br>De opvragende marktpartij is onbekend in het<br>leveranciersregister.<br>•<br>Het allocatiepunt is geen allocatiepunt op een<br>grote aansluiting.|
|Toelichtingafwijsreden|O|O|Ja|Ja|Ja|1||
