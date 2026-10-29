"""Gedeelde onderdelen voor de inname van pagina's en beide publicatiepaden.

Begrippen
- Bronpagina: een Markdown-bestand dat per pagina uit Confluence is geëxporteerd en in
  bron/paginas/ staat. De bestandsnaam doet er niet toe; de titel (eerste kop) is de identiteit.
- Structuur: bron/structuur.yml legt de paginaboom vast zoals in Confluence. scripts/inname.py
  vult hem aan voor nieuwe pagina's en zet de pagina's genormaliseerd in _build/paginas/.
- Bijlage: een los, uniek genummerd diagram, afbeelding, tabel of document (B0001, B0002, ...)
  in bron/bijlagen/. De bestandsnaam begint met het nummer: B0007.svg of 'B0007 Hoofdprocesmodel.svg'.
  Metadata (titel, plaats, Horizzon-link) mag in bron/bijlagen/bijlagen.yml, maar is optioneel.
- Verwijzingen in de (genormaliseerde) tekst:
    [[bijlage:B0007]]   alleen op een regel: de bijlage wordt hier getoond
    [[zie:B0007]]       in de lopende tekst: een verwijzing naar de bijlage
"""
from __future__ import annotations

import csv
import html
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BRON = ROOT / "bron"
BRONPAGINAS = BRON / "paginas"
STRUCTUUR = BRON / "structuur.yml"
BIJLAGEN = BRON / "bijlagen"
REGISTER = BIJLAGEN / "bijlagen.yml"
PAGINAS = ROOT / "_build" / "paginas"          # genormaliseerd, door inname.py gemaakt

BEELD = (".svg", ".png", ".webp", ".jpg", ".jpeg", ".gif")
TABEL = (".csv", ".xlsx", ".md")
DOCUMENT = (".pdf", ".docx", ".pptx", ".zip")

RE_EMBED = re.compile(r"^[ \t]*\[\[bijlage:(B\d{4})\]\][ \t]*$", re.M)
RE_ZIE = re.compile(r"\[\[zie:(B\d{4})\]\]")
RE_NUMMER = re.compile(r"^B(\d{4})$")
RE_BESTAND = re.compile(r"^(B\d{4})(?:[ _\-–.]+(.*))?$")


# ---------------------------------------------------------------- instellingen

def instellingen() -> dict:
    return yaml.safe_load((ROOT / "publicatie.yml").read_text(encoding="utf-8")) or {}


# ---------------------------------------------------------------- front matter

def lees_md(pad: Path) -> tuple[dict, str]:
    tekst = pad.read_text(encoding="utf-8-sig")
    if tekst.startswith("---\n"):
        eind = tekst.find("\n---", 4)
        if eind > 0:
            meta = yaml.safe_load(tekst[4:eind]) or {}
            return meta, tekst[eind + 4:].lstrip("\n")
    return {}, tekst


def schrijf_md(pad: Path, meta: dict, body: str) -> None:
    pad.parent.mkdir(parents=True, exist_ok=True)
    kop = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
    pad.write_text(f"---\n{kop}\n---\n\n{body.strip()}\n", encoding="utf-8")


# ---------------------------------------------------------------- paginaboom (genormaliseerd)

@dataclass
class Pagina:
    pad: Path                      # relatief t.o.v. _build/paginas, bijv. procesdomeinen/index.md
    titel: str
    volgorde: int
    meta: dict
    body: str
    kinderen: list["Pagina"] = field(default_factory=list)

    @property
    def publiek(self) -> bool:
        return self.meta.get("publiceren", True) is not False

    @property
    def sleutel(self) -> str:
        """Stabiele, leesbare id voor ankers in één document (ReSpec)."""
        stam = self.pad.with_suffix("").as_posix()
        stam = stam[:-len("/index")] if stam.endswith("/index") else stam
        return "p-" + (re.sub(r"[^a-z0-9]+", "-", stam.lower()).strip("-") or "start")


