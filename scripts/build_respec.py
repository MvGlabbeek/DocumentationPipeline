"""Publicatiepad 2: ReSpec (één doorlopend document met genummerde secties).

Gebruik: python scripts/build_respec.py [uitvoermap]   (standaard _site/respec)
- De startpagina wordt de samenvatting (abstract); elke pagina een genummerde sectie,
  subpagina's en koppen worden geneste secties.
- Links tussen pagina's worden ankers binnen het document.
- Bijlagen worden op hun plek getoond en staan samen in de bijlage 'Overzicht bijlagen'.
"""
from __future__ import annotations

import datetime
import html
import json
import posixpath
import re
import shutil
import sys
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemeen import (CSS, RE_EMBED, RE_ZIE, ROOT, Pagina, alle, bestand_van, embed_html,  # noqa: E402
                    gebruik, instellingen, lees_register, paginaboom)

RE_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s#]*)(#[^)\s]*)?\)")


def md_naar_html(p: Pagina, reg: dict, sleutels: dict[str, str]) -> str:
    body = RE_EMBED.sub(lambda m: embed_html(m.group(1), reg, "bijlagen", f"#{m.group(1)}"), p.body)
    body = RE_ZIE.sub(lambda m: f'<a class="bijlage-ref" href="#{m.group(1)}">bijlage {m.group(1)}</a>', body)

    def link(m):
        tekst, doel, anker = m.group(1), m.group(2), (m.group(3) or "")[1:]
        if doel.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        if doel and doel.endswith(".md"):
            pad = posixpath.normpath(posixpath.join(p.pad.parent.as_posix(), doel))
            s = sleutels.get(pad)
            if s is None:
                return tekst            # niet-gepubliceerde pagina
        else:
            s = sleutels[p.pad.as_posix()]
        return f"[{tekst}](#{s}--{anker})" if anker else f"[{tekst}](#{s})"
    body = RE_LINK.sub(link, body)
    return markdown.markdown(body, extensions=["tables", "attr_list", "md_in_html", "fenced_code", "toc"])


def nest(fragment: str, prefix: str) -> str:
    """Koppen worden geneste <section>s (voor ReSpec-nummering); id's krijgen de paginasleutel als voorvoegsel."""
    soep = BeautifulSoup(fragment, "html.parser")
    for el in soep.find_all(id=True):
        if not re.match(r"B\d{4}$", el["id"]):
            el["id"] = f"{prefix}--{el['id']}"
    wortel = BeautifulSoup("<div></div>", "html.parser").div
    stapel = [(1, wortel)]
    for el in list(soep.contents):
        naam = getattr(el, "name", None)
        if naam and re.match(r"^h[1-6]$", naam):
            niveau = int(naam[1])
            while stapel[-1][0] >= niveau:
                stapel.pop()
            sec = soep.new_tag("section")
            if el.get("id"):
                sec["id"] = el["id"]
                del el["id"]
            el.name = "h2"
            sec.append(el.extract())
            stapel[-1][1].append(sec)
            stapel.append((niveau, sec))
        else:
            stapel[-1][1].append(el.extract())
    return wortel.decode_contents()


def sectie(p: Pagina, reg, sleutels) -> str:
    binnen = nest(md_naar_html(p, reg, sleutels), sleutels[p.pad.as_posix()])
    kinderen = "\n".join(sectie(k, reg, sleutels) for k in p.kinderen)
    return (f'<section id="{sleutels[p.pad.as_posix()]}">\n<h2>{html.escape(p.titel)}</h2>\n'
            f"{binnen}\n{kinderen}\n</section>")


