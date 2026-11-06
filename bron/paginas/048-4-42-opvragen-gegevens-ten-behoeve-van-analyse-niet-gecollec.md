# 4.42 Opvragen gegevens ten behoeve van analyse niet gecollecteerde meterstand P4


## 4.42.1 Procesafspraken

- a. Een leverancier die volgens het aansluitingenregister geregistreerd staat of uiterlijk 4 maanden geleden geregistreerd is geweest op een allocatiepunt, kan gegevens met betrekking tot een meetinrichting met communicatiefunctionaliteit opvragen om inzicht te krijgen in de redenen waarom het niet mogelijk is om meterstanden via de P4 te collecteren. 

- b. Een overige dienstenaanbieder waarvan een niet beëindigd klantmandaat met betrekking tot een allocatiepunt geregistreerd staat bij de systeembeheerder, kan gegevens met betrekking tot een meetinrichting met communicatiefunctionaliteit opvragen om inzicht te krijgen het niet mogelijk is om meterstanden via de P4 te collecteren. 

- c. Een overige dienstenaanbieder kan met betrekking tot een allocatiepunt inzicht krijgen in zijn actieve en beëindigde klantmandaten die bij de systeembeheerder geregistreerd staan. 

## 4.42.2 Procesbeschrijving

Bijlage B1170: Subprocesplaat zonder SP-code (§4.42.2)

1. De opvragende marktpartij vraagt de ’Gegevens ten behoeve van de analyse niet gecollecteerde meterstand P4’ op. 

2. De systeembeheerder beoordeelt de opvraag op de volgende punten: a. Is de opvraag compleet en syntactisch correct? 

- b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

- c. Is de opvragende marktpartij bekend als leverancier in het leveranciersregister of als overige dienstenaanbieder? 

- d. Is de opvragende marktpartij geregistreerd als actuele leverancier of uiterlijk vier maanden geleden geregistreerd geweest als leverancier, of overige dienstenaanbieder met een actief of een beëindigd klantmandaat op het allocatiepunt? 

Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ’Gegevens ten behoeve van de analyse niet gecollecteerde meterstand P4’ af, en verstuurt de een afwijsbericht naar de opvragende marktpartij. De afwijsredenen die de systeembeheerder kan gebruiken zijn: 

   - a. Onvolledige opvraag of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De opvragende marktpartij is onbekend als leverancier of overige dienstenaanbieder. 

   - d. De opvragende marktpartij is niet de actuele leverancier of is niet uiterlijk vier maanden geleden geregistreerd geweest als leverancier, of overige dienstenaanbieder met een actief of een beëindigd klantmandaat op het allocatiepunt. 

3. De opvragende marktpartij ontvangt en verwerkt de afwijzing. 

4. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘Gegevens ten behoeve van de analyse niet gecollecteerde meterstand P4’ van de opvragende marktpartij en verstuurt de gegevens naar de opvragende marktpartij. 

5. De opvragende marktpartij ontvangt en verwerkt de gegevens. 

## 4.42.3 Termijnen

- a. De aansluitings- en storingsinformatie kan via een synchroon kanaal opgehaald worden door de leverancier of overige dienstenaanbieder. 

## 4.42.4 Gegevensuitwisseling

### Verzoek gegevens ten behoeve van analyse niet gecollecteerde meterstand P4 van opvragende marktpartij naar systeembeheerder

|**Gegeven**|**Toelichting**|
|---|---|
|Opvragende marktpartij|Unieke identificatie van de opvragende marktpartij|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Referentie|Door de opvragende leverancier of overige diensten aanbieder verstrekte referentie<br>bedoeld om de terugkoppeling van de systeembeheerder te kunnen herleiden tot het<br>verzoek.|

### Antwoord vanuit systeembeheerder naar opvragende marktpartij

