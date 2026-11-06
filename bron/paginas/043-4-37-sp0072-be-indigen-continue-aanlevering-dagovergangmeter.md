# 4.37 SP0072 Beëindigen continue aanlevering dagovergangmeterstanden van een allocatiepunt


## 4.37.1 Procesafspraken KA

- a. De verantwoordelijkheid voor het beëindigen van de continue aanlevering wanneer er geen klantvraag (meer) is ligt in beginsel bij de leverancier; 

- b. Mocht er een SVEL-proces op of verwijdering van een allocatiepunt waarop een continue aanlevering loopt plaatsvinden, dan zal de systeembeheerder de continue aanlevering stopzetten. De systeembeheerder stelt de leverancier via het reguliere berichtenverkeer van deze events op de hoogte. De systeembeheerder stelt de leverancier niet expliciet op de hoogte van de beëindiging van de continue aanlevering. De continue aanlevering wordt beëindigd per de datum van het proces dat aanleiding geeft tot beëindiging; 

- c. De leverancier ontvangt alle dagovergangmeterstanden die als zodanig vanaf de startdatum tot en met de beëindigingsdatum van de betreffende continue aanlevering in de 

meetinrichting met communicatiefunctionaliteit geregistreerd zijn via het proces van de continue aanlevering. 

## 4.37.2 Procesbeschrijving KA

Bijlage B1165: Subprocesplaat SP0072 KA

1. De opvragende marktpartij dient een ‘Verzoek beëindigen continu aanleveren dagovergangmeterstanden van een allocatiepunt’ in. 

   - a. Het verzoek bevat tenminste de EAN-code van het allocatiepunt. 

2. De systeembeheerder controleert het ‘Verzoek beëindigen continu aanleveren dagovergangmeterstanden van een allocatiepunt van de opvragende marktpartij. Hierbij wordt ten minste gecontroleerd of er een continue levering van dagovergangmeterstanden op dit allocatiepunt loopt voor de aanvragende leverancier. 

3. De systeembeheerder beantwoordt het verzoek met een antwoordbericht: a. Wanneer de controle(s) een positief resultaat heeft/hebben, antwoordt de systeembeheerder met een antwoordbericht waarin hij meldt dat de continue aanlevering beëindigd wordt; 

   - b. Wanneer (één van de) controle(s) een negatief resultaat heeft/hebben antwoordt de systeembeheerder met een antwoordbericht waarin de reden wordt vermeld dat er geen continue aanlevering wordt beëindigd op het betreffende allocatiepunt. 

4. De opvragende marktpartij verwerkt het antwoordbericht. 

5. De systeembeheerder beëindigt bij een positief antwoord op de controle(s) de continue levering. 

## 4.37.3 Termijnen KA

Voor beëindigingsverzoeken geldt dat een antwoord op een verzoek synchroon volgt. De continue aanlevering wordt beëindigd per de datum waarop het verzoek tot beëindiging wordt ingediend. De leverancier ontvangt alle dagovergangmeterstanden die als zodanig vanaf de startdatum tot en met de beëindigingsdatum van de betreffende continue aanlevering als zodanig in de meetinrichting met communicatiefunctionaliteit geregistreerd zijn via het proces van de continue aanlevering. 

## 4.37.4 Gegevensuitwisseling KA

### Verzoek beëindigen continu aanleveren dagovergangmeterstanden van een allocatiepunt

|**Verzoek beëindigen conti**|**nu aan**|**leveren**|**dagove**|**rgangm**|**eterstanden van een allocatiepunt**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code leverancier|V|Ja|Ja|1|ID van de verzoekende leverancier|
|EAN-code allocatiepunt|V|Ja|Ja|1|ID van het allocatiepunt waarvoor het verzoek gedaan wordt|
|Referentie|O|Ja|Ja|1|Door de aanvragende leverancier verstrekte referentie bedoeld om de terugkoppeling<br>van de systeembeheerder te kunnen herleiden tot het verzoek|

### Antwoordbericht verzoek beëindigen continu aanleveren dagovergangmeterstanden van een allocatiepunt

|**Antwoordbericht verzoek**|**beëi**|**ndigen c**|**ontinu**|**aanlev**|**eren dagovergan**|**gmeterstanden van een allocatiepunt**|
|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n **|**Opmerking**||
|EAN-code leverancier|V|Ja|Ja|1|ID van de verz|oekende leverancier|
|EAN-code allocatiepunt|V|Ja|Ja|1|ID van het allo|catiepunt waarvoor het verzoekgedaan wordt|
|Referentie|A|Ja|Ja|1|Door de aanvr<br>de systeembe|agende leverancier verstrekte referentie bedoeld om de terugkoppeling van<br>heerder te kunnen herleiden tot het verzoek|
|Response|V|Ja|Ja|1|Reactie van de<br>1.<br>2.|systeembeheerder op het verzoek. Mogelijke waarden:<br>Continue aanlevering is met succes beëindigd<br>Er loopt geen continue aanlevering op dit allocatiepunt voor de<br>aanvragende leverancier|
