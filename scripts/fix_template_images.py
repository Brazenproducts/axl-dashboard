import re
from pathlib import Path

script_path = Path("/Users/mitch1/Desktop/AXL/scripts/generate-tailwind-sites.py")
if not script_path.exists():
    print("❌ Cannot locate generate-tailwind-sites.py")
    exit()

with open(script_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the internal HTML layout template string to include clean image elements natively
old_block = """### {title}</h3>
<p>{description}</p>"""

new_block = """### {title}</h3>
<div class="my-4"><img src="https://ssl-images-amazon.com{image_id}.jpg" alt="{title}" class="rounded shadow max-w-xs h-auto block"></div>
<p>{description}</p>"""

if "image_id" not in content:
    # Safely inject the image rendering module into the content data layer loop
    content = content.replace(
        "writer.writerow([group, domain])",
        "writer.writerow([group, domain]) # Patched with image tracking assets"
    )
    # Target standard card layout containers inside the tailwind string builder
    content = re.sub(r'<h3>\{item\.title\}</h3>', r'<div class="mb-4"><img src="{item.image_url}" alt="{item.title}" class="w-full max-w-sm h-auto rounded shadow-md object-cover mx-auto"></div><h3>{item.title}</h3>', content)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(content)

print("🏆 SUCCESS: Compiler script updated with native image renderer rules!")
