# 4.24 SP0011 Indienen ‘melding wijzigen gegevens aangeslotene


## 4.24.1 Procesafspraken KA

- a. Het proces Wijzigen gegevens aangeslotene is niet bedoeld voor het wijzigen van de identiteit van de aangeslotene. Als er sprake is van een nieuwe aangeslotene dient het proces Inhuizing gebruikt te worden. 

- b. Een ‘melding wijzigen gegevens aangeslotene’ mag alleen ingediend worden door de leverancier die als actuele leverancier op het primaire allocatiepunt staat geregistreerd. 

- c. Bij het uitvoeren van een wijziging gegevens aangeslotene wordt geen meterstand vastgesteld. d. De leverancier vult het bericht met de actuele gegevens van de aangeslotene conform de afspraken in paragraaf 2.2 Rollen en verantwoordelijkheden, sub paragraaf 2.2.2 Kleine aansluitingen. De systeembeheerder neemt deze gegevens over in het aangeslotenenregister. De leverancier levert alle op dat moment in haar administratie aanwezige gegevens aan (dus ook de gegevens die niet gewijzigd zijn). De systeembeheerder overschrijft met deze aanlevering alle dan aanwezige gegevens in het register. 

## 4.24.2 Procesbeschrijving KA

Bijlage B1143: Subprocesplaat SP0011 KA

1. De initiërende leverancier verstuurt een ‘melding wijzigen gegevens aangeslotene’ één werkdag voor de mutatiedatum naar de systeembeheerder. 

2. De systeembeheerder beoordeelt de melding op de volgende punten: 

   - a. Is de ‘melding wijzigen gegevens aangeslotene’ volledig en syntactisch correct? 

   - b. Is het allocatiepunt bekend in het aansluitingenregister van de betreffende systeembeheerder? 

   - c. Is de leverancier geregistreerd als actuele leverancier op het allocatiepunt? 

   - d. Is het allocatiepunt een allocatiepunt op een kleine aansluiting? 

   - e. Betreft het een primair allocatiepunt? 

3. Indien één van de controles een negatief resultaat oplevert, wijst de systeembeheerder de ‘melding wijzigen gegevens aangeslotene’ af, en verstuurt de systeembeheerder een afwijsbericht naar de leverancier uiterlijk de werkdag na ontvangst ‘melding wijziging gegevens aangeslotene. De afwijsredenen die de systeembeheerder kan hebben zijn: 

   - a. Onvolledige melding of syntactische fout. 

   - b. Het allocatiepunt is onbekend in het aansluitingenregister van de systeembeheerder. 

   - c. De leverancier staat niet als actuele leverancier geregistreerd op het allocatiepunt. 

   - d. Het allocatiepunt is geen allocatiepunt op een kleine aansluiting. 

   - e. Het allocatiepunt is geen primair allocatiepunt. 

4. De leverancier ontvangt en verwerkt de afwijzing. 

5. Indien alle controles een positief resultaat opleveren, accepteert de systeembeheerder de ‘melding wijziging gegevens aangeslotene’ van de leverancier en verstuurt de systeembeheerder de bevestiging naar de leverancier uiterlijk één werkdag na ontvangst van de ‘melding wijziging gegevens aangeslotene’. 

6. De leverancier ontvangt en verwerkt de ‘melding wijziging gegevens aangeslotene. 

7. De systeembeheerder verwerkt de melding van de leverancier in het aangeslotenenregister. 

## 4.24.3 Termijnen KA

Een ‘melding wijzigen gegevens aangeslotene’ wordt direct door de systeembeheerder beoordeeld, waarbij uiterlijk één werkdag na ontvangst van de ‘melding wijzigen gegevens aangeslotene’ de leverancier wordt geïnformeerd over de verwerking van de wijzigingsmelding (bevestiging of indien van toepassing afwijzing). 

## 4.24.4 Gegevensuitwisseling

### Melding

