# Get top 3 hotfixid and description from most recently installed 
Get-HotFix |
Sort-Object  InstalledOn -Descending |
Select-Object -First 10 | 
Select-Object  HotFixID, Description |
Export-Csv "Evidence/Top3HotfixeLogs.csv"  -NoTypeInformation

Write-Host "Exported top 3 hotfixid and description from most recently installed to Evidence/Top3HotfixeLogs.csv"