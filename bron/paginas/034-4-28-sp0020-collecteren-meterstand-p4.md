# 4.28 SP0020 Collecteren meterstand P4


## 4.28.1 Procesafspraken KA

- a. Bij autorisatie van verzoeken via de P4 wordt onderscheid gemaakt in aanvragen van leveranciers, systeembeheerders en ODA’s. 

- b. De leverancier kan ook meetgegevensverzoeken indienen in de rol van ODA. De leverancier dient hiervoor een aparte bedrijfs-EAN-code aan te vragen om als ODA te kunnen opereren. 

- c. De meetgegevens die in de meetinrichting zijn opgeslagen kunnen via de P4 opgevraagd worden door marktpartijen. Het betreft hierbij de volgende meetgegevens: 

   - **Dagovergangmeterstand** 

De dagovergangmeterstand is de meterstand op het moment van dagovergang (00:00 uur) horend bij de datum van de dag die op dat moment begint. De dagovergangmeterstand voor elektriciteit bestaat uit vier waarden waarmee het volume voor normaaluren en laaguren voor levering en teruglevering wordt geregistreerd. Voor gas bestaat de dagovergangmeterstanduit een enkele waarde (let op: hier wordt bewust afgeweken van het begrip gasdag, welke start op 06:00). 

   - **Intervalmeterstand** 

      - De intervalmeterstand is de meterstand van de totaaltelwerken voor levering en teruglevering op elk kwartier bij elektriciteit of de meterstand op elk uur voor gas. 

   - **Maandovergangmeterstanden** De maandovergangmeterstand is de meterstand op het moment van maandovergang (00:00 uur) horend bij de maand die op dat moment begint. De maandovergangmeterstand is identiek aan de dagovergangmeterstand van de eerste dag van de maand. Voor recovery doeleinden kunnen de laatste 13 maandovergangmeterstanden worden opgehaald uit de meetinrichting. 

- d. Uit de meetinrichting kunnen dagovergangmeterstanden worden opgehaald tot maximaal de laatste 40 kalenderdagen, de intervalmeterstanden voor de laatste 10 kalenderdagen en de maandovergangmeterstanden voor de laatste 13 maanden. 

- e. De meterstanden moeten per type, per individuele dag worden aangevraagd. 

- f. Verzoeken voor allocatiepunten, die op basis van het aansluitingenregister één van de volgende kenmerken hebben, zullen worden afgewezen: 

   - i. Een meetinrichting zonder communicatiefunctionaliteit Een meetinrichting met communicatiefunctionaliteit die administratief uit staat. 

   - ii. Een technisch niet op afstand uitleesbare meetinrichting met communicatiefunctionaliteit. 

   - iii. Geen meetinrichting aanwezig. 

- g. Ingediende verzoeken voor gegevens die buiten de gemaximeerde bewaartermijn liggen zullen worden afgewezen. 

- h. Het is alleen mogelijk om meetgegevens uit de meetinrichting op te vragen over tijdstippen die in het verleden liggen. 

- i. Een partij wordt geacht eenzelfde verzoek pas in te dienen nadat de reactietermijn van de systeembeheerder is verstreken. 

- j. Een meetinrichting elektriciteit is voorzien van meerdere telwerken. Deze telwerken worden geïdentificeerd met behulp van de OBIS codering (IEC 62056-61). In de onderstaande tabel wordt in verkorte wijze aangegeven welke codes worden gebruikt voor de identificatie van een specifiek telwerk. 

|Code|Product|Tariefzone|Eenheid|
|---|---|---|---|
|1.8.1|Levering|Laag|kWh|
|1.8.2|Levering|Hoog|kWh|
|2.8.1|Teruglevering|Laag|kWh|
|2.8.2|Teruglevering|Hoog|kWh|

De eenheid die wordt gebruikt voor dagovergangmeterstanden is kWh voor elektriciteit en m<sup>3</sup> voor gas. Voor intervalmeterstanden wordt voor elektriciteit gebruik gemaakt van Wh en voor gas van m<sup>3</sup> . In de standaard OBIS codering bestaat ook een vierde positie (1.8.1.x); deze wordt echter niet gebruikt in de P4. Deze positie wordt gebruikt om individuele tellerstanden te identificeren. Identificatie van de individuele tellerstanden gebeurt in de P4 met behulp van timestamps. 

Voor gas wordt gebruik gemaakt van een enkel telwerk omdat voor gas bij kleine aansluitingen alleen enkeltarief zonder teruglevering geldt. Daarom is het gebruik van een codering niet nodig bij gas. 

