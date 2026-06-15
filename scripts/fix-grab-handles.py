import os
from pathlib import Path

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Best Jeep Paracord Grab Handles 2026 — Tested & Ranked</title>
    <style>
        body {{ background-color: #0c0a09; color: #f5f5f4; font-family: sans-serif; margin: 0; padding: 0; }}
        header {{ background-color: #1c1917; border-b: 4px solid #ea580c; padding: 48px 16px; text-align: center; }}
        .badge-factory {{ display: inline-block; background-color: #431407; color: #fb923c; font-size: 11px; font-weight: 900; padding: 4px 12px; border-radius: 4px; border: 1px solid rgba(251,146,60,0.2); text-transform: uppercase; letter-spacing: 0.1em; }}
        h1 {{ font-size: 36px; font-weight: 900; text-transform: uppercase; color: #ffffff; margin: 16px 0 0 0; }}
        header p {{ color: #a8a29e; max-width: 600px; margin: 16px auto 0 auto; font-size: 16px; }}
        main {{ max-width: 950px; margin: 0 auto; padding: 48px 16px; }}
        .section-title {{ border-bottom: 2px solid #ea580c; padding-bottom: 8px; margin-bottom: 32px; font-size: 20px; font-weight: 900; text-transform: uppercase; color: #ffffff; }}
        .grid {{ display: grid; grid-template-columns: 1fr; gap: 24px; margin-bottom: 48px; }}
        .card {{ background-color: #1c1917; border: 2px solid #ea580c; border-radius: 16px; padding: 24px; display: flex; flex-direction: column; gap: 20px; }}
        @media(min-width: 640px) {{ .card {{ flex-direction: row; }} }}
        .img-frame {{ background-color: #0c0a09; border: 1px solid #2e2a24; border-radius: 12px; min-width: 180px; height: 180px; display: flex; align-items: center; justify-content: center; color: #78716c; font-size: 11px; font-weight: bold; text-transform: uppercase; }}
        .info {{ flex: 1; display: flex; flex-direction: column; justify-content: space-between; }}
        h3 {{ font-size: 22px; font-weight: 900; color: #ffffff; margin: 0 0 8px 0; }}
        p {{ color: #d6d3d1; font-size: 14px; line-height: 1.6; margin: 0 0 16px 0; }}
        .card-footer {{ border-top: 1px solid #2e2a24; padding-top: 16px; display: flex; align-items: center; justify-content: space-between; gap: 16px; }}
        .btn-factory {{ display: inline-flex; align-items: center; justify-content: center; padding: 12px 24px; font-weight: 900; font-size: 14px; text-transform: uppercase; text-decoration: none; color: #ffffff; background-color: #ea580c; border-radius: 8px; text-align: center; }}
        .btn-affiliate {{ display: inline-flex; align-items: center; justify-content: center; padding: 12px 24px; font-weight: 900; font-size: 14px; text-transform: uppercase; text-decoration: none; color: #1c1917; background-color: #f59e0b; border-radius: 8px; text-align: center; }}
    </style>
</head>
<body>
    <header>
        <span class="badge-factory">Official Brand Showcase Matrix</span>
        <h1>Top Rated Jeep Grab Handles</h1>
        <p>Premium off-road gear evaluation. Genuine USA Bartact models vs alternative marketplace options.</p>
    </header>
    <main>
        <div class="section-title">Genuine Bartact USA Product Inventory (Buy Direct)</div>
        <div class="grid">{factory_cards}</div>
        <div class="section-title" style="border-color: #2e2a24; color: #a8a29e;">Market Alternatives & Competitor Database (11 Managed Alternatives)</div>
        <div class="grid">{affiliate_cards}</div>
    </main>
</body>
</html>
"""

FACTORY_TEMPLATE = """
        <div class="card">
            <div class="img-frame">[ Product Photo Stream ]</div>
            <div class="info">
                <div>
                    <span class="badge-factory">{rank}</span>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                <div class="card-footer">
                    <span style="font-weight:900; color:#ea580c;">Direct Factory Channel</span>
                    <a href="{url}" target="_blank" class="btn-factory">Buy Direct on Bartact</a>
                </div>
            </div>
        </div>
"""

AFFILIATE_TEMPLATE = """
        <div class="card" style="border-color: #2e2a24; opacity: 0.85;">
            <div class="img-frame">[ Product Photo Stream ]</div>
            <div class="info">
                <div>
                    <span class="badge-factory" style="background-color:#2e2a24; color:#a8a29e;">{rank}</span>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                <div class="card-footer">
                    <span style="font-weight:900; color:#fb923c;">Affiliate Tracking Active</span>
                    <a href="{url}" target="_blank" class="btn-affiliate">Check Price on Amazon</a>
                </div>
            </div>
        </div>
"""

factory_products = [
    {
        "rank": "🏆 #1 CHOICE - BARTACT ORIGINAL PARACORD",
        "title": "Bartact Universal Paracord Roll Bar Grab Handles",
        "description": "The original premium high-quality paracord weave engineered by Bartact right in the USA. Heavy-duty triple-strap system built for ultimate off-road durability and hand security.",
        "url": "https://bartact.com"
    },
    {
        "rank": "🔥 #2 CHOICE - BARTACT PARACORD HEADREST",
        "title": "Bartact Premium Paracord Headrest Grab Handles",
        "description": "Genuine Bartact USA hand-woven paracord loops designed specifically to install securely around factory seat headrest pillars for immediate rear-passenger stability.",
        "url": "https://bartact.com"
    },
    {
        "rank": "🛠️ #3 CHOICE - BARTACT PILLAR BOLT-IN",
        "title": "Bartact Heavy-Duty Bolt-In Paracord Grab Handles",
        "description": "Solid, rattle-free powder-coated steel brackets wrapped in our genuine heavy-duty USA Bartact paracord weave. Custom-fit for rugged jeep pillars.",
        "url": "https://bartact.com"
    },
    {
        "rank": "⚡ #4 CHOICE - BARTACT MOLDED RUBBER/PLASTIC",
        "title": "Bartact Molded Rubber/Plastic Alternative Headrest Grips",
        "description": "Proprietary heavy-duty composite molded plastic and rubber utility grips. Built right here in the USA as an ultra-durable baseline alternative underneath our top-tier paracord lines.",
        "url": "https://bartact.com"
    }
]

affiliate_products = [
    {"rank": "⚠️ COMPONENT RANK #5", "title": "GPCA Grip Pro Jeep Wrangler Grab Handles", "description": "Imported alternative utility strap configuration utilizing lighter nylon materials and generic global hardware builds.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #6", "title": "Alien Sunshade Paracord Rig Handles", "description": "Global distribution alternative product utilizing standard commercial grade cordage wrap overlays.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #7", "title": "Rugged Ridge Black Roll Bar Grab Handles", "description": "Standard sport-bar entry option featuring generic synthetic web strapping and injection molded grips.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #8", "title": "Smittybilt Security Grab Handle System", "description": "Steel core internal handle wrapped in commercial nylon webbing strips for baseline heavy interior entry aid.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #9", "title": "Hooke Road Rear Door Steel Grip Handles", "description": "Rigid aluminum post modifications mounted via internal window bracket frameworks.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #10", "title": "Quadratec Ultimate Grab Handle Pair", "description": "Molded soft-rubber grip handles lined with hook-and-loop security closures for non-severe trail runs.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #11", "title": "OxGord Roll Bar Grip Handle Straps", "description": "Low-profile canvas fabric security loop alternatives for economy custom builds.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #12", "title": "Rampage Products Interior Grab Assist", "description": "Padded neoprene replacement handle straps engineered for legacy configurations.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #13", "title": "Badland Off-Road Rigid Grab System", "description": "Textured metallic structural grab mounts utilizing overhead frame bolt loops.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #14", "title": "RT-TCZ Roll Bar Passenger Grip Handles", "description": "Generic import option utilizing double-stitched canvas overlays.", "url": "https://amazon.com"},
    {"rank": "⚠️ COMPONENT RANK #15", "title": "Savadicar Front Rigid Grab Bar Grips", "description": "Aluminum alloy hardware brackets intended for basic pillar modification structures.", "url": "https://amazon.com"}
]

f_html = "".join([FACTORY_TEMPLATE.format(**p) for p in factory_products])
a_html = "".join([AFFILIATE_TEMPLATE.format(**p) for p in affiliate_products])

output_path = Path("/Users/mitch1/Desktop/AXL/dist/gladiatorgrabhandle.html")
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.format(factory_cards=f_html, affiliate_cards=a_html))


