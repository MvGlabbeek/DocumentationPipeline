# 4.30 SP0038 Communicatie systeemtarieven


## 4.30.1 Procesafspraken KA

1. De systeembeheerder communiceert de tarieven per bedrijfs-EAN code systeembeheerder per capaciteitstariefcode. 

2. De systeemtarieven worden door de systeembeheerder per bedrijfs-EAN-code van de leverancier, zoals deze in het aansluitingenregister opgenomen staat, gecommuniceerd. 

3. De gecommuniceerde systeemtarieven betreffen tarieven op dagbasis (met vier decimalen achter de komma). 

4. Indien een systeembeheerder te laat of verkeerde systeemtarieven communiceert, treedt de systeembeheerder met alle leveranciers in overleg. De leverancier kan de tarievenset om deze redenen niet accepteren. 

5. Wanneer de nieuwe systeemtarieven, na overleg, niet tijdig in de systemen opgenomen kunnen worden, worden de huidige systeemtarieven toegepast en zal de systeembeheerder nieuwe systeemtarieven voor een nieuwe datum vaststellen met inachtneming van de juiste termijnen. 

### Aanvullende procesafspraken bij het implementeren van een nieuwe capaciteitstariefcode:

1. De systeembeheerder zorgt ervoor dat de nieuwe capaciteitstariefcode met bijbehorende systeemtarieven worden toegevoegd aan de centrale tarieventabel. 

## 4.30.2 Procesbeschrijving Communiceren te hanteren systeemtarieven KA

Bijlage B1152: Subprocesplaat SP0038 KA

1. De systeembeheerder stelt de door hem te hanteren periodieke systeemkosten vast en verstuurt de ‘melding tarieven’ minimaal één maand voor de ingangsdatum naar de leverancier. 

2. De leverancier ontvangt de ‘melding tarieven’. 

3. De systeembeheerder zet de systeemtarieven in de centrale tarieventabel. 

4. Op basis van de ‘melding tarieven’ haalt de nieuwe leverancier de tarieven op. 

5. De leverancier beoordeelt de tarieven. 

6. Indien de leverancier een tekortkoming constateert, meldt leverancier dit zo spoedig mogelijk en uiterlijk vijf werkdagen voor de ingangsdatum aan de systeembeheerder en treden partijen in overleg. 

7. De systeembeheerder verwerkt de afwijzing. 

8. De systeembeheerder initieert een overleg met de leverancier die de tekortkoming heeft gemeld en betrekt vervolgens, indien nodig, de overige leveranciers. Het is mogelijk dat de systeembeheerder, nieuwe systeemtarieven voor een nieuwe datum vaststelt; het proces start weer bij stap 1. 

9. Als er geen tekortkomingen geconstateerd worden, verwerkt de leverancier de tarievenset in de facturatie. 

## 4.30.3 Procesbeschrijving Communiceren nieuw tarief KA

Bijlage B1153: Subprocesplaat SP0038 KA

1. Bij het opvoeren van een nieuwe capaciteitstariefcode informeert de systeembeheerder de leverancier minimaal drie maanden voor de communicatie van het bijbehorende systeemtarief over het implementeren van een nieuwe capaciteitstariefcode. Hierbij wordt gebruik gemaakt 

van de contactpersonen Periodieke systeemtarieven in het Contactpersonenregister. In de e- mail staan minimaal de volgende gegevens: 

   - a. De nieuwe capaciteitstariefcode. 

   - b. De omschrijving van de aanpassing zoals deze ook wordt toegevoegd aan de tarieventabel. 

   - c. De ingangsdatum van het nieuwe systeemtarief. 

2. De leverancier ontvangt de informatie over de nieuwe capaciteitstariefcode. 

3. De systeembeheerder communiceert het systeemtarief aan de leveranciers tenminste één maand voor livegang van het systeemtarief. 

## 4.30.4 Termijnen KA

- a. Minimaal drie maanden voor de ingangsdatum van de nieuwe capaciteitstariefcodering heeft de systeembeheerder een vooraankondiging hieromtrent naar de leverancier gecommuniceerd. 

- b. Minimaal één maand voor de ingangsdatum van de nieuwe systeemtarieven heeft de systeembeheerder de door hem te hanteren tarieven aan de leverancier gecommuniceerd. 

- c. Indien de leverancier een tekortkoming constateert, meldt leverancier dit zo spoedig mogelijk en uiterlijk vijf werkdagen voor de ingangsdatum aan de systeembeheerder en treden partijen in overleg. 

- d. De leverancier hanteert de ontvangen tarieven vanaf de ingangsdatum van de systeemtarieven. 

## 4.30.5 Gegevensuitwisseling KA

### Melding tarieven

|**Melding tarieven**||||
|---|---|---|---|
|**Gegevens**|**KV**|**1/n**|**Opmerking**|
|Dagtekening|V|1||
|Datum ingang|V|1|Ingangsdatum van de periodieke systeemtarieven|
|Bericht ID|V|1||
|EAN-code systeembeheerder|V|1||
|Valutacode|V|1||
|Productsoort|V|n|Elektriciteit en/of gas|
|Capaciteitstariefcode|V|n||
|Tarief|V|n|Dagtarief systeemtarieven behorende bij de capaciteitstariefcode|
