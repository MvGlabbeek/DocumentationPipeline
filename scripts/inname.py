"""Inname van losse, per pagina uit Confluence geëxporteerde Markdown-bestanden.

Gebruik: python scripts/inname.py [--controle]

1. Leest alle .md in bron/paginas/ (bestandsnamen maken niet uit). De eerste kop is de titel.
   Dezelfde pagina meerdere keren geëxporteerd (Pagina.md, Pagina-1.md, ...)? Dan telt de
   laatste download (hoogste volgnummer).
2. Bouwt de paginaboom zoals in Confluence:
   - bron/structuur.yml is leidend (inspringing = subpagina, volgorde = navigatie);
   - pagina's die daar nog niet in staan worden geplaatst onder de pagina die ernaar linkt
     (Confluence-link) of die hun titel in een opsomming noemt, op die plek in de volgorde;
   - pagina's waarnaar gelinkt wordt maar die (nog) niet zijn aangeleverd, komen als
     'nog geen bestand' in de structuur, zodat ze later vanzelf op de goede plek landen.
   De aangevulde structuur wordt teruggeschreven naar bron/structuur.yml (behalve met --controle).
3. Normaliseert elke pagina naar _build/paginas/:
   - de titelkop gaat naar de front matter, koppen schuiven een niveau op;
   - Confluence-links naar gepubliceerde pagina's worden links binnen de publicatie,
     links naar niet-gepubliceerde pagina's worden gewone tekst;
   - een regel 'Bijlage B0007' (of [[bijlage:B0007]]) toont bijlage B0007 op die plek;
     'bijlage B0007' in een zin wordt een verwijzing. Bijlagen met 'pagina' en 'na' in
     bron/bijlagen/bijlagen.yml worden automatisch na die tekst geplaatst.
"""
from __future__ import annotations

import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote_plus

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemeen import (BRONPAGINAS, PAGINAS, ROOT, STRUCTUUR, bestand_van, lees_register,  # noqa: E402
                    schrijf_md)

RE_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
RE_KOP = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t#]*$", re.M)
RE_LIJST = re.compile(r"^[ \t]*(?:\d+[.)]|[-*+])[ \t]+(.+)$", re.M)
RE_BIJLAGEREGEL = re.compile(r"^[ \t>]*[*_]*\s*(?:\[\[bijlage:(B\d{4})\]\]|bijlage\s+(B\d{4}))\b[*_]*[ \t]*[:\-–]?[ \t]*(.*?)[*_ \t]*$",
                             re.M | re.I)
RE_BIJLAGE_INLINE = re.compile(r"\b[Bb]ijlage\s+(B\d{4})\b")


def norm(t: str) -> str:
    t = unquote_plus(t)
    t = re.sub(r"[*_`\\]", "", t)
    return re.sub(r"[\W_]+", "", t.lower())


def is_confluence(url: str) -> bool:
    return "/wiki/" in url and ("atlassian.net" in url or "/confluence/" in url or url.startswith("/wiki/"))


def confluence_titel(url: str) -> str | None:
    m = re.search(r"/pages/\d+/([^/?#]+)", url)
    return unquote_plus(m.group(1)) if m else None


def slug(t: str) -> str:
    t = re.sub(r"[^\w\s-]", "", unquote_plus(t).lower(), flags=re.UNICODE)
    return re.sub(r"[\s_-]+", "-", t).strip("-")[:60] or "pagina"


# ------------------------------------------------------------------ bronpagina's

@dataclass
class Bron:
    titel: str
    bestand: Path
    body: str


