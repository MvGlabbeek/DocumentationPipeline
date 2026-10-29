"""Zet een Confluence-export (HTML) om naar Markdown-pagina's met losse, genummerde bijlagen.

Gebruik:
    python scripts/confluence_naar_md.py [pad/naar/export.zip | pad/naar/exportmap]

Zonder argument wordt de nieuwste .zip (of map met index.html) in bron/confluence-export/ gebruikt.

Wat er gebeurt
1. De paginaboom wordt gelezen uit index.html van de export (valt terug op de kruimelpaden).
2. Elke pagina wordt bron/paginas/<pad>.md met front matter (titel, volgorde, confluence_id, ...).
   Een pagina met subpagina's wordt een map met index.md. De startpagina van de space wordt
   bron/paginas/index.md. bron/paginas/ wordt bij elke conversie opnieuw opgebouwd:
   Confluence is tijdens de pilot de bron; wijzig de tekst daar.
3. Afbeeldingen, tabellen, bijlagen (pdf e.d.) en links/iframes naar BizzDesign Horizzon worden
   losse bijlagen B0001, B0002, ... in bron/bijlagen/ met een regel in bijlagen.yml.
   In de tekst komt [[bijlage:B0007]] (tonen) of [[zie:B0007]] (verwijzen).
   Nummers blijven stabiel bij een volgende export (op basis van een sleutel per bijlage) en
   worden nooit hergebruikt. Een bestand dat uit BizzDesign is vervangen (bijv. B0007.svg i.p.v.
   B0007.png, of bron: bizzdesign in het register) wordt niet overschreven.
4. Links tussen pagina's worden relatieve Markdown-links, ook naar koppen binnen een pagina.
"""
from __future__ import annotations

import csv
import hashlib
import io
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup, NavigableString, Tag
from markdown.extensions.toc import slugify

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemeen import (BEELD, BIJLAGEN, BRON, PAGINAS, bestand_van, instellingen,  # noqa: E402
                    lees_register, schrijf_md, schrijf_register, volgend_nummer)

RE_HORIZZON = re.compile(r"horizzon|bizzdesign", re.I)
BLOK = ("p", "div", "li", "td", "th", "blockquote", "h1", "h2", "h3", "h4", "h5", "h6", "span")
MACRO_LABEL = {"note": "Let op", "warning": "Waarschuwing", "info": "Info", "tip": "Tip"}


# ------------------------------------------------------------------ export openen

def kies_export(arg: str | None) -> Path:
    if arg:
        return Path(arg)
    map_ = BRON / "confluence-export"
    kand = [p for p in map_.glob("*") if p.suffix.lower() == ".zip" or (p / "index.html").exists()
            or (p.is_dir() and any(p.glob("*/index.html")))]
    if not kand:
        sys.exit("Geen export gevonden in bron/confluence-export/ (zip of map met index.html).")
    return max(kand, key=lambda p: p.stat().st_mtime)


def pak_uit(export: Path) -> Path:
    if export.is_dir():
        basis = export
    else:
        basis = Path(tempfile.mkdtemp(prefix="confluence-"))
        with zipfile.ZipFile(export) as z:
            z.extractall(basis)  # zipfile normaliseert absolute paden en '..'
    indexen = sorted(basis.rglob("index.html"), key=lambda p: len(p.parts))
    if not indexen:
        sys.exit(f"Geen index.html gevonden in {export}; is dit een Confluence HTML-export?")
    return indexen[0].parent


# ------------------------------------------------------------------ paginaboom

def pagina_id(bestand: str) -> str:
    m = re.search(r"(\d+)\.html$", bestand)
    return m.group(1) if m else Path(bestand).stem


