# find all files with the passed string and list their names

# -S - search keyword
# -R - recurse
# -F - file to search in

[bool] $recurse = $false
$patterns = [System.Collections.ArrayList]::new()
$files = [System.Collections.ArrayList]::new()

foreach ($arg in $args) {
    
}

Get-ChildItem $args[0] -Recurse | ForEach-Object { Get-Content $_ -Raw }