def lees_bronnen(verslag: list[str]) -> dict[str, Bron]:
    per: dict[str, list[Bron]] = {}
    for pad in sorted(BRONPAGINAS.rglob("*.md")):
        if any(d.startswith((".", "_")) for d in pad.relative_to(BRONPAGINAS).parts):
            continue
        tekst = pad.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
        m = re.search(r"^#[ \t]+(.+?)[ \t]*$", tekst, re.M)
        if m and not tekst[:m.start()].strip():
            titel, body = re.sub(r"[*_]{2}", "", m.group(1)).strip(), tekst[m.end():]
        else:
            titel, body = re.sub(r"[-_]+\d*$", "", pad.stem).replace("_", " ").strip(), tekst
            verslag.append(f"⚠️ {pad.name}: geen titelkop gevonden; titel '{titel}' afgeleid van bestandsnaam")
        per.setdefault(norm(titel), []).append(Bron(titel, pad, body.strip("\n")))

    def volgnummer(b: Bron) -> int:
        m = re.search(r"[-_ ](\d+)$", b.bestand.stem)
        return int(m.group(1)) if m else 0

    res = {}
    for n, lijst in per.items():
        lijst.sort(key=volgnummer)
        res[n] = lijst[-1]
        if len(lijst) > 1:
            gelijk = len({b.body for b in lijst}) == 1
            verslag.append(f"ℹ️ '{lijst[-1].titel}' staat {len(lijst)}× in bron/paginas "
                           f"({', '.join(b.bestand.name for b in lijst)}); gebruikt: {lijst[-1].bestand.name}"
                           + ("" if gelijk else " (inhoud verschilt!)"))
    return res


# ------------------------------------------------------------------ structuur

@dataclass
class Knoop:
    titel: str
    kinderen: list["Knoop"] = field(default_factory=list)
    pos: int = 0


def lees_structuur() -> list[Knoop]:
    if not STRUCTUUR.exists():
        return []
    def bouw(items) -> list[Knoop]:
        res = []
        for it in items or []:
            if isinstance(it, dict):
                for t, kids in it.items():
                    res.append(Knoop(str(t), bouw(kids)))
            elif it is not None:
                res.append(Knoop(str(it)))
        return res
    return bouw(yaml.safe_load(STRUCTUUR.read_text(encoding="utf-8")))


KOP_STRUCTUUR = """\
# Paginastructuur, zoals in Confluence.
# - Inspringing = subpagina; de volgorde hier is de volgorde in de publicatie.
# - Een titel is de eerste kop van de geëxporteerde pagina. Zet titels tussen "aanhalingstekens".
# - Een pagina met subpagina's eindigt op een dubbele punt.
# - scripts/inname.py vult dit bestand aan voor nieuwe pagina's; verplaats ze gerust.
#   Wat hier staat wordt bij een volgende inname niet meer verplaatst.
# - '# nog geen bestand' = pagina waarnaar gelinkt wordt, maar die niet in bron/paginas staat.
"""


def schrijf_structuur(boom: list[Knoop], bekend: set[str]) -> str:
    regels = [KOP_STRUCTUUR]
    def q(t: str) -> str:
        return '"' + t.replace("\\", "\\\\").replace('"', '\\"') + '"'
    def loop(knopen, diepte):
        for k in knopen:
            noot = "" if norm(k.titel) in bekend else "  # nog geen bestand"
            regels.append(f"{'  ' * diepte}- {q(k.titel)}{':' if k.kinderen else ''}{noot}")
            loop(k.kinderen, diepte + 2)
    loop(boom, 0)
    return "\n".join(regels) + "\n"


def vind_verwijzing(body: str, titel: str) -> tuple[int, str] | None:
    """Positie waar body naar een pagina met deze titel verwijst: via een Confluence-link,
    of via een opsommingsitem met (het laatste deel van) de titel."""
    doel = norm(titel)
    for m in RE_LINK.finditer(body):
        if is_confluence(m.group(2)) and doel in (norm(confluence_titel(m.group(2)) or ""), norm(m.group(1))):
            return m.start(), "link"
    kort = norm(titel.split(":", 1)[1]) if ":" in titel else None
    for m in RE_LIJST.finditer(body):
        item = norm(RE_LINK.sub(r"\1", m.group(1)))
        if item and (item == doel or item == kort):
            return m.start(), "opsomming"
    return None