### Specifieke controles bij indienen door leverancier

- a. Bij iedere aanvraag van een leverancier zal vooraf een autorisatie plaatsvinden op basis van het aansluitingenregister. 

- b. Een leverancier heeft toegang tot meetgegevens over de periode waarin hij in het aansluitingenregister is of was geregistreerd als actieve leverancier op het allocatiepunt. 

### Specifieke controles bij indienen door ODA

- a. Bij iedere aanvraag van een ODA zal vooraf een autorisatie plaatsvinden op basis van het aangeleverde mandaat. 

- b. ODA’s dienen middels een zogenaamd ODA-mandaatbestand aan de systeembeheerder kenbaar te maken voor welke allocatiepunten en voor welke periode de ODA toestemming van de klant heeft ontvangen om een verzoek te mogen indienen voor het opvragen van de meetgegevens van de klant. 

- c. ODA’s dienen ervoor te zorgen dat zij tenminste één keer per jaar een Assuranceverklaring overleggen met betrekking tot de juistheid van de aangeleverde mandaatgegevens. 

- d. Wanneer een inhuizing, uithuizing of leverancierswitch met naamswijziging plaats vindt, dan beschouwt de systeembeheerder het ODA-mandaat op het betreffende allocatiepunt als beëindigd. 

- e. Indien een ODA-mandaat ten onrechte van het allocatiepunt is verwijderd (toestemming wordt beschouwd als zijnde beëindigd) kan de betreffende ODA de levering van meetgegevens 

voor het betreffende allocatiepunt weer laten hervatten door de startdatum van de toestemming in het ODA-mandaatbestand aan te passen naar een datum die later ligt dan de datum van de inhuizing, uithuizing of leverancierswitch met naamswijziging. Toestemmingen met een eerdere datum zullen niet doorgevoerd worden. 

## 4.28.2 Procesbeschrijvingen KA

### Indienen en beoordelen verzoek

Bijlage B1148: Subprocesplaat SP0020 KA – Indienen en beoordelen verzoek

1. De aanvragende partij dient het ‘verzoek collecteren meterstand P4’ in bij de systeembeheerder. 

2. De systeembeheerder beoordeelt het verzoek in zijn geheel op de volgende punten: 

   - a. Voldoet de waarde in het ‘verzoek collecteren meterstand P4’ aan de eisen die door het protocol worden gesteld? 

   - b. Komt de EAN-code van de verzoekende partij overeen met het gebruikte beveiligingscertificaat? 

   - c. Is de verzoekende partij geautoriseerd? 

   - d. Is de geadresseerde systeembeheerder bekend? 

   - e. Kan het verzoek bij de geadresseerde systeembeheerder afgeleverd worden? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder het ‘verzoek collecteren meterstand P4’ af, en verstuurt de systeembeheerder een afwijsbericht naar de aanvragende partij. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. De waarde in het verzoek voldoet niet aan de eisen die door het protocol gesteld worden. 

   - b. EAN-code verzoekende partij komt niet overeen met het certificaat. 

   - c. De verzoekende partij is niet geautoriseerd. 

   - d. EAN-code systeembeheerder onbekend. 

   - e. Verzoek kan niet bij de systeembeheerder afgeleverd worden. 

4. De aanvragende partij verwerkt de afwijzing. 

5. Indien de systeembeheerder het ‘verzoek collecteren meterstand P4’ kan verwerken, verstuurt hij een ontvangstbevestiging naar de aanvragende partij. 

6. Het verzoek wordt door de systeembeheerder intern klaargezet voor verwerking. 

### Verwerken verzoek

Bijlage B1149: Subprocesplaat SP0020 KA – Verwerken verzoek

1. De systeembeheerder controleert het ‘verzoek collecteren meterstand P4’ per aanvraag in het verzoek op de volgende punten: 

   - a. Is de aanvragende partij geauthentiseerd? 

   - b. Is het allocatiepunt bekend op de gevraagde datum? 

   - c. Beschikt het allocatiepunt op het moment van indienen van het ‘verzoek collecteren meterstand P4’ beschikt over een meetinrichting met communicatiefunctionaliteit? 

   - d. Is de meetinrichting met communicatiefunctionaliteit gedeployed? 

   - e. Is de datum van de dagovergangmeterstand, de maandovergangmeterstand of de intervalmeterstand <= huidige datum (= systeemdatum)? 

   - f. Is de datum niet ouder dan de huidige datum min het maximaal aantal dagen voor: 

      - i. intervalmeterstand, 

      - ii. dagovergangmeterstandof 

      - iii. aantal maanden voor maandovergangmeterstand? 

   - g. Zijn de gevraagde meetgegevens beschikbaar? 

   - h. Kan het ingediende ‘verzoek collecteren meterstand P4’ door de meetinrichting uitgevoerd kan worden? 

   - i. Staat de meetinrichting met communicatiefunctionaliteit op het allocatiepunt op het moment van het indienen administratief op aan? 

   - j. Staat de meetinrichting met communicatiefunctionaliteit op het allocatiepunt in het aansluitingenregister technisch op afstand uitleesbaar (uitleesbaarheid meetinrichting met communicatiefunctionaliteit )? 

   - k. Is de verzoekende partij gemandateerd? 

2. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder het ‘verzoek collecteren meterstand P4’ af, en verstuurt de systeembeheerder een afwijsbericht naar de aanvragende partij. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. De waarde in het verzoek voldoet niet aan de eisen die door het protocol gesteld worden. 

   - b. EAN-code verzoekende partij komt niet overeen met het certificaat. 

   - c. De verzoekende partij is niet geautoriseerd. 

   - d. EAN-code systeembeheerder onbekend. 

   - e. Bericht kan niet bij de systeembeheerder afgeleverd worden. 

   - f. De aanvragende partij is niet geauthentiseerd. 

   - g. Het allocatiepunt is onbekend op gevraagde datum. 

   - h. Geen meetinrichting met communicatiefunctionaliteit op het allocatiepunt op gevraagde datum. 

   - i. Gevraagde meetgegevens niet beschikbaar, meetinrichting in deploymentfase. 

   - j. Datum voor gevraagde meetgegevens in de toekomst, meterstanden nog niet beschikbaar. 

   - k. Datum van gevraagde meetgegevens te oud, meterstanden niet meer beschikbaar. 

   - l. Gevraagde meetgegevens niet beschikbaar, storing bekend en in behandeling, of Gevraagde meetgegevens niet beschikbaar, meetinrichting tijdelijk in storing, of Gevraagde meetgegevens niet beschikbaar: grootschalige storing. 

   - m. Dit specifieke verzoek kan niet worden uitgevoerd door de meetinrichting. 

   - n. De meetinrichting met communicatiefunctionaliteit staat administratief op uit. 

   - o. Er hangt een technisch niet op afstand uitleesbare meetinrichting met communicatiefunctionaliteit. 

   - p. De aanvragende partij is niet gemandateerd, omdat de autorisatie is beëindigd naar aanleiding van wijziging van de aangeslotene op het allocatiepunt. 

3. De aanvragende partij verwerkt de afwijzing. 

4. De systeembeheerder voert het ‘verzoek collecteren meterstand P4’ uit. Hierbij zijn twee resultaten mogelijk. Óf de meetgegevens zijn beschikbaar, óf de meetgegevens zijn niet beschikbaar. 

Indien de meetgegevens (deels) niet beschikbaar zijn, dan wordt voor de betreffende meetintervallen de tijdsaanduiding wel en de meetgegevens niet opgegeven in het bericht. De systeembeheerder past deze maatregel toe tot en met de minimale ondergrens van twee meetgegevens per telwerk. 

5. Indien de meetgegevens niet beschikbaar zijn, zal de systeembeheerder één van de volgende afwijzingen versturen naar de aanvragende partij: 

   - a. Gevraagde meetgegevens niet beschikbaar: meetinrichting in deploymentfase. Deze wordt voor de duur van maximaal vijf kalenderdagen geretourneerd; 

   - b. Gevraagde meetgegevens niet beschikbaar: meetinrichting tijdelijk in storing. Deze wordt voor de duur van maximaal 10 werkdagen geretourneerd; 

      - _i. Indien bij een aanvraag van intervalmeterstanden blijkt dat de minimale ondergrens van twee meetgegevens per telwerk per dag niet wordt gehaald, dan communiceert de systeembeheerder deze foutcode._ 

   - c. Gevraagde meetgegevens niet beschikbaar: storing bekend en in behandeling. Deze wordt  geretourneerd totdat de storing opgelost is of één van de technische niet uitleesbaar statussen heeft bereikt. Indien uit het storingsproces blijkt dat de minimale ondergrens voor bereikbaarheid van de meetinrichting niet gehaald kan worden zal de meetinrichting op technisch niet uitleesbaar gezet worden. 

6. De aanvragende partij verwerkt het antwoordbericht. 

