## Plan: Incident Evidence Collection Workflow

This plan outlines a workflow for immediate evidence collection following an incident report. It ensures system and security logs, as well as patch/hotfix information, are gathered and securely stored for audit and investigation purposes.

### Steps
1. Define the incident trigger and responsible personnel for initiating evidence collection.
2. Use or adapt [demo1_systemlogs.ps1](demo1_systemlogs.ps1) to collect relevant system logs.
3. Use or adapt [demo2_adminAuditLogs.ps1](demo2_adminAuditLogs.ps1) to collect security/audit logs.
4. Use or adapt [demo3_hotfixeslogs.ps1](demo3_hotfixeslogs.ps1) to generate a list of installed patches/hotfixes.
5. Save all collected evidence files in the [Evidence/](Evidence/) folder, ensuring proper naming and timestamps.
6. Notify the audit team (via email or internal system) that evidence is collected and available in [Evidence/](Evidence/).

### Further Considerations
1. Should notification be automated (e.g., email script) or manual?
NO
2. Are there specific log retention or access control requirements for [Evidence/](Evidence/)?
No
3. Should scripts be combined into a single orchestrator for efficiency?
No