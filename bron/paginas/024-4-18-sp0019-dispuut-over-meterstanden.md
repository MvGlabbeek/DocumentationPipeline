# 4.18 SP0019 Dispuut over meterstanden


## 4.18.1 Procesafspraken KA

- a. Het subproces Dispuut over meterstanden wordt gebruikt om correcties uit te voeren op alle vastgestelde meterstanden. 

- b. Een wederpartij kan altijd in dispuut gaan over de berekeningswijze van een meterstand met de initiërende marktpartij indien hij constateert dat de initiërende marktpartij een meterstand niet op de juiste wijze heeft berekend. 

- c. Systeembeheerders en leveranciers gebruiken het proces Dispuut over meterstanden in de situaties waarbij het verschil tussen de vastgestelde meterstand en de alternatieve meterstand in de dispuutmelding groter is dan: 

   - i. elektriciteit: 250 kWh 

   - ii. gas: 100 m<sup>3</sup> 

- d. Klachten met betrekking tot verschillen in meterstanden binnen de gestelde grenzen worden door de zorgplichtige leverancier correct en zo spoedig mogelijk naar de klant toe afgehandeld. De zorgplichtige leverancier is in geval van een inhuizing de inhuizende leverancier, in geval 

van een uithuizing of geforceerde uithuizing de uithuizende leverancier en in geval van een switch de nieuwe leverancier. 

- e. De systeembeheerders en leveranciers dienen voor een goede werking van het proces Dispuut over meterstanden de contactgegevens van het organisatieonderdeel dat belast is met de afhandeling van disputen namens de betreffende marktpartij op te nemen in het Contactpersonenregister. 

- f. Indien de initiërende marktpartij beschikt over een overeengekomen meterstand, klantopname of een fysieke opname dan kan de wederpartij verzoeken hiervan bewijs te overleggen. Dit vindt plaats in het deelproces ‘Overleg met wederpartij’. 

- g. Bij een dispuut over meterstanden zijn altijd twee marktpartijen betrokken: 

   - i. _Initiërende marktpartij_ : de marktpartij die de meterstand(en) heeft vastgesteld of nog de mogelijkheid heeft de vastgestelde meterstanden te verbeteren. 

   - ii. _Wederpartij_ : de marktpartij die in dispuut gaat tegen de vastgestelde meterstand(en). 

- h. De marktpartij die het dispuut start, is verplicht om het transactiedossiernummer, ontvangen in het GAIN / LOSS-bericht of in het volumebericht (in geval van een driejaarlijkse fysieke opname of een vastgestelde periodieke meterstand), te vermelden in de 'melding dispuut'. 

- i. De alternatieve meterstand wordt aan de vastgestelde meterstand gekoppeld via het transactiedossiernummer (niet via de datum). Indien de alternatieve meterstand wordt geaccepteerd, dan wordt deze vastgesteld voor de opnamedatum van de oorspronkelijke meterstand. 

- j. Voor een vastgestelde meterstand na dispuut dient het oorspronkelijke kenmerk (Proces ID) meegegeven te worden inclusief oorspronkelijk transactiedossiernummer. Dit geldt voor zowel de leverancier als de systeembeheerder. 

Eventstanden worden alleen gecorrigeerd naar aanleiding van een dispuut. In het geval dat een leverancier een 'eigen' eventstand wil corrigeren (om bijvoorbeeld een berekende meterstand te vervangen door een klantstand), dan is hij in feite met zichzelf in dispuut. De initiërende marktpartij neemt dan contact op met de wederpartij om dit toe te lichten en af te stemmen alvorens de nieuwe eventstand vast te stellen. Indien de initiërende marktpartij dit niet doet, dan zal de wederpartij contact opnemen om bilateraal tot een oplossing te komen. Indien de wederpartij de systeembeheerder is, dan is het mogelijk dat hij de stand afwijst. Voor meer informatie zie bijlage Kruisende meterstanden. 

## 4.18.2 Procesbeschrijvingen KA