def lees_boom(space: Path, bestanden: set[str]) -> list[tuple[str, list]]:
    """Boom uit index.html: lijst van (bestandsnaam, kinderen)."""
    soep = BeautifulSoup((space / "index.html").read_text(encoding="utf-8", errors="replace"), "html.parser")

    def ul_naar_boom(ul: Tag) -> list:
        res = []
        for li in ul.find_all("li", recursive=False):
            a = li.find("a", href=True)
            if not a:
                continue
            naam = unquote(a["href"]).split("#")[0]
            sub = li.find("ul")
            if naam in bestanden:
                res.append((naam, ul_naar_boom(sub) if sub else []))
        return res

    kandidaten = [ul for ul in soep.find_all("ul") if not ul.find_parent("ul")]
    bomen = [ul_naar_boom(ul) for ul in kandidaten]
    bomen = [b for b in bomen if b]
    if not bomen:
        return []
    tel = lambda b: sum(1 + tel(k) for _, k in b)  # noqa: E731
    return max(bomen, key=tel)


def boom_uit_kruimels(info: dict) -> list:
    kinderen: dict[str | None, list[str]] = {}
    for naam, i in info.items():
        ouder = i["ouder"] if i["ouder"] in info else None
        kinderen.setdefault(ouder, []).append(naam)
    def bouw(ouder):
        return [(n, bouw(n)) for n in sorted(kinderen.get(ouder, []), key=lambda n: info[n]["titel"].lower())]
    return bouw(None)


# ------------------------------------------------------------------ hulpjes

def slug(t: str) -> str:
    return slugify(t, "-")[:60] or "pagina"


def kale_titel(soep: BeautifulSoup) -> str:
    el = soep.select_one("#title-text") or soep.find("title")
    t = " ".join(el.get_text(" ").split()) if el else "Zonder titel"
    return t.split(" : ", 1)[1].strip() if " : " in t else t


def zelfstandig(el: Tag) -> Tag | None:
    """Het blok waarin el staat als dat blok verder geen tekst bevat (dan vervangen we het hele blok)."""
    blok = el
    while blok.parent is not None and blok.parent.name in ("span", "a", "p", "div") \
            and blok.parent.get("id") != "main-content":
        if blok.parent.get_text(strip=True) != el.get_text(strip=True):
            break
        if blok.parent.find_all(["img", "iframe"]) and len(blok.parent.find_all(["img", "iframe"])) > 1:
            break
        blok = blok.parent
    return blok if blok.name in ("p", "div") or blok is el else None


def staat_alleen(el: Tag) -> bool:
    """True als el de enige tekst is in zijn alinea/blok."""
    blok = el.find_parent(["p", "li", "td", "th", "div", "blockquote"])
    return blok is None or blok.get_text(strip=True) == el.get_text(strip=True)


def schone_tabel(t: Tag) -> str:
    """Tabel-HTML zonder Confluence-klassen en -opmaak (colspan/rowspan en links blijven)."""
    t = BeautifulSoup(str(t), "html.parser").find("table")
    t.attrs = {}
    for el in t.find_all(True):
        el.attrs = {k: v for k, v in el.attrs.items() if k in ("colspan", "rowspan", "href")}
    for el in t.find_all("colgroup"):
        el.decompose()
    return t.prettify()


def normaliseer_url(url: str) -> str:
    d = urlsplit(url.strip())
    return f"{d.scheme.lower()}://{d.netloc.lower()}{d.path.rstrip('/')}" + (f"?{d.query}" if d.query else "")


def plaats_blok(el: Tag, soep: BeautifulSoup, token: str) -> None:
    """Vervangt el door een eigen alinea met token; staat el midden in tekst, dan komt de alinea erna."""
    nieuw = soep.new_tag("p")
    nieuw.string = token
    blok = zelfstandig(el)
    if blok is not None and blok.get_text(strip=True) in ("", el.get_text(strip=True)):
        blok.replace_with(nieuw)
        return
    ouder = el.find_parent(["p", "li", "td", "th", "blockquote"]) or el.parent
    el.decompose()
    if ouder.name in ("td", "th"):
        ouder.append(" " + token.replace("BIJLAGE", "ZIE"))
    else:
        ouder.insert_after(nieuw)


# ------------------------------------------------------------------ conversie

