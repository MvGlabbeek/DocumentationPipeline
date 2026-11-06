"""Voert de hele MSP-pilotketen uit.

  1. PDF -> raw.md          (pymupdf4llm, alleen als raw.md ontbreekt; ~2 min)
  2. raw.md -> MSP-volledig.md + figuren.json      (msp_naar_md.py)
  3. figuren + Horizzon-catalogus -> bijlagen.yml   (koppel.py)
  4. titels uit het register terugschrijven in de Markdown
  5. splitsen in bron/paginas + structuur.yml      (splits_paginas.py)

Gebruik: python scripts/bouw_pilot.py msp.pdf
"""
import re, subprocess, sys, pathlib, yaml

pdf = sys.argv[1]
root = pathlib.Path(__file__).resolve().parent.parent
werk = root / "werk"
# in de DocumentationPipeline-repo staat bron/ naast deze map; los gebruikt erin
bron = root.parent / "bron" if (root.parent / "publicatie.yml").exists() else root / "bron"
py = [sys.executable, "-I"]
s = root / "scripts"

if not (werk / "raw.md").exists():
    import pymupdf4llm
    werk.mkdir(exist_ok=True)
    md = pymupdf4llm.to_markdown(pdf, write_images=True, image_path=str(werk / "img"),
                                 use_ocr=False, force_text=False, header=True, footer=False)
    (werk / "raw.md").write_text(md.replace(str(werk / "img"), "img"), encoding="utf-8")

subprocess.run(py + [s / "msp_naar_md.py", pdf, werk / "raw.md", werk], check=True)
(bron / "bijlagen").mkdir(parents=True, exist_ok=True)
subprocess.run(py + [s / "koppel.py", werk / "figuren.json", werk / "horizzon_catalogus.json",
                     root / "beoordeling.yml", bron / "bijlagen" / "bijlagen.yml"], check=True)

reg = yaml.safe_load(open(bron / "bijlagen" / "bijlagen.yml", encoding="utf-8"))
volledig = werk / "MSP-volledig.md"
txt = volledig.read_text(encoding="utf-8")
txt = re.sub(r"^Bijlage (B\d{4}):.*$", lambda m: f"Bijlage {m.group(1)}: {reg[m.group(1)]['titel']}", txt, flags=re.M)
volledig.write_text(txt, encoding="utf-8")

subprocess.run(py + [s / "splits_paginas.py", volledig, bron], check=True)

# 5b. in het doorlopende document (niet in bron/paginas: daar maakt de pipeline het onderschrift
#     met de Horizzon-link uit het register) komt de link direct onder de plaat
def met_link(m):
    e = reg[m.group(1)]
    regel = m.group(0)
    if e.get("horizzon"):
        status = "" if e["status"] == "gekoppeld" else " · koppeling nog te bevestigen"
        regel += f"\n\n[Bekijk de view in BizzDesign Horizzon: {e['horizzon_view']}]({e['horizzon']}) (toegang vereist{status})"
    return regel
volledig.write_text(re.sub(r"^Bijlage (B\d{4}):.*$", met_link, txt, flags=re.M), encoding="utf-8")

# 6. tussenoplossing: figuren zonder (bevestigde) Horizzon-view krijgen de uitsnede uit de PDF
import shutil
for b, e in reg.items():
    if e["status"] in ("view ontbreekt", "geen Horizzon-bron"):
        naam = re.sub(r'[\\/:*?"<>|]', "", f"{b} {e['titel']}")[:90].strip() + ".png"
        for oud in (bron / "bijlagen").glob(f"{b} *.png"):
            oud.unlink()
        shutil.copy(werk / e["referentie_pdf"], bron / "bijlagen" / naam)
subprocess.run(py + [s / "dekking.py", bron / "bijlagen" / "bijlagen.yml", root / "DEKKING.md"], check=True)
