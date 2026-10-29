"""Publicatiepad 1: MkDocs Material (meerdere pagina's, navigatie, zoeken).

Gebruik: python scripts/build_mkdocs.py   -> schrijft _build/mkdocs_docs/ en mkdocs.yml
Daarna:  mkdocs build -d _site/mkdocs   (of: mkdocs serve)
"""
from __future__ import annotations

import html
import posixpath
import re
import shutil
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemeen import (CSS, versie_tag, kopieer_huisstijl, RE_EMBED, RE_ZIE, ROOT, Pagina, alle, bestand_van, doelnaam, embed_html, kopieer_bijlage,  # noqa: E402
                    gebruik, instellingen, lees_register, paginaboom)

DOCS = ROOT / "_build" / "mkdocs_docs"
OVERZICHT = "overzicht-bijlagen.md"
RE_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s#]+\.md)(#[^)\s]*)?\)")


def niet_publieke_paden() -> set[str]:
    _, alles = paginaboom(alleen_publiek=False)
    verborgen = set()
    def loop(ps, verborgen_ouder=False):
        for p in ps:
            weg = verborgen_ouder or not p.publiek
            if weg:
                verborgen.add(p.pad.as_posix())
            loop(p.kinderen, weg)
    loop(alles)
    return verborgen


def verwerk(p: Pagina, reg: dict, verborgen: set[str]) -> str:
    diepte = len(p.pad.parts) - 1
    rel = "../" * diepte
    body = RE_EMBED.sub(lambda m: embed_html(m.group(1), reg, f"{rel}bijlagen",
                                             f"{rel}{OVERZICHT[:-3]}.html#{m.group(1)}"), p.body)
    body = RE_ZIE.sub(lambda m: f'<a class="bijlage-ref" href="{rel}{OVERZICHT[:-3]}.html#{m.group(1)}">'
                                f'bijlage {m.group(1)}</a>', body)

    def link(m):                     # links naar niet-gepubliceerde pagina's worden gewone tekst
        doel = posixpath.normpath(posixpath.join(p.pad.parent.as_posix(), m.group(2)))
        return m.group(1) if doel in verborgen else m.group(0)
    body = RE_LINK.sub(link, body)
    return f"# {p.titel}\n\n{body}"


def overzicht(reg: dict, gebruikt: dict[str, list[Pagina]]) -> str:
    regels = ["# Overzicht bijlagen", "",
              "Alle diagrammen, afbeeldingen en tabellen in deze publicatie. Elke bijlage heeft een "
              "vast nummer, waaronder hij ook in BizzDesign Horizzon terug te vinden is.", "",
              '<table class="bijlage-register"><thead><tr><th>Nr.</th><th>Titel</th><th>Soort</th>'
              "<th>Status</th><th>Gebruikt op</th></tr></thead><tbody>"]
    nummers = sorted(gebruikt)
    for n in nummers:
        b = reg.get(n, {})
        op = ", ".join(f'<a href="{posixpath.splitext(p.pad.as_posix())[0]}.html">{html.escape(p.titel)}</a>'
                       for p in gebruikt[n])
        regels.append(f'<tr><td><a href="#{n}">{n}</a></td><td>{html.escape(str(b.get("titel", "")))}</td>'
                      f'<td>{b.get("soort", "")}</td><td>{"aangeleverd" if bestand_van(n) else "volgt"}</td><td>{op}</td></tr>')
    regels += ["</tbody></table>", ""]
    for n in nummers:
        b = reg.get(n, {})
        regels += [f"## {n} {b.get('titel', '')}".rstrip() + f" {{#{n}}}", ""]
        regels.append(embed_html(n, reg, "bijlagen", None))
        meta = []
        if b.get("toelichting"):
            meta.append(f"- **Toelichting:** {b['toelichting']}")
        f = bestand_van(n)
        if f and f.suffix != ".md":
            meta.append(f"- **Bestand:** [{doelnaam(n, f)}](bijlagen/{doelnaam(n, f)})")
        if b.get("horizzon"):
            meta.append(f"- **BizzDesign Horizzon:** [open de view]({b['horizzon']}) (toegang vereist)")
        meta.append("- **Gebruikt op:** " + ", ".join(f"[{p.titel}]({p.pad.as_posix()})" for p in gebruikt[n]))
        regels += meta + [""]
    return "\n".join(regels)