### Controleren meterstand en eventueel melden meterstand in dispuut

Bijlage B1126: Subprocesplaat SP0019 KA – Controleren meterstand en eventueel melden meterstand in dispuut

1. De wederpartij besluit of het proces Dispuut over meterstanden wordt gestart. Hierbij geldt de volgende beslistabel: 

|**Meetinrichting**<br>**Marktproces**|**Herkomst**<br>**vastgestelde**<br>**meterstand(en)**|**Initiërende partij**<br>**(ontvanger**<br>**dispuutmelding)**|**Wederpartij**<br>**(indiener**<br>**dispuutmelding)**|**Toelichting**|
|---|---|---|---|---|
|Metermutatie of<br>fysieke opname|*|Systeembeheerder|Actuele leverancier||
|P<br>Einde levering of<br>Uithuizing (met<br>leegstand tot<br>gevolg)|4-meterstand of Fysieke<br>opname<br>Berekend,<br>Overeengekomen of<br>Klantstand|Systeembeheerder<br>Oude leverancier|Oude leverancier<br>systeembeheerder, tenzij<br>er sprake was van door<br>de systeembeheerder<br>berekende meterstanden|Oude leverancier kan in dispuut bij gerede twijfel over de P4-meterstand t.o.v. andere<br>P4-meterstanden in de meetreeks.<br>Bij een twijfel over de werking van de meetinrichting is het de bedoeling dat de<br>leverancier een melding bij de systeembeheerder doet via het daarvoor afgesproken<br>proces.<br>In geval van door systeembeheerder berekende meterstanden kan de oude leverancier<br>'verbetermeterstanden' indienen zonder dispuutmelding.<br>De systeembeheerder kan niet in dispuut gaan op meterstanden die door de<br>systeembeheerder zelf berekend zijn, maar wel op berekende meterstanden die<br>'overschreven' zijn door de oude leverancier in de vorm van 'overeengekomen'<br>meterstanden of klantstanden.|
|P<br>LV-switch of<br>Inhuizing (zonder<br>|4-meterstand of Fysieke<br>opname|Systeembeheerder|Nieuwe leverancier of<br>Oude leverancier|Zowel oude als nieuwe leverancier kunnen, bij de systeembeheerder in dispuut bij<br>gerede twijfel over de P4-meterstand t.o.v. andere P4-meterstanden in de meetreeks.<br>Bij een twijfel over de werking van de meetinrichting is het de bedoeling dat de<br>leverancier een melding bij de systeembeheerder doet via het daarvoor afgesproken<br>proces.|
|**Op afstand**<br>**uitleesysteembe**<br>voorafgaande<br>leegstand)|Berekend,<br>Overeengekomen of<br>Klttd|Nieuwe leverancier|Oude leverancier|In geval van door systeembeheerder berekende meterstanden kan de nieuwe<br>leverancier 'verbetermeterstanden' indienen: (alleen) de oude leverancier kan een<br>dispuutmelding gebruiken, richting de nieuwe leverancier, om dat proces te initiëren.|
|**heerderaar:**<br>|ansan|||De systeembeheerder is nooit partij (initiërend noch wederpartij) in deze situatie.|
|**(SLM en SMU en**<br>**ADMIN AAN)**||||De nieuwe leverancier kan bij de systeembeheerder in dispuut bij gerede twijfel over<br>de P4- meterstand t.o.v. andere P4-meterstanden in de meetreeks.|
|P<br>LV-switch of<br>Inhuizing (met<br>voorafgaande<br>leegstand)|4-meterstand of Fysieke<br>opname<br>Berekend,<br>Overeengekomen of<br>Klantstand|Systeembeheerder<br>Nieuwe leverancier|Nieuwe leverancier<br>systeembeheerder, tenzij<br>er sprake was van door<br>de systeembeheerder<br>berekende meterstanden|Bij een twijfel over de werking van de meetinrichting is het de bedoeling dat de<br>leverancier een melding bij de systeembeheerder doet via het daarvoor afgesproken<br>proces.<br>In geval van door systeembeheerder berekende meterstanden kan de nieuwe<br>leverancier 'verbetermeterstanden' indienen zonder dispuutmelding.<br>De systeembeheerder kan niet in dispuut gaan op meterstanden die door de<br>systeembeheerder zelf berekend zijn, maar wel op berekende meterstanden die<br>'overschreven' zijn door de oude leverancier in de vorm van 'overeengekomen'<br>meterstanden of klantstanden.|
|P<br>Alle andere<br>mutaties,|4-meterstand of Fysieke<br>opname|Systeembeheerder|Actuele leverancier|De actuele leverancier kan, bij de systeembeheerder in dispuut bij gerede twijfel over<br>de P4- meterstand t.o.v. andere P4-meterstanden in de meetreeks.<br>Bij een twijfel over de werking van de meetinrichting is het de bedoeling dat de<br>leverancier een melding bij de systeembeheerder doet via het daarvoor afgesproken<br>proces.|
|periodieke<br>opnames en<br>maandovergang<br>meterstanden|Berekend,<br>Overeengekomen of<br>Klantstand|Actuele leverancier|Systeembeheerder, tenzij<br>er sprake was van door<br>de systeembeheerder<br>berekende meterstanden|In geval van door systeembeheerder berekende meterstanden kan de actuele<br>leverancier 'verbetermeterstanden' indienen zonder dispuutmelding.<br>De systeembeheerder kan niet in dispuut gaan op meterstanden die door de<br>systeembeheerder zelf berekend zijn, maar wel op berekende meterstanden die<br>'overschreven' zijn door de oude leverancier in de vorm van 'overeengekomen'<br>meterstanden of klantstanden.|
|Metermutatie of<br>fysieke opname|*|Systeembeheerder|Actuele leverancier||
|Einde levering of<br>Uithuizing (met<br>leegstand tot<br>gevolg)|*|Oude leverancier|Systeembeheerder||
|LV-switch of<br>Inhuizing (zonder<br>voorafgaande<br>**Niet op afstand**<br>|*|Nieuwe leverancier|Oude leverancier|De systeembeheerder is nooit partij (initiërend noch wederpartij) in deze situatie.|
|leegstand)<br>**uitleesysteembe**<br>**heerderaar:**|||||
|LV-switch of<br>Inhuizing (met<br>voorafgaande<br>leegstand)<br>**(CVN en/of SMN**<br>**en/of ADMIN**<br>**UIT)**|*|Nieuwe leverancier|Systeembeheerder||
|Alle andere<br>mutaties en<br>periodieke<br>opnames (en<br>maandovergang<br>meterstanden)|*|Actuele leverancier|Systeembeheerder||

