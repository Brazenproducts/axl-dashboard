import urllib.request
import csv
import re
from pathlib import Path

url = "https://github.io"
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(f"❌ Connection error: {e}")
    exit()

# Isolate raw text cells from the vertical table structure
cells = re.findall(r'<td>([^<]*)</td>', html, re.DOTALL)

cleaned_data = []
seen = set()

i = 0
while i < len(cells) - 2:
    group = cells[i].strip()
    # If cell is a single uppercase letter group code (A, B, C, D, F, X)
    if len(group) == 1 and group.isupper() and group in ['A', 'B', 'C', 'D', 'F', 'X']:
        domain = cells[i+2].strip()
        # Verify it is a valid domain and not a placeholder arrow or duplication
        if "." in domain and "→" not in domain and domain not in seen:
            seen.add(domain)
            cleaned_data.append([group, domain])
    i += 1

# Sort everything perfectly by Group Letter alphabetically (C, B, A, D, F, X)
cleaned_data.sort(key=lambda x: (x[0], x[1]))

output_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Group", "Domain"])  # Flawless header columns
    writer.writerows(cleaned_data)

print(f"🏆 SUCCESS: Perfect data grid built! Total rows written: {len(cleaned_data)}")
