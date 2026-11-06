"""Schrijft het dekkingsrapport (Markdown) uit het bijlagenregister."""
import sys, yaml, collections
reg = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
uit = open(sys.argv[2], "w", encoding="utf-8")
w = lambda s="": uit.write(s + "\n")
soorten = collections.defaultdict(collections.Counter)
for e in reg.values(): soorten[e["soort"]][e["status"]] += 1
st = ["gekoppeld", "voorstel", "view ontbreekt", "geen Horizzon-bron"]
w("# Dekkingsrapport MSP-figuren ↔ Horizzon\n")
w(f"{len(reg)} figuren in MSP v13.0. Gegenereerd uit `bron/bijlagen/bijlagen.yml`.\n")
w("| Soort | " + " | ".join(st) + " | Totaal |"); w("|---|" + "---:|" * (len(st) + 1))
for s, c in soorten.items():
    w(f"| {s} | " + " | ".join(str(c[x]) for x in st) + f" | {sum(c.values())} |")
tot = collections.Counter(e["status"] for e in reg.values())
w("| **Totaal** | " + " | ".join(f"**{tot[x]}**" for x in st) + f" | **{len(reg)}** |\n")
for status, kop in [("voorstel", "Te bevestigen koppelingen"), ("gekoppeld", "Gekoppeld")]:
    w(f"## {kop}\n"); w("| Bijlage | Sleutel | MSP | Horizzon-view | Toelichting |"); w("|---|---|---|---|---|")
    for b, e in reg.items():
        if e["status"] == status:
            w(f"| {b} | `{e['sleutel']}` | §{e['msp_paragraaf']} p.{e['msp_pagina']} | [{e['horizzon_view']}]({e['horizzon']}) | {e['reden']} |")
    w()
w("## Views die ontbreken\n"); w("| Bijlage | Sleutel | MSP | Wat er wel is |"); w("|---|---|---|---|")
for b, e in reg.items():
    if e["status"] == "view ontbreekt":
        wel = f"[{e['horizzon_procesobject']}]({e['horizzon_procesobject_link']})" if e.get("horizzon_procesobject") else e["reden"]
        w(f"| {b} | `{e['sleutel']}` | §{e['msp_paragraaf']} p.{e['msp_pagina']} | {wel} |")
w("\n## Zonder Horizzon-bron (tussenoplossing: uitsnede uit de PDF)\n")
w("| Bijlage | Sleutel | Titel | MSP |"); w("|---|---|---|---|")
for b, e in reg.items():
    if e["status"] == "geen Horizzon-bron":
        w(f"| {b} | `{e['sleutel']}` | {e['titel']} | §{e['msp_paragraaf'] or '-'} p.{e['msp_pagina']} |")