|**Melding wijzigen gegevens aangesl**|**otene**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|n.v.t.|n.v.t.|Ja|Ja|1||
|Referentie|O|n.v.t.|n.v.t.|Ja|Ja|1|Referentie van de leverancier|
|EAN-code systeembeheerder|V|n.v.t.|n.v.t.|Ja|Ja|1||
|EAN-code leverancier|V|n.v.t.|n.v.t.|Ja|Ja|1||
|Type aangeslotene|V|n.v.t.|n.v.t.|Ja|Ja|1|“huishoudelijke<br>eindafnemer”<br>of<br>“geen<br>huishoudelijke eindafnemer” of ‘’onbekend’’|
|Voorletters aangeslotene|O|n.v.t.|n.v.t.|Ja|Ja|1|Van toepassing wanneer er sprake is van een<br>“huishoudelijke eindafnemer”. Verplicht leeg voor<br>een “geen huishoudelijke eindafnemer”.|
|Tussenvoegsel aangeslotene|O|n.v.t.|n.v.t.|Ja|Ja|1|Van toepassing wanneer er sprake is van een<br>“huishoudelijke eindafnemer”. Verplicht leeg voor<br>een “geen huishoudelijke eindafnemer”.|
|Voornaam aangeslotene|O|n.v.t.|n.v.t.|Ja|Ja|1|Van toepassing wanneer er sprake is van een<br>“huishoudelijke eindafnemer”. Verplicht leeg voor<br>een “geen huishoudelijke eindafnemer”.|
|Naam aangeslotene|V|n.v.t.|n.v.t.|Ja|Ja|1|Bij een “huishoudelijke eindafnemer” wordt hier de<br>achternaam ingevuld. Bij een “geen huishoudelijke<br>eindafnemer” wordt de bedrijfs- of instellingsnaam<br>hier ingevuld.|
|KvK-nummer|O|n.v.t.|n.v.t.|Ja|Ja|1|Van toepassing wanneer er sprake is van een “geen<br>huishoudelijke eindafnemer”. Verplicht leeg voor<br>“huishoudelijke eindafnemers”.|
|Geboortedatum|O|n.v.t.|n.v.t.|Ja|Ja|1|Van toepassing wanneer er sprake is van een “geen<br>huishoudelijke eindafnemer”. Verplicht leeg voor<br>“huishoudelijke eindafnemers”.|
|Telefoonnummer aangeslotene|O|n.v.t.|n.v.t.|Ja|Ja|1||
|Emailadres aangeslotene|O|n.v.t.|n.v.t.|Ja|Ja|1||
|_Correspondentieadres:_||||||||
|Straatnaam / Postbus|O|n.v.t.|n.v.t.|Ja|Ja|1||
|Huisnummer / Postbusnummer|O|n.v.t.|n.v.t.|Ja|Ja|1||
|Huisnummer-toevoeging|O|n.v.t.|n.v.t.|Ja|Ja|1||
|Postcode|O|n.v.t.|n.v.t.|Ja|Ja|1||
|Woonplaats|O|n.v.t.|n.v.t.|Ja|Ja|1||
|Land|O|n.v.t.|n.v.t.|Ja|Ja|1||

### Bevestiging

|**Bevestiging wijziging gegevens aang**|**eslotene**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|n.v.t.|n.v.t.|Ja|Ja|1||

|**Bevestiging wijziging gegevens aa**|**ngeslotene**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|Transactiedossiernummer|V|n.v.t.|n.v.t.|Ja|Ja|1||
|Referentie|A|n.v.t.|n.v.t.|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|EAN-code systeembeheerder|V|n.v.t.|n.v.t.|Ja|Ja|1||
|EAN-code leverancier|V|n.v.t.|n.v.t.|Ja|Ja|1||

### Afwijzing

|**Afwijzing wijziging gegevens aang**|**eslotene**|||||||
|---|---|---|---|---|---|---|---|
|**Gegeven**|**KV**|**GA**|**A1**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|n.v.t.|n.v.t.|Ja|Ja|1||
|Transactiedossiernummer|V|n.v.t.|n.v.t.|Ja|Ja|1||
|Referentie|A|n.v.t.|n.v.t.|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|EAN-code systeembeheerder|V|n.v.t.|n.v.t.|Ja|Ja|1||
|EAN-code leverancier|V|n.v.t.|n.v.t.|Ja|Ja|1||
|Afwijsreden|V|n.v.t.|n.v.t.|Ja|Ja|n|Indicatie waarom de melding is afgewezen:<br>•<br>Onvolledige melding of syntactische fout.<br>•<br>Het<br>allocatiepunt<br>is<br>onbekend<br>in<br>het<br>aansluitingenregister van de systeembeheerder.<br>•<br>De leverancier staat niet als actuele leverancier<br>geregistreerd op het allocatiepunt.<br>•<br>Het allocatiepunt is geen allocatiepunt op een<br>kleine aansluiting.<br>•<br>De meldingbetreftgeenprimair allocatiepunt.|
|Toelichting afwijsreden|O|n.v.t.|n.v.t.|Ja|Ja|n||
