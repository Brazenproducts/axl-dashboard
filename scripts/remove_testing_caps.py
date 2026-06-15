from pathlib import Path
import re

script_path = Path("/Users/mitch1/Desktop/AXL/scripts/generate-tailwind-sites.py")
if not script_path.exists():
    script_path = Path("/Users/mitch1/Desktop/AXL/generate-tailwind-sites.py")

with open(script_path, "r", encoding="utf-8") as f:
    code = f.read()

# Locate standard counter loop hard-breaks (like 'if count >= 2: break' or matching arrays)
fixed_code = re.sub(r'if\s+.*count\s*(?:>=|==)\s*2\s*:\s*break', '# Testing break disabled globally', code)
fixed_code = re.sub(r'limit\s*=\s*2', 'limit = 1000', fixed_code)

# Safety fallback: Ensure any row limit arrays are forced wide open
if fixed_code == code:
    fixed_code = code.replace("for index, row in df.head(2).iterrows():", "for index, row in df.iterrows():")

with open(script_path, "w", encoding="utf-8") as f:
    f.write(fixed_code)

print("🎯 Testing caps removed! The loop is fully unlocked for bulk assembly line generation.")
