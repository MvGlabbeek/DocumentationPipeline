# 4.15 SP0013 & SP0003: Distribueren stamgegevens na mutatie & Opvragen stamgegevens allocatiepunt


## 4.15.1 Procesafspraken KA

- a. Alleen de actuele leverancier en de actuele balanceringsverantwoordelijke kunnen in dit subproces stamgegevens opvragen. 

- b. De systeembeheerder levert de stamgegevens op bij een wijziging van de stamgegevens aan de partijen die als verantwoordelijke partijen voor het allocatiepunt zijn vermeld in het aansluitingenregister. 

- c. De wijzigingen in de stamgegevens gaan voor zowel gas als elektriciteit in op het begin van de betreffende mutatiedag. 

- d. Als gevolg van wijzigingen in de stamgegevens zullen slechts eenmaal per dag (uiterlijk op de volgende werkdag) de stamgegevens worden verzonden, ook als er meerdere stamgegevens op verschillende momenten op de dag gewijzigd zijn. 

- e. Bij een opvraag stamgegevens verstuurt de systeembeheerder de stamgegevens die betrekking hebben op 00:00 uur van de dag die ligt voor de dag waarop de opvraag door de systeembeheerder ontvangen is. De datum waarop de gegevens betrekking hebben wordt opgenomen in het veld geldigheidsdatum. 

- f. Indien de reactie op een opvraag van stamgegevens samenvalt met een oplevering van stamgegevens, ontvangt de opvragende marktpartij twee stamgegevensberichten van hetzelfde allocatiepunt op die dag. 

- g. Indien het opleveren van stamgegevens naar aanleiding van een technische mutatie (door de systeembeheerder) samenvalt met het opleveren van stamgegevens naar aanleiding van een mutatieproces (door de leverancier), dan wordt één stamgegevensbericht opgeleverd waarin als reden voor verzending het mutatieproces wordt opgenomen. 

- h. De systeembeheerder effectueert een mutatie in het aansluitingenregister ten gevolge van: 

   - i. Marktpartijmutatie: marktpartijen kunnen stamgegevens ontvangen als gevolg van een geeffectueerde mutatie van een marktproces, of 

   - ii. Systeembeheerdersmutatie: actieve marktpartijen op een allocatiepunt kunnen stamgegevens ontvangen als gevolg van een mutatie door de systeembeheerder. 

## 4.15.2 Procesbeschrijving KA Distribueren stamgegevens na mutatie

Bijlage B1110: Subprocesplaat SP0013 KA

1. De systeembeheerder controleert of er voor het betreffende allocatiepunt voor de betreffende dag stamgegevens zijn gewijzigd. 

2. De systeembeheerder verstuurt uiterlijk de werkdag na de mutatiedatum in het aansluitingenregister de stamgegevens naar de actuele leverancier en de actuele balanceringsverantwoordelijke. De stamgegevens betreffen waarden zoals deze op de mutatiedatum geldend zijn. 

3. De leverancier ontvangt en verwerkt de stamgegevens. 

4. De balanceringsverantwoordelijke ontvangt en verwerkt de stamgegevens. 

## 4.15.3 Termijnen KA

De systeembeheerder verstuurt de stamgegevens uiterlijk één werkdag na effectuering van de mutatie in het aansluitingenregister naar de actuele marktpartijen. 

## 4.15.4 Procesafspraken GA

- a. Alleen de actuele leverancier, de actuele balanceringsverantwoordelijke, de actuele meetverantwoordelijke partij en marktpartijen met een machtiging van de aangeslotene, kunnen in dit subproces stamgegevens opvragen. 

- b. De systeembeheerder levert de stamgegevens op bij een wijziging van de stamgegevens aan de partijen die als verantwoordelijke partijen voor het allocatiepunt zijn vermeld in het aansluitingenregister. 

- c. De wijzigingen in de stamgegevens gaan voor zowel gas als elektriciteit in op het begin van de betreffende mutatiedag. 

- d. Als gevolg van wijzigingen in de stamgegevens zal slechts eenmaal per dag (op de volgende werkdag) de stamgegevens worden verzonden, ook als er meerdere stamgegevens op verschillende momenten op de dag gewijzigd zijn. 

