$files = [System.Collections.ArrayList]::new()
$keywords = [System.Collections.ArrayList]::new()

Get-ChildItem *.fasta -Recurse | ForEach-Object {Get-Content $_ -Filter -Raw } | Select-String "Nakhon" 

Get-ChildItem *.fasta -Recurse | ForEach-Object {if ((Get-Content $_ -Raw).ToString().Contains("SLCMV")) {Write-Host $_.FullName}}
