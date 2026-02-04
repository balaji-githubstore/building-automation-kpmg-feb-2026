import csv

input_file = r"D:\Mine\Company\KPMG Feb 2026\BuildingAutomationSession\Evidence\SecurityLogs.csv"
output_file=r"D:\Mine\Company\KPMG Feb 2026\BuildingAutomationSession\Evidence\IncidentReportSecurityLogSummary.log"


cred_reads=[]

with open(input_file,"r") as file:
    reader=csv.DictReader(file)
    for row in reader:
    #  Event Id -  Credential Manager credentials were read.
      if row["EventID"]=="5379":
        cred_reads.append(row)


with open(output_file,"w") as report:
   report.write("Incident Report Summary\n")
   report.write("=======================\n\n")
   report.write(f"Total Credential Manager Read Events: {len(cred_reads)}\n")
   report.write("=======================\n\n")
   report.write("\nDetails of Credential Manager Read Events:\n")

   for event in cred_reads:
      report.write(f"EventID: {event['EventID']}, "
                   f"Message: {event['Message']}, \n")
      report.write("----------------------------\n\n")
      


print("Incident report summary generated.")



   