- e. Bij een opvraag stamgegevens verstuurt de systeembeheerder de stamgegevens die betrekking hebben op het begin van de dag die ligt voor de dag waarop de aanvraag door de systeembeheerder ontvangen is. De datum waarop de gegevens betrekking hebben wordt opgenomen in het veld geldigheidsdatum. 

- f. Indien de reactie op een opvraag van stamgegevens samenvalt met een oplevering van stamgegevens, ontvangt de opvragende marktpartij twee stamgegevensberichten op die dag. 

- g. Bij een wijziging van de stamgegevens van allocatiepunten op grote aansluitingen levert de systeembeheerder de stamgegevens ook op aan de partij die als meetverantwoordelijke partij voor de desbetreffende allocatiepunten in het aansluitingenregister geregistreerd staat. 

- h. Indien alleen de naam van de aangeslotene wijzigt, worden geen stamgegevens door de systeembeheerder verzonden. 

## 4.15.5 Procesbeschrijving GA Distribueren stamgegevens na mutatie

Bijlage B1111: Subprocesplaat SP0013 GA

1. De systeembeheerder controleert of er voor het betreffende allocatiepunt voor de betreffende dag stamgegevens zijn gewijzigd. 

2. De systeembeheerder verstuurt uiterlijk de werkdag na de mutatiedatum in het aansluitingenregister de stamgegevens naar, indien aanwezig, de actuele leverancier, de actuele balanceringsverantwoordelijke en de actuele meetverantwoordelijke partij. De stamgegevens betreffen waarden zoals deze op de mutatiedatum geldend zijn. 

3. De leverancier (indien aanwezig) verwerkt de stamgegevens. 

4. De meetverantwoordelijke partij (indien aanwezig) verwerkt de stamgegevens. 

5. De balanceringsverantwoordelijke (indien aanwezig) verwerkt de stamgegevens. 

## 4.15.6 Termijnen GA

De systeembeheerder verstuurt de stamgegevens uiterlijk één werkdag na effectuering van de mutatie in het aansluitingenregister naar de actuele marktpartijen. 

## 4.15.7 Procesbeschrijving KA Opvragen stamgegevens allocatiepunt

Bijlage B1112: Subprocesplaat SP0003 KA

1. De opvragende marktpartij vraagt de actuele stamgegevens op van het allocatiepunt. 

2. De systeembeheerder beoordeelt de opvraag op de volgende punten: 

   - a. Is de opvraag compleet en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de opvragende marktpartij bekend als leverancier in het leveranciersregister of als balanceringsverantwoordelijke in het BRP-register van de betreffende transmissiesysteembeheerder? 

   - d. Is de opvragende marktpartij geregistreerd als actuele leverancier of balanceringsverantwoordelijke op het allocatiepunt? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘opvraag stamgegevens allocatiepunt’ af, en verstuurt de systeembeheerder een afwijsbericht naar de opvragende marktpartij uiterlijk de werkdag na ontvangst van de ‘opvraag stamgegevens allocatiepunt’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige opvraag of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. c. Opvragende marktpartij is onbekend als leverancier of balanceringsverantwoordelijke. 

   - d. De opvragende marktpartij is niet de actuele leverancier of balanceringsverantwoordelijke op het allocatiepunt. 

4. De opvragende marktpartij ontvangt en verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘opvraag stamgegevens allocatiepunt’ van de opvragende marktpartij en verstuurt de systeembeheerder de stamgegevens naar de opvragende marktpartij uiterlijk de werkdag na ontvangst van de ‘opvraag stamgegevens allocatiepunt’. 

6. De opvragende marktpartij ontvangt en verwerkt de stamgegevens van het allocatiepunt. 

## 4.15.8 Termijnen KA

De systeembeheerder verstuurt de stamgegevens uiterlijk één werkdag na ontvangst van de opvraag naar de opvragende marktpartij. 

## 4.15.9 Procesbeschrijving GA Opvragen stamgegevens allocatiepunt

Bijlage B1113: Subprocesplaat SP0003 GA

1. De opvragende marktpartij vraagt de actuele stamgegevens op van het allocatiepunt. 

