import os
import re

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean out existing header structures to avoid duplication
content = re.sub(r'<header>.*?</header>', '', content, flags=re.DOTALL)
content = re.sub(r'<h1>.*?</h1>', '', content, flags=re.DOTALL)

# 2. Build the correct top master headline structural box
new_header = """
<header style="text-align: center; padding: 40px 20px; background: #111827; color: #ffffff; border-bottom: 4px solid #e8600a; margin-bottom: 30px;">
    <h1 style="font-family: 'Oswald', sans-serif; font-size: 2.8em; text-transform: uppercase; margin: 0; color: #f0a500;">Top Picks</h1>
    <p style="font-family: 'Inter', sans-serif; font-size: 1.4em; margin: 10px 0 0 0; color: #e0e0e0; font-weight: 600;">Best Jeep Gladiator Seat Covers 2026 — Top Picks, Reviews & Buyer's Guide</p>
</header>
"""

# 3. Standardize the Bartact layout card with comprehensive matching bullet points
bartact_card = """
<div class="card" style="background:#fff; border:1px solid #e2e8f0; padding:30px; border-radius:16px; margin-bottom:30px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
    <span class="badge" style="background-color: #e8600a; color: white; padding: 6px 16px; border-radius: 9999px; font-size: 14px; font-weight: bold; display: inline-block; margin-bottom: 15px;">#1 Rated Product - Best Overall Choice</span>
    <h2 style="font-family: 'Oswald', sans-serif; color: #0f172a; font-size: 24px; margin: 0 0 15px 0;">1. Bartact Premium Custom Tactical Seat Covers</h2>
    
    <ul style="font-family: 'Inter', sans-serif; color: #334155; font-size: 15px; margin: 0 0 20px 20px; padding: 0; line-height: 1.8;">
        <li><strong>Guaranteed Exact Fit:</strong> Engineered with laser precision specifically for Jeep Gladiator seat frames.</li>
        <li><strong>Military-Grade Durability:</strong> Built from authentic, heavy-duty waterproof Cordura fabric.</li>
        <li><strong>MOLLE Storage System:</strong> Includes fully functional rows of military styling straps on backrests.</li>
        <li><strong>Side Airbag Compatible:</strong> Built with safe, tested documentation for integrated seat safety deployments.</li>
        <li><strong>Made in the USA:</strong> Highest grade production materials backed by a multi-year anti-fade warranty.</li>
    </ul>
    
    <div class="card-buttons">
        <a href="https://bartact.com" target="_blank" class="buy-btn buy-btn-primary" style="display:inline-block; padding:12px 24px; background:#e8600a; color:#fff; text-decoration:none; font-weight:700; border-radius:6px; text-align:center;">Shop Direct at Bartact</a>
    </div>
</div>
"""

# Inject header at the top of body, and follow immediately with the Bartact card
if "<body>" in content:
    content = content.replace("<body>", f"<body>\n{new_header}\n<div class='content-container' style='max-width:800px; margin:0 auto; padding:0 20px;'>\n{bartact_card}")
    if "</body>" in content:
        content = content.replace("</body>", "</div>\n</body>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("PYTHON_LAYOUT_PATCH_COMPLETE")