def bouw_boom(bronnen: dict[str, Bron], verslag: list[str]) -> list[Knoop]:
    boom = lees_structuur()
    index: dict[str, Knoop] = {}
    def indexeer(knopen):
        for k in knopen:
            index.setdefault(norm(k.titel), k)
            indexeer(k.kinderen)
    indexeer(boom)
    expliciet = set(index)

    # 1. ouder zoeken voor elke pagina die nog niet in de structuur staat
    nieuw = [n for n in bronnen if n not in index]
    ouder: dict[str, tuple[str, int]] = {}
    for n in nieuw:
        kandidaten = []
        for m, b in bronnen.items():
            if m != n and (v := vind_verwijzing(b.body, bronnen[n].titel)):
                kandidaten.append((0 if v[1] == "link" else 1, m, v[0]))
        if kandidaten:
            _, m, pos = min(kandidaten)
            ouder[n] = (m, pos)
    def cyclisch(n):
        gezien, x = {n}, ouder.get(n, (None,))[0]
        while x is not None:
            if x in gezien:
                return True
            gezien.add(x)
            x = ouder.get(x, (None,))[0] if x not in index else None
        return False
    for n in [n for n in ouder if cyclisch(n)]:
        del ouder[n]

    knopen = {n: Knoop(bronnen[n].titel) for n in nieuw}
    for n in nieuw:                                   # hang nieuwe pagina's aan hun ouder
        if n in ouder:
            m, pos = ouder[n]
            knopen[n].pos = pos
            doel = index.get(m) or knopen[m]
            doel.kinderen.append(knopen[n])
    for k in list(index.values()) + list(knopen.values()):
        oud = [c for c in k.kinderen if norm(c.titel) in expliciet]
        erbij = sorted((c for c in k.kinderen if norm(c.titel) not in expliciet), key=lambda c: c.pos)
        k.kinderen = oud + erbij
    wortels = sorted((knopen[n] for n in nieuw if n not in ouder), key=lambda k: k.titel.lower())
    if wortels and boom:
        for k in wortels:
            verslag.append(f"⚠️ '{k.titel}': geen bovenliggende pagina gevonden; staat op het hoogste niveau "
                           "(verplaats hem in bron/structuur.yml)")
    boom += wortels
    for k in knopen.values():
        index.setdefault(norm(k.titel), k)
    for n in nieuw:
        if n in ouder:
            verslag.append(f"➕ '{bronnen[n].titel}' geplaatst onder '{bronnen[ouder[n][0]].titel}'")

    # 2. gelinkte maar niet aangeleverde pagina's als plaatshouder toevoegen
    def plaatshouders(knopen_):
        for k in knopen_:
            b = bronnen.get(norm(k.titel))
            if b:
                for m in RE_LINK.finditer(b.body):
                    if not is_confluence(m.group(2)):
                        continue
                    ct = confluence_titel(m.group(2)) or ""
                    t = m.group(1).strip() if norm(m.group(1)) == norm(ct) else (ct or m.group(1).strip())
                    if t and norm(t) not in index:
                        nk = Knoop(t, pos=m.start())
                        index[norm(t)] = nk
                        k.kinderen.append(nk)
                vast = [c for c in k.kinderen if norm(c.titel) in expliciet]
                los = sorted((c for c in k.kinderen if norm(c.titel) not in expliciet), key=lambda c: c.pos)
                k.kinderen = vast + los
            plaatshouders(k.kinderen)
    plaatshouders(boom)
    return boom


def _titels(boom):
    for k in boom:
        yield k.titel
        yield from _titels(k.kinderen)


# ------------------------------------------------------------------ normaliseren

