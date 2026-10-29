"""Bouwt de complete site in _site/: startpagina plus de publicatiepaden uit publicatie.yml.

Gebruik: python scripts/bouw_site.py [--controle]
  (eerst scripts/inname.py: pagina's uit bron/paginas ordenen volgens bron/structuur.yml;
   met --controle wordt bron/structuur.yml niet bijgewerkt)
Lokaal bekijken: python -m http.server -d _site 8000  -> http://localhost:8000
"""
import html
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemeen import ROOT, footer_html, versie_tag, instellingen, kopieer_huisstijl, top_html  # noqa: E402

SITE = ROOT / "_site"
KAART = {
    "mkdocs": ("mkdocs/", "MkDocs-site", "Per pagina, met navigatie volgens de Confluence-paginaboom en een zoekfunctie."),
    "respec": ("respec/", "ReSpec-document", "Eén doorlopend document met genummerde secties, inhoudsopgave en bijlagen."),
}


def main() -> None:
    cfg = instellingen()
    paden = [p for p in cfg.get("paden", ["mkdocs", "respec"]) if p in KAART]
    shutil.rmtree(SITE, ignore_errors=True)
    SITE.mkdir()
    (SITE / ".nojekyll").touch()
    py = sys.executable
    os.environ.setdefault("NO_MKDOCS_2_WARNING", "true")   # melding van Material over MkDocs 2.0 (zie README)
    subprocess.run([py, "scripts/inname.py"] + sys.argv[1:], cwd=ROOT, check=True)
    if "mkdocs" in paden:
        subprocess.run([py, "scripts/build_mkdocs.py"], cwd=ROOT, check=True)
        subprocess.run([py, "-m", "mkdocs", "build", "-q", "-d", str(SITE / "mkdocs")], cwd=ROOT, check=True)
    if "respec" in paden:
        subprocess.run([py, "scripts/build_respec.py", str(SITE / "respec")], cwd=ROOT, check=True)

    logo = kopieer_huisstijl(SITE)
    sjabloon = (ROOT / "site_root" / "index.template.html").read_text(encoding="utf-8")
    kaarten = "\n".join(
        f'<a class="keuze edw-kaart" href="{KAART[p][0]}"><span><strong>{KAART[p][1]}</strong>'
        f'<span class="uitleg">{KAART[p][2]}</span></span><span class="edw-pijl" aria-hidden="true"></span></a>'
        for p in paden)
    titel = cfg.get("titel", "")
    *kop, laatste = titel.split(" ") if titel else [""]
    titel_html = html.escape(" ".join(kop)) + (" " if kop else "") + f"<em>{html.escape(laatste)}</em>"
    links = [(KAART[p][1], KAART[p][0]) for p in paden]
    repo = cfg.get("repo")
    (SITE / "index.html").write_text(
        sjabloon.replace("{{titel}}", html.escape(titel))
        .replace("{{v}}", versie_tag())
        .replace("{{titel_html}}", titel_html)
        .replace("{{ondertitel}}", html.escape(cfg.get("ondertitel", "")))
        .replace("{{status}}", html.escape(cfg.get("status", "")))
        .replace("{{bovenbalk}}", top_html(cfg, logo, "./", links))
        .replace("{{footer}}", footer_html(cfg, links + ([("Broncode", f"https://github.com/{repo}")] if repo else [])))
        .replace("{{kaarten}}", kaarten), encoding="utf-8")
    print(f"Site gebouwd in {SITE} met: {', '.join(paden)}")


if __name__ == "__main__":
    main()