class Converter:
    def __init__(self, space: Path, cfg: dict):
        self.space, self.cfg = space, cfg
        self.reg = lees_register()
        self.per_sleutel = {v["sleutel"]: k for k, v in self.reg.items() if v.get("sleutel")}
        self.gebruikt: set[str] = set()
        self.waarschuwingen: list[str] = []

    # ---- bijlagen
    def bijlage(self, sleutel: str, *, titel: str, soort: str, bron: str, pagina: str,
                bestand: Path | None = None, ext: str | None = None, inhoud: bytes | None = None,
                horizzon: str | None = None, conf: dict | None = None) -> str:
        nummer = self.per_sleutel.get(sleutel)
        nieuw = nummer is None
        if nieuw:
            nummer = volgend_nummer(self.reg)
            self.reg[nummer] = {"titel": titel, "soort": soort, "bron": bron, "sleutel": sleutel}
            if horizzon:
                self.reg[nummer]["horizzon"] = horizzon
            self.per_sleutel[sleutel] = nummer
        b = self.reg[nummer]
        oud = b.get("confluence") or {}
        paginas = oud.get("paginas", []) if nummer in self.gebruikt else []
        b["confluence"] = {"paginas": sorted(set(paginas) | {pagina}), **(conf or {})}
        self.gebruikt.add(nummer)
        # bestand (her)schrijven: alleen als het nog uit Confluence komt en niet is vervangen
        if bestand is not None or inhoud is not None:
            ext = (ext or (bestand.suffix if bestand else "")).lower()
            huidig = bestand_van(nummer)
            mag = huidig is None or (b.get("bron") == "confluence" and huidig.suffix.lower() == ext)
            if mag:
                doel = BIJLAGEN / f"{nummer}{ext}"
                if bestand is not None:
                    shutil.copyfile(bestand, doel)
                else:
                    doel.write_bytes(inhoud)
        return nummer

    # ---- pagina
    def lees(self, naam: str) -> dict:
        soep = BeautifulSoup((self.space / naam).read_text(encoding="utf-8", errors="replace"), "html.parser")
        kruimels = [unquote(a["href"]).split("#")[0] for a in soep.select("#breadcrumbs a[href]")]
        kruimels = [k for k in kruimels if k != "index.html"]
        labels = [a.get_text(strip=True).lower() for a in soep.select(
            ".labels-content a, .label-list a, a[rel=tag], .aui-label a")]
        inhoud = soep.select_one("#main-content") or soep.select_one(".wiki-content") or soep.body
        ankers = {}
        for h in inhoud.find_all(re.compile(r"^h[1-6]$")):
            if h.get("id"):
                ankers[h["id"]] = slugify(h.get_text(" ", strip=True), "-")
        return {"titel": kale_titel(soep), "ouder": kruimels[-1] if kruimels else None,
                "labels": labels, "inhoud": inhoud, "soep": soep, "ankers": ankers}

    def converteer(self, naam: str, info: dict, paden: dict[str, Path]) -> str:
        i = info[naam]
        soep, inhoud, pid = i["soep"], i["inhoud"], pagina_id(naam)
        hier = paden[naam].parent

        # 1. ruis weg
        for sel in ("script", "style", ".toc-macro", ".client-side-toc-macro", ".confluence-anchor-link",
                    ".confluence-information-macro-icon", ".recently-updated", ".plugin_pagetree",
                    ".children-show-hide", "#likes-and-labels-container", ".labels-content",
                    "#labels-section", ".page-metadata"):
            for el in inhoud.select(sel):
                el.decompose()
        for el in inhoud.select("img.emoticon, img[src^='images/icons']"):
            el.decompose()

        # 2. info/let op/waarschuwing-macro's -> citaatblok met label
        for el in inhoud.select("div.confluence-information-macro"):
            soort = next((k for k in MACRO_LABEL if f"confluence-information-macro-{k}" in el.get("class", [])), "info")
            bq = soep.new_tag("blockquote")
            titel = el.select_one(".title")
            b = soep.new_tag("strong")
            b.string = (titel.get_text(strip=True) if titel else MACRO_LABEL[soort]) + ": "
            body = el.select_one(".confluence-information-macro-body") or el
            p = soep.new_tag("p")
            p.append(b)
            bq.append(p)
            for kind in list(body.children):
                bq.append(kind.extract())
            el.replace_with(bq)
        for el in inhoud.select(".expand-control"):
            s = soep.new_tag("p")
            st = soep.new_tag("strong")
            st.string = el.get_text(" ", strip=True)
            s.append(st)
            el.replace_with(s)
        for el in inhoud.select("span.status-macro"):
            el.replace_with(f"[{el.get_text(strip=True)}]")

        # 3. BizzDesign Horizzon: iframes, ingesloten macro's en links
        for el in list(inhoud.find_all(["iframe", "a", "div", "span"])):
            if el.parent is None:
                continue
            url = el.get("src") if el.name == "iframe" else el.get("href") if el.name == "a" else \
                next((v for k, v in el.attrs.items() if k.startswith("data-") and isinstance(v, str)
                      and v.startswith("http") and RE_HORIZZON.search(v)), None)
            if not url or not RE_HORIZZON.search(url):
                continue
            tekst = el.get_text(" ", strip=True)
            titel = el.get("title") or (tekst if el.name == "a" and not tekst.startswith("http") else "") \
                or "Diagram uit BizzDesign Horizzon"
            n = self.bijlage("horizzon:" + normaliseer_url(url), titel=titel, soort="diagram",
                             bron="bizzdesign", horizzon=url.strip(), pagina=pid)
            if el.name == "a" and not staat_alleen(el):
                el.replace_with(f"{tekst} §§ZIE:{n}§§")       # link midden in de tekst
            else:
                plaats_blok(el, soep, f"§§BIJLAGE:{n}§§")

        # 4. afbeeldingen uit de bijlagen van de pagina
        for img in list(inhoud.find_all("img")):
            if img.parent is None:
                continue
            src = unquote(img.get("data-image-src") or img.get("src") or "").split("?")[0]
            bestand = (self.space / naam).parent / src
            if not src or src.startswith(("http", "data:")) or not bestand.exists():
                if src.startswith("http"):
                    self.waarschuwingen.append(f"{i['titel']}: externe afbeelding blijft extern ({src[:80]})")
                    continue
                self.waarschuwingen.append(f"{i['titel']}: afbeelding niet gevonden in export ({src})")
                img.decompose()
                continue
            aid = img.get("data-linked-resource-id")
            alias = img.get("data-linked-resource-default-alias") or bestand.name
            titel = img.get("title") or img.get("alt") or Path(alias).stem.replace("_", " ").replace("-", " ")
            soort = "diagram" if re.search(r"drawio|gliffy|diagram|archimate|view", alias + " " + titel, re.I) else "afbeelding"
            n = self.bijlage(f"confluence:{aid}" if aid else f"confluence:{src}", titel=titel, soort=soort,
                             bron="confluence", pagina=pid, bestand=bestand,
                             conf={"bestand": alias, **({"bijlage_id": aid} if aid else {})})
            plaats_blok(img, soep, f"§§BIJLAGE:{n}§§")

        # 5. links: naar andere pagina's, naar bijlagen (pdf e.d.), naar Confluence zelf
        for a in inhoud.find_all("a", href=True):
            href = unquote(a["href"])
            doel, _, anker = href.partition("#")
            if doel in paden:
                rel = Path(os_relpath(paden[doel], hier)).as_posix()
                anker = info[doel]["ankers"].get(anker, slugify(anker, "-")) if anker else ""
                a["href"] = rel + (f"#{anker}" if anker else "")
            elif not doel and anker:
                a["href"] = "#" + i["ankers"].get(anker, slugify(anker, "-"))
            elif doel.startswith("attachments/") and (self.space / doel).exists():
                f = self.space / doel
                if f.suffix.lower() in BEELD:
                    soort = "afbeelding"
                elif f.suffix.lower() in (".csv", ".xlsx"):
                    soort = "tabel"
                else:
                    soort = "document"
                tekst = a.get_text(" ", strip=True) or f.name
                n = self.bijlage(f"confluence:{doel}", titel=tekst, soort=soort, bron="confluence",
                                 pagina=pid, bestand=f, conf={"bestand": f.name})
                a.replace_with(f"{tekst} §§ZIE:{n}§§")
            elif doel.endswith(".html") and not doel.startswith("http"):
                reden = "niet-gepubliceerde pagina" if doel in info else "pagina buiten de export"
                self.waarschuwingen.append(f"{i['titel']}: link naar {reden} ({doel}); link verwijderd")
                a.unwrap()
            elif "atlassian.net/wiki" in href or "/confluence/" in href:
                self.waarschuwingen.append(f"{i['titel']}: link naar Confluence blijft staan maar is extern niet bereikbaar ({href[:80]})")

        # 6. tabellen -> bijlage (of blijven staan onder de drempel)
        drempel = int(self.cfg.get("tabel_drempel", 1))
        teller: dict[str, int] = {}
        for t in list(inhoud.find_all("table")):
            if t.parent is None or t.find_parent("table"):
                continue
            rijen = t.find_all("tr")
            complex_ = any(int(c.get("colspan", 1)) > 1 or int(c.get("rowspan", 1)) > 1
                           for c in t.find_all(["td", "th"])) or bool(t.find("table"))
            if len(rijen) < drempel and not complex_:
                continue
            kop = " | ".join(c.get_text(" ", strip=True) for c in rijen[0].find_all(["td", "th"])) if rijen else ""
            h = hashlib.sha1(kop.encode()).hexdigest()[:10]
            teller[h] = teller.get(h, 0) + 1
            sleutel = f"tabel:{pid}:{h}" + (f":{teller[h]}" if teller[h] > 1 else "")
            onderschrift = t.find("caption")
            vorige = t.find_previous(re.compile(r"^h[1-6]$"))
            titel = (onderschrift.get_text(" ", strip=True) if onderschrift else
                     (vorige.get_text(" ", strip=True) if vorige and inhoud in vorige.parents else i["titel"]))
            rijk = complex_ or bool(t.find(["a", "ul", "ol"])) or "§§" in t.get_text()
            if rijk:
                ext, data = ".md", schone_tabel(t).encode("utf-8")
            else:
                buf = io.StringIO()
                w = csv.writer(buf, delimiter=";", lineterminator="\n")
                for r in rijen:
                    w.writerow([" ".join(c.get_text(" ", strip=True).split()) for c in r.find_all(["td", "th"])])
                ext, data = ".csv", buf.getvalue().encode("utf-8-sig")
            n = self.bijlage(sleutel, titel=titel, soort="tabel", bron="confluence", pagina=pid,
                             ext=ext, inhoud=data)
            plaats_blok(t, soep, f"§§BIJLAGE:{n}§§")

        # 7. naar Markdown
        md = pandoc(str(inhoud), naar="gfm-raw_html", kopverschuiving=1)
        md = re.sub(r"§§BIJLAGE:(B\d{4})§§", r"[[bijlage:\1]]", md)
        md = re.sub(r"§§ZIE:(B\d{4})§§", r"[[zie:\1]]", md)
        md = re.sub(r"\n{3,}", "\n\n", md)
        return md


