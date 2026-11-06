"""Koppel MSP-figuren aan Horizzon-views en schrijf het bijlagenregister.

Gebruik: python koppel.py werk/figuren.json werk/horizzon_catalogus.json beoordeling.yml bron/bijlagen/bijlagen.yml

Regels (in volgorde, de eerste die raakt telt):
  R1  MP-3.N[.M]  -> ArchiMate-view in '03A Views Markt- en subprocessen Retail'
                     met nummer NN[.M] vooraan de viewnaam (MSP §3.N.M == view NN.M)
  R2  SPxxxx-..   -> BPMN-collaboration-view waarvan de naam met SPxxxx begint
  R2b SPxxxx-..   -> geen view, wel ArchiMate-procesobject SPxxxx: 'view ontbreekt'
  R3  TL/LEG/FIG  -> geen Horizzon-bron; tussenoplossing: uitsnede uit de PDF
Een handmatige beoordeling (beoordeling.yml) gaat altijd voor.
"""
import json, re, sys, unicodedata, yaml

FIG, CAT, BEO, UIT = sys.argv[1:5]
figs = json.load(open(FIG, encoding="utf-8"))
cat = json.load(open(CAT, encoding="utf-8"))
beo = yaml.safe_load(open(BEO, encoding="utf-8")) or {}
site, hz = cat["site"], cat["horizzon"]

STOP = set("procesplaat subprocesplaat tijdlijn en de het van een in op ter ten t.b.v. tbv voor met bij door kleine grote ka ga e".split())
def tokens(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return {w for w in re.findall(r"[a-z0-9]+", s) if w not in STOP and not w.isdigit()}
def sim(a, b):
    a, b = tokens(a), tokens(b)
    return round(len(a & b) / len(a | b), 2) if a and b else 0.0
def var_of(s):
    k, g = bool(re.search(r"\bKA\b|\bKleine\b|\bKeine\b", s)), bool(re.search(r"\bGA\b|\bGrote\b", s))
    return "KA-GA" if k and g else "KA" if k else "GA" if g else None

views = cat["views"]
def vnum(v):
    m = re.match(r"^(\d{2})(?:\.(\d))?\.?\s", v["naam"])
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else None

def match(f):
    key, titel = f["sleutel"], re.sub(r"^\d+(\.\d+)*\s+", "", f["titel"])
    m = re.match(r"MP-3\.(\d+)(?:\.(\d+))?$", key)
    if m:
        n, sub = int(m.group(1)), int(m.group(2)) if m.group(2) else None
        kand = [v for v in views if vnum(v) and vnum(v)[0] == n]
        if not kand:
            return dict(status="view ontbreekt", regel="R1", reden=f"geen view met nummer {n:02d} in 03A Retail")
        def score(v):
            vn = vnum(v)
            s = sim(titel, v["naam"])
            s += 0.5 if vn[1] == sub or (sub is None and vn[1] in (None, 1)) else 0
            s += 0.3 if var_of(v["naam"]) == var_of(titel) else 0
            return s
        best = max(kand, key=score)
        nm_ok = vnum(best)[1] == sub or (sub is None and vnum(best)[1] in (None, 1))
        var_ok = var_of(best["naam"]) in (var_of(titel), None)
        s = sim(titel, best["naam"])
        zeker = nm_ok and var_ok and s >= 0.3
        reden = f"nummer {'klopt' if nm_ok else 'wijkt af'}, KA/GA {'klopt' if var_ok else 'wijkt af'}, naamovereenkomst {s}"
        if len(kand) > 1:
            reden += f"; {len(kand)} kandidaten"
        return dict(status="gekoppeld" if zeker else "voorstel", regel="R1", view=best, zekerheid=s, reden=reden)
    m = re.match(r"(SP\d{4}[a-z]?)", key)
    if m:
        code = m.group(1)
        bp = [v for v in views if v["soort"].startswith("BPMN") and v["naam"].startswith(code)]
        if bp:
            v = bp[0]
            several = sum(1 for g in figs if g["sleutel"].startswith(code + "-")) > 1
            return dict(status="voorstel" if several else "gekoppeld", regel="R2", view=v, zekerheid=1.0,
                        reden="SP-code in viewnaam" + ("; meerdere MSP-figuren voor deze code, view dekt mogelijk niet alles" if several else ""))
        po = [o for o in cat["sp_procesobjecten"] if o["sp"] == code]
        return dict(status="view ontbreekt", regel="R2b", procesobject=po[0] if po else None,
                    reden=("procesobject in Horizzon, nog geen BPMN-view" if po else "SP-code niet gevonden in Horizzon"))
    if key.startswith("PB-"):
        return dict(status="view ontbreekt", regel="R2b", reden="MSP-paragraaf zonder SP-code; eerst code toekennen")
    return dict(status="geen Horizzon-bron", regel="R3", reden="tijdlijn/legenda/toelichting; tussenoplossing uitsnede uit PDF")

reg, rapport = {}, []
for f in figs:
    b = f["bijlage"]
    over = beo.get(b, {})
    if "sleutel" in over:
        oud = re.match(r"(SP\d{4}[a-z]?)", f["sleutel"])
        nieuw = re.match(r"(SP\d{4}[a-z]?)", over["sleutel"])
        if oud and nieuw:
            f["titel"] = f["titel"].replace(oud.group(1), nieuw.group(1))
        f["sleutel"] = over["sleutel"]
    r = match(f)
    if "view_id" in over:
        v = next(v for v in views if v["id"] == over["view_id"])
        r = dict(status="gekoppeld", regel="handmatig", view=v, zekerheid=1.0, reden=over.get("reden", "handmatig beoordeeld"))
    elif over.get("status"):
        r["status"], r["reden"] = over["status"], over.get("reden", r["reden"])
    e = dict(titel=re.sub(r"^\d+(\.\d+)*\s+", "", f["titel"]), sleutel=f["sleutel"], soort=f["type"].split(" |")[0],
             msp_paragraaf=f["paragraaf"], msp_pagina=f["pdf_pagina"], status=r["status"], regel=r["regel"], reden=r["reden"])
    if r.get("view"):
        e["horizzon_view_id"] = r["view"]["id"]
        e["horizzon_view"] = r["view"]["naam"]
        e["horizzon"] = f"{hz}/sites/{site}/views/{r['view']['id']}"
    if r.get("procesobject"):
        e["horizzon_procesobject"] = r["procesobject"]["naam"]
        e["horizzon_procesobject_link"] = f"{hz}/sites/{site}/objects/{r['procesobject']['id']}/explore"
    if "controle" in f["type"] and "sleutel" not in over:
        e["status"] = "voorstel" if e["status"] == "gekoppeld" else e["status"]
        e["reden"] += "; meerdere SP-codes in paragraaf, sleutel controleren"
    e["referentie_pdf"] = f["referentie"]
    reg[b] = e

with open(UIT, "w", encoding="utf-8") as fh:
    fh.write("# Bijlagenregister MSP-pilot. Gegenereerd door scripts/koppel.py; handmatige keuzes in beoordeling.yml.\n"
             "# status: gekoppeld | voorstel (bevestigen) | view ontbreekt | geen Horizzon-bron\n")
    yaml.safe_dump(reg, fh, allow_unicode=True, sort_keys=False, width=200)
from collections import Counter
print(Counter(e["status"] for e in reg.values()))
