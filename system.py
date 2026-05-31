def tourist_system(action, day_type, report_type):
    if action == "RecordTouristtry":
        if day_type == "Weekend":
            print("Record High Traffic")
        else:
            print("Record Normal Traffic")
    elif action == "GenerateReport":
        if report_type == "Monthly":
            print("Generate Monthly Report")
        else:
            print("Generate Weekly Report")

# Example Usage
tourist_system("RecordTouristEntry", "Weekend", "")
tourist_system("GenerateReport", "", "Monthly")
