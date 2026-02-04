
# Script: Export Local Administrators Audit Log
# Description: Retrieves local administrator group members and exports details to a CSV file for evidence collection.

# Define output file path
$outputPath = "Evidence/AdminAccessUsers.csv"

# Get local administrators and select relevant properties
$adminMembers = Get-LocalGroupMember -Group "Administrators" |
	Select-Object Name, PrincipalSource

# Export results to CSV
$adminMembers | Export-Csv $outputPath -NoTypeInformation

# Notify user of export location
Write-Host "Exported admin details to $outputPath"

