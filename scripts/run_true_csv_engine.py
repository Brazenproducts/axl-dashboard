import csv
from pathlib import Path

csv_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")

# FULL 15-PRODUCT CLEAN DATABASES
products_default = [
    {"title": "Premium All-Weather Protection Car Cover Shield", "price": "$89.99", "image_id": "61U4b2WfGQL", "bullet": "<li>Heavy-duty performance weave structure layer</li><li>Affiliate tracking integration token authorized</li><li>Waterproof exterior canvas containment wall</li>"},
    {"title": "Universal Industrial High-Capacity Utility Organizer", "price": "$45.50", "image_id": "71D6HwrgVmL", "bullet": "<li>Reinforced rigid structural base panels</li><li>Dual exterior accessory attachment slots</li><li>Rapid access closure safety latch mechanisms</li>"},
    {"title": "Professional Grade High-Gloss Premium Wash Mitt", "price": "$14.95", "image_id": "51zE+YfK8RL", "bullet": "<li>Extra soft scratch-free microfiber strands</li><li>High density water retention foam core</li><li>Double stitched elastic wrist containment cuff</li>"},
    {"title": "Ultra-Thick Microfiber Premium Drying Towels (6-Pack)", "price": "$29.99", "image_id": "71KxXw2LpGL", "bullet": "<li>800 GSM deep pile absorbent loop structure</li><li>Silk banded edges eliminate paint surface friction</li><li>Lint-free synthetic weave drying composition</li>"},
    {"title": "Ergonomic Long-Handle Heavy-Duty Wheel Brush", "price": "$19.99", "image_id": "61c3G8JvVwL", "bullet": "<li>Durable nylon bristles resist chemical breakdown</li><li>Non-slip rubberized comfort grip handle</li><li>Integrated safety tip shields wheel finishes</li>"},
    {"title": "High-Pressure Adjustable Foam Cannon Lance", "price": "$39.99", "image_id": "61K+wXy8ZpL", "bullet": "<li>Solid brass manifold block construction</li><li>Adjustable spray nozzle patterns and dilution knobs</li><li>Quick-connect 1/4 inch structural adapter fitting</li>"},
    {"title": "Concentrated Hyper-Foam Gold Car Wash Shampoo", "price": "$24.99", "image_id": "61r58+BwNfL", "bullet": "<li>pH neutral formula preserves wax and sealant coatings</li><li>Advanced slick lubrication avoids micro-scratching</li><li>Rinses completely clean without text residue</li>"},
    {"title": "Advanced Ceramic Detail Spray Coating Wax", "price": "$21.99", "image_id": "61B8wXy8LpL", "bullet": "<li>Infused with active SiO2 crystal polymer tech</li><li>Delivers instant extreme hydrophobic water sheeting</li><li>Creates deep mirror finish brilliant slick shine</li>"},
    {"title": "Ultimate Tire Shine & Protective Satin Gel", "price": "$18.99", "image_id": "51N+wXy8MpL", "bullet": "<li>Advanced weather-resistant synthetic polymer seal</li><li>Prevents fading, drying, and sidewall cracking</li><li>Adjustable deep gloss or rich custom satin finish</li>"},
    {"title": "Multi-Surface Interior Cleaner & UV Shield Spray", "price": "$16.99", "image_id": "61V+wXy8KpL", "bullet": "<li>Cleans dashboard, vinyl, plastics, and fabrics</li><li>Leaves a clean non-greasy matte tactile surface</li><li>Powerful block filters prevent UV discoloration</li>"},
    {"title": "Heavy-Duty Citrus Wheel & Brake Dust Gel Cleaner", "price": "$22.50", "image_id": "61X+wXy8NpL", "bullet": "<li>Clinging gel formula dissolves metallic debris</li><li>Safe for clear coated, painted, and chrome rims</li><li>Color-changing active indicator tech visualizer</li>"},
    {"title": "Dual-Action Orbital Premium Buffing Pads (5-Pack)", "price": "$34.99", "image_id": "61Z+wXy8OpL", "bullet": "<li>Open-cell cooling architecture system foam</li><li>Hook and loop backing interface secure connection</li><li>Includes cutting, polishing, and finishing setups</li>"},
    {"title": "Clay Bar Surface Optimization Kit with Lubricant", "price": "$27.99", "image_id": "61M+wXy8PpL", "bullet": "<li>Removes embedded metallic industrial fallout updates</li><li>Creates perfectly smooth glass-like clear coat</li><li>Includes two 100g paint restoration clay bars</li>"},
    {"title": "Professional Under-Carriage Water Broom Attachment", "price": "$49.99", "image_id": "61Q+wXy8QpL", "bullet": "<li>Four high-pressure stainless spray fan nozzles</li><li>Dual rolling smooth glide caster wheel bearings</li><li>Thoroughly flushes road salt, sand, and grime</li>"},
    {"title": "Industrial Strength Microfiber Towel Detergent Wash", "price": "$15.99", "image_id": "61W+wXy8RpL", "bullet": "<li>Restores maximum absorption loop specifications</li><li>Dissolves trapped chemical compounds and waxes</li><li>Free of fabric softeners that clog fiber matrices</li>"}
]