def nav_van(paginas: list[Pagina]) -> list:
    res = []
    for p in paginas:
        if p.kinderen:
            res.append({p.titel: [p.pad.as_posix()] + nav_van(p.kinderen)})
        else:
            res.append({p.titel: p.pad.as_posix()})
    return res


def main() -> None:
    cfg = instellingen()
    start, paginas = paginaboom()
    if start is None and not paginas:
        sys.exit("Geen pagina's in bron/paginas/. Draai eerst scripts/inname.py.")
    reg = lees_register()
    verborgen = niet_publieke_paden()
    shutil.rmtree(DOCS, ignore_errors=True)
    (DOCS / "bijlagen").mkdir(parents=True)
    logo = kopieer_huisstijl(DOCS)

    for p in alle(paginas):
        (DOCS / p.pad).parent.mkdir(parents=True, exist_ok=True)
        (DOCS / p.pad).write_text(verwerk(p, reg, verborgen), encoding="utf-8")

    startpagina = start or Pagina(Path("index.md"), cfg.get("titel", "Architectuur"), 0, {}, "")
    knoppen = (f'\n\n[Overzicht bijlagen]({OVERZICHT}){{ .md-button }} '
               f'<a class="md-button" href="../respec/">Eén doorlopend document (ReSpec)</a>\n')
    (DOCS / "index.md").write_text(verwerk(startpagina, reg, verborgen) + knoppen, encoding="utf-8")

    gebruikt = gebruik(([start] if start else []) + paginas)
    for n in gebruikt:                      # alleen bijlagen van gepubliceerde pagina's gaan mee
        f = bestand_van(n)
        if f and f.suffix != ".md":         # .md-tabellen staan al in de pagina; MkDocs zou er een pagina van maken
            kopieer_bijlage(n, DOCS / "bijlagen")
    (DOCS / OVERZICHT).write_text(overzicht(reg, gebruikt), encoding="utf-8")

    basis = yaml.safe_load((ROOT / "mkdocs.base.yml").read_text(encoding="utf-8"))
    repo = cfg.get("repo", "")
    eigenaar, _, naam = repo.partition("/")
    basis.update({
        "site_name": cfg.get("titel", "Architectuur"),
        "site_description": cfg.get("ondertitel", ""),
        "site_author": ", ".join(r["naam"] for r in cfg.get("redacteuren", [])),
        "docs_dir": "_build/mkdocs_docs",
        "use_directory_urls": False,
        "nav": [{"Home": "index.md"}] + nav_van(paginas) + [{"Overzicht bijlagen": OVERZICHT}],
    })
    if repo:
        basis.setdefault("repo_url", f"https://github.com/{repo}")
        basis.setdefault("repo_name", repo)
        basis.setdefault("site_url", f"https://{eigenaar.lower()}.github.io/{naam}/mkdocs/")
    v = versie_tag()
    basis["extra_css"] = [f"css/huisstijl.css?v={v}", f"css/mkdocs.css?v={v}"] + basis.get("extra_css", [])
    if logo:
        basis["theme"]["logo"] = logo
        basis["theme"]["favicon"] = logo
    import datetime
    basis["copyright"] = (f"© {datetime.date.today().year} {cfg.get('organisatie', '')} · "
                          f"{cfg.get('status', '')}")
    (ROOT / "mkdocs.yml").write_text(
        "# Gegenereerd door scripts/build_mkdocs.py; wijzig mkdocs.base.yml of publicatie.yml.\n"
        + yaml.safe_dump(basis, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"MkDocs-bron gebouwd: {sum(1 for _ in alle(paginas))} pagina's, {len(gebruikt)} bijlagen.")


if __name__ == "__main__":
    main()