2. De systeembeheerder beoordeelt de opvraag op de volgende punten: 

   - a. Is de opvraag compleet en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de opvragende marktpartij bekend: 

      - i. als leverancier in het leveranciersregister, 

      - ii. als balanceringsverantwoordelijke in het BRP-register van de betreffende transmissiesysteembeheerder, of 

      - iii. heeft de opgeven meetverantwoordelijke partij een volledige erkenning volgens het MV-register? 

   - d. Is de opvragende marktpartij geregistreerd als actuele leverancier, balanceringsverantwoordelijke of meetverantwoordelijke partij op het allocatiepunt? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘opvraag stamgegevens allocatiepunt’ af, en verstuurt de systeembeheerder een afwijsbericht naar de opvragende marktpartij uiterlijk de werkdag na ontvangst van de ‘opvraag stamgegevens allocatiepunt’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige opvraag of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. c. De opvragende marktpartij is onbekend als leverancier, balanceringsverantwoordelijke of meetverantwoordelijke partij. 

   - d. De opvragende marktpartij is niet de actuele leverancier, balanceringsverantwoordelijke, of meetverantwoordelijke partij op het allocatiepunt. 

4. De opvragende marktpartij ontvangt en verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘opvraag stamgegevens allocatiepunt’ van de opvragende marktpartij en verstuurt de systeembeheerder de stamgegevens naar de opvragende marktpartij uiterlijk de werkdag na ontvangst van de ‘opvraag stamgegevens allocatiepunt’. 

6. De opvragende marktpartij ontvangt en verwerkt de stamgegevens van het allocatiepunt. 

## 4.15.10 Termijnen GA

De systeembeheerder verstuurt de stamgegevens uiterlijk één werkdag na ontvangst van de opvraag naar de opvragende marktpartij. 

## 4.15.11 Gegevensuitwisseling

### Stamgegevens: actuele leverancier

### Opvraag

|**Opvraag stamgegevens**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n **|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Referentie|O|O|O|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code opvragende marktpartij|V|V|V|Ja|Ja|1||

### Response

|**Stamgegevens**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer(s)|V|V|V|Ja|Ja|n|Verplicht|
|Proces ID|V|V|V|Ja|Ja|n|‘Beantwoording van aanvraag’ bij aanvraag stamgegevens,<br>andersgevuld vanuit deprocessen|
|Referentie|A|A|A|Ja|Ja|1|Leeg bij spontane oplevering stamgegevens, anders gevuld<br>vanuit de processen indien ingevuld in de opvraag of de<br>meldingvan de mutatie|
|Begindatum|V|V|V|Ja|Ja|1|Datum van opgeleverde gegevensgegevens|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|O|O|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|O|O|Ja|Ja|1||
|EAN-code<br>meetverantwoordelijke<br>partij|nvt|O|O|Ja|Ja|1||
|Systeemgebied|A|A|A|Ja|Ja|1||
|Productsoort|V|V|V|Ja|Ja|1|Elektriciteit of Gas|
|Wijze van bemeting|V|V|V|Ja|Ja|1|De verschillende manieren van bemeten:<br>•<br>Onbemeten<br>•<br>Jaarlijks<br>•<br>Maandelijks<br>•<br>Telemetrie<br>•<br>Niet continue<br>•<br>Anders bemeten<br>•<br>Onbekend|
|Profielcategorie|A|A|A|Ja|Ja|1|Een in bedrijf zijnde allocatiepunt heeft verplicht een<br>profiel/afnamecategorie, tenzij het een telemetrisch<br>gealloceerd allocatiepunt op een grote aansluiting<br>elektriciteit betreft:<br>•<br>Elektriciteit: E1A, E1B, E1C, E2A, E2B, E3A, E3, E4A, OPC<br>•<br>Gas: G1A,G2A,G2C,GGV,GXX,GIS,GIN|
|Afrekenmaand|nvt|A|A|Ja|Ja|1|Allocatiepunten die jaarlijks worden afgerekend moeten<br>worden ingevuld,overige niet.|
|Contractcapaciteit|nvt|A|nvt|Ja|Ja|1|Vermogen voor het primair allocatiepunt. Voor een AAP zal<br>hier de waarde 0 worden vermeld.|
|Fysieke capaciteit|Nee|O|O|Ja|Ja|1|Een in bedrijf zijnde allocatiepunt op een grote aansluiting<br>heeft verplicht een fysieke capaciteit.<br>Elektriciteit:<br>•<br>Voor allocatiepunten op grote aansluitingen kleiner of<br>gelijk 3x80A; 1x6A, 1x10A, 1x25A, 1x35A, 1x50A,<br>1x63A, 1x80A, 3x25A, 3x35A, 3x50A, 3x63A, 3x80A,<br>OBK<br>•<br>Voor allocatiepunten op grote aansluitingen groter<br>dan 3x80A; in kVA (leeg indien onbekend)<br>Gas: in m<sup>3</sup>(n)/uur(leegindien onbekend)|
|Maxverbruik|nvt|A|nvt|Ja|Nee|1|<br>Dit gegeven is verplicht voor telemetrisch bemeten<br>allocatiepunten op grote aansluitingengas.|
|Capaciteitstariefcode|A|nvt|nvt|Ja|Ja|1|Indicatie van het door de systeembeheerder aan dit primaire<br>allocatiepunt op een kleine aansluiting toegekende<br>capaciteitstarief voor de systeemkosten. Voor een<br>additioneel allocatiepunt zal hier een capaciteitstariefcode<br>worden vermeld die aangeeft dat er een 0-tarief toegepast<br>moet worden.|