7. De systeembeheerder zet het resultaat klaar om opgehaald te worden. 

### Ophalen resultaat

Bijlage B1150: Subprocesplaat SP0020 KA – Ophalen resultaat

1. De aanvragende partij dient een ‘verzoek ophalen resultaat’ in. 

2. De systeembeheerder voert een authenticatie en validatie uit voor het ‘verzoek ophalen resultaat’ van de aanvragende partij. Hierbij beoordeelt de systeembeheerder de aanvraag ‘verzoek ophalen resultaat’ op de volgende punten: 

   - a. Voldoet de waarde in het ‘verzoek ophalen resultaat’ aan de eisen die door het protocol worden gesteld? 

   - b. Komt de EAN-code van de verzoekende partij overeen met het gebruikte beveiligingscertificaat? 

   - c. Is de verzoekende partij geautoriseerd? 

   - d. Is de geadresseerde systeembeheerder bekend? 

   - e. Kan het bericht bij de geadresseerde systeembeheerder afgeleverd worden? 

3. Indien de systeembeheerder het ‘verzoek ophalen resultaat’ niet kan verwerken, verstuurt systeembeheerder een afwijzing naar de aanvragende partij. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. De waarde in het verzoek voldoet niet aan de eisen die door het protocol gesteld worden. 

   - b. EAN-code verzoekende partij komt niet overeen met het certificaat. 

   - c. De verzoekende partij is niet geautoriseerd. 

   - d. EAN-code systeembeheerder onbekend. 

   - e. Bericht kan niet bij de systeembeheerder afgeleverd worden. 

4. De aanvragende partij verwerkt de afwijzing. 

5. Indien de systeembeheerder het ‘verzoek ophalen resultaat’ van de aanvragende partij kan verwerken, dan beantwoordt hij het verzoek naar de aanvragende partij met de beschikbare meetgegevens. 

6. De aanvragende partij verwerkt het antwoordbericht. 

## 4.28.3 Termijnen KA

- a. Voor verzoeken via het batchkanaal geldt dat wanneer deze op dag 1 (tussen 00:00 – 24:00 uur) worden ingediend, antwoordberichten uiterlijk om 23:00 uur op dag 2 beschikbaar dienen te zijn. 

- b. De antwoordberichten, die door de systeembeheerder zijn klaargezet, moeten binnen 10 dagen opgehaald worden door de partij die de verzoeken heeft ingediend. 

- c. Specifiek voor ODA’s geldt: 

   - i. De Assuranceverklaring moet jaarlijks uiterlijk 31 maart worden verstrekt aan de systeembeheerder en de gegevensuitwisselingsentiteit. 

   - ii. Indien niet op tijd een Assuranceverklaring wordt verstrekt dan worden geen meetgegevens meer ter beschikking gesteld voor nieuw door de ODA aangemelde allocatiepunten. 

   - iii. Indien op 15 mei van dat jaar, na aanmaning door systeembeheerder of gegevensuitwisselingsentiteit, nog geen Assuranceverklaring is verstrekt, zullen in het geheel geen meetgegevens meer beschikbaar worden gesteld aan de betreffende ODA. 

   - iv. Specifiek voor een ODA die voor het eerst actief wordt in het systeemgebied van een systeembeheerder: Uiterlijk vier maanden na de eerste aanvraag van meetgegevens geeft de ODA op verzoek van de systeembeheerder of gegevensuitwisselingsentiteit een Assuranceverklaring af. 

## 4.28.4 Gegevensuitwisseling KA

### Dataverzoek

|**Dataverzoek**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|V|Ja|Ja|1|Door de aanvragende partij verstrekte referentie bedoeld om de<br>terugkoppeling van de systeembeheerder te kunnen herleiden tot het<br>verzoek.|
|Datum|V|Ja|Ja|1|Datum waarvoor meetgegevens worden aangevraagd.|
|Procescode|V|Ja|Ja|1|Dagovergangmeterstand/intervalmeterstand/<br>maandovergangmeterstand|

### Dataverzoek afwijzen

|**Afwijzing dataverzoek**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Afwijsreden|V|Ja|Ja|1|Code van de reden van de afwijzing, de mogelijke afwijsredenen zijn:<br>•<br>De waarde in het verzoek voldoet niet aan de eisen die door het<br>protocol gesteld worden;<br>•<br>EAN-code verzoekende partij komt niet overeen met het certificaat;<br>•<br>De verzoekende partij is niet geautoriseerd;<br>•<br>EAN-code systeembeheerder onbekend;<br>•<br>Bericht kan niet bijde systeembeheerder afgeleverd worden.|
|Toelichting afwijsreden|O|Ja|Ja|1|Toelichting op de reden van afwijzing|

