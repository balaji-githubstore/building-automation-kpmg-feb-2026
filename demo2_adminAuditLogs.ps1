# Get the admin details of the system and export to Evidence/AdminAccessUsers.csv 

Get-LocalGroupMember -Group  "Administrators" |
Select-Object  Name, PrincipleSource |
Export-Csv  "Evidence/AdminAccessUsers.csv" -NoTypeInformation

Write-Host  "Exported admin details to Evidence/AdminAccessUsers.csv"

