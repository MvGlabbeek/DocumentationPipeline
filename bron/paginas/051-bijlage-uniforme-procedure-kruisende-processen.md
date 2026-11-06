# Bijlage Uniforme procedure Kruisende processen


Mutatie-aanvragen zijn op te delen in mutatie-aanvragen om handelingsbevoegd te worden (leverancierswitch, inhuizing), om de handelingsbevoegdheid te beëindigen (einde levering, uithuizing) en om de balanceringsverantwoordelijkheid te wijzigen (BRP-switch). Onderstaande afspraken zijn gebaseerd op het principe dat indien de leverancier handelingsbevoegd is op de mutatiedatum van een uithuizing, einde levering of BRP-switch deze mutatie-aanvraag dient te worden doorgevoerd. 

Een **leverancierswitch** of **inhuizing** wordt niet altijd doorgevoerd. 

Afhankelijk van de mutatiedatum wordt een aanvraag dan wel / niet gehonoreerd. Een aanvraag voor een **leverancierswitch** of **inhuizing** wordt afgewezen als de mutatiedatum vóór de mutatiedatum van de reeds ingediende aanvraag ligt (Figuur 1). Als de leverancierswitch of inhuizing is ingediend met een mutatiedatum <u>na de reeds ingediende aanvraag wordt de</u> **leverancierswitch** of **inhuizing** aanvraag gehonoreerd (figuur 2). Als de **leverancierswitch** of **inhuizing** is ingediend met dezelfde mutatiedatum dan zal de eerst ontvangen **leverancierswitch** of **inhuizing** worden geannuleerd/overschreven (Figuur 3). Voor de geannuleerde/overschreven leverancierswitch of inhuizing wordt een LOSS verstuurd (Figuur 3) 

Bijlage B1179: Bijlage Uniforme procedure Kruisende processen

Bijlage B1180: Bijlage Uniforme procedure Kruisende processen

Een uithuizing, einde levering of BRP-switch wordt op het moment van indienen afgewezen als er reeds een leverancierswitch, inhuizing, uithuizing of einde levering is ingediend, indien de mutatiedatum van de uithuizing, einde levering of BRP-switch gelijk is of later dan de mutatiedatum van de leverancierswitch, de inhuizing, de uithuizing of de einde levering. 

Bijlage B1181: Bijlage Uniforme procedure Kruisende processen

_De leverancier van de BRP-switch dient in dit geval de balanceringsverantwoordelijke die hij als nieuwe balanceringsverantwoordelijke had gemeld op de hoogte te brengen, dat de BRP-switch niet is doorgegaan (overigens zal deze balanceringsverantwoordelijke ook geen stamgegevens ontvangen)._ 

Een ingediende uithuizing, einde levering of BRP-switch die nog niet geëffectueerd is wordt verwijderd op het moment dat er een leverancierswitch of inhuizing wordt ingediend, indien de mutatiedatum van de uithuizing, einde levering of BRP-switch gelijk is of later dan de mutatiedatum van de leverancierswitch of de inhuizing. 

Bijlage B1182: Bijlage Uniforme procedure Kruisende processen

Een ingediende BRP-switch wordt op het moment van indienen afgewezen als er reeds een uithuizing of einde levering is ingediend, indien de mutatiedatum van de BRP-switch gelijk is of later dan de mutatiedatum van de uithuizing of einde levering. 

Bijlage B1183: Bijlage Uniforme procedure Kruisende processen

Een ingediende BRP-switch die nog niet geëffectueerd is wordt verwijderd op het moment dat er een leverancierswitch, inhuizing, uithuizing of einde levering wordt ingediend, indien de mutatiedatum van de BRP-switch gelijk is of later dan de mutatiedatum van de uithuizing of einde levering. 

Bijlage B1184: Bijlage Uniforme procedure Kruisende processen

Om te garanderen dat er altijd één initiërende leverancier is bij een inhuizing en uithuizing dienen de uithuizingen aan het einde of onmiddellijk na de mutatiedag door de systeembeheerder verwerkt te worden. Hierdoor wordt bij een inhuizing en een uithuizing met dezelfde mutatiedag altijd de inhuizing gehonoreerd en de uithuizing afgewezen. 

Bijlage B1185: Bijlage Uniforme procedure Kruisende processen

De leverancier die een uithuizing, einde levering of BRP-switch initieert wordt op de hoogte gebracht van de verwijdering van een aanvraag door de LOSS veroorzaakt door een aanvraag van de leverancier die een leverancierswitch of inhuizing initieert. 

In een situatie met een uithuizing en een inhuizing van dezelfde leverancier kan het voorkomen dat de uithuizing na de inhuizing wordt doorgevoerd, waardoor de leverancier zichzelf ongewenst uithuist. Om dit te voorkomen zal de leverancier zelf de daartoe benodigde functionaliteit moeten inrichten. Wanneer de leverancier voor een allocatiepunt zowel een einde levering als een uithuizing instuurt voor dezelfde mutatiedatum, worden de berichten door de systeembeheerder in volgorde van ontvangst verwerkt.