def os_relpath(doel: Path, van: Path) -> str:
    import os
    return os.path.relpath(doel, van if str(van) != "." else ".")


def pandoc(html_: str, naar: str, kopverschuiving: int = 0) -> str:
    cmd = ["pandoc", "-f", "html", "-t", naar, "--wrap=none"]
    if kopverschuiving:
        cmd.append(f"--shift-heading-level-by={kopverschuiving}")
    return subprocess.run(cmd, input=html_, check=True, capture_output=True, text=True).stdout


# ------------------------------------------------------------------ paden en hoofdroutine

def ken_paden_toe(boom: list, info: dict) -> tuple[dict[str, Path], dict[str, int], str | None]:
    paden: dict[str, Path] = {}
    volgorde: dict[str, int] = {}
    start = None
    if len(boom) == 1:                       # één wortel = startpagina van de space
        start, kinderen = boom[0]
        paden[start] = Path("index.md")
        volgorde[start] = 0
        boom = kinderen

    def loop(knopen, map_: Path):
        gebruikt: set[str] = set()
        for nr, (naam, kinderen) in enumerate(knopen, 1):
            s = slug(info[naam]["titel"])
            basis, k = s, 2
            while s in gebruikt:
                s, k = f"{basis}-{k}", k + 1
            gebruikt.add(s)
            volgorde[naam] = nr
            if kinderen:
                paden[naam] = map_ / s / "index.md"
                loop(kinderen, map_ / s)
            else:
                paden[naam] = map_ / f"{s}.md"
    loop(boom, Path("."))
    paden = {k: Path(*[p for p in v.parts if p != "."]) for k, v in paden.items()}
    return paden, volgorde, start


