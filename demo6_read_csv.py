import csv

input_file = r"D:\Mine\Company\KPMG Feb 2026\BuildingAutomationSession\Evidence\Top3HotfixeLogs.csv"

with open(input_file,"r") as file:
  
    reader=csv.DictReader(file)

    for row in reader:
      print(row)
      print(row["HotFixID"])
      print(row["Description"])
      print("----------")