2. Indien de wederpartij geen proces Dispuut over meterstanden start, is de wederpartij akkoord met de vastgestelde meterstand. 

3. Indien de wederpartij heeft besloten om het proces Dispuut over meterstanden te starten, dan stuurt de wederpartij uiterlijk de 20<sup>e</sup> werkdag voordat de oorspronkelijk vastgestelde meterstand dispuutvrij is een ‘melding dispuut’ naar de initiërende marktpartij, waarbij hij verplicht is een alternatieve meterstand mee te sturen in de dispuutmelding. De opnamedatum van de meegestuurde alternatieve meterstand is de daadwerkelijke opnamedatum van de alternatieve meterstand. 

4. De initiërende marktpartij ontvangt en verwerkt het bericht ‘melding dispuut’ van de wederpartij. 

### Beoordelen van de melding dispuut en de alternatieve stand

Bijlage B1127: Subprocesplaat SP0019 KA – Beoordelen van de melding dispuut en de alternatieve stand

1. Als de initiërende marktpartij uiterlijk de 20<sup>e</sup> werkdag voordat de meterstand dispuutvrij is geworden een ‘melding dispuut’ ontvangt, beoordeelt hij de meegestuurde alternatieve meterstand op basis van de beslistabel uit het proces ‘Controleren meterstand en eventueel melden meterstand in dispuut’. De situaties beschreven in de groene vlakken moet de initiërende marktpartij accepteren en gereedzetten voor het deelproces ‘vaststellen meterstand na dispuut’. In de overige situaties besluit de initiërende marktpartij tot: 

   - a. Het accepteren van de alternatieve meterstand op basis van eigen interne regels en het gereedzetten van de alternatieve meterstand voor het deelproces ‘vaststellen meterstand na dispuut’. 

