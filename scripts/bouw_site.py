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
from gemeen import ROOT, instellingen  # noqa: E402

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

    sjabloon = (ROOT / "site_root" / "index.template.html").read_text(encoding="utf-8")
    kaarten = "\n".join(f'<a class="kaart" href="{KAART[p][0]}"><strong>{KAART[p][1]}</strong><br>{KAART[p][2]}</a>'
                        for p in paden)
    (SITE / "index.html").write_text(
        sjabloon.replace("{{titel}}", html.escape(cfg.get("titel", "")))
        .replace("{{ondertitel}}", html.escape(cfg.get("ondertitel", "")))
        .replace("{{status}}", html.escape(cfg.get("status", "")))
        .replace("{{organisatie}}", html.escape(cfg.get("organisatie", "")))
        .replace("{{kaarten}}", kaarten), encoding="utf-8")
    print(f"Site gebouwd in {SITE} met: {', '.join(paden)}")


if __name__ == "__main__":
    main()
