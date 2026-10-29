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


def onderschrift(nummer: str, b: dict, details_url: str | None) -> str:
    titel = b.get("titel")
    delen = [f"<strong>Bijlage {nummer}</strong>" + (f" {html.escape(str(titel))}" if titel else "")]
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
            f'<p class="bijlage-onderschrift">{onderschrift(nummer, b, details_url)}</p>\n</div>\n')


def gebruik(paginas: list[Pagina]) -> dict[str, list[Pagina]]:
    """Op welke (gepubliceerde) pagina's wordt elke bijlage getoond of genoemd."""
    res: dict[str, list[Pagina]] = {}
    for p in alle(paginas):
        for n in sorted(set(RE_EMBED.findall(p.body)) | set(RE_ZIE.findall(p.body))):
            res.setdefault(n, []).append(p)
    return res


CSS = """
.bijlage { margin: 1.2em 0; padding: .8em; border: 1px solid #d0d7d7; border-radius: 6px; }
.bijlage img { max-width: 100%; height: auto; display: block; margin: 0 auto; }
.bijlage-onderschrift { font-size: .85em; margin: .6em 0 0; opacity: .85; }
.bijlage-tabelwrap { overflow-x: auto; }
.bijlage-tabel { border-collapse: collapse; font-size: .85em; width: 100%; }
.bijlage-tabel th, .bijlage-tabel td { border: 1px solid #c8d2d2; padding: .3em .5em; vertical-align: top; text-align: left; }
.bijlage-tabel th { background: rgba(0, 133, 124, .1); }
.bijlage-ontbreekt { padding: .8em; background: rgba(224, 168, 0, .12); border-left: 4px solid #e0a800; font-size: .9em; }
.bijlage-register td, .bijlage-register th { font-size: .85em; }
"""
