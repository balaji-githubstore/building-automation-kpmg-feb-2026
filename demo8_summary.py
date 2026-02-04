fruits = ["apple", "banana", "cherry","mango"]

output_file = r"D:\Mine\Company\KPMG Feb 2026\BuildingAutomationSession\Evidence\fruits_summary.log"

with open(output_file, "w") as report:
    report.write("Fruits List Summary\n")
    report.write("===================\n\n")

    report.write(f"Total Fruits Count:{len(fruits)}\n")

    for fruit in fruits:
        report.write(fruit+"\n")