|**Stamgegevens**<br>**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|---|---|---|---|---|---|---|---|
|<br>Fysieke status|V|V|V|Ja|Ja|<br>1|<br>Een indicatie van de fysieke status van een allocatiepunt:<br>•<br>In aanleg<br>•<br>In bedrijf<br>•<br>Uit bedrijf<br>•<br>Verwijderd|
|Leveringsstatus|V|V|V|Ja|Ja|1|Een indicatie van de leveringsstatus van een allocatiepunt,<br>afhankelijk<br>of<br>een<br>leverancier<br>en<br>balanceringsverantwoordelijke zijn geregistreerd op een<br>allocatiepunt, zijnde:<br>•<br>Actief<br>•<br>Inactief|
|Leveringsrichting|A|A|A|Ja|Ja|1|<br>Indicatie van de leveringsrichting op het allocatiepunt:<br>•<br>Levering<br>•<br>Teruglevering<br>•<br>Combi|
|Verbruikssegment|V|V|V|Ja|Ja|1|Specificatie van het segment waartoe het allocatiepunt<br>behoort(GAKAA1)|
|SJI laag tarief|O|O|O|Nee|Ja|1|, ,|
|SJI normaal tarief|O|O|O|Nee|Ja|1||
|SJA laag tarief|O|O|O|Nee|Ja|1||
|<br>SJA normaal tarief|O|O|O|Nee|Ja|1||
|SJV|O|O|nvt|Ja|Nee|1|Wordt gecommuniceerd middels het veld SJA normaal tarief|
|_Aansluitadres_:||||||||
|Straatnaam|O|O|O|Ja|Ja|1||
|Huisnummer|O|O|O|Ja|Ja|1||
|Huisnummertoevoeging|O|O|O|Ja|Ja|1||
|<br>Postcode|O|O|O|Ja|Ja|1||
|Woonplaats|V|V|V|Ja|Ja|1|Een allocatiepunt in Nederland heeft verplicht een<br>woonlaats|
|Landcode|V|V|V|Ja|Ja|1|p|
|Locatieomschrijving|O|O|O|Ja|Ja|1|Via locatieomschrijving wordt ook gecommuniceerd of het<br>eengelijkspanningsallocatiepunt betreft|
|BAG nummeridentificatie|O|O|O|Ja|Ja|1||
|Allocatiemethode|V|V|V|Ja|Ja|1|Telemetrie, slimmemeterallocatie of geprofileerd|
|EAN-code additioneel allocatiepunt|A|A|A|Nee|A|n|In geval het een primair allocatiepunt betreft en er sprake is<br>van één of meer additionele allocatiepunten dan verplicht te<br>vullen met de EAN-code(s) van het(de) bijbehorend(e)<br>additionele allocatiepunt(en).<br>Dient leeg te worden gelaten indien het een additioneel<br>allocatiepunt betreft. Voor KA geldt een maximum van 5<br>EAN-codes voor additionele allocatiepunten. Voor GA geldt<br>dit i it|
|EAN-code primaire allocatiepunt|A|A|A|Nee|A|1|maxmum ne.<br>Indien het een additioneel allocatiepunt betreft dan<br>verplicht te vullen met de EAN-code van het bijbehorende<br>primaire allocatiepunt.<br>Dient leeg te worden gelaten indien het een primair<br>allocatieunt betreft|
|Meetinrichtingnummer|A|nvt|nvt|Ja|Ja|1|p.<br>Verplicht bij een in bedrijf zijnde allocatiepunt op een kleine<br>aansluiting<br>met<br>wijze<br>van<br>bemeting<br>ongelijk<br>aan<br>OnbemetenAnders bemeten en Onbekend|
|Type meetinrichting|A|nvt|nvt|Ja|Ja|1|, <br>Omschrijving van de soort meetinrichting (functionaliteit):<br>•<br>Meetinrichting zonder communicatiefunctionaliteit<br><br>iihiiifilii|
|Administratieve<br>status<br>van<br>de<br>meetinrichting|A|nvt|nvt|Ja|Ja|1|•<br>Meetnrctngmet communcateunctonatet<br>Verplicht<br>bij<br>een<br>meetinrichting<br>met<br>communicatiefunctionaliteit:<br>•<br>Administratief aan<br><br>Adiiif i|
|Uitleesbaarheid meetinrichting met<br>communicatiefunctionaliteit|A|nvt|nvt|Ja|Ja|1|•<br>mnstrate ut<br>Verplicht<br>bij<br>een<br>meetinrichting<br>met<br>communicatiefunctionaliteit:<br>•<br>Technisch op afstand uit te lezen<br>•<br>Technisch niet oafstand uit te lezen|
|Temperatuurcorrectie|A|nvt|nvt|Ja|Nee|1|p <br>Verplicht bij een meetinrichting voor een allocatiepunt op<br>een kleine aansluitinggas.|
|Aantal telwerken|A|nvt|nvt|Nee|Ja|1|<br>Het aantal actieve telwerken op de meetinrichting<br>geïnstalleerd. Niet van toepassing op meetinrichting met<br>communicatiefunctionaliteit of in de situatie van geen of<br>meerdere meetinrichtingen.|

