# Haalt de Horizzon-exports op (URL's uit de MCP zijn 24 uur geldig) en zet ze in bron\bijlagen.
# Gebruik (PowerShell, vanuit de map van de pilot):  .\scripts\haal_exports.ps1 .\exports\exports-2026-11-06.tsv
param([string]$Lijst = ".\exports\exports-2026-11-06.tsv", [string]$Doel = ".\bron\bijlagen")
New-Item -ItemType Directory -Force -Path $Doel | Out-Null
Import-Csv -Path $Lijst -Delimiter "`t" | ForEach-Object {
    $pad = Join-Path $Doel $_.bestand
    try {
        Invoke-WebRequest -Uri $_.url -OutFile $pad -UseBasicParsing
        Write-Host "OK  $($_.bijlage)  $($_.sleutel)  [$($_.status)]"
    } catch {
        Write-Warning "MISLUKT $($_.bijlage): $($_.Exception.Message) (verlopen? Exporteer opnieuw via de MCP.)"
    }
}
