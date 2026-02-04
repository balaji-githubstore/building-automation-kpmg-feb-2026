
$PSVersionTable.PSVersion


Get-EventLog -LogName Security |
	Sort-Object TimeGenerated -Descending |
	Select-Object -First 10 |
	Export-Csv "Evidence/SecurityLogs.csv" -NoTypeInformation

Write-Host "LOGGED: 50 recent Security logs is added to Evidence/SecurityLogs.csv"


