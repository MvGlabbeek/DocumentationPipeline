"""Platformonafhankelijke variant van haal_exports.ps1.
Gebruik: python scripts/haal_exports.py exports/exports-2026-11-06.tsv bron/bijlagen"""
import csv, sys, pathlib, urllib.request
lijst, doel = sys.argv[1], pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "bron/bijlagen")
doel.mkdir(parents=True, exist_ok=True)
for r in csv.DictReader(open(lijst, encoding="utf-8"), delimiter="\t"):
    try:
        urllib.request.urlretrieve(r["url"], doel / r["bestand"])
        print("OK ", r["bijlage"], r["sleutel"], f"[{r['status']}]")
    except Exception as e:
        print("MISLUKT", r["bijlage"], e, "(verlopen? opnieuw exporteren via de MCP)")
