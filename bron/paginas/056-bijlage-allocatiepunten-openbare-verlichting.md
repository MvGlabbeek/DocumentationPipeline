# Bijlage Allocatiepunten openbare verlichting


Voor allocatiepunten die worden gebruikt voor openbare verlichting (OVL) geldt een aantal specifieke aandachtspunten. Artikel 1.3 van de Energiewet schrijft voor dat de allocatiepunten van een organisatorische eenheid, die zich in hoofdzaak bezighoudt met openbare verlichting, geen onderdeel hoeven te zijn van het segment van kleine aansluitingen. OVL-aansluitingen met een capaciteit groter dan 3*80A zijn reguliere grote aansluitingen. OVL-aansluitingen met een capaciteit kleiner of gelijk aan 3*80A kunnen worden aangemerkt als A1 (artikel 1.3 lid 1 of lid 2) en worden behandeld conform de marktprocessen voor grote aansluitingen. Partijen hebben in de praktijk zelf de keuze om onder het segment van kleine aansluitingen te vallen of onder A1. 

De processen voor meetgegevens zijn voor OVL gelijk aan de reguliere proces voor kleine- of grote aansluitingen, tenzij specifiek benoemd in deze bijlage. 

## Registratiewijze van allocatiepunten bijbehorend bij OVL-aansluitingen in het aansluitingenregister

In de basis kunnen in het aansluitingenregister vier varianten worden onderscheiden voor de registratie van OVL-allocatiepunten: 

Variant 1: Individueel bemeten OVL-allocatiepunten; 

Variant 2: Collectief bemeten OVL-allocatiepunten; 

Variant 3: Onbemeten OVL-allocatiepunten (individuele afhandeling); 

Variant 4: Onbemeten OVL-allocatiepunten (gegroepeerde afhandeling). 

Daarnaast kan er door de systeembeheerder gebruik worden gemaakt van een (administratief) allocatiepunt voor systeemkosten OVL: 

Variant 5: Allocatiepunt voor collectieve systeemkosten OVL 

In deze paragraaf is per variant een korte toelichting opgenomen op de registratiewijze in het aansluitingenregister, zodat herkend kan worden wat voor allocatiepunt het betreft. 

<mark>De attributen ‘Soort aansluiting’ en ‘Gebruik aansluiting’ maken momenteel geen onderdeel uit van de stamgegevensberichten voor allocatiepunten in zowel het kleinverbruik-, grootverbruik- en A1 verbruikssegment. Dit geldt ook voor het attribuut ‘Fysieke capaciteit’ in segment van kleine aansluitingen. In de tabellen van deze bijlage zijn deze attributen daarom niet zichtbaar.</mark> Stamgegevens van ‘Bijzondere aansluitingen’ worden in zijn geheel niet gedeeld met marktpartijen middels stamgegevensberichten. 

## Variant 1: Individueel bemeten OVL-allocatiepunten

Kenmerkend voor bemeten OVL-allocatiepunten is het volgende: 

- Individueel bemeten lichtmast (allocatiepunt), of; 

- Bemeten overdrachtspunt met de OVL-installatie van de klant; 

- De afhandeling van deze variant is niet anders dan reguliere bemeten allocatiepunten, 

- alleen het profiel E4A is specifiek voor OVL; 

- Alle reguliere processen zijn van toepassing, waaronder collecteren, valideren en 

- vaststellen van meterstanden. 

- Voor allocatiepunten op een kleine aansluiting kan de systeembeheerder gevraagd 

- worden om een (tussentijdse) meteropname te verrichten in situaties waar: 

   - <mark>de meetinrichting zonder communicatiefunctionaliteit niet uitleesbaar is door</mark> 

   - <mark>de aangeslotene of</mark> 

   - <mark>de meetinrichting met communicatiefunctionaliteit niet op afstand uitleesbaar</mark> 

   - <mark>is</mark> 

- Alle systeembeheerders kennen deze variant. 

De allocatiepunten zijn te herkennen in de stamgegevens aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|E4A|N.v.t.|E4A|
|Wijze van bemeting|JRL|N.v.t.|TMT/JRL/MND|
|Fysieke capaciteit||N.v.t.|1x6A t/m 3x80A|
|Allocatiemethode|PRF of SMA|N.v.t.|PRF of TMT|
|SJA/SJI Normaal tarief<br>SJA/SJI Laagtarief|> 0 (automatisch berekend<br>conform MSP-R)|N.v.t.|> 0 (automatisch berekend<br>conform MSP-R)|

## Variant 2: Collectief bemeten OVL-allocatiepunten

## Kenmerkend voor collectief bemeten OVL-allocatiepunten is het volgende:

