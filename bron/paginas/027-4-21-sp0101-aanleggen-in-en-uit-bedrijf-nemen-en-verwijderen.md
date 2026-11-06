# 4.21 SP0101 Aanleggen, in- en uit bedrijf nemen en verwijderen allocatiepunt


## 4.21.1 Procesafspraken KA en GA

Deze procesafspraken gelden voor allocatiepunten op zowel grote als kleine aansluitingen. 

### Algemeen

- a. De processen ‘aanleggen, in bedrijf nemen, uit bedrijf nemen en verwijderen van een allocatiepunt’ omvatten een fysieke handeling en het administratief verwerken in het aansluitingenregister van de fysieke handeling. 

- b. In dit hoofdstuk wordt alléén de administratieve verwerking van het proces beschreven tezamen met de termijn waarbinnen de administratieve verwerking uitgevoerd moet worden. 

- c. Ten behoeve van het informeren door de systeembeheerder over het fysiek in bedrijf nemen, uit bedrijf nemen en verwijderen van allocatiepunten, worden de gegevens van het organisatieonderdeel in de contactgroep meetinrichting (bij de meetverantwoordelijke partij(en)) gepubliceerd: 

   - Dit geeft de meetverantwoordelijke partij de kans tijdig de telemetrie meetinrichting uit te lezen en bij handopgenomen meetinrichtingen de meterstand op te nemen. Bij 

handopgenomen meetinrichtingen wordt de meterstand bij in bedrijf nemen, uit bedrijf en verwijderen van een allocatiepunt in het eerstvolgende (maand)volumebericht gecommuniceerd. 

### Aanleggen van een allocatiepunt

- a. Het ‘aanleggen van een allocatiepunt’ betreft het administratief registreren van een nieuw allocatiepunt. 

- b. De systeembeheerder neemt de EAN-code van het allocatiepunt op in zijn aansluitingenregister uiterlijk de werkdag nadat de EAN-code is uitgegeven. 

- c. De leverancier met een inhuizing op een allocatiepunt dat de fysieke status ‘In aanleg’ heeft ontvangt alleen de gegevens die op dat moment bekend zijn. 

- d. Bij allocatiepunten met de fysieke status ‘In aanleg’ wordt op het moment van inhuizing geen meterstand vastgesteld. 

- e. De systeembeheerder draagt er zorg voor dat hij van de aangeslotene minimaal die gegevens van het allocatiepunt verkrijgt die nodig zijn voor het aanmaken van de EAN-code van het allocatiepunt. 

- f. Bij een telemetrisch bemeten allocatiepunt op een grote aansluiting, die de fysieke status ‘in aanleg’ heeft, en waarbij de meetverantwoordelijke partij in staat is om de meetinrichting uit te lezen, worden de meetgegevens opgeleverd aan de systeembeheerder. 

### In bedrijf nemen van een allocatiepunt

- a. Als een aansluiting in de loop van de dag fysiek in bedrijf wordt gesteld geldt deze situatie administratief voor de gehele dag, ofwel de fysieke status van het allocatiepunt in het aansluitingenregister zal voor die gehele dag ‘in bedrijf’ zijn. 

- b. Bij het fysiek in bedrijf nemen van een (bestaande) kleine aansluiting neemt de systeembeheerder de meterstand op: 

   - i. Wanneer het fysiek in bedrijf nemen van de aansluiting samenvalt met een mutatie van de meetinrichting, wordt de fysiek opgenomen meterstand gecommuniceerd via het subproces ‘Mutatie van de meetinrichting’ aan de leverancier die aanwezig is op het allocatiepunt en wordt de meterstand opgenomen in het TMR; 

   - ii. Wanneer het fysiek in bedrijf nemen van de aansluiting niet samenvalt met een mutatie van de meetinrichting, wordt de fysiek opgenomen meterstand gecommuniceerd middels het subproces ‘Fysieke opname‘ aan de leverancier die aanwezig is op het allocatiepunt, waarbij de meterstand het kenmerk (ProcesID) Fysieke Opname krijgt en wordt de meterstand opgenomen in het TMR. 

- c. Bij het fysiek in bedrijf nemen van een (bestaande) grote aansluiting informeert de systeembeheerder de meetverantwoordelijke partij 10 werkdagen (indien mogelijk) voor de datum van in bedrijf nemen. 

- d. Bij het fysiek in bedrijf nemen van een grote aansluiting neemt de meetverantwoordelijke partij de meterstand op: 

   - i. Wanneer het in bedrijf nemen van de aansluiting samenvalt met een mutatie van de meetinrichting, wordt de meterstand gecommuniceerd via het proces ‘Meetverantwoordelijke partij switch met wissel van de meetinrichting’. 

   - ii. Wanneer het in bedrijf nemen van de aansluiting niet samenvalt met een mutatie van de meetinrichting, wordt de fysiek opgenomen meterstand gecommuniceerd middels het proces ‘Periodieke meterstand en volume’. 

