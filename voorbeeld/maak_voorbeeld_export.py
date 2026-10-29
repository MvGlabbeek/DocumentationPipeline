"""Maakt een synthetische Confluence Cloud HTML-export (structuur zoals 'Export space > HTML')."""
import zipfile, io, sys
from PIL import Image, ImageDraw

def png(tekst, kleur):
    im = Image.new("RGB", (640, 300), "white"); d = ImageDraw.Draw(im)
    d.rectangle([10, 10, 630, 290], outline=kleur, width=4)
    for i, (x, y) in enumerate([(60, 120), (260, 120), (460, 120)]):
        d.rectangle([x, y, x + 120, y + 60], fill=kleur); d.text((x + 10, y + 22), f"Element {i+1}", fill="white")
    d.text((30, 30), tekst, fill="black")
    b = io.BytesIO(); im.save(b, "PNG"); return b.getvalue()

SP = "VOORBEELD"
def pagina(titel, pid, kruimels, inhoud):
    kr = '<li class="first"><span><a href="index.html">Voorbeeldruimte</a></span></li>' + "".join(
        f'<li><span><a href="{h}">{t}</a></span></li>' for t, h in kruimels)
    return f"""<!DOCTYPE html><html><head><title>Voorbeeldruimte : {titel}</title>
<link rel="stylesheet" href="styles/site.css" type="text/css" /></head><body class="theme-default aui-theme-default">
<div id="page"><div id="main" class="aui-page-panel"><div id="main-header">
<div id="breadcrumb-section"><ol id="breadcrumbs">{kr}</ol></div>
<h1 id="title-heading" class="pagetitle"><span id="title-text"> Voorbeeldruimte : {titel} </span></h1></div>
<div id="content" class="view"><div class="page-metadata">Created by <span class='author'> Martijn</span></div>
<div id="main-content" class="wiki-content group">{inhoud}</div></div></div></div></body></html>"""

