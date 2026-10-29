"""Gedeelde onderdelen voor de converter en beide publicatiepaden.

Begrippen
- Pagina: een Markdown-bestand in bron/paginas/ met front matter (titel, volgorde, ...).
  Een pagina met subpagina's is een map met index.md; de subpagina's staan in die map.
- Bijlage: een los, uniek genummerd onderdeel (B0001, B0002, ...): diagram, afbeelding,
  tabel of document. Het bestand heet naar het nummer (B0007.svg, B0012.csv) en staat in
  bron/bijlagen/. De metadata staat in bron/bijlagen/bijlagen.yml.
- Verwijzingen in de tekst:
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
PAGINAS = BRON / "paginas"
BIJLAGEN = BRON / "bijlagen"
REGISTER = BIJLAGEN / "bijlagen.yml"

# Voorkeursvolgorde als er meerdere bestanden met hetzelfde nummer staan.
BEELD = (".svg", ".png", ".webp", ".jpg", ".jpeg", ".gif")
TABEL = (".csv", ".xlsx", ".md")
DOCUMENT = (".pdf", ".docx", ".pptx", ".zip")
SOORTEN = ("diagram", "afbeelding", "tabel", "document")

RE_EMBED = re.compile(r"^[ \t]*\[\[bijlage:(B\d{4})\]\][ \t]*$", re.M)
RE_ZIE = re.compile(r"\[\[zie:(B\d{4})\]\]")
RE_NUMMER = re.compile(r"^B(\d{4})$")


# ---------------------------------------------------------------- instellingen

def instellingen() -> dict:
    return yaml.safe_load((ROOT / "publicatie.yml").read_text(encoding="utf-8")) or {}


# ---------------------------------------------------------------- front matter

def lees_md(pad: Path) -> tuple[dict, str]:
    tekst = pad.read_text(encoding="utf-8")
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


# ---------------------------------------------------------------- paginaboom

@dataclass
class Pagina:
    pad: Path                      # relatief t.o.v. bron/paginas, bijv. architectuur/index.md
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
    """Geeft (startpagina, hoofdstukken). De startpagina is bron/paginas/index.md (optioneel)."""
    def lees(pad: Path) -> Pagina:
        meta, body = lees_md(pad)
        rel = pad.relative_to(PAGINAS)
        titel = meta.get("titel") or pad.stem.replace("-", " ").capitalize()
        return Pagina(rel, str(titel), int(meta.get("volgorde", 999)), meta, body)

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
        if alleen_publiek:
            res = [x for x in res if x.publiek]
        return res

    if not PAGINAS.is_dir():
        return None, []
    start = lees(PAGINAS / "index.md") if (PAGINAS / "index.md").exists() else None
    return start, map_(PAGINAS)


def alle(paginas: list[Pagina]):
    for p in paginas:
        yield p
        yield from alle(p.kinderen)


# ---------------------------------------------------------------- bijlagen

def lees_register() -> dict[str, dict]:
    if not REGISTER.exists():
        return {}
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8")) or {}
    return {k: (v or {}) for k, v in data.items() if RE_NUMMER.match(str(k))}


KOP_REGISTER = """\
# Register van bijlagen (diagrammen, afbeeldingen, tabellen, documenten).
#
# - Het nummer (B0001) is vast en wordt nooit hergebruikt. Een nieuwe bijlage krijgt
#   het eerstvolgende vrije nummer.
# - Het bestand heet naar het nummer en staat in deze map: B0001.svg, B0002.png,
#   B0003.csv. Een export uit BizzDesign vervangt eenvoudig het bestand met hetzelfde nummer.
# - Velden: titel, soort (diagram|afbeelding|tabel|document), horizzon (link naar de view
#   in BizzDesign Horizzon), toelichting, bron (confluence|bizzdesign|handmatig).
#   'sleutel' en 'confluence' worden door de converter beheerd; niet wijzigen.
"""


def schrijf_register(reg: dict[str, dict]) -> None:
    BIJLAGEN.mkdir(parents=True, exist_ok=True)
    volg = ("titel", "soort", "bron", "horizzon", "toelichting", "confluence", "sleutel")
    netjes = {}
    for k in sorted(reg):
        v = reg[k]
        netjes[k] = {**{x: v[x] for x in volg if v.get(x) not in (None, "")},
                     **{x: y for x, y in v.items() if x not in volg and y not in (None, "")}}
    REGISTER.write_text(KOP_REGISTER + "\n" + yaml.safe_dump(
        netjes, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")


def volgend_nummer(reg: dict) -> str:
    bestaand = [int(RE_NUMMER.match(k).group(1)) for k in reg]
    bestaand += [int(m.group(1)) for p in BIJLAGEN.glob("B[0-9][0-9][0-9][0-9].*")
                 if (m := RE_NUMMER.match(p.stem))]
    return f"B{(max(bestaand) + 1 if bestaand else 1):04d}"


def bestand_van(nummer: str, map_: Path = BIJLAGEN) -> Path | None:
    for ext in BEELD + TABEL + DOCUMENT:
        p = map_ / f"{nummer}{ext}"
        if p.exists():
            return p
    return None


# ---------------------------------------------------------------- weergave

def tabel_html(pad: Path) -> str:
    """Zet een tabelbijlage (csv, xlsx of md) om naar HTML."""
    if pad.suffix == ".csv":
        tekst = pad.read_text(encoding="utf-8-sig")
        try:
            dialect = csv.Sniffer().sniff(tekst[:4096], delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        rijen = list(csv.reader(tekst.splitlines(), dialect))
    elif pad.suffix == ".xlsx":
        import openpyxl
        ws = openpyxl.load_workbook(pad, data_only=True, read_only=True).worksheets[0]
        rijen = [["" if c is None else str(c) for c in r] for r in ws.iter_rows(values_only=True)]
        rijen = [r for r in rijen if any(x.strip() for x in r)]
    else:  # .md: kan pipe-tabel of HTML bevatten
        import markdown
        return markdown.markdown(pad.read_text(encoding="utf-8"), extensions=["tables", "md_in_html"])
    if not rijen:
        return "<p><em>Lege tabel.</em></p>"
    kop, *rest = rijen
    def cel(x: str) -> str:
        x = html.escape(x)
        return re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', x)
    regels = ["<table class=\"bijlage-tabel\"><thead><tr>"
              + "".join(f"<th>{cel(c)}</th>" for c in kop) + "</tr></thead><tbody>"]
    regels += ["<tr>" + "".join(f"<td>{cel(c)}</td>" for c in r) + "</tr>" for r in rest]
    regels.append("</tbody></table>")
    return "".join(regels)


def inhoud_html(nummer: str, b: dict, url_map: str) -> str:
    """De bijlage zelf (afbeelding, tabel, link of plaatshouder). url_map: pad naar bijlagenmap."""
    pad = bestand_van(nummer)
    titel = html.escape(str(b.get("titel") or nummer))
    if pad is None:
        if b.get("horizzon"):
            return (f'<div class="bijlage-ontbreekt">Dit diagram is nog niet uit BizzDesign '
                    f'geëxporteerd. <a href="{html.escape(b["horizzon"])}">Bekijk het in Horizzon</a> '
                    f'(toegang vereist) of exporteer het als <code>{nummer}.svg</code> naar '
                    f'<code>bron/bijlagen/</code>.</div>')
        return f'<div class="bijlage-ontbreekt">Bestand <code>{nummer}.*</code> ontbreekt in <code>bron/bijlagen/</code>.</div>'
    src = f"{url_map}/{pad.name}"
    if pad.suffix in BEELD:
        return f'<a href="{src}"><img src="{src}" alt="{titel}" loading="lazy"></a>'
    if pad.suffix in TABEL:
        return f'<div class="bijlage-tabelwrap">{tabel_html(pad)}</div>'
    return f'<p><a href="{src}">Download {titel} ({pad.suffix[1:].upper()})</a></p>'


def onderschrift(nummer: str, b: dict, details_url: str | None) -> str:
    delen = [f"<strong>Bijlage {nummer}</strong> {html.escape(str(b.get('titel') or ''))}".strip()]
    if b.get("horizzon"):
        delen.append(f'<a href="{html.escape(b["horizzon"])}">bron in BizzDesign Horizzon</a>')
    if details_url:
        delen.append(f'<a href="{details_url}">details</a>')
    return " · ".join(delen)


def embed_html(nummer: str, reg: dict, url_map: str, details_url: str | None, id_: str | None = None) -> str:
    b = reg.get(nummer)
    if b is None:
        print(f"::warning::Verwijzing naar onbekende bijlage {nummer}")
        return f'<p class="bijlage-ontbreekt">Onbekende bijlage {nummer}.</p>'
    soort = b.get("soort", "afbeelding")
    ida = f' id="{id_}"' if id_ else ""
    return (f'\n<div class="bijlage bijlage-{soort}"{ida}>\n{inhoud_html(nummer, b, url_map)}\n'
            f'<p class="bijlage-onderschrift">{onderschrift(nummer, b, details_url)}</p>\n</div>\n')


def gebruik(paginas: list[Pagina]) -> dict[str, list[Pagina]]:
    """Op welke (gepubliceerde) pagina's wordt elke bijlage getoond of genoemd."""
    res: dict[str, list[Pagina]] = {}
    for p in alle(paginas):
        for n in set(RE_EMBED.findall(p.body)) | set(RE_ZIE.findall(p.body)):
            res.setdefault(n, []).append(p)
    return res


CSS = """
.bijlage { margin: 1.2em 0; padding: .8em; border: 1px solid var(--rand, #d0d7d7); border-radius: 6px; }
.bijlage img { max-width: 100%; height: auto; display: block; margin: 0 auto; }
.bijlage-onderschrift { font-size: .85em; margin: .6em 0 0; color: var(--zacht, #4a5a5a); }
.bijlage-tabelwrap { overflow-x: auto; }
.bijlage-tabel { border-collapse: collapse; font-size: .85em; width: 100%; }
.bijlage-tabel th, .bijlage-tabel td { border: 1px solid #c8d2d2; padding: .3em .5em; vertical-align: top; text-align: left; }
.bijlage-tabel th { background: #e6f2f1; }
.bijlage-ontbreekt { padding: .8em; background: #fff6e0; border-left: 4px solid #e0a800; font-size: .9em; }
.bijlage-register td, .bijlage-register th { font-size: .85em; }
"""