def main(argv: list[str]) -> None:
    cfg = instellingen()
    export = kies_export(argv[1] if len(argv) > 1 else None)
    space = pak_uit(export)
    bestanden = {p.relative_to(space).as_posix() for p in space.glob("*.html") if p.name != "index.html"}
    conv = Converter(space, cfg)
    info = {n: conv.lees(n) for n in sorted(bestanden)}
    boom = lees_boom(space, bestanden) or boom_uit_kruimels(info)

    # Pagina's met een niet-publiceren-label (en hun subpagina's) worden helemaal niet omgezet:
    # zo komt hun inhoud ook niet in de repository terecht.
    niet = {l.lower() for l in cfg.get("labels_niet_publiceren", [])}
    uitgesloten: set[str] = set()
    def snoei(knopen):
        res = []
        for naam, kinderen in knopen:
            if niet & set(info[naam]["labels"]):
                stapel = [(naam, kinderen)]
                while stapel:
                    n, k = stapel.pop()
                    uitgesloten.add(n)
                    stapel.extend(k)
            else:
                res.append((naam, snoei(kinderen)))
        return res
    boom = snoei(boom)
    paden, volgorde, _ = ken_paden_toe(boom, info)
    weg = sorted(set(info) - set(paden) - uitgesloten)
    for n in weg:                            # pagina's die niet in de boom staan: los onder 'Overig'
        paden[n] = Path("overig") / f"{slug(info[n]['titel'])}.md"
        volgorde[n] = 900
    if weg and not any(p == Path("overig/index.md") for p in paden.values()):
        schrijf_later = True
    else:
        schrijf_later = False

    BIJLAGEN.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(PAGINAS, ignore_errors=True)
    PAGINAS.mkdir(parents=True)
    for naam, pad in sorted(paden.items(), key=lambda x: str(x[1])):
        i = info[naam]
        body = conv.converteer(naam, info, paden)
        meta = {"titel": i["titel"], "volgorde": volgorde.get(naam, 999),
                "confluence_id": pagina_id(naam), "confluence_bestand": naam}
        if i["labels"]:
            meta["labels"] = i["labels"]
        schrijf_md(PAGINAS / pad, meta, body)
    if schrijf_later:
        schrijf_md(PAGINAS / "overig" / "index.md", {"titel": "Overig", "volgorde": 900},
                   "Pagina's uit de export die niet in de paginaboom voorkwamen.")
    schrijf_register(conv.reg)

    ontbreekt = [n for n in sorted(conv.gebruikt) if bestand_van(n) is None]
    print(f"Geconverteerd uit {export.name}: {len(paden)} pagina's, {len(conv.gebruikt)} bijlagen "
          f"({len(conv.reg)} in register).")
    if uitgesloten:
        print(f"Niet omgezet vanwege label ({', '.join(sorted(niet))}): "
              + ", ".join(info[n]["titel"] for n in sorted(uitgesloten)))
    if ontbreekt:
        print(f"Nog te exporteren uit BizzDesign ({len(ontbreekt)}): " + ", ".join(
            f"{n} ({conv.reg[n].get('titel')})" for n in ontbreekt))
    for w in conv.waarschuwingen:
        print(f"::warning::{w}")
    ongebruikt = sorted(set(conv.reg) - conv.gebruikt)
    if ongebruikt:
        print("Bijlagen in het register die in deze export niet meer voorkomen: " + ", ".join(ongebruikt))


if __name__ == "__main__":
    main(sys.argv)