|**Stamgegevens**<br>||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|_Per telwerk:_||||||_n_|_n telwerken per meetinrichting_|
|Telwerkidentificatie|A|nvt|nvt|Ja|Ja|1|De telwerkidentificatie door middel van een numerieke<br>aanduiding. Verplicht indien bemeten.<br>•<br>meetinrichting met communicatie functionaliteit:<br>telwerkidentificatie door middel van de OBIS-code<br>•<br>meetinrichting zonder communicatie functionaliteit:<br>telwerkidentificatie door middel van een numerieke<br>aanduiding|
|Tariefzone|A|nvt|nvt|Ja|Ja|1|Verplicht<br>bij<br>meetinrichting<br>zonder<br>communicatiefunctionaliteit:<br>•<br>Totaal<br>•<br>Normaal<br>•<br>Laag|
|Meetrichting|A|nvt|nvt|Nee|Ja|1|Verplicht<br>bij<br>meetinrichting<br>zonder<br>communicatie<br>functionaliteit:<br>•<br>Levering<br>•<br>Teruglevering (bij gas niet mogelijk)|
|Aantal telwielen|A|nvt|nvt|Ja|Ja|1|Verplicht bij alle meetinrichtingen, indien bemeten.|
|Vermenigvuldigingsfactor|A|nvt|nvt|Ja|Ja|1|Verplicht bij alle meetinrichtingen, indien bemeten.|

### Afwijzing

|**Afwijzing opvraag stamgegevens**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code opvragende marktpartij|V|V|V|Ja|Ja|1||
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens technische<br>redenen is afgewezen|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|Afwijsreden|V|V|V|Ja|Ja|n|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledige opvraag of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister van de systeembeheerder.<br>•<br>De opvragende marktpartij onbekend als leverancier,<br>balanceringsverantwoordelijke<br>of<br>meetverantwoordelijke partij (alleen GA).<br>•<br>De opvragende marktpartij is niet de actuele<br>leverancier,<br>balanceringsverantwoordelijke,<br>of<br>meetverantwoordelijke partij (alleen GA) op het<br>allocatiepunt.|

### Stamgegevens: actuele balanceringsverantwoordelijke op het KA allocatiepunt of balanceringsverantwoordelijke/meetverantwoordelijke partij op een GA allocatiepunt

