# 4.3 SP0052 Opvragen gegevens ten behoeve van pre-mutatiefase


## 4.3.1 Procesafspraken KA

Na het sluiten van de leveringsovereenkomst kan de leverancier extra informatie van het allocatiepunt opvragen ten behoeve van het voorbereiden van de leverancierswitch of inhuizing. Hiervoor heeft de leverancier een raadpleegmogelijkheid op het aansluitingenregister. Deze mogelijkheid voor het raadplegen van het aansluitingenregister ter voorbereiding op de leverancierswitch of inhuizing wordt hieronder beschreven. 

## 4.3.2 Procesbeschrijving KA

Bijlage B1087: Subprocesplaat SP0052 KA

1. De leverancier vraagt de allocatiepuntgegevens ten behoeve van pre-mutatiefase op van het allocatiepunt. 

2. De systeembeheerder ontvangt de opvraag ‘allocatiepuntgegevens ten behoeve van premutatiefase’ van de leverancier. De systeembeheerder beoordeelt de opvraag op de volgende punten: 

   - a. Is de opvraag volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de leverancier bekend in het leveranciersregister? 

   - d. Heeft de leverancier een contract voor dit allocatiepunt in het Contracteinderegister geregistreerd? 

   - e. Is het een allocatiepunt op een kleine aansluiting? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de opvraag ‘allocatiepuntgegevens ten behoeve van pre-mutatiefase’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier direct na ontvangst van de opvraag ‘allocatiepuntgegevens ten behoeve van pre-mutatiefase’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige opvraag of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de distributiesysteembeheerder. 

   - c. De leverancier komt niet voor in het leveranciersregister. 

   - d. Geen contract van de leverancier voor het betreffende allocatiepunt geregistreerd in het Contracteinderegister. 

   - e. Het allocatiepunt betreft geen allocatiepunt op een kleine aansluiting. 

4. De leverancier ontvangt en verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de opvraag ‘allocatiepuntgegevens ten behoeve van pre-mutatiefase’ van de leverancier en verstuurt de systeembeheerder de allocatiepuntgegevens direct naar de leverancier. 

6. De leverancier ontvangt en verwerkt de gegevens van het allocatiepunt ten behoeve van het proces Inhuizing of proces Leverancierswitch. 

## 4.3.3 Termijnen KA

De opvraag ‘allocatiepuntgegevens ten behoeve van pre-mutatiefase’ wordt direct beantwoord. 

## 4.3.4 Gegevensuitwisseling

### Opvraag

|**Opvraag allocatiepuntgegevens**|**ten behoev**|**e van pre**|**-mutatie**|**fase**||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GV**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|nvt|nvt|Ja|Ja|1||
|Referentie|O|nvt|nvt|Ja|Ja|1||
|EAN-code leverancier|V|nvt|nvt|Ja|Ja|1||

### Response

|**Response allocatiepuntgegevens t**|**en behoev**|**e van de**|**pre-mu**|**tatiefase**||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GV**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|nvt|nvt|Ja|Ja|1||
|Transactiedossiernummer(s)|V|nvt|nvt|Ja|Ja|n|Verplicht|
|Proces ID|V|nvt|nvt|Ja|Ja|n|‘Beantwoording<br>van<br>opvraag’<br>bij<br>opvraag<br>allocatiepuntgegevens,andersgevuld vanuit deprocessen|
|Referentie|A|nvt|nvt|Ja|Ja|1|Indien ingevuld in de opvraag, anders leeg.|
|Begindatum|V|nvt|nvt|Ja|Ja|1|Datum van opgeleverde gegevens|
|EAN-code systeembeheerder|V|nvt|nvt|Ja|Ja|1||
|Productsoort|V|nvt|nvt|Ja|Ja|1|Elektriciteit of gas|
|Systeemgebied|A|nvt|nvt|Ja|Ja|1||
|Wijze van bemeting|V|nvt|nvt|Ja|Ja|1|De verschillende manieren van bemeten:<br>•<br>Onbemeten<br>•<br>Jaarlijks<br>•<br>Anders bemeten<br>•<br>Onbekend|
|Profielcategorie|A|nvt|nvt|Ja|Ja|1|Een in bedrijf zijnde allocatiepunt heeft verplicht een<br>profiel/afnamecategorie, tenzij het een telemetrisch<br>bemeten allocatiepunt op een grote aansluiting betreft:<br>•<br>Elektriciteit: E1A, E1B, E1C, E2A, E2B E4A, OPC<br>•<br>Gas: G1A,G2A|