- De lichtmasten (allocatiepunten) bevinden zich achter een voedingspunt met eigen 

- meter (meter bevindt zich bijv. in middenspanningsruimte of OV-kast); 

- De individuele lichtmasten (allocatiepunten) gaan niet zelfstandig mee in de allocatie 

- (afhandeling van verbruiken middels de allocatiepunt) en zijn niet opgenomen in het aansluitingenregister; 

- De meter is gekoppeld aan het voedingspunt. Dit voedingspunt is als allocatiepunt 

- geregistreerd in het aansluitingenregister; 

- De registratiewijze onderscheidt zich niet van het individueel bemeten allocatiepunt 

- (variant 1), echter achter de administratief allocatiepunt bevinden zich meerdere individuele lichtmasten (allocatiepunten), dit vertaalt zich naar één gesommeerd SJA/SJI op het allocatiepunt; 

- Alle reguliere processen zijn van toepassing, waaronder collecteren, valideren en 

- vaststellen van meterstanden. 

- Voor allocatiepunten op een kleine aansluitingen kan de systeembeheerder gevraagd 

- worden om een (tussentijdse) meteropname te verrichten in situaties waar: 

   - <mark>de meetinrichting zonder communicatiefunctionaliteit niet uitleesbaar is door</mark> 

   - <mark>de aangeslotene of</mark> 

   - <mark>de meetinrichting met communicatiefunctionaliteit niet op afstand uitleesbaar</mark> 

   - <mark>is.</mark> 

- Systeembeheerders Liander, Enexis en Rendo kennen deze variant. 

Het allocatiepunt is in de stamgegevens te herkennen aan de volgende registratiewijze (indien van toepassing): 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|E4A|N.v.t.|E4A|
|Wijze van bemeting|JRL|N.v.t.|JRL/MND/TMT|
|Fysieke capaciteit||N.v.t.|1x6A t/m 3x80A|
|Allocatiemethode|PRF of SMA|N.v.t.|PRF of TMT|
|SJA/SJI Normaal tarief<br>SJA/SJI Laag tarief|> 0 (automatisch berekend<br>conform MSP-R op basis van<br>meetgegevensvoedingspunt)|N.v.t.|> 0 (automatisch berekend<br>conform MSP-R op basis van<br>meetgegevens voedingspunt)|

## Variant 3: Onbemeten OVL-allocatiepunten (Individuele afhandeling)

Kenmerkend voor onbemeten OVL-allocatiepunten die individueel worden afgehandeld is het volgende: 

- Betreft een onbemeten lichtmast (allocatiepunt); 

- Allocatiepunt gaat zelfstandig mee in allocatie (middels profielallocatie, voorzien van 

- SJA/SJI); 

- Attribuut ‘Locatieomschrijving’ geeft (eventueel) een indicatie dat het OVL betreft; 

- De afhandeling van deze variant is niet anders dan regulier onbemeten 

- allocatiepunten; 

- Systeembeheerder Stedin, Stedin - regio Zeeland en Enexis kennen deze variant. 

De allocatiepunten zijn te herkennen in de stamgegevens aan de volgende registratiewijze (indien van toepassing): 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|E1A|N.v.t.|N.v.t.|
|Wijze van bemeting|OBM|N.v.t.|N.v.t.|
|Fysieke capaciteit||N.v.t.|N.v.t.|
|Allocatiemethode|PRF|N.v.t.|N.v.t.|
|Locatie omschrijving|Vrije tekst|N.v.t.|N.v.t.|
|SJA/SJI Normaal tarief<br>SJA/SJI Laagtarief|> 0 (op basis van opgave klant)|N.v.t.|N.v.t.|

**Variant 4: Onbemeten OVL-allocatiepunten (Gegroepeerde afhandeling)** 

Kenmerkend voor onbemeten OVL-allocatiepunten die gegroepeerd worden afgehandeld is het volgende: 

- Betreft meerdere onbemeten lichtmasten (allocatiepunten) achter een onbemeten 

- voedingspunt, per gebied (bijv. wijk of gemeente) ; 

- Allocatiepunten gaan niet zelfstandig mee in allocatie, volumes worden afgehandeld 

- middels een allocatiepunt; 

- Alle systeembeheerders kennen deze variant (m.u.v. Rendo), waarbij Liander en Stedin 

- de onbemeten voedingspunten ook hebben opgenomen in het aansluitingenregister. 

De onbemeten voedingspunten (allocatiepunten) zijn te herkennen in de stamgegevens aan de volgende registratiewijze (indien van toepassing): 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|OPC|N.v.t.|OPC|
|Wijze van bemeting|OBM|N.v.t.|OBM|
|Fysieke capaciteit||N.v.t.|1x6A t/m 3x25A|
|Allocatiemethode|PRF|N.v.t.|PRF|

