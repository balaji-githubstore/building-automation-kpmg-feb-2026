# Incident Evidence Collection Workflow Script
# demo5.ps1

# 1. Define the incident trigger and responsible personnel
Write-Host "Incident reported. Initiating evidence collection..."
# (Add logic to identify responsible personnel if needed)

# 2. Collect relevant system logs
Write-Host "Collecting system logs..."
.\demo1_systemlogs.ps1

# 3. Collect security/audit logs
Write-Host "Collecting security/audit logs..."
.\demo2_adminAuditLogs.ps1

# 4. Generate a list of installed patches/hotfixes
Write-Host "Collecting installed patches/hotfixes..."
.\demo3_hotfixeslogs.ps1

# 5. Save all collected evidence files in the Evidence folder
Write-Host "Saving evidence files to Evidence folder..."
# (Assume each script outputs to Evidence/ with proper naming/timestamp)

# 6. Notify the audit team
Write-Host "Evidence collection complete. Notify audit team."
# (Notification is manual as per plan)