### Uit bedrijf nemen van een allocatiepunt

- a. In geval van een onveilige situatie neemt de systeembeheerder het initiatief tot het uit bedrijf nemen van de aansluiting. 

- b. Bij een aansluiting die fysiek uit bedrijf is genomen blijven de marktpartijen op het allocatiepunt geregistreerd staan. 

- c. Het indienen van mutaties voor een allocatiepunt dat administratief uit bedrijf genomen is, blijft mogelijk. 

- d. Wanneer de systeembeheerder een primair allocatiepunt uit bedrijf neemt, zal de systeembeheerder tevens eventuele bijbehorende additionele allocatiepunten uit bedrijf nemen. De systeembeheerder neemt hierbij niet alleen de meterstand van het primaire allocatiepunt op maar ook de meterstanden van alle bij het primair allocatiepunt behorende additionele allocatiepunten. 

- e. Als een allocatiepunt in de loop van de dag fysiek uit bedrijf wordt genomen geldt administratief gezien deze situatie vanaf de volgende kalenderdag. Het allocatiepunt zal de gehele dag van fysieke uitbedrijfname de fysieke status ‘in bedrijf’ behouden. De fysieke status wordt per eerstvolgende kalenderdag aangepast naar ‘uit bedrijf’. 

- f. Bij het fysiek uit bedrijf nemen van een kleine aansluiting neemt de systeembeheerder de fysiek opgenomen meterstand op en plaatst deze met bijbehorend verbruik in het TMR: 

   - i. Wanneer het fysiek uit bedrijf nemen van de aansluiting samenvalt met een mutatie van de meetinrichting, wordt de fysieke meterstand gecommuniceerd via het subproces ‘Mutatie van de meetinrichting’. 

   - ii. Wanneer het fysiek uit bedrijf nemen van de aansluiting niet samenvalt met een mutatie van de meetinrichting, wordt de fysieke meterstand gecommuniceerd middels het subproces ‘Fysieke opname’. 

- g. Bij het fysiek uit bedrijf nemen van een (bestaande) grote aansluiting informeert de systeembeheerder de meetverantwoordelijke partij 10 werkdagen (indien mogelijk) voor de datum van uit bedrijf nemen. 

- h. Bij het uit bedrijf nemen van een grote aansluiting neemt de meetverantwoordelijke partij de meterstand op: 

   - i. Wanneer het uit bedrijf nemen van de aansluiting samenvalt met een mutatie van de meetinrichting, wordt de fysiek opgenomen meterstand gecommuniceerd via het subproces ‘Meetverantwoordelijke partij switch met wissel van de meetinrichting’. 

   - ii. Wanneer het uit bedrijf nemen van de aansluiting niet samenvalt met een mutatie van de meetinrichting, wordt de fysiek opgenomen meterstand gecommuniceerd middels het subproces ‘Periodieke meterstand en volume’. 

   - iii. Indien het niet mogelijk is een meterstand op te nemen (bv. in geval van buitenshuis afsluiten) bepaalt de meetverantwoordelijke partij een meterstand. De meterstand wordt gecommuniceerd middels het subproces ‘Periodieke meterstand en volume’. 

### Verwijderen van een allocatiepunt

- a. Wanneer een aansluiting verwijderd wordt en er bevinden zich op de mutatiedatum marktpartijen op het allocatiepunt, dan informeert de systeembeheerder de marktpartijen daarover middels een stamgegevensbericht. 

- b. Voorwaarde voor het administratief verwerken van de verwijdering van een allocatiepunt is, dat er geen goedgekeurde doch nog niet geëffectueerde berichten meer aanwezig zijn voor het betreffende allocatiepunt. 

   - Wanneer dit wel het geval is, verwijdert de systeembeheerder eerst de betreffende berichten, informeert de leverancier over deze verwijdering en effectueert daarna de wijziging van de fysieke status van het allocatiepunt in het aansluitingenregister. 

- c. Wanneer de systeembeheerder een primair allocatiepunt op een kleine aansluiting verwijdert, zal de systeembeheerder tevens eventuele bijbehorende additionele allocatiepunten verwijderen. De systeembeheerder neemt hierbij niet alleen de meterstand van het primaire allocatiepunt op maar ook de meterstanden van alle bij het primair allocatiepunt behorende additionele allocatiepunten. 

