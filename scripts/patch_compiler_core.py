from pathlib import Path
import re

script_path = Path("/Users/mitch1/Desktop/AXL/scripts/generate-tailwind-sites.py")
if not script_path.exists():
    script_path = Path("/Users/mitch1/Desktop/AXL/generate-tailwind-sites.py")

with open(script_path, "r", encoding="utf-8") as f:
    code = f.read()

# Force the core loop to inject physical img tags and brand logic natively
html_template_patch = """
        # Build Item Card Component Natively
        item_html = f'''
        <div class="bg-white rounded-lg shadow-md p-6 mb-6">
            <div class="mb-4 flex justify-center">
                <img src="https://ssl-images-amazon.com{item.get('image_id', '')}.jpg" alt="{item.get('title', '')}" class="w-full max-w-sm h-auto rounded object-cover">
            </div>
            <h3 class="text-xl font-bold mb-2">{item.get('title', '')}</h3>
            <p class="text-gray-600 mb-4">{item.get('description', '')}</p>
            <a href="{item.get('link', '')}?tag=brazenprodu01-20" class="inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">View on Amazon</a>
        </div>
        '''
"""

# Hard rewrite the layout assembler rule block
if "item_html" not in code:
    code = re.sub(r'# Write layout content.*?\n\s*\n', html_template_patch, code, flags=re.DOTALL)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(code)

print("🎯 Compiler engine code layout fixed with hardcoded image/brand anchors!")