### Opvraag

|**Opvraag stamgegevens**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Referentie|O|O|O|Ja|Ja|1||
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code opvragende marktpartij|V|V|V|Ja|Ja|1||

### Response

|**Stamgegevens**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer(s)|V|V|V|Ja|Ja|n|Verplicht|
|Proces ID|V|V|V|Ja|Ja|n|‘Beantwoording van opvraag’ bij aanvraag stamgegevens,<br>andersgevuld vanuit deprocessen|

|**Stamgegevens**<br>**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|---|---|---|---|---|---|---|---|
|<br>Referentie|A|A|A|Ja|Ja|<br>1|<br>Leeg bij spontane oplevering stamgegevens, anders gevuld<br>vanuit de processen indien ingevuld in de opvraag of de<br>meldingvan de mutatie|
|Begindatum|V|V|V|Ja|Ja|1|Datum van opgeleverde gegevens|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|EAN-code leverancier|V|O|O|Ja|Ja|1||
|EAN-code<br>balanceringsverantwoordelijke|V|O|O|Ja|Ja|1||
|EAN-code<br>meetverantwoordelijke<br>partij|nvt|O|O|Ja|Ja|1||
|Systeemgebied|A|A|A|Ja|Ja|1||
|Productsoort|V|V|V|Ja|Ja|1|Elektriciteit of gas|
|Wijze van bemeting|V|V|V|Ja|Ja|1|De verschillende manieren van bemeten:<br>•<br>Onbemeten<br>•<br>Jaarlijks<br>•<br>Maandelijks<br>•<br>Telemetrie<br>•<br>Niet continue<br>•<br>Anders bemeten<br>•<br>Onbekend|
|Profielcategorie|A|A|A|Ja|Ja|1|<br>Een in bedrijf zijnde allocatiepunt heeft verplicht een<br>profiel/afnamecategorie, tenzij het een telemetrisch<br>gealloceerd allocatiepunt op een grote aansluiting<br>elektriciteit betreft:<br>•<br>Elektriciteit: E1A, E1B, E1C, E2A, E2B, E3, E4A, OPC<br>•<br>Gas: G1AG2AG2CGGVGXXGISGIN|
|Afrekenmaand|nvt|A|A|Ja|Ja|1|, , , , , , <br>Allocatiepunten die jaarlijks worden afgerekend moeten<br>worden ingevuld,overige niet.|
|Contractcapaciteit|nvt|A|nvt|Ja|Ja|1|Vermogen voor het primaire allocatiepunt. Voor een<br>additioneel allocatiepunt zal hier de waarde 0 worden<br>vermeld|
|Fysieke capaciteit|Nee|O|O|Ja|Ja|1|.<br>Een in bedrijf zijnde allocatiepunt op een grote aansluiting<br>heeft verplicht een fysieke capaciteit.<br>Elektriciteit:<br>•<br>Voor allocatiepunten op grote aansluitingen kleiner of<br>gelijk 3x80A; 1x6A, 1x10A, 1x25A, 1x35A, 1x50A,<br>1x63A, 1x80A, 3x25A, 3x35A, 3x50A, 3x63A, 3x80A,<br>OBK<br>•<br>Voor allocatiepunten op grote aansluitingen groter<br>dan 3x80A; in kVA (leeg indien onbekend)<br>Gas: in m<sup>3</sup>(n)/uur(leegindien onbekend)|
|Maxverbruik|nvt|A|nvt|Ja|Nee|1|<br>Dit gegeven is verplicht voor telemetrisch bemeten<br>allocatieunten orote aansluitinenas|
|Capaciteitstariefcode|A|nvt|nvt|Ja|Ja|1|p p g g g.<br>Indicatie van het door de systeembeheerder aan dit<br>primaire allocatiepunt op een kleine aansluiting toegekende<br>capaciteitstarief voor de systeemkosten. Voor een<br>additioneel allocatiepunt zal hier een capaciteitstariefcode<br>worden vermeld die aangeeft dat er een 0-tarief toegepast<br>moet worden|
|Fysieke status|V|V|V|Ja|Ja|1|.<br>Een indicatie van de fysieke status van een allocatiepunt:<br>•<br>In aanleg<br>•<br>In bedrijf<br>•<br>Uit bedrijf<br>•<br>Vidd|
|Leveringsstatus|V|V|V|Ja|Ja|1|erwjer<br>Een indicatie van de leveringsstatus van een allocatiepunt,<br>afhankelijk<br>of<br>een<br>leverancier<br>en<br>balanceringsverantwoordelijke zijn geregistreerd op een<br>allocatiepunt, zijnde:<br>•<br>Actief<br><br>|
|Leveringsrichting|A|A|A|Ja|Ja|1|•<br>Inactief<br>Indicatie van de leveringsrichting op het allocatiepunt:<br>•<br>Levering<br>•<br>Teruglevering<br>•<br>Combi|
|Verbruikssegment|V|V|V|Ja|Ja|1|<br>Specificatie van het segment waartoe het allocatiepunt<br>behoort(GAKAA1)|
|SJI laag tarief<br>SJI normaal tarief|O<br>O|O<br>O|O<br>O|Nee<br>Nee|Ja<br>Ja|1<br>1|,,|

