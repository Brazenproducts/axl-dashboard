import csv
from pathlib import Path

csv_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")
script_path = Path("/Users/mitch1/Desktop/AXL/scripts/generate-tailwind-sites.py")
if not script_path.exists(): script_path = Path("/Users/mitch1/Desktop/AXL/generate-tailwind-sites.py")

with open(script_path, "r", encoding="utf-8", errors="ignore") as f: orig_code = f.read()

html_template = orig_code.split('HTML_TEMPLATE = """').split('"""')
card_template = orig_code.split('CARD_TEMPLATE = """').split('"""')

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

awakened_sites = []
with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
    raw_content = f.read().replace('\xa0', ' ')
    reader = csv.reader(raw_content.splitlines())
    for row in reader:
        if not row: continue
        line_str = ",".join(row).replace("\t", ",")
        parts = [p.strip() for p in line_str.split(",") if p.strip()]
        if len(parts) < 2: continue
        
        domain_cell = ""
        group_cell = ""
        for part in parts:
            if "." in part and ".html" not in part and "walkway" not in part.lower():
                domain_cell = part
            elif len(part) == 1 and part.upper() in ["A", "B", "C"]:
                group_cell = part.upper()
                
        # ABSOLUTE SAFETY LATCH: Exclude X sites completely from processing
        if group_cell in ["X"]: 
            continue
            
        if domain_cell and group_cell:
            filename = domain_cell.lower().strip() + ".html"
            awakened_sites.append((group_cell, filename, domain_cell.lower().strip()))

print(f"🛡️ Compiling verified database targets for {len(awakened_sites)} unique domains...")

for group, filename, raw_domain in awakened_sites:
    niche = "CYBERTRUCK" if "cybertruck" in filename or "tesla" in filename else "DEFAULT"
    cards_html = ""
    for p in sample_products[niche]:
        img_tag = f'<img src="https://ssl-images-amazon.com{p["image_id"]}.jpg" alt="{p["title"]}" class="w-full max-w-sm h-auto rounded object-cover mx-auto">'
        card_rendered = card_template.format(title=p["title"], price=p["price"], bullet_items=p["bullet"], affiliate_url="https://amazon.com")
        card_rendered = card_rendered.replace('[ High-Res Media Stream ]', img_tag)
        cards_html += card_rendered

    site_html = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"UTF-8\">\n<title>{raw_domain.upper()}</title>\n<script src=\"https://tailwindcss.com\"></script>\n</head>\n<body class=\"bg-slate-950 text-slate-100 font-sans antialiased\">\n<header class=\"bg-black border-b-4 border-orange-600 text-center py-12 px-4 shadow-2xl\">\n<span class=\"text-xs font-bold uppercase tracking-widest text-orange-400 bg-orange-950/40 px-3 py-1.5 rounded-full border border-orange-500/20\">Automated Agent Network Expansion</span>\n<h1 class=\"text-4xl md:text-5xl font-black tracking-tight text-amber-500 mt-4 uppercase\">TOP RATED ACCESSORIES FOR {raw_domain.upper()}</h1>\n</header>\n<main class=\"max-w-4xl mx-auto px-4 py-12 pb-24\">\n<div class=\"space-y-10\">{cards_html}</div>\n</main>\n<footer class=\"bg-black border-t border-slate-800 text-center py-8 px-4 text-xs text-slate-500\">\n<p>As an Amazon Associate we earn from qualifying purchases. Affiliate links use tracking ID: brazenprodu01-20.</p>\n</footer>\n</body>\n</html>"
    with open(Path("/Users/mitch1/Desktop/AXL") / filename, "w", encoding="utf-8", errors="ignore") as out_f: out_f.write(site_html)

print("🏆 Complete CSV database compilation loop finished successfully!")