### Antwoordbericht resultaat dataverzoek

|**Antwoordbericht resultaat dat**|**averzoek**|||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|V|Ja|Ja|1|Door de aanvragende partij verstrekte referentie bedoeld om de<br>terugkoppeling van de S systeembeheerder te kunnen herleiden tot het<br>verzoek|
|Procescode|V|Ja|Ja|1|Dagovergangmeterstand/intervalmeterstand/<br>maandovergangmeterstand|
|Datum|O|Ja|Ja|1|Datum waarvoor meetgegevens werden aangevraagd|
|**Meetinrichting:**|||||**1 per allocatiepunt**|
|Meetinrichtingnummer|V|Ja|Ja|1|Nummer van de meetinrichting waarop de opgeleverde meterstanden<br>betrekkinghebben|
|**Telwerk:**|||||n per meetinrichting|
|Telwerkidentificatie|A|O|Ja|1|Telwerkidentificatie. Verplicht voor elektriciteit. Bij gas wordt<br>gebruikgemaakt van een enkel telwerk zonder teruglevering.|
|Meeteenheid|V|Ja|Ja|1|Van een meetinrichting wordt per telwerk de meeteenheid vastgelegd|
|**Meterstand:**|||||1 per telwerk per timestamp|
|Timestamp|V|Ja|Ja|1|De datum en tijd waarop de meterstand betrekking heeft|
|Meterstand|O|Ja|Ja|1|Meterstand, indien beschikbaar; de op het opgegeven tijdstip gemeten<br>waarde|

### Afwijzing dataverzoek

|**Afwijzing dataverzoek**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|V|Ja|Ja|1|Door de aanvragende partij verstrekte referentie bedoeld om de<br>terugkoppeling van de systeembeheerder te kunnen herleiden tot het<br>verzoek|
|Procescode|V|Ja|Ja|1|Dagovergangmeterstand/intervalmeterstand/<br>maandovergangmeterstand|
|Datum|V|Ja|Ja|1|Datum waarvoor meetgegevens werden aangevraagd|
|Afwijsreden|V|Ja|Ja|1|Code van de reden van de afwijzing, de mogelijke afwijsredenen zijn:<br>•<br>De waarde in het verzoek voldoet niet aan de eisen die door het<br>protocol gesteld worden;<br>•<br>EAN-code verzoekende partij komt niet overeen met het certificaat;<br>•<br>De verzoekende partij is niet geautoriseerd;<br>•<br>EAN-code systeembeheerder onbekend;<br>•<br>Bericht kan niet bij de systeembeheerder afgeleverd worden;<br>•<br>De aanvragende partij is niet geauthenticeerd;<br>•<br>De EAN-code van het allocatiepunt is onbekend op gevraagde<br>datum;<br>•<br>Geen meetinrichting met communicatiefunctionaliteit op de EAN-<br>code van het allocatiepunt op gevraagde datum;<br>•<br>De verzoekende partij is niet geautoriseerd;<br>•<br>Gevraagde meetgegevens niet beschikbaar: meetinrichting in<br>deploymentfase;<br>•<br>Datum voor gevraagde gegevens in de toekomst, meterstanden nog<br>niet beschikbaar;<br>•<br>Datum van gevraagde meetgegevens te oud, meterstanden niet<br>meer beschikbaar;|

|**Afwijzing dataverzoek**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
||||||•<br>Gevraagde meetgegevens niet beschikbaar, meetinrichting tijdelijk<br>in storing;<br>•<br>Dit specifieke verzoek kan niet worden uitgevoerd door de<br>meetinrichting;<br>•<br>Gevraagde meetgegevens niet beschikbaar: storing bekend en in<br>behandeling;<br>•<br>Gevraagde meetgegevens niet beschikbaar: grootschalige storing;<br>•<br>De<br>meetinrichting<br>met<br>communicatiefunctionaliteit<br>staat<br>administratief op uit;<br>•<br>Er hangt een technisch niet op afstand uitleesbare meetinrichting<br>met communicatiefunctionaliteit;<br>•<br>De aanvragende partij is niet gemandateerd, omdat de autorisatie<br>is beëindigd n.a.v. wijzigingvan de contractant ophet allocatiepunt.|
|Toelichting afwijsreden|O|Ja|Ja|1|Toelichting op de reden van afwijzing|