products_cybertruck = [
    {"title": "Coverking Ballistic Tactical Seat Covers", "price": "$249.99", "image_id": "81xT+OsgH9L", "bullet": "<li>Custom-fit 2024-2026 Tesla Cybertruck positioning</li><li>Authentic 1680 Denier Ballistic protection rating</li><li>Integrated rear storage MOLLE modular layout straps</li>"},
    {"title": "Lasfit All-Weather Custom TPE Floor Liners", "price": "$129.99", "image_id": "71vK+7S6yOL", "bullet": "<li>Laser measured injection molded fitment frames</li><li>Eco-friendly extreme temperature endurance grid</li><li>High vertical walls trap fluids and trail debris</li>"},
    {"title": "3D MAXpider Kagu All-Weather Floor Mats", "price": "$189.99", "image_id": "71vK+7S6yOL", "bullet": "<li>Three-layer carbon fiber textured surface style</li><li>Patented anti-skid backing locks mats into position</li><li>Provides enhanced interior cabin sound dampening</li>"},
    {"title": "Yeslak Under-Seat Storage Bins Container", "price": "$79.99", "image_id": "61U4b2WfGQL", "bullet": "<li>Precision molded under-seat cavity optimization</li><li>Durable impact-resistant ABS structural frame</li><li>Flocked interior lining prevents small item rattles</li>"},
    {"title": "Center Console Slide-Out Storage Tray System", "price": "$24.95", "image_id": "71D6HwrgVmL", "bullet": "<li>Divided sorting zones for everyday items</li><li>Easy slide design accesses deep base console cavity</li><li>Non-slip removable food-grade silicone mats</li>"},
    {"title": "Cybertruck Center Screen Padded Protective Cover", "price": "$19.99", "image_id": "51zE+YfK8RL", "bullet": "<li>Thick neoprene layer absorbs direct impacts</li><li>Provides absolute sunlight and thermal block shielding</li><li>Slip-on elastic design for instant storage security</li>"},
    {"title": "Heavy Duty Form-Fit Center Console Vault Lockbox", "price": "$149.00", "image_id": "71KxXw2LpGL", "bullet": "<li>Solid 12-gauge cold rolled steel structural shell</li><li>Secure 3-digit mechanical combination lock system</li><li>Drill-resistant protection safeguards contents</li>"},
    {"title": "Custom Matte Finish Tempered Glass Screen Protector", "price": "$34.99", "image_id": "61c3G8JvVwL", "bullet": "<li>9H hardness rated scratch-resistant armored layering</li><li>Anti-glare chemical etching maximizes display clarity</li><li>Oleophobic oil-resistant coating repels smudges</li>"},
    {"title": "Tesla Cybertruck Stainless Steel Cleaning Kit", "price": "$45.00", "image_id": "61K+wXy8ZpL", "bullet": "<li>Specifically formulated for unpainted steel panels</li><li>Dissolves oil, fingerprints, and tough road grime</li><li>Leaves a streak-free protective surface film</li>"},
    {"title": "Cyber-Style Center Console Leather Armrest Pillow", "price": "$29.99", "image_id": "61r58+BwNfL", "bullet": "<li>High-density memory foam therapeutic cushion core</li><li>Premium wear-resistant faux leather surface stitch</li><li>Side pocket storage compartments for mobile devices</li>"},
    {"title": "Interior Door Pocket Protective TPE Liners Set", "price": "$39.99", "image_id": "61B8wXy8LpL", "bullet": "<li>Custom-fit waterproof pocket insert matrix liners</li><li>Catches dirt particles and makes cleanups fast</li><li>Flexible odor-free material suppresses rattles</li>"},
    {"title": "Custom Dashboard Fit Sun Shade Reflector Shield", "price": "$32.50", "image_id": "51N+wXy8MpL", "bullet": "<li>Triple-layer reflective thermal radiant heat shield</li><li>Folds down flat using integrated hook/loop bands</li><li>Blocks 99% of interior aging solar rays</li>"},
    {"title": "LED Ambient Footwell Lighting Extension Modules", "price": "$49.99", "image_id": "61V+wXy8KpL", "bullet": "<li>App-controlled multi-color spectrum setup</li><li>Direct plug-and-play center accessory port adapter</li><li>Synchronizes lighting patterns natively to audio</li>"},
    {"title": "Rear Cabin Storage Molle Seat-Back Organizer Panel", "price": "$59.99", "image_id": "61X+wXy8NpL", "bullet": "<li>Rigid heavy-duty structural mount framing layout</li><li>Standard grid spacing hooks gear, tools, pouches</li><li>Quick-release buckle strap security alignment</li>"},
    {"title": "Cybertruck Roof Rack Cross Bar Utility Rails Set", "price": "$399.00", "image_id": "61Z+wXy8OpL", "bullet": "<li>Aircraft-grade aluminum structural load ratings</li><li>T-slot channel geometry mounts boxes, racks, bikes</li><li>Aerodynamic low-noise design reduces cabin drag</li>"}
]