- d. Bij het verwijderen van een kleine aansluiting met de fysieke status ‘In bedrijf’ neemt de systeembeheerder de meterstand op: 

   - i. Omdat het verwijderen van de aansluiting samenvalt met een mutatie van de meetinrichting, wordt de meterstand gecommuniceerd via het subproces ‘Mutatie van de meetinrichting’ als er een leverancier aanwezig is op het allocatiepunt. 

   - ii. Indien er geen leverancier op het allocatiepunt aanwezig is registreert de systeembeheerder de eindmeterstand en plaatst deze in het TMR. 

- e. Bij het verwijderen van een grote aansluiting met de fysieke status ‘In bedrijf’ neemt de meetverantwoordelijke partij de fysieke meterstand op: 

   - i. Omdat het verwijderen van de aansluiting samenvalt met een mutatie van de meetinrichting, wordt de fysieke meterstand gecommuniceerd via het subproces ‘Meetverantwoordelijke partij switch met wissel van de meetinrichting’. 

   - ii. Indien het niet mogelijk is een meterstand op te nemen (bv. in geval van brand) bepaalt de meetverantwoordelijke een meterstand. De meterstand wordt gecommuniceerd middels het subproces ‘Periodieke meterstand en volume’. 

- f. Bij het verwijderen van een allocatiepunt met de fysieke status ‘Uit bedrijf’ wordt geen meterstand vastgesteld; de eindmeterstand is immers al vastgesteld, door de systeembeheerder bij een allocatiepunt op een kleine aansluiting en door de meetverantwoordelijke partij bij een allocatiepunt op een grote aansluiting, op de datum van het fysiek uit bedrijf nemen van de aansluiting. 

- g. Bij het verwijderen van een (bestaande) grote aansluiting informeert de systeembeheerder de meetverantwoordelijke partij vijf werkdagen (indien mogelijk) voor de datum van uit bedrijf nemen. 

## 4.21.2 Procesbeschrijvingen KA en GA

### Aanleggen van een allocatiepunt KA en GA

Bijlage B1134: Subprocesplaat SP0101 KA-GA – Aanleggen van een allocatiepunt KA en GA

1. De systeembeheerder kent een EAN-code toe aan het nieuwe allocatiepunt. De systeembeheerder verstrekt de toegekende EAN-code aan de aangeslotene. 

2. De systeembeheerder registreert in het aansluitingenregister de gegevens van het nieuwe allocatiepunt die beschikbaar zijn. De administratieve status wordt daarbij inactief’ en de fysieke status wordt ‘In aanleg’. 

### In bedrijf nemen van een allocatiepunt KA en GA

Bijlage B1135: Subprocesplaat SP0101 KA-GA – In bedrijf nemen van een allocatiepunt KA en GA

1. De systeembeheerder neemt de aansluiting fysiek in bedrijf. 

2. De systeembeheerder verwerkt de mutatie zo spoedig mogelijk in het aansluitingenregister doch uiterlijk de vijfde werkdag na het fysiek in bedrijf nemen van de aansluiting. De fysieke status van de allocatiepunt in het aansluitingenregister wordt ‘In bedrijf’. 

### Uit bedrijf nemen van een allocatiepunt KA en GA

Bijlage B1136: Subprocesplaat SP0101 KA-GA – Uit bedrijf nemen van een allocatiepunt KA en GA

1. De systeembeheerder neemt de aansluiting fysiek uit bedrijf. 

2. De systeembeheerder verwerkt de mutatie zo spoedig mogelijk in het aansluitingenregister doch uiterlijk de 5<sup>e</sup> werkdag na het fysiek uit bedrijf nemen van de aansluiting. De fysieke status van het allocatiepunt in het aansluitingenregister wordt ‘Uit bedrijf’ en de administratieve status wordt ‘Inactief’. 

### Verwijderen van een allocatiepunt KA

Bijlage B1137: Subprocesplaat SP0101 KA – Verwijderen van een allocatiepunt KA

1. De systeembeheerder verwijdert de aansluiting. 

2. De systeembeheerder verwijdert nog niet geeffectueerde mutaties en informeert de leverancier. 

3. De leverancier ontvangt de informatie over de verwijderde, nog niet geëffectueerde, mutatie van de systeembeheerder. 

4. De leverancier informeert de balanceringsverantwoordelijke over deze verwijdering. 

5. De balanceringsverantwoordelijke verwerkt de ontvangen informatie. 

6. De systeembeheerder verwerkt de mutatie zo spoedig mogelijk in het aansluitingenregister doch uiterlijk de 5<sup>e</sup> werkdag na de verwijdering van het allocatiepunt. De fysieke status van het allocatiepunt in het aansluitingenregister wordt ‘Verwijderd’ en de administratieve status wordt ‘Inactief’. 

### Verwijderen van een allocatiepunt GA

