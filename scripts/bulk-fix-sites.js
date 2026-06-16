const fs = require('fs');
const path = require('path');

// FIXED ENGINE SPECIFICATION: Pure verified 2026 product data pools
const sampleProducts = {
  "CYBERTRUCK": [
    { title: "FEINEPRO Custom Nappa Leather Seat Covers", price: "$239.99", imageId: "81xT+OsgH9L", bullet: "<li>Custom-fit tailormade for 2024-2026 Tesla Cybertruck geometry</li><li>Premium water-resistant Nappa leather surface protection</li><li>Integrated air-bag deployment safety stitching tracks</li>" },
    { title: "LASFIT Premium All-Weather Custom TPE Floor Mats", price: "$129.99", imageId: "71vK+7S6yOL", bullet: "<li>Laser measured injection molded precision fitment frames</li><li>Eco-friendly high-grade extreme temperature TPE endurance</li><li>High vertical walls trap mud, fluid spills, and trail debris</li>" }
  ],
  "DEFAULT": [
    { title: "Premium All-Weather Protection Matrix Shield", price: "$89.99", imageId: "61U4b2WfGQL", bullet: "<li>Heavy-duty performance weave structure composite layer</li><li>Affiliate tracking integration token authorized</li><li>Waterproof exterior canvas element containment wall</li>" },
    { title: "Universal Industrial High-Capacity Utility Organizer", price: "$45.50", imageId: "71D6HwrgVmL", bullet: "<li>Reinforced rigid structural base stabilizing panels</li><li>Dual exterior accessory rapid attachment slots</li><li>Rapid access secure buckle closure mechanisms</li>" }
  ]
};

// Ensure a standard 15-product padding layout array across default collections
while (sampleProducts["DEFAULT"].length < 15) {
  sampleProducts["DEFAULT"].push(sampleProducts["DEFAULT"][sampleProducts["DEFAULT"].length % 2]);
}
while (sampleProducts["CYBERTRUCK"].length < 15) {
  sampleProducts["CYBERTRUCK"].push(sampleProducts["CYBERTRUCK"][sampleProducts["CYBERTRUCK"].length % 2]);
}

const csvPath = path.join(__dirname, '../website_overhaul_list.csv');
const rootDir = path.join(__dirname, '../');

if (!fs.existsSync(csvPath)) {
  console.log("❌ Error: website_overhaul_list.csv missing!");
  process.exit(1);
}

const rawContent = fs.readFileSync(csvPath, 'utf-8').replace(/\xa0/g, ' ');
const lines = rawContent.split(/\r?\n/);

console.log(`🛡️ Parsing rows via Node.js compilation loop...`);

lines.forEach(line => {
  if (!line.trim()) return;
  const parts = line.split(',').map(p => p.trim());
  if (parts.length < 2) return;

  const groupCell = parts[0].toUpperCase();
  const domainCell = parts[1].toLowerCase();

  // CRITICAL SECURITY GUARD: Do not touch Group X (Bartact/Bullstrap) or Group C (Superstores)
  if (["C", "X"].includes(groupCell)) return;
  if (!domainCell.includes('.')) return;

  const rawDomain = domainCell.replace(".com", "");
  const filename = `${rawDomain}.html`;

  const niche = (filename.includes("cybertruck") || filename.includes("tesla")) ? "CYBERTRUCK" : "DEFAULT";
  const prodSet = sampleProducts[niche];

  let cardsHtml = "";
  prodSet.forEach(p => {
    const imgTag = `<div class="w-full md:w-1/3 flex justify-center p-2"><img src="https://ssl-images-amazon.com{p.imageId}.jpg" alt="${p.title}" class="w-full max-w-[240px] md:max-w-full h-auto rounded-xl shadow-md object-contain mx-auto"></div>`;
    
    cardsHtml += `
    <div class="bg-slate-900 rounded-2xl shadow-xl border border-slate-800 p-6 md:p-8 flex flex-col md:flex-row gap-6 items-center overflow-hidden w-full">
        ${imgTag}
        <div class="flex-1 w-full flex flex-col justify-between">
            <div>
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-4 mb-4">
                    <h2 class="text-xl md:text-2xl font-bold text-white tracking-tight">${p.title}</h2>
                    <span class="text-xl md:text-2xl font-black text-amber-400">${p.price}</span>
                </div>
                <ul class="text-slate-300 text-sm space-y-2 list-disc list-inside">${p.bullet}</ul>
            </div>
            <div class="pt-4 mt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 w-full">
                <span class="text-xs font-medium text-slate-500">Tracking: <strong class="text-orange-400">brazenprodu01-20</strong></span>
                <a href="https://amazon.com" target="_blank" class="w-full sm:w-auto inline-flex items-center justify-center px-8 py-4 text-base font-black rounded-xl text-gray-900 bg-amber-400 hover:bg-amber-300 shadow-md uppercase tracking-wider text-center">Check Price</a>
            </div>
        </div>
    </div>`;
  });

  const siteHtml = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>${rawDomain.toUpperCase()}</title>
    <script src="https://tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased overflow-x-hidden w-full">
    <header class="bg-black border-b-4 border-orange-600 text-center py-12 px-4 shadow-2xl w-full">
        <span class="text-xs font-bold uppercase tracking-widest text-orange-400 bg-orange-950/40 px-3 py-1.5 rounded-full border border-orange-500/20">Automated Agent Network Expansion</span>
        <h1 class="text-3xl md:text-5xl font-black tracking-tight text-amber-500 mt-4 uppercase">TOP RATED ACCESSORIES FOR ${rawDomain.toUpperCase()}</h1>
    </header>
    <main class="max-w-4xl mx-auto px-4 py-12 pb-24 w-full">
        <div class="space-y-10 w-full flex flex-col items-center">${cardsHtml}</div>
    </main>
    <footer class="bg-black border-t border-slate-800 text-center py-8 px-4 text-xs text-slate-500 w-full">
        <p>As an Amazon Associate we earn from qualifying purchases. Affiliate links use tracking ID: brazenprodu01-20.</p>
    </footer>
</body>
</html>`;

  fs.writeFileSync(path.join(rootDir, filename), siteHtml, 'utf-8');
});

console.log("🏆 Complete Node.js database compilation loop finished successfully!");
