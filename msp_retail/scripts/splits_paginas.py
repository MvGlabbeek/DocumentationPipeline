"""Splits MSP-volledig.md in pagina's voor de publicatiepipeline (bron/paginas + structuur.yml).

Hoofdstukken worden een pagina; hoofdstuk 4 wordt een pagina per subproces (4.x),
elke bijlage een eigen pagina. De eerste kop van elk bestand is de paginatitel.
"""
import re, sys, pathlib, yaml

SRC, UIT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
lines = SRC.read_text(encoding="utf-8").splitlines()
body = lines[lines.index(next(l for l in lines if l.startswith("## "))):]

pages, cur = [], None
for l in body:
    m2 = re.match(r"^## (.+)$", l)          # hoofdstuk / bijlage
    m3 = re.match(r"^### (4\.\d+ .+)$", l)  # subproces
    if m2 or (m3 and cur and cur["hoofd"].startswith("4 ")):
        title = (m2 or m3).group(1).strip()
        cur = dict(titel=title, hoofd=title if m2 else cur["hoofd"], niveau=2 if m2 else 3, regels=[])
        pages.append(cur)
        continue
    cur["regels"].append(l)

paginas = UIT / "paginas"; paginas.mkdir(parents=True, exist_ok=True)
for f in paginas.glob("*.md"): f.unlink()
tree, ch4 = [], None
for i, p in enumerate(pages, 1):
    shift = p["niveau"] - 1   # koppen schuiven op zodat de pagina met '#' begint
    txt = ["# " + p["titel"], ""]
    for l in p["regels"]:
        m = re.match(r"^(#+) (.*)$", l)
        txt.append("#" * max(2, len(m.group(1)) - shift) + " " + m.group(2) if m else l)
    if p["titel"].startswith("4 "):
        subs = [q["titel"] for q in pages if q["niveau"] == 3]
        txt += ["", "Subprocessen in dit hoofdstuk:", ""] + [f"- {s}" for s in subs]
    slug = re.sub(r"[^a-z0-9]+", "-", p["titel"].lower())[:60].strip("-")
    (paginas / f"{i:03d}-{slug}.md").write_text("\n".join(txt).strip() + "\n", encoding="utf-8")
    if p["niveau"] == 2:
        node = p["titel"]
        if p["titel"].startswith("4 "):
            ch4 = {p["titel"]: []}; node = ch4
        tree.append(node)
    else:
        ch4[next(iter(ch4))].append(p["titel"])

TITEL = "Markt- en subprocessen Retailprocessen"
tops = [k if isinstance(k, str) else next(iter(k)) for k in tree]
(paginas / "000-markt-en-subprocessen-retailprocessen.md").write_text(
    f"# {TITEL}\n\n"
    "Dit is een **pilotpublicatie** van de *Markt- en subprocessen Retailprocessen* (MSP Retail), versie 13.0 "
    "van 01-10-2026, status Vastgesteld. De tekst is automatisch omgezet uit de PDF-versie. "
    "De vastgestelde PDF blijft de officiële versie.\n\n"
    "De procesplaten komen waar mogelijk rechtstreeks uit BizzDesign Horizzon. Onder elke plaat staat een link "
    "naar de view in Horizzon (daarvoor is een account nodig). Platen waarvoor nog geen view bestaat, "
    "zijn voorlopig overgenomen uit de PDF.\n\nInhoud:\n\n" + "\n".join(f"- {t}" for t in tops) + "\n",
    encoding="utf-8")
root = [{TITEL: tree}]
with open(UIT / "structuur.yml", "w", encoding="utf-8") as fh:
    fh.write("# Paginastructuur (gegenereerd door msp_retail/scripts/splits_paginas.py; verplaatsen mag).\n"
             "# - Inspringing = subpagina; de volgorde hier is de volgorde in de publicatie.\n"
             "# - Een titel is de eerste kop van de pagina in bron/paginas.\n\n")
    yaml.safe_dump(root, fh, allow_unicode=True, sort_keys=False, width=200)
print(len(pages), "pagina's")
