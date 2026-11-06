"""MSP (Word-PDF) -> Markdown zonder afbeeldingen, met figuurverwijzingen.

Gebruik:  python msp_naar_md.py msp.pdf raw.md uitmap/

raw.md is de uitvoer van pymupdf4llm (write_images=True, image_path=img).
Elke afbeelding wordt vervangen door een regel
    Bijlage B1012: Inhuizing KA
en krijgt in figuren.yml een stabiele sleutel (bijv. MP-3.2.1), het type, de
context (paragraaf, SP-code, KA/GA) en de referentie-afbeelding uit de PDF.
"""
import re, sys, json, unicodedata, pathlib, yaml, pymupdf

PDF, RAW, UIT = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
B_START = 1001  # nummerreeks voor deze pilot; B0001..B0999 is in gebruik bij CB

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[*_#`]", "", s)
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"^\s*[-•]\s+", "", s)
    s = re.sub(r"(?<=\w)-\s+", "", s)      # afbreekstreepjes: 'aan- en' == 'aanen'
    return re.sub(r"\s+", " ", s).strip().lower()

toc = [(lvl, re.sub(r"\s+", " ", t).strip(), p) for lvl, t, p in pymupdf.open(PDF).get_toc()]
toc_n = [norm(t) for _, t, _ in toc]

lines = open(RAW, encoding="utf-8").read().splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith("#") and norm(l) == "versiebeheer")
lines = lines[start:]

FOOTER = re.compile(r"^\s*\**\s*\d{1,3}\s*-\s*301\s*\**\s*$|^\s*HerNormo-?\s*$|^\s*Het\s?Normo\s*$", re.I)
IMG = re.compile(r"^!\[\]\((img/msp\.pdf-(\d{4})-(\d{2})\.png)\)\s*$")
NUM = re.compile(r"^(\d+(?:\.\d+)*)\s+(.*)$")
SPC = re.compile(r"\bSP(\d{4}[a-z]?)\b")

out, figs = [], []
ptr = 0                     # wijzer in de TOC (koppen komen in volgorde)
chain = {}                  # niveau -> (nummer, titel)
cur_lvl = 1
counter = {}
last_sp = None              # laatst genoemde SP-code in een kop binnen de huidige 4.x-paragraaf

def variant(texts):
    for t in reversed(texts):
        k, g = re.search(r"\bKA\b|\bKV\b", t), re.search(r"\bGA\b|\bGV\b", t)
        if k and g: return "KA-GA"
        if k: return "KA"
        if g: return "GA"
    return None

def kies_code(parent, leaf, deeper):
    """Paragraaf met meerdere SP-codes: kies de code waarvan de naam het best past bij de kop."""
    codes = ["SP" + c for c in SPC.findall(parent)]
    if len(codes) < 2:
        return codes[0] if codes else None
    if ":" in parent:
        names = re.split(r"\)?\s+&\s+(?=[A-Z])", parent.split(":", 1)[1])
    else:
        names = re.split(r"SP\d{4}[a-z]?", parent)[1:]
    if len(names) != len(codes):
        return codes[0]
    words = set(re.findall(r"[a-zë]{4,}", norm(" ".join([leaf] + deeper))))
    scores = [len(words & set(re.findall(r"[a-zë]{4,}", norm(n)))) for n in names]
    return codes[scores.index(max(scores))]

NUMIDX = {}
for j, (_, t, _) in enumerate(toc):
    mm = re.match(r"^(\d+(?:\.\d+)*)\s", t)
    if mm: NUMIDX.setdefault(mm.group(1), j)

def heading_match(text, strict=False):
    """Genummerde koppen: vaste opzoeking op nummer. Ongenummerde: alleen dichtbij de wijzer."""
    global ptr
    n = norm(text)
    if not n: return None
    mm = re.match(r"^(\d+(?:\.\d+)*)\s", n)
    if mm and mm.group(1) in NUMIDX:
        j = NUMIDX[mm.group(1)]
        if toc_n[j][:25] == n[:25] or toc_n[j].split(" ", 1)[0] == mm.group(1) and len(n) < 160:
            ptr = j + 1
            return toc[j]
    if mm:
        return None
    for j in range(ptr, min(ptr + (4 if strict else 8), len(toc))):
        if re.match(r"^\d", toc_n[j]):
            break          # niet voorbij de volgende genummerde kop zoeken
        if toc_n[j] == n or (len(n) > 12 and toc_n[j].startswith(n[:60])):
            ptr = j + 1
            return toc[j]
    return None