HZ = "https://hetnormo.horizzon.cloud/repository/views/9f1c2a7e-0001"
HZ2 = "https://hetnormo.horizzon.cloud/repository/views/9f1c2a7e-0002"
p = {}
p["Voorbeeldruimte_1001.html"] = pagina("Architectuur MSP CB", 1001, [], f"""
<p>Dit is de startpagina van de <strong>voorbeeld</strong>ruimte voor de pilot.</p>
<div class="toc-macro client-side-toc-macro"><ul><li>Inhoud</li></ul></div>
<h1 id="ArchitectuurMSPCB-Leeswijzer">Leeswijzer</h1>
<p>Lees eerst de <a href="Architectuurvisie_1002.html">architectuurvisie</a> en daarna de
<a href="Principes_1003.html#Principes-Ontwerpprincipes">ontwerpprincipes</a>.</p>""")
p["Architectuurvisie_1002.html"] = pagina("Architectuurvisie", 1002, [("Architectuur MSP CB", "Voorbeeldruimte_1001.html")], f"""
<h1 id="Architectuurvisie-Context">Context</h1>
<p>De context staat in het onderstaande diagram uit BizzDesign.</p>
<p><iframe src="{HZ}" title="Contextdiagram" width="800" height="500"></iframe></p>
<div class="confluence-information-macro confluence-information-macro-note"><span class="aui-icon confluence-information-macro-icon"></span>
<div class="confluence-information-macro-body"><p>Het diagram is een momentopname.</p></div></div>
<h1 id="Architectuurvisie-Overzicht">Overzicht</h1>
<p><span class="confluence-embedded-file-wrapper"><img class="confluence-embedded-image" src="attachments/1002/2001.png"
 data-image-src="attachments/1002/2001.png" data-linked-resource-id="2001" data-linked-resource-default-alias="overzicht-lagen.png"
 data-linked-resource-container-id="1002" alt="Lagenmodel" title="Lagenmodel"></span></p>
<p>Zie ook de uitwerking in de <a href="Capabilitykaart_1005.html">capabilitykaart</a>. <img class="emoticon emoticon-smile" src="images/icons/emoticons/smile.svg" alt="(smile)"></p>""")
p["Principes_1003.html"] = pagina("Principes", 1003, [("Architectuur MSP CB", "Voorbeeldruimte_1001.html")], """
<h1 id="Principes-Ontwerpprincipes">Ontwerpprincipes</h1>
<div class="table-wrap"><table class="confluenceTable"><tbody>
<tr><th class="confluenceTh">ID</th><th class="confluenceTh">Principe</th><th class="confluenceTh">Rationale</th></tr>
<tr><td class="confluenceTd">P01</td><td class="confluenceTd">Gegevens worden eenmalig vastgelegd</td><td class="confluenceTd">Voorkomt inconsistentie</td></tr>
<tr><td class="confluenceTd">P02</td><td class="confluenceTd">Open standaarden waar mogelijk</td><td class="confluenceTd">Interoperabiliteit; zie https://www.forumstandaardisatie.nl</td></tr>
</tbody></table></div>
<h1 id="Principes-Rollen">Rollen</h1>
<div class="table-wrap"><table class="confluenceTable"><tbody>
<tr><th class="confluenceTh" colspan="2">Rollen en verantwoordelijkheden</th></tr>
<tr><td class="confluenceTd">Architect</td><td class="confluenceTd"><ul><li>Ontwerp</li><li>Review</li></ul></td></tr>
</tbody></table></div>
<p>Download het <a href="attachments/1003/2002.pdf">principedocument (pdf)</a>.</p>""")
p["Bedrijfsarchitectuur_1004.html"] = pagina("Bedrijfsarchitectuur", 1004, [("Architectuur MSP CB", "Voorbeeldruimte_1001.html")], """
<p>Deze sectie beschrijft de bedrijfsarchitectuur.</p>""")
p["Capabilitykaart_1005.html"] = pagina("Capabilitykaart", 1005, [("Architectuur MSP CB", "Voorbeeldruimte_1001.html"), ("Bedrijfsarchitectuur", "Bedrijfsarchitectuur_1004.html")], f"""
<p><a href="{HZ2}">Capabilitykaart MSP CB</a></p>
<p>De capabilities sluiten aan op de <a href="{HZ}">contextview in Horizzon</a> en op de principes uit <a href="Principes_1003.html">Principes</a>.</p>""")
p["Ketenprocessen_1006.html"] = pagina("Ketenprocessen", 1006, [("Architectuur MSP CB", "Voorbeeldruimte_1001.html"), ("Bedrijfsarchitectuur", "Bedrijfsarchitectuur_1004.html")], """
<p>Het ketenproces in een draw.io-diagram:</p>
<p><img class="confluence-embedded-image" src="attachments/1006/2003.png" data-image-src="attachments/1006/2003.png" data-linked-resource-id="2003" data-linked-resource-default-alias="ketenproces.drawio.png"></p>
<p>Zie <a href="Onbekend_9999.html">een pagina in een andere space</a> en <a href="https://hetnormo.atlassian.net/wiki/spaces/ARCH/pages/123">Confluence</a>.</p>""")
p["Interne-notities_1007.html"] = pagina("Interne notities", 1007, [("Architectuur MSP CB", "Voorbeeldruimte_1001.html")], """
<p>Niet voor publicatie.</p><div class="labels-content"><ul class="label-list"><li><a class="aui-label" rel="tag" href="#">intern</a></li></ul></div>""")

index = """<!DOCTYPE html><html><head><title>Voorbeeldruimte</title></head><body><div id="main-content">
<div class="pageSection"><div class="pageSectionHeader"><h2 class="pageSectionTitle">Space Details:</h2></div></div>
<div class="pageSection"><div class="pageSectionHeader"><h2 class="pageSectionTitle">Available Pages:</h2></div>
<ul><li><a href="Voorbeeldruimte_1001.html">Architectuur MSP CB</a><ul>
 <li><a href="Architectuurvisie_1002.html">Architectuurvisie</a></li>
 <li><a href="Principes_1003.html">Principes</a></li>
 <li><a href="Bedrijfsarchitectuur_1004.html">Bedrijfsarchitectuur</a><ul>
   <li><a href="Capabilitykaart_1005.html">Capabilitykaart</a></li>
   <li><a href="Ketenprocessen_1006.html">Ketenprocessen</a></li></ul></li>
 <li><a href="Interne-notities_1007.html">Interne notities</a></li>
</ul></li></ul></div></div></body></html>"""

with zipfile.ZipFile(sys.argv[1], "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr(f"{SP}/index.html", index)
    for n, h in p.items(): z.writestr(f"{SP}/{n}", h)
    z.writestr(f"{SP}/attachments/1002/2001.png", png("Lagenmodel (voorbeeld)", "#00857c"))
    z.writestr(f"{SP}/attachments/1006/2003.png", png("Ketenproces (voorbeeld, draw.io)", "#3a6ea5"))
    z.writestr(f"{SP}/attachments/1003/2002.pdf", b"%PDF-1.4\n% voorbeeld\n")
    z.writestr(f"{SP}/styles/site.css", "body{}")
print("ok")