|**Gegeven**|**Toelichting**|
|---|---|
|Referentie|Door de opvragende leverancier of overige dienstenaanbieder verstrekte referentie<br>bedoeld om de terugkoppeling van de systeembeheerder te kunnen herleiden tot het<br>verzoek.|
|_Gegevens allocatiepunt:_||
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Systeembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt (verzender afwijzing)|
|Productsoort|Elektriciteit of gas|
|Verbruikssegment|Het verbruikssegment van de aansluiting: Kleine aansluiting|
|Fysieke status|De technische toestand voor fysieke energieoverdracht op dit allocatiepunt:<br>• In aanleg<br>• In bedrijf<br>• Uit bedrijf<br>• Gesloopt|
|_Gegevens meetinrichting:_||
|Meternummer|Identificerend nummer van de meetinrichting|

|**Gegeven**|**Toelichting**|
|---|---|
|Plaatsingsdatum meetinrichting|Datum waarop de meetinrichting is geplaatst|
|Type meetinrichting|Het type meetinrichting dat is geregistreerd:<br>• Conventioneel<br>• Slim|
|Uitleesbaarheid slimme meetinrichting|Aanduiding of meetinrichting met communicatiefunctionaliteit op afstand uitleesbaar is:<br>• Technisch op afstand uit te lezen<br>• Technisch niet opafstand uit te lezen|
|Administratieve status meetinrichting|De administratieve status van de meetinrichting met communicatiefunctionaliteit geeft aan<br>of de communicatiefunctionaliteit administratief is uitgeschakeld:<br>• Aan<br>• Uit|
|_Storingsgegevens:_||
|Status storing|De volgende statussen zijn mogelijk:<br>• Storing bekend en wordt geanalyseerd<br>• Afspraak wordt ingepland<br>• Klant is benaderd<br>• Afspraak bevestigd<br>• Hulp nodig van marktpartij voor het maken klantafspraak<br>• Oplossingwordtgecontroleerd|
|Datum storing|Datum waarop de storing is geregistreerd door de systeembeheerder|
|Reden technisch niet uitleesbaar|De reden waarom de systeembeheerder de meetinrichting op technisch niet uitleesbaar<br>heeft gezet (de storing niet op kan lossen). De volgende redenen zijn mogelijk:<br>• Geen fysieke toegang<br>• Aansluiting langdurig spanningsloos of niet in gebruik<br>• Uitlezing geblokkeerd i.v.m. incident meetinrichting of telecom<br>• Geen telecomdekking door inpandige situatie<br>• Geen telecomdekking aanwezig<br>• De meetinrichting gas hangt te ver van de meetinrichting elektriciteit of er hangt een losse<br>meetinrichting gas|
|Datum melding niet uitleesbaar|Datum waarop de meetinrichting op technisch niet op afstand uitleesbaar is gezet door de<br>systeembeheerder|
|_Klantmandaatgegevens:_|Wordt alleen aan een overige dienstenaanbieder ter beschikking gesteld|
|Per klantmandaat||
|Startdatum|Startdatum van het klantmandaat|
|Einddatum|Einddatum van het klantmandaat|
|Eventtype|Het type event dat de laatste aanpassing op het klantmandaat heeft gedaan:<br>• Inhuizing<br>• Uithuizing<br>• Leverancierswitch|
|Effectueringsdatum event|De datum waarop het laatste event met betrekking tot het geregistreerde klantmandaat<br>heeftplaatsgevonden|

### Afwijzing vanuit systeembeheerder naar opvragende marktpartij

|**Gegeven**|**Toelichting**|
|---|---|
|Opvragende marktpartij|Unieke identificatie van de opvragende marktpartij|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Referentie|Door de opvragende leverancier of overige diensten aanbieder verstrekte referentie<br>bedoeld om de terugkoppeling van de systeembeheerder te kunnen herleiden tot het<br>verzoek.|
|Systeembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt|
|Afwijsreden|Indicatie van de reden waarom de opvraag is afgewezen:<br>• Onvolledige melding of syntactische fout.<br>• Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder.<br>• De opvragende marktpartij is onbekend als leverancier of overige dienstenaanbieder<br>• De opvragende marktpartij is niet de actuele leverancier of overige dienstenaanbieder<br>(geweest) op het allocatiepunt.|