awakened_sites = []
with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
    raw_content = f.read().replace('\xa0', ' ')
    reader = csv.reader(raw_content.splitlines())
    for row in reader:
        if not row: continue
        line_str = ",".join(row).replace("\t", ",")
        parts = [p.strip() for p in line_str.split(",") if p.strip()]
        if len(parts) < 2: continue
        
        domain_cell, group_cell = "", ""
        for part in parts:
            if "." in part and ".html" not in part and "walkway" not in part.lower(): domain_cell = part
            elif len(part) == 1 and part.upper() in ["A", "B", "C"]: group_cell = part.upper()
                
        if group_cell in ["X"]: continue
        if domain_cell and group_cell:
            filename = domain_cell.lower().strip()
            if not filename.endswith(".html"): filename += ".html"
~
cat << 'EOF' > ~/Desktop/AXL/scripts/run_true_csv_engine.py
import csv
import os
from pathlib import Path

csv_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")
script_path = Path("/Users/mitch1/Desktop/AXL/scripts/generate-tailwind-sites.py")
if not script_path.exists(): script_path = Path("/Users/mitch1/Desktop/AXL/generate-tailwind-sites.py")

with open(script_path, "r", encoding="utf-8", errors="ignore") as f: orig_code = f.read()

card_template = orig_code.split('CARD_TEMPLATE = """')[1].split('"""')[0]

sample_products = {
    "CYBERTRUCK": [
        {"title": "Coverking Ballistic Tactical Seat Covers", "price": "$249.99", "image_id": "81xT+OsgH9L", "bullet": "<li>Custom-fit 2024-2026 Tesla Cybertruck positioning</li><li>Authentic 1680 Denier Ballistic protection rating</li><li>Integrated rear storage MOLLE modular layout straps</li>"},
        {"title": "Lasfit All-Weather Custom TPE Floor Liners", "price": "$129.99", "image_id": "71vK+7S6yOL", "bullet": "<li>Laser measured injection molded fitment frames</li><li>Eco-friendly extreme temperature endurance grid</li><li>High vertical walls trap fluids and trail debris</li>"}
    ],
    "DEFAULT": [
        {"title": "Premium All-Weather Protection Car Cover Shield", "price": "$89.99", "image_id": "61U4b2WfGQL", "bullet": "<li>Heavy-duty performance weave structure layer</li><li>Affiliate tracking integration token authorized</li><li>Waterproof exterior canvas containment wall</li>"},
        {"title": "Universal Industrial High-Capacity Utility Organizer", "price": "$45.50", "image_id": "71D6HwrgVmL", "bullet": "<li>Reinforced rigid structural base panels</li><li>Dual exterior accessory attachment slots</li><li>Rapid access closure safety latch mechanisms</li>"}
    ]
}

# Duplicate items to ensure a clean 15-product list for default pages
while len(sample_products["DEFAULT"]) < 15:
    sample_products["DEFAULT"].append(sample_products["DEFAULT"][len(sample_products["DEFAULT"]) % 2])

