import re
from pathlib import Path

script_path = Path("/Users/mitch1/Desktop/AXL/scripts/generate-tailwind-sites.py")

with open(script_path, "r", encoding="utf-8") as f:
    code = f.read()

# Force the layout matrix loop to generate direct HTML image tags for every item row
old_pattern = r'<h3>\{item\.title\}</h3>'
new_pattern = r'<div class="mb-4"><img src="https://ssl-images-amazon.com{item.image_id}.jpg" alt="{item.title}" class="w-full max-w-sm h-auto rounded shadow mx-auto"></div><h3>{item.title}</h3>'

if 'image_id' in code and 'mb-4' not in code:
    code = re.sub(old_pattern, new_pattern, code)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(code)

print("🎯 Global image injection rules integrated into core template script!")