Bijlage B1138: Subprocesplaat SP0101 GA – Verwijderen van een allocatiepunt GA

   1. De systeembeheerder verwijdert de aansluiting. Bij het verwijderen van een aansluiting met de fysieke status ‘In bedrijf’ bepaalt de meetverantwoordelijke partij de meterstand. Voordat de systeembeheerder het allocatiepunt de fysieke status ‘Verwijderd’ geeft, controleert de systeembeheerder of er voor het betreffende allocatiepunt goedgekeurde maar nog niet geëffectueerde mutaties aanwezig zijn. 

   2. Wanneer dit het geval is verwijdert de systeembeheerder deze mutaties en informeert de leverancier en/of meetverantwoordelijke partij hierover uiterlijk de werkdag na effectuering in het aansluitingenregister. 

   3. De leverancier ontvangt de informatie van de systeembeheerder. 

   4. De meetverantwoordelijke partij ontvangt de informatie van de systeembeheerder. 

   5. De systeembeheerder verwerkt de mutatie zo spoedig mogelijk doch uiterlijk de vijfde werkdag na de verwijdering van het allocatiepunt in het aansluitingenregister. De fysieke status van het allocatiepunt in het aansluitingenregister wordt ‘Verwijderd’ en de administratieve status wordt ‘Administratief afgesloten’. 

## 4.21.3 Termijnen KA

   - a. De inbedrijfname wordt zo veel mogelijk op de datum van de fysieke werkzaamheden doch uiterlijk de vijfde werkdag na de fysieke werkzaamheden in het aansluitingenregister verwerkt. 

   - b. De uitbedrijfname wordt zo veel mogelijk op de datum van de fysieke werkzaamheden doch uiterlijk de vijfde werkdag na de fysieke werkzaamheden in het aansluitingenregister verwerkt. 

   - c. De verwijdering van de aansluiting wordt zo veel mogelijk op de datum van de fysieke werkzaamheden doch uiterlijk vijf werkdagen na de fysieke werkzaamheden in het aansluitingenregister verwerkt. 

Zie voor de overige termijnen de subprocessen ‘Distribueren stamgegevens na mutatie’ en ‘Vaststellen en communiceren meterstand’. 

## 4.21.4 Termijnen GA

### In bedrijf nemen allocatiepunt

- a. 10 werkdagen (indien mogelijk) voor de inbedrijfnamedatum kondigt de systeembeheerder de voorgenomen inbedrijfnamedatum aan bij de betrokken marktpartijen. 

- b. Op de inbedrijfnamedatum heeft de systeembeheerder contact met de meetverantwoordelijke partij tijdens of direct na de inbedrijfname van het allocatiepunt. 

- c. De fysieke ingebruikname wordt zo veel mogelijk op de datum van de fysieke werkzaamheden doch uiterlijk vijf werkdagen na de fysieke werkzaamheden in het aansluitingenregister verwerkt. 

### Uit bedrijf nemen allocatiepunt

- a. 10 werkdagen (indien mogelijk) voor de voorgenomen uitbedrijfnamedatum kondigt de systeembeheerder de geplande uitbedrijfname aan bij de betrokken marktpartijen. 

- b. Op de uitbedrijfnamedatum heeft de systeembeheerder contact met de meetverantwoordelijke partij over de spoedige uitbedrijfname van de aansluiting. 

- c. De meetverantwoordelijke partij doet een laatste uitlezing van de meetinrichting voorafgaand aan uitbedrijfname. 

- d. De fysieke uitbedrijfname wordt zo veel mogelijk op de datum van de fysieke werkzaamheden doch uiterlijk vijf werkdagen na de fysieke werkzaamheden in het aansluitingenregister verwerkt. 

### Verwijderen van een allocatiepunt

- a. De systeembeheerder informeert vijf werkdagen (indien mogelijk) voor de fysieke werkzaamheden de meetverantwoordelijke partij (indien aanwezig). 

- b. De fysieke verwijdering van de aansluiting wordt zo veel mogelijk op de datum van de fysieke werkzaamheden doch uiterlijk vijf werkdagen na de fysieke werkzaamheden in het aansluitingenregister verwerkt. 

- c. Wanneer een aansluiting wordt verwijderd en er bevinden zich op de mutatiedatum in het aansluitingenregister marktpartijen op het allocatiepunt, dan past de systeembeheerder de fysieke status van het allocatiepunt aan naar ‘verwijderd’ en informeert de systeembeheerder de marktpartijen daarover uiterlijk één werkdag na de mutatie in het aansluitingenregister middels een stamgegevensbericht. 

Zie voor de overige termijnen de subprocessen ‘Distribueren stamgegevens na mutatie’ en ‘Vaststellen en communiceren meterstand’. 

## 4.21.5 Gegevensuitwisseling

Voor de gegevensuitwisseling zie de subprocessen ‘Distribueren stamgegevens na mutatie’ en ‘Vaststellen en communiceren meterstand’.