for raw in lines:
    if FOOTER.match(raw):
        continue
    m = IMG.match(raw)
    if m:
        path, page, idx = m.group(1), int(m.group(2)), int(m.group(3))
        nums = [chain[k][0] for k in sorted(chain) if chain[k][0]]
        titles = [chain[k][1] for k in sorted(chain)]
        para = nums[-1] if nums else ""
        top = titles[0] if titles else ""
        var = variant(titles)
        sps = []
        for t in titles:
            sps += ["SP" + c for c in SPC.findall(t)]
        leaf = re.sub(r"</?u>", "", titles[-1]) if titles else ""
        if para.startswith("3.") and para != "3.1":
            n = counter.get(("MP", para), 0)
            counter[("MP", para)] = n + 1
            if n == 0:
                typ, key, titel = "marktprocesplaat", f"MP-{para}", "Procesplaat " + NUM.sub(r"\2", leaf)
            else:
                typ, key, titel = "tijdlijn", f"TL-{para}" + (f"-{n}" if n > 1 else ""), "Tijdlijn " + NUM.sub(r"\2", leaf)
        elif para == "3":
            typ, key, titel = "legenda", "LEG-3", "Legenda procesplaten"
        elif para.startswith("4."):
            # dichtstbijzijnde SP-code; bij meerdere codes in de paragraaf: eerst de kop zelf
            own = ["SP" + c for c in SPC.findall(" ".join(titles[2:]))] or ([last_sp] if last_sp else [])
            code = own[-1] if own else (kies_code(titles[1] if len(titles) > 1 else "", leaf, titles[2:]) if sps else None)
            sfx = f"-{var}" if var else ""
            base = f"{code}{sfx}" if code else f"PB-{'.'.join(para.split('.')[:2])}{sfx}"
            n = counter.get(base, 0) + 1; counter[base] = n
            typ = "subprocesplaat (BPMN)"
            key = base if n == 1 else f"{base}-{n}"
            sub = "" if NUM.match(leaf) else f" – {leaf}"
            titel = f"Subprocesplaat {code or 'zonder SP-code (§' + para + ')'}{' ' + var if var else ''}{sub}"
            if len(set(sps)) > 1 and not own:
                typ += " | controle: meerdere SP-codes in paragraaf"
        else:
            slug = re.sub(r"[^a-z0-9]+", "-", norm(top).replace("bijlage ", ""))[:24].strip("-")
            base = f"FIG-{para or slug}"
            n = counter.get(base, 0) + 1; counter[base] = n
            typ, key, titel = "overige figuur", f"{base}-{n}", leaf
        b = f"B{B_START + len(figs):04d}"
        figs.append(dict(bijlage=b, sleutel=key, type=typ, titel=titel, paragraaf=para,
                         kop=" > ".join(titles), variant=var, sp_codes=sorted(set(sps)),
                         pdf_pagina=page, referentie=path))
        out += [f"Bijlage {b}: {titel}", ""]
        continue
    hm = None
    rest = ""
    bm = re.match(r"^\s*(?:-\s+)?(\*\*[^*]+\*\*)\s*(.*)$", raw)
    if raw.startswith("#"):
        hm = heading_match(raw)
    elif bm:
        hm = heading_match(bm.group(1), strict=bool(bm.group(2).strip()))
        if hm:
            rest = bm.group(2).strip()
    if raw.startswith("#"):
        if not hm and raw.startswith("#"):
            # onbekende kop (niet in TOC): één niveau dieper dan de huidige
            txt = norm(raw)
            if not txt: continue
            lvl = min(cur_lvl + 1, 6)
            title = re.sub(r"[*#]", "", raw).strip()
            out += ["#" * lvl + " " + title, ""]
            chain = {k: v for k, v in chain.items() if k < lvl}; chain[lvl] = ("", title)
            continue
    if hm:
        lvl, title, _ = hm
        mm = NUM.match(title)
        num = mm.group(1) if mm else ""
        cur_lvl = lvl
        chain = {k: v for k, v in chain.items() if k < lvl}
        chain[lvl] = (num, title)
        if lvl <= 2:
            last_sp = None
        else:
            found = SPC.findall(title)
            if found:
                last_sp = "SP" + found[-1]
        out += ["#" * lvl + " " + title, ""]
        if rest:
            out += [rest, ""]
        continue
    out.append(raw)

md = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"
UIT.mkdir(parents=True, exist_ok=True)
kop = ("# Markt- en subprocessen Retailprocessen\n\n"
       "*Het Normo · versie 13.0 · 01-10-2026 · Vastgesteld · pilot-conversie, geen officiële publicatie*\n\n")
(UIT / "MSP-volledig.md").write_text(kop + re.sub(r"^#", "##", md, flags=re.M), encoding="utf-8")
(UIT / "figuren.json").write_text(json.dumps(figs, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(figs), "figuren;", len(md.splitlines()), "regels")