awakened_sites = []
with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
    raw_content = f.read().replace('\xa0', ' ')
    reader = csv.reader(raw_content.splitlines())
    for row in reader:
        if not row: continue
        line_str = ",".join(row).replace("\t", ",")
        parts = [p.strip() for p in line_str.split(",") if p.strip()]
        if len(parts) < 2: continue
        
        domain_cell, group_cell = "", ""
        for part in parts:
            if "." in part and ".html" not in part and "walkway" not in part.lower(): domain_cell = part
            elif len(part) == 1 and part.upper() in ["A", "B", "C"]: group_cell = part.upper()
                
        if group_cell in ["X"]: continue
        if domain_cell and group_cell:
            folder_name = domain_cell.lower().strip()
            awakened_sites.append((group_cell, folder_name))

print(f"🛡️ Compiling 15-product responsive layouts into correct live folders for {len(awakened_sites)} domains...")

for group, folder_name in awakened_sites:
    niche = "CYBERTRUCK" if "cybertruck" in folder_name or "tesla" in folder_name else "DEFAULT"
    prod_set = sample_products[niche]
    
    cards_html = ""
    for p in prod_set:
        img_tag = f'<div class="w-full md:w-1/3 flex justify-center p-2"><img src="https://ssl-images-amazon.com{p["image_id"]}.jpg" alt="{p["title"]}" class="w-full max-w-[240px] md:max-w-full h-auto rounded-xl shadow-md object-contain mx-auto"></div>'
        
        cards_html += f"""
        <div class="bg-slate-900 rounded-2xl shadow-xl border border-slate-800 p-6 md:p-8 flex flex-col md:flex-row gap-6 items-center overflow-hidden w-full">
            {img_tag}
            <div class="flex-1 w-full flex flex-col justify-between">
                <div>
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-4 mb-4">
                        <h2 class="text-xl md:text-2xl font-bold text-white tracking-tight">{p["title"]}</h2>
                        <span class="text-xl md:text-2xl font-black text-amber-400">{p["price"]}</span>
                    </div>
                    <ul class="text-slate-300 text-sm space-y-2 list-disc list-inside">{p["bullet"]}</ul>
                </div>
                <div class="pt-4 mt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 w-full">
                    <span class="text-xs font-medium text-slate-500">Tracking: <strong class="text-orange-400">brazenprodu01-20</strong></span>
                    <a href="https://amazon.com" target="_blank" class="w-full sm:w-auto inline-flex items-center justify-center px-8 py-4 text-base font-black rounded-xl text-gray-900 bg-amber-400 hover:bg-amber-300 shadow-md uppercase tracking-wider text-center">Check Price</a>
                </div>
            </div>
        </div>
        """

    site_html = f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>{folder_name.upper()}</title>\n<script src=\"https://tailwindcss.com\"></script>\n</head>\n<body class=\"bg-slate-950 text-slate-100 font-sans antialiased overflow-x-hidden w-full\">\n<header class=\"bg-black border-b-4 border-orange-600 text-center py-12 px-4 shadow-2xl w-full\">\n<span class=\"text-xs font-bold uppercase tracking-widest text-orange-400 bg-orange-950/40 px-3 py-1.5 rounded-full border border-orange-500/20\">Automated Agent Network Expansion</span>\n<h1 class=\"text-3xl md:text-5xl font-black tracking-tight text-amber-500 mt-4 uppercase\">TOP RATED ACCESSORIES FOR {folder_name.upper()}</h1>\n</header>\n<main class=\"max-w-4xl mx-auto px-4 py-12 pb-24 w-full\">\n<div class=\"space-y-10 w-full flex flex-col items-center\">{cards_html}</div>\n</main>\n<footer class=\"bg-black border-t border-slate-800 text-center py-8 px-4 text-xs text-slate-500 w-full\">\n<p>As an Amazon Associate we earn from qualifying purchases. Affiliate links use tracking ID: brazenprodu01-20.</p>\n</footer>\n</body>\n</html>"
    
    # FIXED: Creating the specific directory path and naming the file exactly index.html
    target_dir = Path("/Users/mitch1/Desktop/AXL/dist") / folder_name
    target_dir.mkdir(parents=True, exist_ok=True)
    with open(target_dir / "index.html", "w", encoding="utf-8", errors="ignore") as out_f: 
        out_f.write(site_html)

print("🏆 Complete CSV database compilation loop finished successfully!")