def paginaboom(alleen_publiek: bool = True) -> tuple[Pagina | None, list[Pagina]]:
    """Geeft (startpagina, hoofdstukken) uit _build/paginas/."""
    def lees(pad: Path) -> Pagina:
        meta, body = lees_md(pad)
        titel = meta.get("titel") or pad.stem.replace("-", " ").capitalize()
        return Pagina(pad.relative_to(PAGINAS), str(titel), int(meta.get("volgorde", 999)), meta, body)

    def map_(d: Path) -> list[Pagina]:
        res = []
        for p in sorted(d.iterdir()):
            if p.name.startswith(("_", ".")):
                continue
            if p.is_file() and p.suffix == ".md" and p.name != "index.md":
                res.append(lees(p))
            elif p.is_dir() and (p / "index.md").exists():
                pg = lees(p / "index.md")
                pg.kinderen = map_(p)
                res.append(pg)
        res.sort(key=lambda x: (x.volgorde, x.titel.lower()))
        return [x for x in res if x.publiek] if alleen_publiek else res

    if not PAGINAS.is_dir():
        return None, []
    start = lees(PAGINAS / "index.md") if (PAGINAS / "index.md").exists() else None
    return start, map_(PAGINAS)


def alle(paginas: list[Pagina]):
    for p in paginas:
        yield p
        yield from alle(p.kinderen)


# ---------------------------------------------------------------- bijlagen

def bijlagebestanden() -> dict[str, Path]:
    """Nummer -> bestand. Bij meerdere bestanden met hetzelfde nummer wint de voorkeursvolgorde."""
    volgorde = {e: i for i, e in enumerate(BEELD + TABEL + DOCUMENT)}
    res: dict[str, Path] = {}
    if not BIJLAGEN.is_dir():
        return res
    for p in BIJLAGEN.iterdir():
        m = RE_BESTAND.match(p.stem)
        if not (p.is_file() and m and p.suffix.lower() in volgorde):
            continue
        n = m.group(1)
        if n not in res or volgorde[p.suffix.lower()] < volgorde[res[n].suffix.lower()]:
            res[n] = p
    return res


def alle_formaten(nummer: str) -> list[Path]:
    """Alle bestanden met dit nummer (bijv. B0002.svg én B0002.png), in voorkeursvolgorde."""
    volgorde = {e: i for i, e in enumerate(BEELD + TABEL + DOCUMENT)}
    if not BIJLAGEN.is_dir():
        return []
    res = [p for p in BIJLAGEN.iterdir() if p.is_file() and p.suffix.lower() in volgorde
           and (m := RE_BESTAND.match(p.stem)) and m.group(1) == nummer]
    uniek = {}
    for p in sorted(res, key=lambda p: volgorde[p.suffix.lower()]):
        uniek.setdefault(p.suffix.lower(), p)
    return list(uniek.values())


def kopieer_bijlage(nummer: str, doelmap: Path) -> None:
    """Kopieert alle formaten van een bijlage naar doelmap als B0002.svg, B0002.png, ...
    Een SVG verliest zijn vaste breedte/hoogte, zodat hij met de pagina meeschaalt
    (exports uit Horizzon hebben bijv. width="371px" bij een veel groter viewBox)."""
    import shutil
    doelmap.mkdir(parents=True, exist_ok=True)
    for f in alle_formaten(nummer):
        doel = doelmap / doelnaam(nummer, f)
        if f.suffix.lower() != ".svg":
            shutil.copy(f, doel)
            continue
        tekst = f.read_text(encoding="utf-8-sig", errors="replace")
        m = re.search(r"<svg\b[^>]*>", tekst)
        if m:
            kop = m.group(0)
            w = re.search(r'\swidth="([\d.]+)(?:px)?"', kop)
            h = re.search(r'\sheight="([\d.]+)(?:px)?"', kop)
            if "viewBox" not in kop and w and h:
                kop = kop.replace("<svg", f'<svg viewBox="0 0 {w.group(1)} {h.group(1)}"', 1)
            kop = re.sub(r'\s(width|height)="[^"]*"', "", kop)
            tekst = tekst[:m.start()] + kop + tekst[m.end():]
        doel.write_text(tekst, encoding="utf-8")


def bestand_van(nummer: str) -> Path | None:
    return bijlagebestanden().get(nummer)


def doelnaam(nummer: str, pad: Path) -> str:
    """Naam waaronder het bestand op de site staat (zonder spaties): B0007.svg."""
    return f"{nummer}{pad.suffix.lower()}"


def soort_van(pad: Path | None) -> str:
    if pad is None:
        return "afbeelding"
    s = pad.suffix.lower()
    return "tabel" if s in TABEL else "document" if s in DOCUMENT else "afbeelding"