- b. Het niet accepteren van de alternatieve meterstand en in overleg treden met de wederpartij. 

- 2. De initiërende marktpartij bevestigt de acceptatie dan wel afwijzing van de alternatieve meterstand uiterlijk vijf werkdagen na ontvangst van de melding dispuut aan de wederpartij middels een terugkoppelingsbericht. 

3. Indien conform de beslistabel een dispuut mogelijk is, en de initiërende marktpartij wijst het dispuut af dan dient de initiërende marktpartij in overleg te treden met de wederpartij. 

4. Indien conform de beslistabel geen dispuut mogelijk is, tussen de betreffende wederpartij en de initiërende marktpartij, maar de wederpartij start alsnog een dispuut op en de initiërende marktpartij wijst het dispuut af dan geldt de toelichting in de afwijzing als in overleg geweest te zijn. 

5. Als de initiërende marktpartij een onvolledige melding dispuut ontvangt, verstuurt hij een afwijzing van de alternatieve meterstand. In de toelichting in het bericht vermeldt hij de reden voor het afwijzen van de alternatieve stand. In dit specifieke geval geldt de toelichting als het in overleg treden met de wederpartij. 

### Overleg met wederpartij

Bijlage B1128: Subprocesplaat SP0019 KA – Overleg met wederpartij

1. Indien de initiërende marktpartij de door de wederpartij voorgestelde meterstand niet accepteert dan treedt de initiërende marktpartij in overleg met de wederpartij om gezamenlijk een meterstand te bepalen. De uitkomst van dit overleg leidt tot: 

   - a. Indien de initiërende marktpartij en de wederpartij een akkoord bereiken over de meterstand die anders is dan de reeds vastgestelde meterstand en dan wordt deze in overleg gezamenlijk geaccordeerde meterstand klaargezet voor het deelproces ‘vaststellen meterstand na dispuut’; 

   - b. Indien de initiërende marktpartij en de wederpartij geen akkoord bereiken over een gezamenlijk geaccordeerde meterstand, dan plant de initiërende marktpartij een fysieke opname op basis van kosten ongelijk in, nadat beide partijen overeenstemming hebben bereikt over de te maken kosten. 

### Fysieke opname op basis kosten ongelijk

Bijlage B1129: Subprocesplaat SP0019 KA – Fysieke opname op basis kosten ongelijk

1. Indien de wederpartij en de initiërende marktpartij in overleg geen akkoord bereiken over de te gebruiken meterstand, dan zal de initiërende marktpartij een fysieke opname uitvoeren (of laten uitvoeren) op het allocatiepunt waarvan de meterstand in dispuut is. Als de initiërende marktpartij niet uiterlijk vijf werkdagen voor het einde van de dispuutstermijn een fysieke opname kan (laten) uitvoeren, dan zal de alternatieve meterstand aangeleverd door de wederpartij worden geaccepteerd en worden vastgesteld door de initiërende marktpartij. 

2. Indien de fysieke opname succesvol is uitgevoerd, dan wordt de oorspronkelijk vastgestelde meterstand door de initiërende marktpartij beoordeeld op basis van de fysiek opgenomen meterstand. Bij deze beoordeling van de oorspronkelijk vastgestelde meterstand worden de volgende criteria gebruikt: 

