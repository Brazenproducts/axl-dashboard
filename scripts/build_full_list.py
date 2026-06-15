import os
import csv
from pathlib import Path

master_file = Path("/Users/mitch1/Desktop/AXL/AXL-MASTER.md")
output_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")

if not master_file.exists():
    print("❌ Error: AXL-MASTER.md not found on your desktop.")
    exit()

with open(master_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_data = []
current_group = "A"

# Core parsing loop reading your inventory sections natively
for line in lines:
    if "— A · Pure Affiliate" in line: current_group = "A"
    elif "— B · Branded" in line: current_group = "B"
    elif "— C · Built/Brand" in line: current_group = "C"
    elif "— D · Parked" in line: current_group = "D"
    elif "— F · Forward" in line: current_group = "F"
    elif "— X · Protected" in line: current_group = "X"
    
    # Isolate domain format strings inside your log charts
    if line.strip().startswith(current_group) and "." in line:
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) >= 3:
            domain = parts[2]
            niche = parts[3] if len(parts) > 3 else "General"
            brand = parts[4] if len(parts) > 4 else "None"
            cleaned_data.append([domain, current_group, current_group, niche, brand, "✅ Active"])

# Sort everything perfectly by Group Letter alphabetically (A to X)
cleaned_data.sort(key=lambda x: (x[1], x[0]))

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Domain", "Current_Group", "Target_Group", "Niche", "Core_Brand", "Current_Status"])
    writer.writerows(cleaned_data)

print(f"🏆 SUCCESS: Full inventory compiled from local master log! Total unique records: {len(cleaned_data)}")
