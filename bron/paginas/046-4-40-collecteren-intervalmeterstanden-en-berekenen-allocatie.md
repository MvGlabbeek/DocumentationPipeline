# 4.40 Collecteren intervalmeterstanden en berekenen allocatievolumes SMA


## 4.40.1 Procesafspraken

- a. Voor de allocatiepunten met de allocatiemethodiek “slimmemeterallocatie” collecteert de systeembeheerder minimaal één keer per 5 kalenderdagen de intervalmeterstanden van de meetinrichting met communicatiefunctionaliteit. 

- b. Indien de collectie niet slaagt, dan verricht de systeembeheerder een dag later opnieuw een poging om de intervalmeterstanden uit te lezen tot uiterlijk 9 werkdagen na de meetdag. 

- c. De volumes per onbalansverrekeningsperiode en per energierichting voor individuele allocatiepunten worden bepaald door het verschil tussen twee opeenvolgende uitgelezen intervalmeterstanden te berekenen. 

- d. Voor de allocatiepunten met de allocatiemethodiek “slimmemeterallocatie” waarvan de meetinrichting met communicatiefunctionaliteit nog niet is uitgelezen, de intervalmeterstanden niet beschikbaar zijn of de uitgelezen intervalmeterstanden niet plausibel zijn, worden de allocatievolumes voor slimmemeterallocatie gerepareerd. 

- e. De systeembeheerder vervangt de gerepareerde volumes indien plausibele gemeten intervalmeterstanden voor de betreffende meetdag zijn gecollecteerd. Of anders repareert de systeembeheerder gerepareerde volumes opnieuw indien de dynamische profielfracties gewijzigd zijn (zie MSP Wholesale elektriciteit) of wanneer een reparatie mogelijk is op basis van interpolatie die geëxtrapoleerde volumes vervangt. 

- f. De berekende volumes van allocatiepunten worden bij eerste gelegenheid per systeemgebied, per energierichting, per onbalansverrekeningsperiode, per herkomstindicator (gemeten of gerepareerd), per balanceringsverantwoordelijke en per leverancier geaggregeerd. 

- g. Mits er geen verwerkingsdoeleinden voor andere processen dan slimmemeterallocatie van toepassing zijn op de intervalmeterstanden en volumes waarvoor de gegevens langer behouden dienen te blijven, worden de intervalmeterstanden en volumes van allocatiepunten direct na de definitieve allocatie vernietigd. Indien sprake is van een laatste uitgelezen intervalmeterstand per meetinrichting en per energierichting van een allocatiepunt, dan wordt deze niet verwijderd zodat interpolatie voor de reparatie van slimmemeterallocatie mogelijk blijft. Deze laatst uitgelezen intervalmeterstanden worden maximaal voor een periode van twee maanden bewaard. 

## 4.40.2 Procesbeschrijving

Bijlage B1168: Subprocesplaat zonder SP-code (§4.40.2)

1. De systeembeheerder collecteert de intervalmeterstanden van allocatiepunten met de allocatiemethodiek “slimmemeterallocatie”. 

2. De systeembeheerder berekent de volumes per energierichting en per onbalansverrekeningsperiode van de uitgelezen allocatiepunten. 

3. De systeembeheerder bepaalt of meetgegevens voor slimmemeterallocatie gerepareerd dienen te worden aan de hand van de volgende criteria: 

   - a. er kan geen volume voor een onbalansverrekeningsperiode berekend worden door het ontbreken van uitgelezen intervalmeterstanden, of, 

   - b. de waarde van het berekende verschil tussen de intervalmeterstanden per energierichting voor een onbalansverrekeningsperiode is kleiner dan 0,000 kWh of groter dan 20,000 kWh per onbalansverrekeningsperiode. 

4. De systeembeheerder aggregeert de allocatievolumes per systeemgebied, per balanceringsverantwoordelijke, per leverancier, per onbalansverrekeningsperiode en per energierichting, op basis van gemeten intervalmeterstanden van de allocatiepunten met allocatiemethode “slimmemeterallocatie” waarbij geen reparatie van meetgegevens benodigd is (herkomstindicatie gemeten). 

5. De systeembeheerder repareert de volumes voor SMA door het toepassen van de rekenregels zoals opgenomen is in de Bijlage B Generieke rekenregels reparatie meetgegevens meetinrichting met communicatiefunctionaliteit elektriciteit van het MSP Wholesale elektriciteit. 

6. De systeembeheerder aggregeert de gerepareerde allocatievolumes van de allocatiepunten met allocatiemethode “slimmemeterallocatie” per systeemgebied, per balanceringsverantwoordelijke, per leverancier, per onbalansverrekeningsperiode, per energierichting (herkomstindicatie gerepareerd). 

## 4.40.3 Termijnen

- a. De systeembeheerder berekent de geaggregeerde volumes slimmemeterallocatie als onderdeel van het ter beschikking stellen van allocatieresultaten elektriciteit uiterlijk de eerste kalenderdag voor 16.00uur na de meetdag. 

- b. De systeembeheerder repareert de volumes voor SMA op de eerste dag na de meetdag na 10 uur en uiterlijk voor het versturen van de allocatieresultaten van de voorlopige allocatie op de eerste kalenderdag na de meetdag. 

- c. Indien dynamische profielfracties gewijzigd zijn op de tweede dag na de meetdag, repareert de systeembeheerder de volumes voor SMA opnieuw voor de eerstvolgende allocatie. 

- d. De systeembeheerder vervangt of repareert de gerepareerde volumes opnieuw uiterlijk de negende werkdag na de meetdag indien: 

   - i. na de eerdere reparatie alsnog gemeten intervalmeterstanden voor de betreffende meetdag worden gecollecteerd die voldoen aan de criteria (zie 3b.); 

   - ii. de gefixeerde dynamische profielfracties gewijzigd zijn ten gevolge van het Calamiteitenproces (zie Bijlage C Calamiteitenproces Bepalen dynamische profielfracties in het MSP Wholesale elektriciteit); 

   - iii. na de meetdag een reparatie mogelijk is op basis van interpolatie die geëxtrapoleerde volumes vervangt (zie Bijlage B Generieke rekenregels reparatie meetgegevens meetinrichting met communicatiefunctionaliteit elektriciteit in het MSP Wholesale elektriciteit). 

## 4.40.4 Gegevensuitwisseling

### N.v.t.
