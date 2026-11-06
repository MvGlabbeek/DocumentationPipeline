# 4.36 SP0072 Ophalen gereedstaande dagovergangmeterstanden


## 4.36.1 Procesafspraken KA

- a. De systeembeheerder zet de te leveren dagovergangmeterstanden klaar voor de aanvragende leverancier direct nadat deze zijn opgeslagen in de database; 

- b. De aanvragende leverancier haalt de dagovergangmeterstanden op een door hem te kiezen moment op door middel van het sturen van een verzoek; 

- c. Elke dagovergangmeterstand die door de systeembeheerder is verstrekt in het kader van de continue aanlevering van de dagovergangmeterstanden wordt in de database als zodanig aangemerkt en niet meer via deze dienst uitgeleverd. Gegevens die bij de leverancier verloren gaan kunnen door de leverancier met behulp van de dienst Eenmalig aanleveren historische dagovergangmeterstanden van een allocatiepunt alsnog achterhaald worden. 

## 4.36.2 Procesbeschrijving KV

Bijlage B1164: Subprocesplaat SP0072 KA

1. De opvragende marktpartij dient een ’ophaalverzoek gereedstaande dagovergangmeterstanden’ in; 

2. De systeembeheerder verwerkt het verzoek. 

3. De systeembeheerder reageert met een antwoordbericht met daarin de gereedstaande dagovergangmeterstanden. Wanneer er geen dagovergangmeterstanden gereed staan voor de aanvragende leverancier bevat het antwoordbericht geen meetgegevens (leeg bericht). 

4. De opvragende marktpartij verwerkt het antwoordbericht. 

## 4.36.3 Termijnen KA

Voor een ‘Ophaalverzoek gereedstaande dagovergangmeterstand’ geldt dat een antwoord synchroon volgt. 

## 4.36.4 Gegevensuitwisseling KA

### Ophaalverzoek gereedstaande dagovergangmeterstanden

|**Ophaalverzoek gereedsta**|**ande da**|**goverga**|**ngmete**|**rstande**|**n**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code leverancier|V|Ja|Ja|1|ID van de aanvragende leverancier|

### Antwoordbericht ophaalverzoek gereedstaande dagovergangmeterstanden

|**Antwoordbericht ophaalver**|**zoekg**|**ereedst**|**aande**|**dagover**|**gangmeterstanden**|
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n **|**Opmerking**|
|EAN-code leverancier|V|Ja|Ja|1|ID van de aanvragende leverancier|
|**Allocatiepunt(n per batch)**||||||
|EAN-code allocatiepunt|V|Ja|Ja|1|ID van het allocatiepunt waarop de betreffende set dagovergangmeterstanden<br>betrekkingheeft|
|Referentie|A|Ja|Ja|1|Door de aanvragende leverancier bij het Verzoek starten continue aanlevering<br>dagovergangmeterstanden van een allocatiepunt verstrekte referentie bedoeld om de<br>terugkoppeling van de systeembeheerder te kunnen herleiden tot de ingediende<br>aanvraag.|
|**Meetinrichting (n per alloca**|**tiepun**|**t):**|||Wanneer er tijdens de periode die in een batch uitgeleverd wordt een of meerdere<br>wissel(s) van de meetinrichting hebben plaatsgevonden worden meerdere<br>meternummers meegegeven(aantal wissels van de meetinrichting+1)|
|Meetinrichtingnummer|A|Ja|Ja|1|Nummer van de meetinrichting waarop de opgeleverde dagovergangmeterstanden<br>betrekking hebben. Verplicht indien dagovergangmeterstanden van de betreffende<br>meetinrichtingworden opgeleverd.|
|**Telwerk(n per meetinrichti**|**ng):**||||Voor elektriciteit 4,voorgas 1.|
|Telwerkidentificatie|V|Ja|Ja|1||
|Meeteenheid|V|Ja|Ja|1|Van een meetinrichting wordt per telwerk de meeteenheid meegestuurd (kWh voor<br>elektriciteit,m<sup>3</sup>voorgas)|
|**Meterstand:**|||||1per telwerkper timestamp|
|Timestamp|V|Ja|Ja|1|De datum en tijd waaropde dagovergangmeterstand betrekkingheeft|
|Dagovergangmeterstand|V|Ja|Ja|1|Dagovergangmeterstand, indien beschikbaar; de op het opgegeven tijdstip gemeten<br>waarde|