Aan het profiel ‘OPC’ i.c.m. allocatiemethode ‘PRF’ is te herkennen dat deze allocatiepunten alleen zijn vastgelegd in het aansluitingenregister ter registratie voor de systeembeheerder. 

De volumes van de individuele onbemeten lichtmasten (allocatiepunten) worden gegroepeerd afgehandeld middels het allocatiepunt. Hieronder een toelichting per distributiesysteembeheerder omtrent de registratie van dit allocatiepunten in het aansluitingenregister. 

## Enexis

De volumes van de achterliggende lichtmasten (allocatiepunten) worden binnen Enexis afgewikkeld door A1-allocatiepunten, waarbij het volume wordt gedimensioneerd naar telemetrie-waarden (telemetrie-allocatie). De leverancier ontvangt maandvolumes. 

Het administratieve allocatiepunt t.b.v. afhandeling volume is in de stamgegevens te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|N.v.t.|N.v.t.|OPC|
|Wijze van bemeting|N.v.t.|N.v.t.|OBM|
|Fysieke capaciteit||N.v.t.|1x6A|
|Allocatiemethode|N.v.t.|N.v.t.|TMT|

## Liander

De volumes van de achterliggende lichtmasten (allocatiepunten) worden binnen Liander afgewikkeld middels allocatiepunten, met onderscheid tussen allocatiepunten waarbij het volumes wordt gedimensioneerd naar telemetrie-waarden (telemetrie-allocatie) of wordt afgehandeld door profielallocatie. 

De allocatiepunten t.b.v. afhandeling volumes voor telemetrie-allocatie betreft bijzondere aansluitingen en zijn niet zichtbaar voor marktpartijen middels stamgegevens. De leverancier ontvangt maandvolumes. 

De allocatiepunten t.b.v. afhandeling volume voor profiel-allocatie is te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|E4A|n.v.t.|E4A|
|Wijze van bemeting|AND|n.v.t.|AND|
|Fysieke capaciteit||n.v.t.|1x6A|
|Allocatiemethode|PRF|n.v.t.|PRF|
|SJA/SJI Normaal tarief<br>SJA/SJI Laagtarief|> 0 (op basis van opgave klant)|n.v.t.|> 0 (op basis van opgave<br>klant)|

## Stedin

De volumes van de achterliggende lichtmasten (allocatiepunten) worden binnen Stedin afgewikkeld middels kleine- en grote aansluitingen, met onderscheid tussen allocatiepunten waarbij het volumes wordt gedimensioneerd naar telemetrie-waarden (telemetrie-allocatie) of wordt afgehandeld door profielallocatie. 

Het allocatiepunt voor telemetrie-allocatie is te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|OPC|OPC|N.v.t.|
|Wijze van bemeting|OBM|OBM|N.v.t.|
|Fysieke capaciteit||1x6A t/m 1x10A|N.v.t.|
|Allocatiemethode|TMT|TMT|N.v.t.|

De leverancier ontvangt maandvolumes. 

Het allocatiepunt voor profielallocatie is te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|N.v.t.|N.v.t.|E4A|
|Wijze van bemeting|N.v.t.|N.v.t.|AND|
|Fysieke capaciteit||N.v.t.|1x6A t/m 1x10A|
|Allocatiemethode|N.v.t.|N.v.t.|PRF|
|SJA/SJI Normaal tarief<br>SJA/SJI Laagtarief|N.v.t.|N.v.t.|> 0 (op basis van opgave klant)|

## Stedin – regio Zeeland

De volumes van de achterliggende lichtmasten (allocatiepunten) worden binnen Stedin – regio Zeeland afgewikkeld door A1-allocatiepunten, waarbij het verbruik wordt gedimensioneerd naar telemetriewaarden (telemetrie-allocatie). De leverancier ontvangt maandvolumes. 

Het allocatiepunt t.b.v. afhandeling verbruik is te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|N.v.t.|N.v.t.|OPC|
|Wijze van bemeting|N.v.t.|N.v.t.|OBM|
|Fysieke capaciteit||N.v.t.|OBK|
|Allocatiemethode|N.v.t.|N.v.t.|TMT|

## Westland Infra

De volumes van de achterliggende lichtmasten (allocatiepunten) worden binnen Westland Infra afgewikkeld door A1-allocatiepunten, met onderscheid tussen allocatiepunten waarbij het volumes wordt gedimensioneerd naar telemetrie-waarden (telemetrie-allocatie) of wordt afgehandeld door profielallocatie. 

