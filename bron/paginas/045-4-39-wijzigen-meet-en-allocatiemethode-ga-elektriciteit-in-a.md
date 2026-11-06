# 4.39 Wijzigen meet- en allocatiemethode GA elektriciteit in aansluitingenregister op verzoek van MV


## 4.39.1 Procesafspraken GA

- a. De meetverantwoordelijke partij stuurt het verzoek in als hij vaststelt dat er een geschikte telemetriemeetinrichting voor allocatiepunten op een grote aansluiting elektriciteit aanwezig is voor een allocatiepunt waarbij de meet- en allocatiemethode niet op telemetrie staat in het aansluitingenregister. 

## 4.39.2 Procesbeschrijving GA

Bijlage B1167: Subprocesplaat zonder SP-code (§4.39.2) GA

1. De meetverantwoordelijke partij plaatst een telemetriegrootverbruikmeetinrichting of stelt vast dat er een telemetriegrootverbruikmeetinrichting aanwezig is op een allocatiepunt dat administratief in het aansluitingenregister nog niet op meet- en allocatiemethode “TMT” staat. Op dat moment heeft de meetverantwoordelijke partij de mogelijkheid, bijv. op verzoek van de aangeslotene, om de meet- en allocatiemethode aan te laten passen in het aansluitingenregister. Dit kan de meetverantwoordelijke partij doen middels een serviceverzoek aan de systeembeheerder. In het verzoek geeft de meetverantwoordelijke partij aan voor welke EANcode(s) de meet- en allocatiemethode mag worden aangepast. 

2. De systeembeheerder controleert het verzoek van de meetverantwoordelijke partij door te controleren of de meetverantwoordelijke partij voor de doorgegeven EAN-code(s) inderdaad de meetverantwoordelijke partij is op het allocatiepunt. 

3. De systeembeheerder koppelt, indien de controle bij processtap 2 een negatief resultaat oplevert, terug aan de meetverantwoordelijke partij dat het verzoek is afgewezen; 

4. De meetverantwoordelijke partij ontvangt en controleert de afwijzing en dient, indien door hem gewenst, een nieuw verzoek in. 

5. De systeembeheerder koppelt, indien de controle bij processtap 2 een positief resultaat oplevert, terug aan de meetverantwoordelijke partij dat het verzoek is goedgekeurd en geeft daarbij aan per welke datum de meet- en allocatiemethode wijziging geëffectueerd zal worden in het aansluitingenregister, waarbij dit zoveel als mogelijk op de eerste kalenderdag van de maand wordt uitgevoerd. 

6. De meetverantwoordelijke partij ontvangt de goedkeuring en verwerkt indien gewenst de mutatie in haar administratie. 

7. De systeembeheerder past de meet- en allocatiemethode aan in het aansluitingenregister. 

8. De meetverantwoordelijke partij waarvoor de wijziging is doorgevoerd ontvangt de stamgegevens wijzigingen via het reguliere berichtenverkeer en verwerkt de stamgegevens wijzigingen in de decentrale administratie en processen. 

9. De betrokken leverancier ontvangt de stamgegevens wijzigingen via het reguliere berichtenverkeer en verwerkt de stamgegevens wijzigingen in de decentrale administratie en processen. 

10. De betrokken balanceringsverantwoordelijke ontvangt de stamgegevens wijzigingen via het reguliere berichtenverkeer en verwerkt de stamgegevens wijzigingen in de decentrale administratie en processen. 

## 4.39.3 Termijnen GA

- a. Een ‘melding verzoek aanpassen meet- en allocatiemethode’ wordt ingediend op de mutatiedatum zelf. 

- b. Een afwijzing of goedkeuring van ‘melding verzoek aanpassen meet- en allocatiemethode’ wordt binnen 10 werkdagen verstuurd.. De mutatie in het aansluitingenregister wordt doorgevoerd op een tussen meetverantwoordelijke partij en systeembeheerder overeengekomen datum. 

## 4.39.4 Gegevensuitwisseling

### Verzoek aanpassen meet- en allocatiemethode van meetverantwoordelijke partij naar systeembeheerder

|**Gegeven**|**Toelichting**|
|---|---|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Systeembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt|
|Meetverantwoordelijke partij|Unieke identificatie van de meetverantwoordelijke partij van het allocatiepunt (indiener<br>verzoek)|

**Afwijzing vanuit systeembeheerder naar meetverantwoordelijke partij** 

|**Gegeven**|**Toelichting**|
|---|---|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Systeembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt (verzender afwijzing)|
|Meetverantwoordelijke partij|Unieke identificatie van de meetverantwoordelijke partij van het allocatiepunt|
|Afwijsreden|Indicatie van de reden waarom de melding is afgewezen:<br>• Onvolledige melding of syntactische fout.<br>• Het betreft geen aansluiting elektriciteit.<br>• Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder.<br>• De meetverantwoordelijke partij staat niet als actuele meetverantwoordelijke partij<br>geregistreerd op het allocatiepunt.<br>• De melding houdt geen wijziging in van de allocatiemethode ten opzichte van de huidige<br>allocatiemethode.|

**Bevestiging van systeembeheerder naar meetverantwoordelijke partij** 

|**Gegeven**|**Toelichting**|
|---|---|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Systeembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt (verzender<br>bevestiging)|
|Meetverantwoordelijke partij|Unieke identificatie van de meetverantwoordelijke partij van het allocatiepunt|
|Verwachte effectuering|Verwachte datum dat wijziging geëffectueerd wordt in het aansluitingenregister|
