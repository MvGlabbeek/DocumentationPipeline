# 4.34 SP0071 Eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt


## 4.34.1 Procesafspraken KA

- a. De systeembeheerder probeert tenminste een keer per 3 dagen de dagovergangmeterstanden uit de meetinrichting met communicatiefunctionaliteit uit te lezen en slaat deze voor 24 maanden op. Reden dat de systeembeheerder dit opslaat is dat dagovergangmeterstanden tot maximaal de laatste 40 kalenderdagen worden opgeslagen in de meetinrichting met communicatiefunctionaliteit. De meetgegevens die de leverancier in dit kader kan opvragen betreft alleen dagovergangmeterstanden. 

- b. **Dagovergangmeterstand** 

   - De dagovergangmeterstand is de meterstand op het moment van dagovergang (00:00 uur) horend bij de datum van de dag die op dat moment begint. De dagovergangmeterstand voor elektriciteit bestaat uit vier waarden waarmee het volume voor normaaluren en laaguren voor levering en teruglevering wordt geregistreerd. Voor gas bestaat de dagovergangmeterstand uit een enkele waarde. 

- c. De leverancier vraagt op verzoek van de eindafnemer eenmalig de historische dagovergangmeterstanden van een allocatiepunt op. De opvraag heeft betrekking op een door de leverancier aan te duiden periode. 

Op basis van de door de leverancier ingediende opvraag verstrekt de systeembeheerder de in de database beschikbare dagovergangmeterstanden voor zover de opvragende marktpartij in het aansluitingenregister op dit allocatiepunt geregistreerd stond op de dagen binnen de door de leverancier aangegeven periode. Hierbij controleert de systeembeheerder of er gedurende de door de leverancier aangegeven periode een SVEL (Switchen, Verhuizen, Einde Levering)-proces plaatsgevonden heeft op het betreffende allocatiepunt. Wanneer dit het geval is levert de systeembeheerder de dagovergangmeterstand vanaf de datum van het meest recente SVEL-proces tot en met de einddatum van de aangegeven periode. Is dit niet het geval, dan levert de systeembeheerder de dagovergangmeterstand van de gehele door de leverancier aangegeven periode. De systeembeheerder levert in dit proces geen dagovergangmeterstand ouder dan 24 maanden. De systeembeheerder controleert niet of er een klantvraag is voor deze periode; deze verantwoordelijkheid ligt bij de aanvragende leverancier. Wanneer op de einddatum van de door de leverancier opgegeven periode een SVEL-proces heeft plaatsgevonden, wordt het SVEL-proces van deze datum genegeerd bij de hierboven omschreven controle. 

## 4.34.2 Procesbeschrijving KA

Bijlage B1162: Subprocesplaat SP0071 KA

1. De opvragende marktpartij dient een ‘verzoek eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt in. 

   - a. Dit verzoek moet bevatten: 

      - i. EAN-code van het allocatiepunt; 

      - ii. De begin- en einddatum (tot-en-met-datum) van de periode waarover de leverancier meetgegevens wil ontvangen. 

2. De systeembeheerder verwerkt het ‘Verzoek eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt’ van de aanvragende leverancier 

3. De systeembeheerder beantwoordt het verzoek met een antwoordbericht. Dit antwoordbericht bevat de voor de opvragende marktpartij beschikbare dagovergangmeterstanden binnen de verzochte periode. De systeembeheerder controleert hierbij of gedurende de door de leverancier opgegeven periode een SVEL-proces heeft plaatsgevonden. Wanneer dit het geval is levert de systeembeheerder de dagovergangmeterstanden vanaf de datum van het meest recente SVEL-proces tot en met de einddatum van de aangegeven periode. Is dit niet het geval, dan levert de systeembeheerder de dagovergangmeterstanden van de gehele door de leverancier aangegeven periode. De systeembeheerder levert in dit proces geen dagovergangmeterstanden ouder dan 24 maanden. De systeembeheerder controleert niet of er een klantvraag is voor deze periode; deze verantwoordelijkheid ligt bij de aanvragende leverancier. 

   - a. Wanneer op de einddatum van de door de leverancier opgegeven periode een SVELproces heeft plaatsgevonden, wordt het SVEL-proces van deze datum genegeerd bij de hierboven omschreven controle. 

4. De opvragende marktpartij verwerkt het antwoordbericht. 

## 4.34.3 Termijnen KA

Voor dataverzoeken geldt dat het antwoord op een verzoek synchroon volgt. 

## 4.34.4 Gegevensuitwisseling KA

### Verzoek eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt

|**Verzoek eenmalig aanleve**|**ren hist**|**orische d**|**agoverg**|**angmet**|**erstanden van een allocatiepunt**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code leverancier|V|Ja|Ja|1|ID van de aanvragende leverancier|
|EAN-code allocatiepunt|V|Ja|Ja|1|ID van het allocatiepunt waarvoor de leverancier de aanvraag doet|
|Referentie|O|Ja|Ja|1|Door de aanvragende leverancier verstrekte referentie bedoeld om de terugkoppeling<br>van de systeembeheerder te kunnen herleiden tot het verzoek|
|Startdatum|V|Ja|Ja|1|Vanaf datum van de periode waarover meterstanden opgevraagd worden|
|Einddatum|V|Ja|Ja|1|Tot-en-met datum van de periode waarover meterstanden opgevraagd worden|

### Antwoordbericht verzoek eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt

|**Antwoordbericht verzoek e**|**enmali**|**g aanlev**|**eren his**|**torische**|**dagovergangmeterstanden van een allocatiepunt**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1|ID van het betreffende allocatiepunt|
|Referentie|A|Ja|Ja|1|Door de aanvragende leverancier verstrekte referentie bedoeld om de terugkoppeling<br>van de systeembeheerder te kunnen herleiden tot het verzoek|
|**Meetinrichting: (n per alloc**|**atiepu**|**nt)**|||Wanneer er tijdens de opgegeven periode een of meerdere wissel(s)van de<br>meetinrichting hebben plaatsgevonden worden meerdere meetinrichtingnummers<br>meegegeven(aantal wissels van de meetinrichting+1)|
|Meetinrichtingnummer|A|Ja|Ja|1|Nummer van de meetinrichting waarop de opgeleverde meterstanden betrekking<br>hebben. Verplicht indien meterstanden van de betreffende meetinrichting worden<br>opgeleverd.|
|**Telwerk: (n per meter)**|||||Voor elektriciteit 4, voor gas 1.|
|Telwerkidentificatie|V|Ja|Ja|1||
|Meeteenheid|V|Ja|Ja|1|Van een meterinrichting wordt per telwerk de meeteenheid vastgelegd|
|**Meterstand:**|||||1 per telwerk per timestamp|
|Timestamp|V|Ja|Ja|1|De datum en tijd waarop de dagovergangmeterstand betrekking heeft|
|Dagovergangmeterstand|V|Ja|Ja|1|Dagovergangmeterstand, indien beschikbaar; de op het opgegeven tijdstip gemeten<br>waarde|