|**Stamgegevens**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|SJA laag tarief|O|O|O|Nee|Ja|1||
|SJA normaal tarief|O|O|O|Nee|Ja|1||
|SJV|O|O|nvt|Ja|Nee|1|Wordt gecommuniceerd middels het veld SJA normaal tarief|
|_Aansluitadres_:||||||||
|Straatnaam|Nee|O|O|Ja|Ja|1||
|Huisnummer|Nee|O|O|Ja|Ja|1||
|Huisnummertoevoeging|Nee|O|O|Ja|Ja|1||
|Postcode|Nee|O|O|Ja|Ja|1||
|Woonplaats|Nee|V|V|Ja|Ja|1|Een allocatiepunt in Nederland heeft verplicht een<br>woonplaats|
|Landcode|Nee|V|V|Ja|Ja|1||
|Locatieomschrijving|Nee|O|O|Ja|Ja|1|Via locatieomschrijving wordt ook gecommuniceerd of het<br>eengelijkspanningsallocatiepunt betreft|
|BAG nummeridentificatie|Nee|O|O|Ja|Ja|1||
|Allocatiemethode|V|V|V|Ja|Ja|1|Telemetrie, slimmemeterallocatie of geprofileerd|
|EAN-code additioneel allocatiepunt|Nee|A|A|Nee|A|n|In geval het een primair allocatiepunt betreft en er sprake is<br>van één of meer additionele allocatiepunten dan verplicht te<br>vullen met de EAN-code(s) van het(de) bijbehorende<br>additionele allocatiepunt(en). Dient leeg te worden gelaten<br>indien het een additioneel allocatiepunt betreft. Voor KA<br>geldt een maximum van 5 EAN-codes voor additionele<br>allocatiepunten. Voor GAgeldt dit maximum niet.|
|EAN-code primaire allocatiepunt|Nee|A|A|Nee|A|1|Indien het een additioneel allocatiepunt betreft dan<br>verplicht te vullen met de EAN-code van het bijbehorende<br>primaire allocatiepunt.<br>Dient leeg te worden gelaten indien het een primair<br>allocatiepunt betreft.|

### Afwijzing

|**Afwijzing opvraag stamgegevens**||||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KA**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code opvragende marktpartij|V|V|V|Ja|Ja|1||
|EAN-code allocatiepunt|V|V|V|Ja|Ja|1||
|Transactiedossiernummer|A|A|A|Ja|Ja|1|Verplicht gevuld, tenzij de opvraag wegens technische<br>redenen is afgewezen|
|Referentie|A|A|A|Ja|Ja|1|Gevuld indien meegegeven in de opvraag|
|EAN-code systeembeheerder|V|V|V|Ja|Ja|1||
|Afwijsreden|V|V|V|Ja|Ja|n|Indicatie van de reden waarom de opvraag is afgewezen:<br>•<br>Onvolledige opvraag of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister van de systeembeheerder.<br>•<br>De opvragende marktpartij onbekend als leverancier,<br>balanceringsverantwoordelijke<br>of<br>meetverantwoordelijke partij (alleen GA).<br>•<br>De opvragende marktpartij is niet de actuele<br>leverancier,<br>balanceringsverantwoordelijke,<br>of<br>meetverantwoordelijke partij (alleen GA) op het<br>allocatiepunt.|