a. De oorspronkelijk vastgestelde meterstand wordt gehandhaafd als: 

   - i. deze in een marge van 15% * SJA/ vermenigvuldigingsfactor boven of onder de fysieke opname (geïnterpoleerd op basis van de profielenmethodiek naar de datum van de meterstand in dispuut) ligt; 

   - ii. dan wel (voor teruglevertelwerken) wanneer die binnen een marge van 15% * SJI/vermenigvuldigingsfactor boven of onder de fysieke opname (geïnterpoleerd op basis van een tijdsevenredige verdeling van het gemeten verbruik naar de datum van de meterstand in dispuut; 

   - iii. dan wel voor SJV in een marge van 15% * SJV/ vermenigvuldigingsfactor boven of onder de fysieke opname (geïnterpoleerd op basis van de profielenmethodiek naar de datum van de meterstand in dispuut ligt ). 

- b. De oorspronkelijk vastgestelde meterstand wordt verworpen indien deze buiten de in 2a bepaalde grenzen valt. 

Bijlage B1130: Subprocesplaat SP0019 KA – Fysieke opname op basis kosten ongelijk

Als de oorspronkelijk vastgestelde meterstand wordt gehandhaafd, heeft de initiërende marktpartij het recht om de kosten van de fysieke opname te verhalen op de wederpartij (kosten ongelijk) en wordt de oorspronkelijk vastgestelde meterstand gehandhaafd. 

Indien de oorspronkelijk vastgestelde meterstand is verworpen, dan interpoleert de initiërende marktpartij de fysieke opname naar de mutatiedatum, waarop de oorspronkelijk vastgestelde meterstand betrekking had. 

3. De initiërende marktpartij geeft de wederpartij, na overleg tussen de marktpartijen en uiterlijk vijf werkdagen voor het verstrijken van de dispuuttermijn, een terugkoppeling van de beoordeling van de oorspronkelijk vastgestelde meterstand op basis van de fysieke meterstand. Deze terugkoppeling zal (elektronisch) schriftelijk plaatsvinden en bevat in ieder geval de fysieke opname. 

4. De wederpartij ontvangt de terugkoppeling. 

### Vaststellen meterstand na dispuut

Bijlage B1131: Subprocesplaat SP0019 KA – Vaststellen meterstand na dispuut

1. Indien de oorspronkelijk vastgestelde meterstand wordt herzien, stelt de initiërende marktpartij zo snel mogelijk doch uiterlijk de vijfde werkdag voordat de oorspronkelijke meterstand dispuutvrij is een meterstand vast. De herziene meterstand wordt vastgesteld 

voor dezelfde datum als waarop de oorspronkelijke meterstand geldig was. Hiervoor wordt de volgende meterstand gebruikt: 

- a. De alternatieve meterstand als deze na beoordeling door de initiërende marktpartij is geaccepteerd of als de initiërende marktpartij geen fysieke opname heeft kunnen uitvoeren; 

- b. De meterstand waarmee de initiërende marktpartij en de wederpartij in overleg akkoord zijn gegaan; 

- c. De fysieke opname, geïnterpoleerd naar de datum waarvoor de oorspronkelijke meterstand was vastgesteld, indien de oorspronkelijke meterstand op basis van de fysieke opname is verworpen. Deze geïnterpoleerde stand krijgt de herkomstindicatie ‘overeengekomen’. 

Indien de initiërende marktpartij uiterlijk de vijfde werkdag voordat de oorspronkelijk vastgestelde meterstand dispuutvrij is niet expliciet een meterstand heeft vastgesteld op basis van bovenstaande regels, dan is impliciet de alternatieve meterstand van de wederpartij vastgesteld. 

2. De initiërende marktpartij verstuurt de in processtap 1 vastgestelde meterstand binnen één werkdag doch uiterlijk de vijfde werkdag voor het einde van de dispuutstermijn naar de systeembeheerder. 

3. De systeembeheerder ontvangt en verwerkt de vastgestelde meterstand. 

## 4.18.3 Termijnen KA

- a. De dispuuttermijn eindigt op de laatste kalenderdag van de derde maand na de maand waarin de dag valt waarop de meterstand betrekking heeft. 

- b. De wederpartij heeft tot 20 werkdagen voor het einde van de dispuuttermijn om in dispuut te treden. 

- c. De initiërende marktpartij heeft tot uiterlijk vijf werkdagen na ontvangst van het bericht ‘melding dispuut’ de tijd om de alternatieve meterstand te beoordelen en om terug te koppelen naar de wederpartij of de alternatieve meterstand wordt geaccepteerd. 

- d. Indien de initiërende marktpartij akkoord gaat met de alternatieve meterstand van de wederpartij dan dient de initiërende marktpartij deze meterstand zo snel mogelijk doch uiterlijk vijf werkdagen voor het verstrijken van de dispuuttermijn vast te stellen en te verzenden naar de systeembeheerder voor verbruiksbepaling en distributie naar de belanghebbende marktpartijen. 

- e. Indien de initiërende marktpartij niet akkoord gaat met de alternatieve meterstand van de wederpartij heeft de initiërende marktpartij tot maximaal vijf werkdagen voor het einde van de dispuuttermijn om in overleg te treden met de wederpartij en eventueel, na onderlinge overeenstemming over de te maken kosten, een fysieke opname te laten uitvoeren, een meterstand (indien herzien) vast te stellen en te verzenden naar de systeembeheerder. 

- f. Als de initiërende marktpartij niet binnen vijf werkdagen een terugkoppeling op de ‘melding dispuut’ geeft of als de initiërende marktpartij er niet in is geslaagd om uiterlijk vijf werkdagen voor het einde van de dispuuttermijn in overleg een meterstand overeen te komen of een fysieke opname uit te voeren, dan zal de alternatieve meterstand van de wederpartij worden vastgesteld. 

## 4.18.4 Gegevensuitwisseling

### Melding dispuut

|**Melding dispuut**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|O|Ja|Ja|1||
|Transactiedossiernummer|V|Ja|Ja|1|Transactiedossiernummer van de vastgestelde meterstand (en het proces)<br>dat in dispuut wordtgetrokken.|
|Proces ID|V|Ja|Ja|1|Dispuut|
|EAN-code afzender|V|Ja|Ja|1|EAN-code van wederpartij|

|**Melding dispuut**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KA**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code ontvanger|V|Ja|Ja|1|EAN-code van initiërende partij|
|Productsoort|V|Ja|Ja|1|Elektriciteit of gas|
|**_Meetinrichting_**||||**_1 per E_**|**_AN-code_**allocatiepunt|
|Meetinrichtingnummer|V|Ja|Ja|1||
|Aantal telwerken|V|Nee|Ja|1|Aantal actieve telwerken|
|**_Telwerk_**||||**_n per_**|**_meetinrichting_**|
|Registertype|V|Nee|Ja|1|Toegestane waarden:<br>Normaal<br>Laag<br>Teruglevering normaal<br>Terugleveringlaag|
|Meeteenheid|V|Ja|Ja|1||
|Aantal telwielen|V|Ja|Ja|1||
|**_Meterstand_**||||**_1 per t_**|**_elwerk_**|
|Meterstand|V|Ja|Ja|1||
|Meterstanddatum|V|Ja|Ja|1||
|Herkomstindicatie|V|Ja|Ja|1||
|Toelichting|O|Ja|Ja|1||

### Terugkoppeling dispuut

|**Terugkoppeling dispuut**||||||
|---|---|---|---|---|---|
|**Gegeven**|**KV**|**Gas**|**EL**|**1/n**|**Opmerking**|
|EAN-code allocatiepunt|V|Ja|Ja|1||
|Referentie|A|Ja|Ja|1|Gevuld indien meegegeven in de melding|
|Transactiedossiernummer|V|Ja|Ja|1|Transactiedossier van de vastgestelde stand.|
|EAN-code afzender|V|Ja|Ja|1|EAN-code van initiërende partij|
|EAN-code ontvanger|V|Ja|Ja|1|EAN-code van wederpartij|
|Resultaat|V|Ja|Ja|1|Wel of niet geaccepteerd|
|Toelichting resultaat|O|Ja|Ja|1||
