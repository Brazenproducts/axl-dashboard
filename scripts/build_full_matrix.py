import urllib.request
import re
import csv
from pathlib import Path

url = "https://github.io"
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(f"❌ Connection error: {e}")
    exit()

# Complete raw table layout extractor regex loop
pattern = re.compile(r'<tr>\s*<td>([A-Z])</td>\s*<td>\d+</td>\s*<td>([^<]+)</td>\s*<td>([^<]+)</td>\s*<td>([^<]*)</td>\s*<td>([^<]+)</td>')
matches = pattern.findall(html)

if not matches:
    # Alternative boundary block parse loop if white space patterns shift tags
    pattern = re.compile(r'<td>([A-Z])</td>.*?<td>([^<]+)</td>.*?<td>([^<]+)</td>.*?<td>([^<]*)</td>.*?<td>([^<]+)</td>', re.DOTALL)
    matches = pattern.findall(html)

cleaned_data = []
seen = set()

for match in matches:
    group, domain, niche, brand, status = [x.strip() for x in match]
    if "→" in niche or "→" in domain:
        continue
    if domain not in seen and "." in domain and "Domain" not in domain:
        seen.add(domain)
        cleaned_data.append([domain, group, group, niche, brand if brand else "None", status])

# Sort everything perfectly by Group Letter alphabetically (A to X)
cleaned_data.sort(key=lambda x: (x[1], x[0]))

output_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Domain", "Current_Group", "Target_Group", "Niche", "Core_Brand", "Current_Status"])
    writer.writerows(cleaned_data)

print(f"🏆 SUCCESS: Complete network sheet built! Total rows written: {len(cleaned_data)}")
