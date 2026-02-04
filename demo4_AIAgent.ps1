<# Extract failed Windows login attempts (Event ID 4625) from Security logs and export to CSV #>
$outputFile = "Evidence/FailedLogins.csv"
$events = Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} | Select-Object TimeCreated, @{Name='User';Expression={$_.Properties[5].Value}}, @{Name='IpAddress';Expression={$_.Properties[18].Value}}, @{Name='FailureReason';Expression={$_.Properties[23].Value}}
$events | Export-Csv $outputFile -NoTypeInformation
Write-Host "Exported failed login attempts to $outputFile"