def normaliseer(b: Bron, paden: dict[str, Path], hier: Path, reg: dict, verslag: list[str],
                bijlagetitels: dict[str, str], titels: dict[str, str]) -> str:
    body = b.body
    # koppen: inhoud begint onder de paginatitel
    stukken = re.split(r"(^```.*?^```)", body, flags=re.M | re.S)
    heeft_h1 = any(re.search(r"^#[ \t]", s, re.M) for i, s in enumerate(stukken) if i % 2 == 0)
    def kop(m):
        niveau = min(len(m.group(1)) + (1 if heeft_h1 else 0), 6)
        tekst = re.sub(r"[*_]{2}(.+?)[*_]{2}", r"\1", m.group(2)).strip()
        return f"{'#' * niveau} {tekst}"
    body = "".join(RE_KOP.sub(kop, s) if i % 2 == 0 else s for i, s in enumerate(stukken))

    # bijlagen: regels 'Bijlage B0007 ...' tonen de bijlage, 'bijlage B0007' in een zin verwijst
    def regel(m):
        n = m.group(1) or m.group(2)
        rest = m.group(3).strip()
        if rest and n not in bijlagetitels:
            bijlagetitels[n] = rest
        return f"\n[[bijlage:{n}]]\n"
    body = RE_BIJLAGEREGEL.sub(regel, body)
    body = RE_BIJLAGE_INLINE.sub(lambda m: f"[[zie:{m.group(1)}]]", body)

    # bijlagen met een vaste plaats in het register
    for n, info in sorted(reg.items()):
        if not info.get("pagina") or norm(str(info["pagina"])) != norm(b.titel) or f"[[bijlage:{n}]]" in body:
            continue
        na = info.get("na")
        if na:
            delen = re.split(r"(\n[ \t]*\n)", body)
            hit = next((i for i, d in enumerate(delen) if i % 2 == 0 and
                        " ".join(str(na).lower().split()) in " ".join(d.lower().split())), None)
            if hit is not None:
                delen[hit] += f"\n\n[[bijlage:{n}]]"
                body = "".join(delen)
                continue
            verslag.append(f"⚠️ Bijlage {n}: tekst '{na}' niet gevonden op '{b.titel}'; bijlage aan het eind gezet")
        body = body.rstrip() + f"\n\n[[bijlage:{n}]]\n"

    # opsommingsitems die precies een gepubliceerde (sub)pagina noemen, worden een link
    def item(m):
        tekst = m.group(1)
        if "](" in tekst or "[[" in tekst:
            return m.group(0)
        for n, pad in paden.items():
            t = titels.get(n, "")
            kort = t.split(":", 1)[1] if ":" in t else None
            if norm(tekst) and norm(tekst) in (n, norm(kort or "")) and n != norm(b.titel):
                rel = Path(os.path.relpath(pad, hier)).as_posix()
                return m.group(0).replace(tekst.rstrip(), f"[{tekst.strip()}]({rel})", 1)
        return m.group(0)
    body = RE_LIJST.sub(item, body)

    # links
    def link(m):
        tekst, url = m.group(1), m.group(2)
        if not is_confluence(url):
            return m.group(0)
        doel = norm(confluence_titel(url) or "") or norm(tekst)
        if doel not in paden:
            doel = norm(tekst) if norm(tekst) in paden else doel
        if doel in paden:
            return f"[{tekst}]({Path(os.path.relpath(paden[doel], hier)).as_posix()})"
        verslag.append(f"🔗 '{b.titel}': link naar niet-gepubliceerde Confluence-pagina '{tekst}' wordt tekst")
        voor = body[m.start() - 1] if m.start() > 0 else " "
        return (" " if voor.isalnum() else "") + tekst
    body = RE_LINK.sub(link, body)
    return re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"


def paden_toekennen(boom: list[Knoop], bronnen: dict[str, Bron]) -> tuple[dict[str, Path], dict[str, int], list]:
    """Alleen knopen met een bestand (of met afstammelingen met een bestand) krijgen een pagina."""
    def heeft_inhoud(k: Knoop) -> bool:
        return norm(k.titel) in bronnen or any(heeft_inhoud(c) for c in k.kinderen)
    boom = [k for k in boom if heeft_inhoud(k)]
    paden, volgorde, stubs = {}, {}, []
    if len(boom) == 1:
        k = boom[0]
        paden[norm(k.titel)] = Path("index.md")
        volgorde[norm(k.titel)] = 0
        boom = k.kinderen
        if norm(k.titel) not in bronnen:
            stubs.append(k)

    def loop(knopen, map_: Path):
        gebruikt = set()
        nr = 0
        for k in knopen:
            if not heeft_inhoud(k):
                continue
            nr += 1
            s, i = slug(k.titel), 2
            while s in gebruikt:
                s, i = f"{slug(k.titel)}-{i}", i + 1
            gebruikt.add(s)
            n = norm(k.titel)
            volgorde[n] = nr
            if n not in bronnen:
                stubs.append(k)
            kids = [c for c in k.kinderen if heeft_inhoud(c)]
            if kids:
                paden[n] = map_ / s / "index.md"
                loop(kids, map_ / s)
            else:
                paden[n] = map_ / f"{s}.md"
    loop(boom, Path("."))
    return {k: Path(*[p for p in v.parts if p != "."]) for k, v in paden.items()}, volgorde, stubs


