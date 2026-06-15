import os
from pathlib import Path

# Automated 24-Template Visual Grid Matrix
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{site_title}</title>
    <script src="https://tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased">
    <!-- Premium Header Banner -->
    <header class="bg-black border-b-4 border-orange-600 text-center py-12 px-4 shadow-2xl">
        <span class="text-xs font-bold uppercase tracking-widest text-orange-400 bg-orange-950/40 px-3 py-1.5 rounded-full border border-orange-500/20">Automated Agent Network Expansion</span>
        <h1 class="text-4xl md:text-5xl font-black tracking-tight text-amber-500 mt-4 uppercase">{headline_text}</h1>
        <p class="mt-4 text-base md:text-lg text-slate-400 max-w-2xl mx-auto">Independent Field Testing & Curated Performance Product Matrix</p>
    </header>

    <!-- Main Content Container Grid -->
    <main class="max-w-4xl mx-auto px-4 py-12 pb-24">
        <div class="space-y-10">
            {product_cards}
        </div>
    </main>

    <!-- Enforced Corporate Footer Layer -->
    <footer class="bg-black border-t border-slate-800 text-center py-8 px-4 text-xs text-slate-500">
        <p class="max-w-2xl mx-auto">As an Amazon Associate we earn from qualifying purchases. Affiliate links on this page use tracking ID: brazenprodu01-20.</p>
    </footer>
</body>
</html>
"""

# The Custom Product Component Card Mold Managed by our Design Models
CARD_TEMPLATE = """
        <div class="bg-slate-900 rounded-2xl shadow-xl border border-slate-800 p-6 md:p-8 flex flex-col md:flex-row gap-6 transition-all duration-300 hover:border-orange-500/40">
            <div class="w-full md:w-1/3 bg-slate-950 rounded-xl flex items-center justify-center p-6 border border-slate-800 min-h-[200px]">
                <span class="text-slate-600 font-bold uppercase tracking-wider text-xs">[ High-Res Media Stream ]</span>
            </div>
            
            <div class="flex-1 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between gap-4 border-b border-slate-800 pb-4 mb-4">
                        <div>
                            <span class="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold bg-orange-950 text-orange-400 uppercase tracking-wider mb-2 border border-orange-500/20">Verified Choice</span>
                            <h2 class="text-xl md:text-2xl font-bold text-white tracking-tight">{title}</h2>
                        </div>
                        <div class="text-right">
                            <span class="text-xs text-slate-500 block uppercase font-semibold tracking-wider">Target Price</span>
                            <span class="text-2xl font-black text-amber-400">{price}</span>
                        </div>
                    </div>
                    
                    <div class="text-slate-300 text-sm leading-relaxed mb-6">
                        <ul class="space-y-2">
                            {bullet_items}
                        </ul>
                    </div>
                </div>
                
                <div class="pt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
                    <span class="text-xs font-medium text-slate-500">Tracking Account: <strong class="text-orange-400">brazenprodu01-20</strong></span>
                    <a href="{affiliate_url}" target="_blank" class="w-full sm:w-auto inline-flex items-center justify-center px-8 py-4 border border-transparent text-base font-black rounded-xl text-gray-900 bg-amber-400 hover:bg-amber-300 shadow-md transition duration-150 transform hover:-translate-y-0.5 text-center uppercase tracking-wider">
                        Check Price on Amazon
                    </a>
                </div>
            </div>
        </div>
"""

def build_affiliate_url(url):
    if "amazon.com" in url:
        if "?" in url:
            return url + "&tag=brazenprodu01-20"
        return url + "?tag=brazenprodu01-20"
    return url

# Multi-Agent Configuration Maps holding your active niches
portfolio_expansion_batch = {
    "besttruckbedmats.html": {
        "headline": "Best Heavy Duty Truck Bed Mats 2026",
        "products": [
            {"title": "1. Dee Zee Heavy Duty Rubber Truck Bed Mat", "price": "$124.99", "url": "https://amazon.com", "bullets": "<li><strong>Premium Protection:</strong> High-density rubber compounds deflect tools and massive impact drops natively.</li>"},
            {"title": "2. Husky Liners Heavy Duty Bed Xact Contour", "price": "$159.99", "url": "https://amazon.com", "bullets": "<li><strong>Custom Fit Profiles:</strong> Form-fitted design loops map exact manufacturer tailgates perfectly.</li>"}
        ]
    },
    "bestjeepseats.html": {
        "headline": "Top Premium Custom Jeep Wrangler Seats Ranked",
        "products": [
            {"title": "1. Corbeau Trailcat Diamond Vinyl Reclining Seats", "price": "$899.00 / Pair", "url": "https://amazon.com", "bullets": "<li><strong>Ergonomic Offroad Support:</strong> Strategically bolstered seat design locks drivers in place over severe obstacles.</li>"},
            {"title": "2. Smittybilt Premium Custom Vinyl Front Seating", "price": "$219.99", "url": "https://amazon.com", "bullets": "<li><strong>Weatherproof Materials:</strong> Marine-grade commercial vinyl blocks dust, mud, and intense UV sun damage.</li>"}
        ]
    }
}

output_dir = Path("/Users/mitch1/Desktop/AXL/dist")
output_dir.mkdir(parents=True, exist_ok=True)

print(f"🚀 MULTI-AGENT COMPILER ACTIVE: GENERATING PORTFOLIO FACELIFTS...")
for filename, data in portfolio_expansion_batch.items():
    cards_html = ""
    for prod in data["products"]:
        cards_html += CARD_TEMPLATE.format(
            title=prod["title"],
            price=prod["price"],
            bullet_items=prod["bullets"],
            affiliate_url=build_affiliate_url(prod["url"])
        )
    
    out_path = output_dir / filename
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(site_title=filename, headline_text=data["headline"], product_cards=cards_html))
    print(f"  └─ ✅ Automated Agent Build Success: {out_path.name}")

print(f"\\n🏆 SUCCESS: Multi-agent generation loop completed successfully inside your local dist folder!")