def bijlagen_sectie(reg: dict, gebruikt: dict, sleutels: dict) -> str:
    delen = ['<section class="appendix" id="overzicht-bijlagen"><h2>Overzicht bijlagen</h2>',
             "<p>Alle diagrammen, afbeeldingen, tabellen en documenten in dit document. Elke bijlage "
             "heeft een vast nummer; diagrammen uit BizzDesign Horizzon zijn daar onder hetzelfde nummer "
             "terug te vinden.</p>"]
    for n in sorted(gebruikt):
        b = reg.get(n, {})
        op = ", ".join(f'<a href="#{sleutels[p.pad.as_posix()]}">{html.escape(p.titel)}</a>' for p in gebruikt[n])
        extra = []
        if b.get("toelichting"):
            extra.append(f"<p>{html.escape(str(b['toelichting']))}</p>")
        f = bestand_van(n)
        regel = [f"Gebruikt in: {op}"]
        if f:
            regel.append(f'bestand: <a href="bijlagen/{f.name}">{f.name}</a>')
        extra.append(f"<p class=\"bijlage-onderschrift\">{' · '.join(regel)}</p>")
        delen.append(f'<section id="{n}"><h2>{n} {html.escape(str(b.get("titel", "")))}</h2>'
                     f'{embed_html(n, reg, "bijlagen", None)}{"".join(extra)}</section>')
    delen.append("</section>")
    return "\n".join(delen)


def main() -> None:
    uit = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site" / "respec"
    cfg = instellingen()
    start, paginas = paginaboom()
    if start is None and not paginas:
        sys.exit("Geen pagina's in bron/paginas/. Draai eerst scripts/confluence_naar_md.py.")
    reg = lees_register()
    sleutels = {p.pad.as_posix(): p.sleutel for p in alle(paginas)}
    if start:
        sleutels[start.pad.as_posix()] = "abstract"
    shutil.rmtree(uit, ignore_errors=True)
    (uit / "bijlagen").mkdir(parents=True)

    alle_p = ([start] if start else []) + paginas
    gebruikt = gebruik(alle_p)
    for n in gebruikt:
        f = bestand_van(n)
        if f:
            shutil.copy(f, uit / "bijlagen" / f.name)

    samenvatting = nest(md_naar_html(start, reg, sleutels), "abstract") if start else \
        f"<p>{html.escape(cfg.get('ondertitel', ''))}</p>"
    repo = cfg.get("repo", "")
    eigenaar, _, naam = repo.partition("/")
    config = {
        "specStatus": "base",
        "subtitle": f"{cfg.get('ondertitel', '')} · versie {cfg.get('versie', '')}",
        "publishDate": datetime.date.today().isoformat(),
        "editors": [{"name": r["naam"], "company": r.get("organisatie", "")} for r in cfg.get("redacteuren", [])],
        "otherLinks": [{"key": "Andere weergave", "data": [{"value": "MkDocs-site", "href": "../mkdocs/"}]}],
        "maxTocLevel": 3, "lint": False, "noRecTrack": True,
        "overrideCopyright": f"<p class='copyright'>© {datetime.date.today().year} "
                             f"{html.escape(cfg.get('organisatie', ''))}.</p>",
    }
    if repo:
        config["github"] = f"https://github.com/{repo}"
        config["latestVersion"] = f"https://{eigenaar.lower()}.github.io/{naam}/respec/"
    sjabloon = (ROOT / "respec" / "index.template.html").read_text(encoding="utf-8")
    pagina = (sjabloon
              .replace("{{titel}}", html.escape(cfg.get("titel", "")))
              .replace("{{config}}", json.dumps(config, ensure_ascii=False, indent=2))
              .replace("{{css}}", CSS)
              .replace("{{samenvatting}}", samenvatting)
              .replace("{{status}}", html.escape(cfg.get("status", "")))
              .replace("{{secties}}", "\n".join(sectie(p, reg, sleutels) for p in paginas))
              .replace("{{bijlagen}}", bijlagen_sectie(reg, gebruikt, sleutels)))
    (uit / "index.html").write_text(pagina, encoding="utf-8")
    print(f"ReSpec gebouwd: {sum(1 for _ in alle(paginas))} pagina's, {len(gebruikt)} bijlagen -> {uit}")


if __name__ == "__main__":
    main()
