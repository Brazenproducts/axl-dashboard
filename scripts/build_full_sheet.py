import urllib.request
import csv
import re
from pathlib import Path

url = "https://github.io"
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(f"❌ Network block: {e}")
    exit()

# Extract every piece of text inside <td> tags sequentially
cells = re.findall(r'<td>([^<]*)</td>', html, re.DOTALL)

cleaned_data = []
seen = set()

# Axl's vertical column count layout rule: Type, #, Domain, Niche, Brand, Status...
i = 0
while i < len(cells) - 2:
    group = cells[i].strip()
    # Check if this cell is a single letter group code (A, B, C, D, F, X)
    if len(group) == 1 and group.isupper() and group in ['A', 'B', 'C', 'D', 'F', 'X']:
        # Ensure we have enough remaining cells to pull the domain safely
        if i + 2 < len(cells):
            domain = cells[i+2].strip()
            # Verify it is a true web domain name string
            if "." in domain and "→" not in domain and domain not in seen:
                seen.add(domain)
                cleaned_data.append([domain, group, group])
    i += 1

# Sort everything perfectly by Group Letter alphabetically (A to X)
cleaned_data.sort(key=lambda x: (x[1], x[0]))

output_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Domain", "Current_Group", "Target_Group"])
    writer.writerows(cleaned_data)

print(f"🏆 SUCCESS: Complete network sheet built! Total rows written: {len(cleaned_data)}")