|**Response allocatiepuntgegevens ten**<br>**Gegeven**|**behoe**<br>**KV**|**ve van de**<br>**GV**|**pre-mu**<br>**A1**|**tatiefase**<br>**Gas**|<br>**EL**|**1/n**|**Opmerking**|
|---|---|---|---|---|---|---|---|
|<br>Capaciteitstariefcode<br>Fysieke status|<br>A<br>V|<br>nvt<br>nvt|<br>nvt<br>nvt|<br>Ja<br>Ja|<br>Ja<br>Ja|<br>1<br>1|<br>Indicatie van het door de systeembeheerder aan dit<br>primaire<br>allocatiepunt<br>op<br>een<br>kleine<br>aansluiting<br>toegekende capaciteitstarief voor de systeemkosten.<br>Voor een additioneel allocatiepunt zal hier een<br>capaciteitstariefcode worden vermeld die aangeeft dat er<br>een 0-tarief toegepast moet worden.<br>Een indicatie van de fysieke status van een allocatiepunt:<br>•<br>In aanleg<br>•<br>In bedrijf<br>•<br>Uit bedrijf|
|Leveringsrichting|A|nvt|nvt|Ja|Ja|1|<br>Indicatie van de leveringsrichting op het allocatiepunt:<br>•<br>Levering<br>•<br>Teruglevering<br>•<br>Combi|
|Verbruikssegment|V|nvt|nvt|Ja|Ja|1|<br>Specificatie van het segment waartoe het allocatiepunt<br>|
|SJI laag tarief|O|nvt|nvt|Nee|Ja|1|behoort(GA,KA,A1)|
|SJI normaal tarief|O|nvt|nvt|Nee|Ja|1||
|SJA laag tarief|O|nvt|nvt|Nee|Ja|1||
|SJA normaal tarief|O|nvt|nvt|Nee|Ja|1||
|SJV|O|nvt|nvt|Ja|Nee|1|Wordt gecommuniceerd middels het veld SJA normaal<br>tarief|
|_Aansluitadres_:||||||||
|Straatnaam|O|nvt|nvt|Ja|Ja|1||
|Huisnummer|O|nvt|nvt|Ja|Ja|1||
|Huisnummertoevoeging|O|nvt|nvt|Ja|Ja|1||
|Postcode|O|nvt|nvt|Ja|Ja|1||
|Woonplaats|V|nvt|nvt|Ja|Ja|1|Een allocatiepunt in Nederland heeft verplicht een<br>woonplaats|
|Land|V|nvt|nvt|Ja|Ja|1||
|Locatieomschrijving|O|nvt|nvt|Ja|Ja|1|Via locatieomschrijving wordt ook gecommuniceerd of het<br> likilitibtft|
|BAG identificatienummer|O|nvt|nvt|Ja|Ja|1|eengejspannngsaansungere.|
|EAN-code additioneel allocatiepunt|A|nvt|nvt|Nee|A|N|In geval het een primair allocatiepunt betreft en er sprake<br>is van één of meer additionele allocatiepunten dan<br>verplicht te vullen met de EAN-code(’s) van het(de)<br>bijbehorend additionele allocatiepunt(en).<br>Dient leeg te worden gelaten indien het een additioneel<br>allocatiepunt betreft. Voor KA geldt een maximum van 5<br>EAN-codes voor additioneel allocatiepunten. Voor GA<br>ldt dit i it|
|EAN-code primaire allocatiepunt|A|nvt|nvt|Nee|A|1|ge  maxmum ne<br>Indien het een additioneel allocatiepunt betreft dan<br>verplicht te vullen met de EAN-code van het bijbehorende<br>primaire allocatiepunt.<br>Dient leeg te worden gelaten indien het een primair<br>allocatieunt betreft|
|Meetinrichtingnummer|A|nvt|nvt|Ja|Ja|1|p.<br>Verplicht bij een in bedrijf zijnde allocatiepunt op een<br>kleine aansluiting met wijze van bemeting ongelijk aan<br>|
|Type meetinrichting|A|nvt|nvt|Ja|Ja|1|onbemeten,anders bemeten en onbekend<br>Omschrijving van de soort meetinrichting (functionaliteit):<br>•<br>Meetinrichting zonder communicatiefunctionaliteit<br>Meetinrichtinmet communicatiefunctionaliteit|
|Administratieve<br>status<br>van<br>de<br>meetinrichting|A|nvt|nvt|Ja|Ja|1|g <br>Verplicht<br>bij<br>een<br>meetinrichting<br>met<br>communicatiefunctionaliteit:<br>•<br>Administratief aan<br>•<br>Adiittif it|
|Uitleesbaarheid meetinrichting met<br>communicatiefunctionaliteit|A|nvt|nvt|Ja|Ja|1|mnsrae u<br>Verplicht<br>bij<br>een<br>meetinrichting<br>met<br>communicatiefunctionaliteit:<br>•<br>Technisch op afstand uit te lezen<br>•<br>Technisch niet opafstand uit te lezen|
|Aantal telwerken|A|nvt|nvt|Nee|Ja|1|<br>Het aantal actieve telwerken op de meetinrichting<br>geïnstalleerd. Niet van toepassing op de meetinrichting<br>met communicatiefunctionaliteit of in de situatie van geen|
|_Per telwerk:_||nvt|nvt|||_n_|<br>of meerdere meetinrichtingen.<br>_n telwerken per meetinrichting_|

