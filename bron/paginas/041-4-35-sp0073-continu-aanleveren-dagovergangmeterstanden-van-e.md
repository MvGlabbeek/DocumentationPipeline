# 4.35 SP0073 Continu aanleveren dagovergangmeterstanden van een allocatiepunt


## 4.35.1 Procesafspraken KA

   - a. De systeembeheerder leest ten minste een keer per drie dagen de dagovergangmeterstanden uit de meetinrichting met communicatie functionaliteit uit en slaat deze voor tenminste 24 maanden op. Reden dat de systeembeheerder dit opslaat is dat dagovergangmeterstanden tot maximaal de laatste 40 kalenderdagen worden opgeslagen in de meetinrichting met communicatie functionaliteit. De meetgegevens die de leverancier in dit kader kan opvragen betreffen alleen dagovergangmeterstanden. 

### Dagovergangmeterstand

- **b.** De dagovergangmeterstand is de meterstand op het moment van dagovergang (00:00 uur) horend bij de datum van de dag die op dat moment begint. De dagovergangmeterstand voor elektriciteit bestaat uit vier waarden waarmee het volume voor normaaluren en laaguren voor levering en teruglevering wordt geregistreerd. Voor gas bestaat de dagovergangmeterstand uit een enkele waarde. 

- c. De leverancier vraagt de systeembeheerder een continue aanlevering te starten van de dagovergangmeterstanden van een allocatiepunt. 

- d. De systeembeheerder controleert niet of er een klantvraag ten grondslag ligt aan het verzoek tot starten van de continue aanlevering, deze verantwoordelijkheid ligt bij de leverancier. 

- e. Elke dagovergangmeterstand die door de systeembeheerder is verstrekt in het kader van de continue aanlevering van de dagovergangmeterstanden wordt in de database als zodanig aangemerkt en niet meer via deze dienst uitgeleverd. Gegevens die bij de leverancier verloren gaan kunnen door de leverancier met behulp van de dienst Eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt alsnog achterhaald worden. 

- f. De systeembeheerder zal de continue aanlevering beëindigen op verzoek van de leverancier. Ook zal de systeembeheerder de continue aanlevering proactief beëindigen in het geval van een SVEL-proces op of verwijdering van het betreffende allocatiepunt. De systeembeheerder stelt de leverancier via het reguliere berichtenverkeer van deze events op de hoogte. De systeembeheerder stelt de leverancier niet expliciet op de hoogte van de beëindiging van de continue aanlevering. De continue aanlevering wordt beëindigd per de datum van het proces dat aanleiding geeft tot beëindiging. 

- g. De leverancier ontvangt alle dagovergangmeterstanden die als zodanig vanaf de startdatum 

tot en met de beëindigingsdatum van de betreffende continue aanlevering in de meetinrichting met communicatiefunctionaliteit geregistreerd zijn via het proces van de continue aanlevering. 

Op basis van het door de leverancier ingediende verzoek antwoordt de systeembeheerder met een antwoordbericht. In geval van een positief antwoord start hij de continue aanlevering. 

## 4.35.2 Procesbeschrijving KA

Bijlage B1163: Subprocesplaat SP0073 KA

1. De opvragende marktpartij dient een ‘Verzoek starten continu aanleveren dagovergangmeterstanden van een allocatiepunt in. 

   - a. Het verzoek bevat ten minste de EAN-code van het allocatiepunt 

2. De systeembeheerder controleert het ‘Verzoek starten continu aanleveren dagovergangmeterstanden van het allocatiepunt’ van de opvragende marktpartij. Er wordt tenminste gecontroleerd of: 

   - a. De aanvragende leverancier geregistreerd staat op het betreffende allocatiepunt in het aansluitingenregister; 

   - b. De meetinrichting Administratief Aan staat; 

   - c. De meetinrichting technisch uitleesbaar is. 

3. De systeembeheerder antwoordt met een antwoordbericht: 

   - a. In geval van een positief resultaat van alle controles antwoordt de systeembeheerder met een antwoordbericht waarin hij aangeeft dat de continue aanlevering gestart wordt; 

   - b. In geval van een negatief resultaat van een of meer van de controles antwoordt de systeembeheerder met een antwoordbericht waarin de reden van het niet starten van de continue aanlevering vermeld wordt. 

4. De opvragende marktpartij verwerkt het antwoordbericht. 

5. De systeembeheerder start bij een positief antwoord de continue aanlevering uiterlijk de volgende kalenderdag. De dagovergangmeterstand van de dag van indienen van de aanvraag wordt na starten van de continue aanlevering ook via dat proces geleverd. 

## 4.35.3 Termijnen KA

Voor een startverzoek geldt dat het antwoord synchroon volgt. Voor het opvragen van de gegevens geldt dat de leverancier de klaargezette gegevens op moet halen middels de dienst ‘Ophalen gereedstaande dagovergangmeterstanden’. De continue aanlevering van dagovergangmeterstanden van het allocatiepunt wordt uiterlijk de volgende kalenderdag gestart. Wanneer de aanvragende leverancier ook de historische dagovergangmeterstanden van het allocatiepunt aan de klant moet leveren dient hij deze apart op te vragen via de dienst “Eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt”. 

## 4.35.4 Gegevensuitwisselingen KA

### Verzoek starten continue aanlevering dagovergangstanden van een allocatiepunt

|**Verzoek starten continue a**|**anlever**|**ing dag**|**overga**|**ngmete**|**rstanden van een allocatiepunt**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code leverancier|V|Ja|Ja|1|ID van de aanvragende leverancier|
|EAN-code allocatiepunt|V|Ja|Ja|1|ID van het allocatiepunt waarvoor de leverancier de aanvraag doet|
|Referentie|O|Ja|Ja|1|Door de aanvragende leverancier verstrekte referentie bedoeld om de<br>terugkoppeling van de systeembeheerder te kunnen herleiden tot het verzoek. Deze<br>referentie<br>wordt<br>ook<br>elke<br>keer<br>gekoppeld<br>aan<br>de<br>verstrekte<br>dagovergangmeterstanden in het antwoordbericht van de systeembeheerder in de<br>dienst ‘Ophalengereedstaande dagovergangmeterstanden’|

### Antwoordbericht verzoek starten continue aanlevering dagovergangmeterstanden van een allocatiepunt

|**Antwoordbericht verzoek**|**starten**|**continu**|**e aanle**|**vering d**|**agovergangmeterstanden van een allocatiepunt**|
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code leverancier|V|Ja|Ja|1|ID van de aanvragende leverancier|
|EAN-code allocatiepunt|V|Ja|Ja|1|ID van het allocatiepunt waarvoor de leverancier de aanvraag doet|
|Referentie|A|Ja|Ja|1|Door de aanvragende leverancier verstrekte referentie bedoeld om de<br>terugkoppelingvan de systeembeheerder te kunnen herleiden tot het verzoek|
|Response|V|Ja|Ja|1|Reactie op het ingediende verzoek. Mogelijke responsewaarden:<br>1.<br>Continue aanlevering wordt gestart;<br>2.<br>Er loopt al een continue aanlevering op dit allocatiepunt voor de aanvragende<br>leverancier;<br>3.<br>Leverancier<br>is<br>niet<br>geregistreerd<br>op<br>het<br>allocatiepunt<br>in<br>het<br>aansluitingenregister;<br>4.<br>Meetinrichting staat Administratief uit;<br>5.<br>Meetinrichtingis Technisch Niet Uitleesbaar.|