def main(argv: list[str]) -> int:
    controle = "--controle" in argv
    verslag: list[str] = []
    bronnen = lees_bronnen(verslag)
    if not bronnen:
        print("Geen pagina's in bron/paginas/.")
        return 1
    boom = bouw_boom(bronnen, verslag)
    tekst = schrijf_structuur(boom, set(bronnen))
    oud = STRUCTUUR.read_text(encoding="utf-8") if STRUCTUUR.exists() else ""
    if tekst != oud:
        if controle:
            verslag.append("ℹ️ bron/structuur.yml zou worden bijgewerkt (controle-modus: niet geschreven)")
        else:
            STRUCTUUR.write_text(tekst, encoding="utf-8")
            verslag.append("ℹ️ bron/structuur.yml bijgewerkt")

    paden, volgorde, stubs = paden_toekennen(boom, bronnen)
    reg = lees_register()
    bijlagetitels: dict[str, str] = {}
    shutil.rmtree(PAGINAS, ignore_errors=True)
    PAGINAS.mkdir(parents=True)
    for n, pad in paden.items():
        b = bronnen.get(n)
        if b is None:
            k = next(s for s in stubs if norm(s.titel) == n)
            schrijf_md(PAGINAS / pad, {"titel": k.titel, "volgorde": volgorde[n]}, "")
            verslag.append(f"ℹ️ '{k.titel}' is niet aangeleverd maar heeft subpagina's; lege pagina gemaakt")
            continue
        body = normaliseer(b, paden, pad.parent, reg, verslag, bijlagetitels,
                           {m: x.titel for m, x in bronnen.items()})
        schrijf_md(PAGINAS / pad, {"titel": b.titel, "volgorde": volgorde[n], "bron": b.bestand.name}, body)
    (PAGINAS.parent / "bijlagetitels.yml").write_text(
        yaml.safe_dump(bijlagetitels, allow_unicode=True), encoding="utf-8")

    gebruikt = set()
    for p in PAGINAS.rglob("*.md"):
        gebruikt |= set(re.findall(r"\[\[(?:bijlage|zie):(B\d{4})\]\]", p.read_text(encoding="utf-8")))
    ontbreekt = sorted(n for n in gebruikt if bestand_van(n) is None)
    from gemeen import bijlagebestanden
    los = sorted(set(bijlagebestanden()) - gebruikt)

    def toon(knopen, d=0):
        for k in knopen:
            yield f"{'  ' * d}- {k.titel}" + ("" if norm(k.titel) in bronnen else "  (nog geen bestand)")
            yield from toon(k.kinderen, d + 1)
    uit = [f"## Inname: {len(bronnen)} pagina's, {len(gebruikt)} bijlagen", "", "### Structuur", "",
           *toon(boom), ""]
    if ontbreekt:
        uit += ["### Bijlagen nog niet aangeleverd", "", ", ".join(ontbreekt), ""]
    if los:
        uit += ["### Bijlagen in bron/bijlagen die nergens gebruikt worden", "", ", ".join(los), ""]
    if verslag:
        uit += ["### Meldingen", "", *[f"- {v}" for v in verslag], ""]
    rapport = "\n".join(uit)
    print(rapport)
    (PAGINAS.parent / "inname-verslag.md").write_text(rapport, encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(rapport + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
