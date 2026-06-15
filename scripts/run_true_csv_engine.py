import csv
from pathlib import Path

csv_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")
script_path = Path("/Users/mitch1/Desktop/AXL/scripts/generate-tailwind-sites.py")
if not script_path.exists():
    script_path = Path("/Users/mitch1/Desktop/AXL/generate-tailwind-sites.py")

# Read the HTML and Card Layouts from Axl's original file structure
with open(script_path, "r", encoding="utf-8") as f:
    orig_code = f.read()

html_template = orig_code.split('HTML_TEMPLATE = """')[1].split('"""')[0]
card_template = orig_code.split('CARD_TEMPLATE = """')[1].split('"""')[0]

# Sample dynamic content lists to automatically populate items cleanly
sample_products = {
    "CYBERTRUCK": [
        {"title": "Coverking Ballistic Tactical Seat Covers", "price": "$249.99", "bullet": "<li>Custom-fit 2024-2026 Tesla Cybertruck positioning</li><li>Authentic 1680 Denier Ballistic protection rating</li><li>Integrated rear storage MOLLE modular layout straps</li>", "image_id": "81xT+OsgH9L"},
        {"title": "Lasfit All-Weather Custom TPE Floor Liners", "price": "$129.99", "bullet": "<li>Laser measured injection molded fitment frames</li><li>Eco-friendly extreme temperature endurance grid</li><li>High vertical walls trap fluids and trail debris</li>", "image_id": "71vK+7S6yOL"}
    ],
    "DEFAULT": [
        {"title": "Premium All-Weather Protection Matrix Shield", "price": "$89.99", "bullet": "<li>Heavy-duty performance weave structure layer</li><li>Affiliate tracking integration token authorized</li><li>Waterproof exterior canvas containment wall</li>", "image_id": "61U4b2WfGQL"},
        {"title": "Universal Industrial High-Capacity Utility Organizer", "price": "$45.50", "bullet": "<li>Reinforced rigid structural base panels</li><li>Dual exterior accessory attachment slots</li><li>Rapid access closure safety latch mechanisms</li>", "image_id": "71D6HwrgVmL"}
    ]
}

# Scan every row in your LibreOffice spreadsheet
awakened_sites = []
with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        if not row or len(row) < 2: continue
        # Handle tab separation if pasted raw
        parts = [p.strip() for p in row[0].replace("\t", ",").split(",") if p.strip()]
        if len(parts) < 2: continue
        
        group = parts[0].upper()
        domain = parts[1].lower().replace(".com", "") + ".html"
        
        if group in ["A", "B", "C"]:
            awakened_sites.append((group, domain, parts[1].lower()))

print(f"🛡️ Initializing production line for {len(awakened_sites)} verified database targets...")

for group, filename, raw_domain in awakened_sites:
    niche = "CYBERTRUCK" if "cybertruck" in filename or "tesla" in filename else "DEFAULT"
    prod_set = sample_products[niche]
    
    # Handle targeted brand suppression rules natively
    cards_html = ""
    for p in prod_set:
        # STRICT PROTECTION GUARD: Do not print Bartact on non-Jeep/Bronco pages
        title = p["title"]
        if niche != "DEFAULT" and "Bartact" in title: continue
            
        bullet_str = p["bullet"]
        # Inject structural image code directly inside the frame loop
        img_tag = f'<img src="https://ssl-images-amazon.com{p["image_id"]}.jpg" alt="{title}" class="w-full max-w-sm h-auto rounded object-cover mx-auto">'
        
        card_rendered = card_template.format(
            title=title, price=p["price"], bullet_items=bullet_str, affiliate_url="https://amazon.com"
        )
        # Force insert image tag directly inside Axl's media placeholder space
        card_rendered = card_rendered.replace('[ High-Res Media Stream ]', img_tag)
        cards_html += card_rendered

    # Burn page data structure directly onto your storage tracks
    site_html = html_template.format(
        site_title=raw_domain.upper(), headline_text=f"TOP RATED ACCESSORIES FOR {raw_domain.upper()}", product_cards=cards_html
    )
    
    out_path = Path("/Users/mitch1/Desktop/AXL") / filename
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(site_html)

print("🏆 Complete CSV database compilation loop finished successfully!")