Het allocatiepunt t.b.v. afhandeling volumes (telemetrie-allocatie) is te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|N.v.t.|N.v.t.|OPC|
|Wijze van bemeting|N.v.t.|N.v.t.|OBM|
|Fysieke capaciteit||N.v.t.|1x6A t/m 3x25A|
|Allocatiemethode|N.v.t.|N.v.t.|TMT|

De leverancier ontvangt maandvolumes. 

Het allocatiepunt voor profielallocatie is te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|N.v.t.|N.v.t.|E4A|
|Wijze van bemeting|N.v.t.|N.v.t.|AND|
|Fysieke capaciteit||N.v.t.|3x25A|
|Allocatiemethode|N.v.t.|N.v.t.|PRF|
|SJA/SJI Normaal tarief<br>SJA/SJI Laagtarief|N.v.t.|N.v.t.|> 0 (op basis van opgave<br>klant)|

## Coteq

De volumes van de achterliggende lichtmasten (allocatiepunten) worden binnen Coteq afgewikkeld middels allocatiepunten behorende bij een kleine aansluiting, waarbij het volume wordt afgehandeld door profielallocatie. 

Het allocatiepunt t.b.v. afhandeling verbruik voor profielallocatie is te herkennen aan de volgende registratiewijze: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|E4A|N.v.t.|N.v.t.|
|Wijze van bemeting|AND|N.v.t.|N.v.t.|
|Fysieke capaciteit||N.v.t|N.v.t|
|Allocatiemethode|PRF|N.v.t.|N.v.t.|
|SJA/SJI Normaal tarief<br>SJA/SJI Laagtarief|> 0 (op basis van opgave klant)|N.v.t.|N.v.t.|

## Systeemkosten OVL

Bij OVL-allocatiepunten komen bij zowel de fysieke als de allocatiepunten de volgende situaties voor bij de Captarcode: 

- Regulier (op basis soort aansluiting, additionele allocatiepunten, fysieke capaciteit en 

- wijze van bemeting): de systeemkosten worden regulier verrekend middels het individuele allocatiepunt; 

- Captarcode is gekoppeld aan een nul-tarief: De systeemkosten van het allocatiepunt 

- worden middels een (ander) allocatiepunt verrekend; 

- Captarcode is gekoppeld aan een uniek tarief: De systeemkosten van achterliggende 

- allocatiepunt worden middels dit allocatiepunt verrekend. 

Als er wijzigingen plaatsvinden in het aantal allocatiepunten van de bundel (uniek tarief), dan wordt het totaaltarief niet tussentijds aangepast. De systeembeheerder verrekent de kosten voor de allocatiepunten, die tussentijds worden aangelegd of verwijderd, bilateraal met de betreffende gemeente. 

## Variant 5: Allocatiepunt voor systeemkosten OVL

De distributiesysteembeheerder kan ervoor kiezen om de systeemkosten af te handelen middels een separaat allocatiepunt. Dit wordt toegepast bij Enexis en Liander. Aan het profiel ‘OPC’ i.c.m. allocatiemethode ‘PRF’ is te herkennen dat deze allocatiepunten niet worden gebruikt voor meetgegevensprocessen. 

## Enexis

Enexis maakt gebruik van allocatiepunten voor systeemkosten OVL. Deze zijn voor allocatiepunten behorende bij een kleine aansluiting als volgt te herkennen: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Type allocatiepunt|Normaal|N.v.t.|N.v.t.|
|Profielcategorie|OPC|N.v.t.|N.v.t.|
|Wijze van bemeting|OBM|N.v.t.|N.v.t.|
|Fysieke capaciteit||N.v.t.|N.v.t.|
|Allocatiemethode|PRF|N.v.t.|N.v.t.|
|Locatieomschrijving|Fictieve EAN-code t.b.v.<br>afrekeningOVL|N.v.t.|N.v.t.|

## Liander

Voor allocatiepunten behorende bij een kleine aansluiting en allocatiepunten behorende bij een grote aansluiting maakt Liander gebruik van allocatiepunten voor systeemkosten OVL. Deze zijn als volgt geregistreerd: 

|**Gegeven**||||
|---|---|---|---|
|Verbruikssegment|KA|GA|A1|
|Profielcategorie|OPC|N.v.t.|OPC|
|Wijze van bemeting|OBM|N.v.t.|OBM|
|Fysieke capaciteit||N.v.t.|OBK|
|Allocatiemethode|PRF|N.v.t.|PRF|

Het A1-allocatiepunt wordt alleen gebruikt voor de eigen administratie van de systeembeheerder t.b.v. de facturatie van systeemkosten door de systeembeheerder.
