# 4.43 Aanpassen meetmethode GA gas in AR op verzoek van MV


## 4.43.1 Procesafspraken

- a. De meetverantwoordelijke partij stuurt het verzoek in als hij vaststelt dat er een geschikte telemetriegrootverbruikmeetinrichting aanwezig is voor een allocatiepunt waarbij de meetmethode niet op telemetrie staat in het aansluitingenregister. 

## 4.43.2 Procesbeschrijving

Bijlage B1171: Subprocesplaat zonder SP-code (§4.43.2) GA

1. De meetverantwoordelijke partij plaatst een telemetriegrootverbruikmeetinrichting of stelt vast dat er een telemetriegrootverbruikmeetinrichting aanwezig is op een allocatiepunt die administratief in het aansluitingenregister nog de meetmethode TMT heeft. Op dat moment heeft de meetverantwoordelijke partij de mogelijkheid, bijv. op verzoek van de aangeslotene, om de meetmethode aan te laten passen in het aansluitingenregister. Dit doet de meetverantwoordelijke partij middels een serviceverzoek aan de systeembeheerder. In het verzoek geeft de meetverantwoordelijke partij aan voor welke allocatiepunten de meetmethode moet worden aangepast. 

2. De systeembeheerder controleert het verzoek van de meetverantwoordelijke partij door voor ieder allocatiepunt in het verzoek te controleren of: 

   - a. De opvraag compleet en syntactisch correct is; 

   - b. Het allocatiepunt bekend is in het aansluitingenregister van de systeembeheerder; 

   - c. Het allocatiepunt een grote aansluiting gas betreft; 

   - d. Het geen gesloopt allocatiepunt betreft; 

   - e. De meetverantwoordelijke partij de actuele meetverantwoordelijke partij is voor het allocatiepunt; 

   - f. De meetmethode niet reeds op TMT staat. 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder het ‘verzoek aanpassen meetmethode’ af, en verstuurt de systeembeheerder een afwijsbericht naar de meetverantwoordelijke partij uiterlijk de 10de werkdag na ontvangst van het verzoek ‘aanpassen meetmethode’. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. c. Het betreft geen allocatiepunt op een grote aansluiting gas. 

   - d. Het betreft een gesloopt allocatiepunt. 

   - e. De meetverantwoordelijke partij staat niet als actuele meetverantwoordelijke partij geregistreerd op het allocatiepunt. 

   - f. De melding houdt geen wijziging in van de meetmethode ten opzichte van de huidige meetmethode. 

4. De meetverantwoordelijke partij ontvangt en verwerkt de afwijzing. 

5. De systeembeheerder koppelt, indien de controle bij processtap 2 een positief resultaat oplevert, terug aan de meetverantwoordelijke partij dat het verzoek is goedgekeurd en geeft daarbij aan per welke datum de meetmethodewijziging geëffectueerd wordt in het aansluitingenregister, waarbij dit zoveel als mogelijk op de eerste kalenderdag van de maand wordt uitgevoerd. 

6. De meetverantwoordelijke partij ontvangt de goedkeuring en verwerkt de mutatie in haar administratie. 

7. De systeembeheerder past de meetmethode aan in het aansluitingenregister. 

8. De meetverantwoordelijke partij waarvoor de wijziging is doorgevoerd ontvangt de stamgegevens en verwerkt de stamgegevens in de decentrale administratie en processen. 

9. De leverancier ontvangt de stamgegevens en verwerkt de stamgegevens in de decentrale administratie en processen. 

10. De balanceringsverantwoordelijke ontvangt de stamgegevens en verwerkt de stamgegevens in de decentrale administratie en processen. 

## 4.43.3 Termijnen

- a. Een afwijzing of goedkeuring van ‘melding verzoek aanpassen meetmethode’ wordt binnen 10 werkdagen verstuurd. De mutatie in het aansluitingenregister wordt doorgevoerd op een tussen de meetverantwoordelijke partij en systeembeheerder overeengekomen datum. 

## 4.43.4 Gegevensuitwisseling

### Melding verzoek aanpassen meetmethode van meetverantwoordelijke partij naar systeembeheerder

|**Gegeven**|**Toelichting**|
|---|---|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Distributiesysteembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt|
|Meetverantwoordelijke partij|Unieke identificatie van de meetverantwoordelijke partij van het allocatiepunt (indiener<br>verzoek)|

**Afwijzing vanuit systeembeheerder naar meetverantwoordelijke partij** 

|**Gegeven**|**Toelichting**|
|---|---|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Systeembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt (verzender afwijzing)|
|Meetverantwoordelijke partij|Unieke identificatie van de meetverantwoordelijke partij van het allocatiepunt|
|Afwijsreden|Indicatie van de reden waarom de melding is afgewezen:<br>• Onvolledige melding of syntactische fout.<br>• Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder.<br>• Het betreft geen allocatiepunt op een grote aansluiting gas.<br>• Het betreft een gesloopt allocatiepunt.<br>• De meetverantwoordelijke partij staat niet als actuele meetverantwoordelijke partij<br>geregistreerd op het allocatiepunt.<br>• De melding houdt geen wijziging in van de meetmethode ten opzichte van de huidige<br>meetmethode.|

**Bevestiging vanuit systeembeheerder naar meetverantwoordelijke partij** 

|**Gegeven**|**Toelichting**|
|---|---|
|Allocatiepunt|Unieke identificatie van het allocatiepunt|
|Systeembeheerder|Unieke identificatie van de systeembeheerder van het allocatiepunt (verzender afwijzing)|
|Meetverantwoordelijke partij|Unieke identificatie van de meetverantwoordelijke partij van het allocatiepunt|
|Verwachte effectuering|Verwachte datum dat wijziging geëffectueerd wordt in het aansluitingenregister|