def lees_register() -> dict[str, dict]:
    """Register uit bijlagen.yml, aangevuld met bijlagen die alleen als bestand bestaan.
    Titel valt terug op de bestandsnaam ('B0007 Hoofdprocesmodel.svg' -> 'Hoofdprocesmodel')."""
    data = {}
    if REGISTER.exists():
        data = yaml.safe_load(REGISTER.read_text(encoding="utf-8")) or {}
    reg = {str(k): dict(v or {}) for k, v in data.items() if RE_NUMMER.match(str(k))}
    extra = PAGINAS.parent / "bijlagetitels.yml"      # titels uit regels 'Bijlage B0007: titel'
    if extra.exists():
        for n, t in (yaml.safe_load(extra.read_text(encoding="utf-8")) or {}).items():
            reg.setdefault(str(n), {}).setdefault("titel", t)
    for n, pad in bijlagebestanden().items():
        b = reg.setdefault(n, {})
        if not b.get("titel"):
            rest = RE_BESTAND.match(pad.stem).group(2)
            if rest:
                b["titel"] = rest.strip()
        b.setdefault("soort", soort_van(pad))
    return reg


# ---------------------------------------------------------------- weergave

def tabel_html(pad: Path) -> str:
    """Zet een tabelbijlage (csv, xlsx of md) om naar HTML."""
    if pad.suffix.lower() == ".csv":
        tekst = pad.read_text(encoding="utf-8-sig")
        try:
            dialect = csv.Sniffer().sniff(tekst[:4096], delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        rijen = list(csv.reader(tekst.splitlines(), dialect))
    elif pad.suffix.lower() == ".xlsx":
        import openpyxl
        ws = openpyxl.load_workbook(pad, data_only=True, read_only=True).worksheets[0]
        rijen = [["" if c is None else str(c) for c in r] for r in ws.iter_rows(values_only=True)]
        rijen = [r for r in rijen if any(x.strip() for x in r)]
    else:
        import markdown
        return markdown.markdown(pad.read_text(encoding="utf-8"), extensions=["tables", "md_in_html"])
    if not rijen:
        return "<p><em>Lege tabel.</em></p>"
    kop, *rest = rijen

    def cel(x: str) -> str:
        return re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', html.escape(x))
    regels = ['<table class="bijlage-tabel"><thead><tr>'
              + "".join(f"<th>{cel(c)}</th>" for c in kop) + "</tr></thead><tbody>"]
    regels += ["<tr>" + "".join(f"<td>{cel(c)}</td>" for c in r) + "</tr>" for r in rest]
    regels.append("</tbody></table>")
    return "".join(regels)


def titel_van(nummer: str, b: dict) -> str:
    return str(b.get("titel") or f"Bijlage {nummer}")


def inhoud_html(nummer: str, b: dict, url_map: str) -> str:
    pad = bestand_van(nummer)
    titel = html.escape(titel_van(nummer, b))
    if pad is None:
        link = (f' <a href="{html.escape(b["horizzon"])}">Bekijk in BizzDesign Horizzon</a> (toegang vereist).'
                if b.get("horizzon") else "")
        return f'<div class="bijlage-ontbreekt">Bijlage {nummer} volgt; deze is nog niet aangeleverd.{link}</div>'
    src = f"{url_map}/{doelnaam(nummer, pad)}"
    s = pad.suffix.lower()
    if s in BEELD:
        return f'<a href="{src}"><img src="{src}" alt="{titel}" loading="lazy"></a>'
    if s in TABEL:
        return f'<div class="bijlage-tabelwrap">{tabel_html(pad)}</div>'
    return f'<p><a href="{src}">Download {titel} ({s[1:].upper()})</a></p>'


def onderschrift(nummer: str, b: dict, details_url: str | None, url_map: str = "bijlagen") -> str:
    titel = b.get("titel")
    delen = [f"<strong>Bijlage {nummer}</strong>" + (f" {html.escape(str(titel))}" if titel else "")]
    beelden = [f for f in alle_formaten(nummer) if f.suffix.lower() in BEELD]
    if beelden:
        delen.append("download " + " / ".join(
            f'<a href="{url_map}/{doelnaam(nummer, f)}" download>{f.suffix[1:].upper()}</a>' for f in beelden))
    if b.get("horizzon"):
        delen.append(f'<a href="{html.escape(b["horizzon"])}">bron in BizzDesign Horizzon</a>')
    if details_url:
        delen.append(f'<a href="{details_url}">details</a>')
    return " · ".join(delen)


def embed_html(nummer: str, reg: dict, url_map: str, details_url: str | None, id_: str | None = None) -> str:
    b = reg.get(nummer, {})
    soort = b.get("soort", soort_van(bestand_van(nummer)))
    ida = f' id="{id_}"' if id_ else ""
    return (f'\n<div class="bijlage bijlage-{soort}"{ida}>\n{inhoud_html(nummer, b, url_map)}\n'
            f'<p class="bijlage-onderschrift">{onderschrift(nummer, b, details_url, url_map)}</p>\n</div>\n')


def gebruik(paginas: list[Pagina]) -> dict[str, list[Pagina]]:
    """Op welke (gepubliceerde) pagina's wordt elke bijlage getoond of genoemd."""
    res: dict[str, list[Pagina]] = {}
    for p in alle(paginas):
        for n in sorted(set(RE_EMBED.findall(p.body)) | set(RE_ZIE.findall(p.body))):
            res.setdefault(n, []).append(p)
    return res


STIJL = ROOT / "stijl"


def kopieer_huisstijl(doel: Path) -> str | None:
    """Kopieert stijl/*.css naar <doel>/css/ en het logo (publicatie.yml: logo) naar <doel>/img/.
    Geeft het relatieve pad van het logo terug, of None."""
    import shutil
    (doel / "css").mkdir(parents=True, exist_ok=True)
    for f in STIJL.glob("*.css"):
        shutil.copy(f, doel / "css" / f.name)
    logo = instellingen().get("logo")
    if logo and (ROOT / logo).is_file():
        (doel / "img").mkdir(exist_ok=True)
        naam = "logo" + Path(logo).suffix.lower()
        shutil.copy(ROOT / logo, doel / "img" / naam)
        return f"img/{naam}"
    return None


# De bijlagestijl staat in stijl/huisstijl.css.
CSS = ""


def merk_html(cfg: dict, logo: str | None, href: str) -> str:
    """Merk linksboven: logo (publicatie.yml: logo) of een woordmerk van organisatie en titel."""
    if logo:
        return f'<a class="edw-merk" href="{href}"><img src="{logo}" alt="{html.escape(cfg.get("organisatie", ""))}"></a>'
    return (f'<a class="edw-merk" href="{href}"><span class="edw-merk__tekst">'
            f'<span class="edw-merk__org">{html.escape(cfg.get("organisatie", ""))}</span>'
            f'<span class="edw-merk__titel">{html.escape(cfg.get("titel", ""))}</span></span></a>')


def top_html(cfg: dict, logo: str | None, home: str, links: list[tuple[str, str]]) -> str:
    nav = "".join(f'<a href="{u}">{html.escape(t)}</a>' for t, u in links)
    return (f'<header class="edw-top"><div class="edw-top__inner">{merk_html(cfg, logo, home)}'
            f'<nav class="edw-top__nav">{nav}</nav></div></header>')


def footer_html(cfg: dict, links: list[tuple[str, str]]) -> str:
    import datetime
    nav = " · ".join(f'<a href="{u}">{html.escape(t)}</a>' for t, u in links)
    org = html.escape(cfg.get("organisatie", ""))
    if cfg.get("organisatie_url"):
        org = f'<a href="{html.escape(cfg["organisatie_url"])}">{org}</a>'
    return (f'<footer class="edw-footer"><div class="edw-footer__inner">'
            f'<div><div class="edw-footer__merk">{html.escape(cfg.get("titel", ""))}</div>'
            f'<div>{html.escape(cfg.get("status", ""))}</div></div>'
            f'<div><div>{nav}</div><div>© {datetime.date.today().year} {org}</div></div>'
            f'</div></footer>')


def versie_tag() -> str:
    """Korte tag tegen verouderde stylesheets in de browsercache (GitHub Pages cachet 10 min)."""
    import hashlib
    h = hashlib.sha1()
    for f in sorted(STIJL.glob("*.css")):
        h.update(f.read_bytes())
    return h.hexdigest()[:8]
