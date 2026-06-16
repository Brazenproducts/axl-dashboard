import csv
from pathlib import Path

csv_path = Path("/Users/mitch1/Desktop/AXL/website_overhaul_list.csv")
# TARGETING ROOT LEVEL: Forcing the script to write directly to the active root directory
root_dir = Path("/Users/mitch1/Desktop/AXL")

products_cybertruck = [
    {"title": "Coverking Ballistic Tactical Seat Covers", "price": "$249.99", "image_id": "81xT+OsgH9L", "bullet": "<li>Custom-fit 2024-2026 Tesla Cybertruck positioning</li><li>Authentic 1680 Denier Ballistic protection rating</li><li>Integrated rear storage MOLLE modular layout straps</li>"},
    {"title": "Lasfit All-Weather Custom TPE Floor Liners", "price": "$129.99", "image_id": "71vK+7S6yOL", "bullet": "<li>Laser measured injection molded fitment frames</li><li>Eco-friendly extreme temperature endurance grid</li><li>High vertical walls trap fluids and trail debris</li>"}
]

products_default = [
    {"title": "Premium All-Weather Protection Car Cover Shield", "price": "$89.99", "image_id": "61U4b2WfGQL", "bullet": "<li>Heavy-duty performance weave structure layer</li><li>Affiliate tracking integration token authorized</li><li>Waterproof exterior canvas containment wall</li>"},
    {"title": "Universal Industrial High-Capacity Utility Organizer", "price": "$45.50", "image_id": "71D6HwrgVmL", "bullet": "<li>Reinforced rigid structural base panels</li><li>Dual exterior accessory attachment slots</li><li>Rapid access closure safety latch mechanisms</li>"}
]

while len(products_default) < 15:
    products_default.append(products_default[len(products_default) % 2])

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
                
        # STRICT PROTECTION GUARD: Completely exclude Groups C and X to isolate operations
        if group_cell in ["C", "X"]: continue
        if domain_cell and group_cell:
            raw_domain = domain_cell.lower().strip().replace(".com", "")
            filename = f"{raw_domain}.html"
            awakened_sites.append((group_cell, filename, raw_domain))

print(f"🛡️ Compiling pristine layouts directly to root for {len(awakened_sites)} targets...")

for group, filename, raw_domain in awakened_sites:
    niche = "CYBERTRUCK" if "cybertruck" in filename or "tesla" in filename else "DEFAULT"
    prod_set = products_cybertruck if niche == "CYBERTRUCK" else products_default
    
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

    site_html = f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=5.0\">\n<title>{raw_domain.upper()}</title>\n<script src=\"https://tailwindcss.com\"></script>\n</head>\n<body class=\"bg-slate-950 text-slate-100 font-sans antialiased overflow-x-hidden w-full\">\n<header class=\"bg-black border-b-4 border-orange-600 text-center py-12 px-4 shadow-2xl w-full\">\n<span class=\"text-xs font-bold uppercase tracking-widest text-orange-400 bg-orange-950/40 px-3 py-1.5 rounded-full border border-orange-500/20\">Automated Agent Network Expansion</span>\n<h1 class=\"text-3xl md:text-5xl font-black tracking-tight text-amber-500 mt-4 uppercase\">TOP RATED ACCESSORIES FOR {raw_domain.upper()}</h1>\n</header>\n<main class=\"max-w-4xl mx-auto px-4 py-12 pb-24 w-full\">\n<div class=\"space-y-10 w-full flex flex-col items-center\">{cards_html}</div>\n</main>\n<footer class=\"bg-black border-t border-slate-800 text-center py-8 px-4 text-xs text-slate-500 w-full\">\n<p>As an Amazon Associate we earn from qualifying purchases. Affiliate links use tracking ID: brazenprodu01-20.</p>\n</footer>\n</body>\n</html>"
    
    with open(root_dir / filename, "w", encoding="utf-8", errors="ignore") as out_f:
        out_f.write(site_html)

print("🏆 Complete CSV database compilation loop finished successfully!")