|**Response allocatiepuntgegeve**|**ns ten behoev**|**e van de**|**pre-mu**|**tatiefase**||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GV**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Telwerkidentificatie|A|nvt|nvt|Ja|Ja|1|De telwerkidentificatie door middel van een numerieke<br>aanduiding. Verplicht indien bemeten.<br>•<br>Meetinrichting met communicatiefunctionaliteit:<br>telwerkidentificatie door middel van de OBIS-code<br>•<br>Meetinrichting zonder communicatiefunctionaliteit:<br>telwerkidentificatie door middel van een numerieke<br>aanduiding|
|Tariefzone|A|nvt|nvt|Ja|Ja|1|Verplicht bij meetinrichting zonder<br>communicatiefunctionaliteit:<br>•<br>Totaal<br>•<br>Normaal<br>•<br>Laag|
|Meetrichting|A|nvt|nvt|Nee|Ja|1|Verplicht bij meetinrichting zonder<br>communicatiefunctionaliteit:<br>•<br>Levering<br>•<br>Teruglevering (bij gas niet mogelijk)|
|Aantal telwielen|A|nvt|nvt|Ja|Ja|1|Verplicht bij alle meetinrichtingen, indien bemeten.|

### Afwijzing

|**Afwijzing opvraag allocatiepuntge**|**gevens ten**|**behoev**|**e van de**|**pre-mut**|**atiefase**|||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GV**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code leverancier|V|nvt|nvt|Ja|Ja|Ja||
|EAN-code allocatiepunt|V|nvt|nvt|Ja|Ja|1||
|Transactiedossiernummer|A|nvt|nvt|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens technische<br>redenen is afgewezen|
|Referentie|A|nvt|nvt|Ja|Ja|1|Gevuld indien meegegeven in de opvraag|
|EAN-code systeembeheerder|V|nvt|nvt|Ja|Ja|1||
|Afwijsreden|V|nvt|nvt|Ja|Ja|n|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledige opvraag of syntactische fout.<br>•<br>Het allocatiepunt is onbekend in het<br>aansluitingenregister van de betreffende<br>systeembeheerder.<br>•<br>De leverancier komt niet voor in het<br>leveranciersregister.<br>•<br>Geen contract van de leverancier voor het<br>allocatiepunt geregistreerd in het<br>Contracteinderegister.<br>•<br>Het allocatiepunt is geen allocatiepunt op een kleine<br>aansluiting.|
