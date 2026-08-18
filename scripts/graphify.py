import os
import sys
import json
import re

# Fix Windows console UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else r'D:\My Resume\scripts'
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, 'data')
EXP_DIR = os.path.join(BASE_DIR, 'experience')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("🔍 Building Interactive Career Knowledge Graph (Graphify)...")

with open(os.path.join(DATA_DIR, 'profile.json'), 'r', encoding='utf-8') as f:
    profile = json.load(f)

nodes = []
links = []
node_ids = set()

def add_node(node_id, label, group, radius, color, desc="", meta=None):
    if node_id not in node_ids:
        node_ids.add(node_id)
        nodes.append({
            "id": node_id,
            "label": label,
            "group": group,
            "radius": radius,
            "color": color,
            "desc": desc,
            "meta": meta or {}
        })

def add_link(source, target, value=1, type_name="connected"):
    if source in node_ids and target in node_ids:
        links.append({
            "source": source,
            "target": target,
            "value": value,
            "type": type_name
        })
    else:
        missing = []
        if source not in node_ids: missing.append(f"source '{source}'")
        if target not in node_ids: missing.append(f"target '{target}'")
        # Debugging aid
        # print(f"⚠️ Link skipped: missing {', '.join(missing)}")

# 1. Root Candidate Node
root_id = "root-hendri"
add_node(root_id, profile.get("name", "MUHAMAD HENDRI FEBRIANSYAH"), "root", 26, "#38bdf8", 
         f"Senior Software Engineer | {profile.get('summaries', {}).get('general', '')[:120]}...", {
             "title": profile.get("title", "Senior Software Engineer"),
             "email": profile.get("contact", {}).get("email", ""),
             "github": profile.get("contact", {}).get("github", ""),
             "linkedin": profile.get("contact", {}).get("linkedin", "")
         })

# 2. Domain Core Clusters
domains = [
    ("dom-frontend", "Frontend Engineering", "domain", 20, "#60a5fa", "React 19, Next.js 15, React Router v7, Tailwind v4, TanStack Query/Table, Vue.js"),
    ("dom-web3", "Web3 & AI Agents", "domain", 20, "#c084fc", "Smart Contracts (Solidity), Telegram Mini Apps SDK, SSE Streaming, RainbowKit, TON"),
    ("dom-backend", "Backend & APIs", "domain", 20, "#34d399", "Laravel 12, NestJS, PHP 8.2+, Node.js, WebSockets (Reverb/Pusher), Livewire"),
    ("dom-android", "Native Android", "domain", 20, "#a3e635", "Kotlin, Android Jetpack, MVVM, Coroutines, Room DB, Retrofit 2, 1.5M+ Users"),
    ("dom-db", "Databases & Cloud", "domain", 20, "#fbbf24", "MySQL, MongoDB, AWS S3, KilatStorage S3, Midtrans Gateway, Strava API, Redis")
]

for d_id, d_label, d_grp, d_rad, d_col, d_desc in domains:
    add_node(d_id, d_label, d_grp, d_rad, d_col, d_desc)
    add_link(root_id, d_id, 3, "specializes_in")

# 3. Company Nodes
company_map = {
    "pt-lapantiga-solusi-algoritma": ("PT Lapantiga Solusi Algoritma", "#ef4444", ["dom-frontend", "dom-backend"]),
    "kipley-pte-ltd": ("Kipley Pte. Ltd.", "#a855f7", ["dom-web3", "dom-frontend"]),
    "pt-qira-teknologi-indonesia": ("PT Qira Teknologi Indonesia", "#10b981", ["dom-backend", "dom-android", "dom-db"]),
    "pt-aku-pintar-indonesia": ("PT Aku Pintar Indonesia", "#f59e0b", ["dom-android", "dom-frontend", "dom-db"])
}

for exp in profile.get("experiences", []):
    pref = exp.get("project_ref", "")
    comp_slug = os.path.basename(pref.replace("\\", "/"))
    comp_info = company_map.get(comp_slug)
    
    comp_name = exp.get("company", comp_slug)
    comp_color = comp_info[1] if comp_info else "#64748b"
    comp_id = f"comp-{comp_slug}"
    
    add_node(comp_id, comp_name, "company", 18, comp_color, 
             f"Role: {exp.get('role')} ({exp.get('period')}) - {exp.get('location')}", {
                 "role": exp.get("role"),
                 "period": exp.get("period"),
                 "location": exp.get("location"),
                 "summary": exp.get("summary", ""),
                 "bullets": exp.get("highlights", [])
             })
    add_link(root_id, comp_id, 4, "worked_at")
    
    if comp_info:
        for dom_id in comp_info[2]:
            add_link(comp_id, dom_id, 2, "focuses_on")

# 4. Technologies & Libraries
tech_nodes = [
    ("tech-react19", "React 19.x", "tech", 11, "#61dafb", "Modern React UI Engine with Server Components"),
    ("tech-nextjs15", "Next.js 15.x", "tech", 11, "#ffffff", "Next.js App Router & Turbopack bundler"),
    ("tech-laravel12", "Laravel 12.x / 10.x", "tech", 11, "#ff2d20", "Modern PHP Enterprise MVC Framework & Reverb WebSockets"),
    ("tech-typescript", "TypeScript 5.x", "tech", 11, "#3178c6", "Strict static typing with zero 'any' policy"),
    ("tech-tailwind4", "Tailwind CSS v4 / v3", "tech", 11, "#38bdf8", "Next-gen atomic CSS styling engine & Flowbite"),
    ("tech-tanstack", "TanStack Query / Table", "tech", 11, "#ff4154", "Server-state caching & virtualized DataTables"),
    ("tech-pusher", "Pusher / Reverb WS", "tech", 11, "#5c42ec", "Real-time incident event & ticket broadcast channels"),
    ("tech-telegram-tma", "Telegram TMA SDK", "tech", 11, "#229ed9", "@telegram-apps/sdk-react native platform integration"),
    ("tech-solidity", "Solidity & Ethers", "tech", 11, "#627eea", "Ethereum smart contracts & RainbowKit wallets"),
    ("tech-midtrans", "Midtrans Payment", "tech", 11, "#002b49", "Virtual Account, QRIS & GoPay Webhook Gateway"),
    ("tech-mongodb", "MongoDB / NoSQL", "tech", 11, "#47a248", "High-volume GPS coordinate & telemetry logging"),
    ("tech-kotlin-android", "Android Kotlin / Java", "tech", 11, "#7f52ff", "Native Android Jetpack, MVVM, Coroutines, Room DB"),
    ("tech-strava", "Strava API", "tech", 11, "#fc4c02", "Strava OAuth2 & Athlete Activity Synchronization"),
    ("tech-s3-storage", "AWS S3 / KilatStorage", "tech", 11, "#eab308", "Cloud Object Storage & Document Vaults"),
    ("tech-yajra-datatables", "Yajra DataTables", "tech", 11, "#06b6d4", "High-performance server-side SQL paging grid"),
    ("tech-livewire", "Livewire & Blade", "tech", 11, "#fb7185", "Server-driven reactive components without full page reloads"),
    ("tech-webrtc-liferay", "WebRTC & Java OSGi", "tech", 11, "#f97316", "Live video streams & 100+ modular portal services")
]

for t_id, t_lbl, t_grp, t_rad, t_col, t_desc in tech_nodes:
    add_node(t_id, t_lbl, t_grp, t_rad, t_col, t_desc)

# Link Techs to Domains
add_link("tech-react19", "dom-frontend", 2)
add_link("tech-nextjs15", "dom-frontend", 2)
add_link("tech-tailwind4", "dom-frontend", 2)
add_link("tech-tanstack", "dom-frontend", 2)
add_link("tech-typescript", "dom-frontend", 2)
add_link("tech-solidity", "dom-web3", 2)
add_link("tech-telegram-tma", "dom-web3", 2)
add_link("tech-laravel12", "dom-backend", 2)
add_link("tech-pusher", "dom-backend", 2)
add_link("tech-livewire", "dom-backend", 2)
add_link("tech-midtrans", "dom-db", 2)
add_link("tech-mongodb", "dom-db", 2)
add_link("tech-strava", "dom-db", 2)
add_link("tech-s3-storage", "dom-db", 2)
add_link("tech-yajra-datatables", "dom-backend", 2)
add_link("tech-kotlin-android", "dom-android", 2)
add_link("tech-webrtc-liferay", "dom-frontend", 2)
add_link("tech-webrtc-liferay", "dom-backend", 2)

# 5. Full 37 Subprojects & Detailed Tech Mappings
project_tech_map = {
    # PT Lapantiga Solusi Algoritma (14 projects)
    "proj-koda-fe-utama": ["tech-react19", "tech-typescript", "tech-tailwind4", "tech-tanstack", "tech-pusher"],
    "proj-koda-fe-client": ["tech-react19", "tech-typescript", "tech-tailwind4", "tech-tanstack"],
    "proj-eri-helpdesk": ["tech-laravel12", "tech-pusher", "tech-tailwind4"],
    "proj-petrokimia-asuransi": ["tech-laravel12", "tech-livewire", "tech-tailwind4", "tech-s3-storage"],
    "proj-ebupot": ["tech-laravel12", "tech-yajra-datatables", "tech-tailwind4", "tech-s3-storage"],
    "proj-a3jni-backend": ["tech-laravel12", "tech-s3-storage", "tech-yajra-datatables"],
    "proj-digipor-bank-bmpdjatim": ["tech-laravel12", "tech-strava"],
    "proj-efosh-v1": ["tech-laravel12", "tech-mongodb"],
    "proj-efosh-v2": ["tech-laravel12", "tech-yajra-datatables"],
    "proj-miracle-wish-be": ["tech-laravel12"],
    "proj-miracle-wish-fe": ["tech-laravel12", "tech-tailwind4"],
    "proj-miracle-wish-android": ["tech-kotlin-android"],
    "proj-flondr": ["tech-laravel12", "tech-yajra-datatables"],
    "proj-produk-lokal": ["tech-laravel12"],

    # Kipley Pte. Ltd. (11 projects)
    "proj-superior-agents": ["tech-nextjs15", "tech-react19", "tech-solidity", "tech-typescript"],
    "proj-kip-superior-agents": ["tech-nextjs15", "tech-react19", "tech-solidity"],
    "proj-voxi-ai-girlfriend": ["tech-nextjs15", "tech-telegram-tma", "tech-tanstack"],
    "proj-kip-telegram-ai-girlfriend": ["tech-nextjs15", "tech-telegram-tma"],
    "proj-rethinkable-xyz": ["tech-telegram-tma", "tech-typescript", "tech-react19"],
    "proj-knowledge-fi": ["tech-nextjs15", "tech-react19", "tech-tailwind4"],
    "proj-opencampus-university": ["tech-nextjs15", "tech-solidity", "tech-typescript"],
    "proj-kb-builder": ["tech-nextjs15", "tech-react19", "tech-tailwind4"],
    "proj-igroup": ["tech-nextjs15", "tech-react19", "tech-tailwind4"],
    "proj-milei": ["tech-nextjs15", "tech-react19", "tech-pusher"],
    "proj-kip-ecosystem-website": ["tech-nextjs15", "tech-tailwind4"],

    # PT Qira Teknologi Indonesia (11 projects)
    "proj-epak-dev": ["tech-laravel12", "tech-s3-storage", "tech-yajra-datatables"],
    "proj-fix-automart": ["tech-laravel12", "tech-midtrans"],
    "proj-tmap-telkom": ["tech-laravel12", "tech-yajra-datatables"],
    "proj-qisales-backend": ["tech-laravel12", "tech-mongodb"],
    "proj-pmp-smart-backend": ["tech-laravel12", "tech-s3-storage"],
    "proj-e-budgeting": ["tech-laravel12", "tech-yajra-datatables"],
    "proj-samurai-point": ["tech-laravel12", "tech-midtrans"],
    "proj-pmp-store": ["tech-laravel12", "tech-s3-storage"],
    "proj-growth-v2": ["tech-laravel12", "tech-mongodb"],
    "proj-balai-center-android": ["tech-kotlin-android"],
    "proj-ezbli-android": ["tech-kotlin-android"],

    # PT Aku Pintar Indonesia (1 project)
    "proj-aku-pintar-mvp-website": ["tech-webrtc-liferay", "tech-kotlin-android", "tech-mongodb"]
}

# Scan subprojects from directory to guarantee node creation and company linking
company_colors = {
    "pt-lapantiga-solusi-algoritma": "#ef4444",
    "kipley-pte-ltd": "#a855f7",
    "pt-qira-teknologi-indonesia": "#10b981",
    "pt-aku-pintar-indonesia": "#f59e0b"
}

if os.path.exists(EXP_DIR):
    for comp in sorted(os.listdir(EXP_DIR)):
        comp_dir = os.path.join(EXP_DIR, comp)
        if not os.path.isdir(comp_dir) or comp == 'template-project': continue
        
        comp_id = f"comp-{comp}"
        op_dir = os.path.join(comp_dir, 'overview-projects')
        
        if os.path.exists(op_dir):
            for sub in sorted(os.listdir(op_dir)):
                sub_dir = os.path.join(op_dir, sub)
                if not os.path.isdir(sub_dir): continue
                
                sub_id = f"proj-{sub}"
                readme_path = os.path.join(sub_dir, 'README.md')
                sub_title = sub.replace('-', ' ').title()
                sub_desc = f"Project in {comp}"
                
                if os.path.exists(readme_path):
                    with open(readme_path, 'r', encoding='utf-8') as rf:
                        txt = rf.read()
                        first_h1 = re.search(r'^#\s+(.+)$', txt, re.MULTILINE)
                        if first_h1:
                            sub_title = first_h1.group(1).split('—')[0].strip()
                        prob_match = re.search(r'## 🎯 Latar Belakang & Masalah.*?\n(.*?)(?=\n##|$)', txt, re.DOTALL)
                        if prob_match:
                            sub_desc = prob_match.group(1).strip()[:180] + '...'
                
                sub_color = company_colors.get(comp, "#38bdf8")
                add_node(sub_id, sub_title, "project", 13, sub_color, sub_desc, {
                    "slug": sub,
                    "company": comp,
                    "readme_link": f"experience/{comp}/overview-projects/{sub}/README.md"
                })
                # Link Company -> Subproject
                add_link(comp_id, sub_id, 2, "built_project")

# Link all subprojects to their respective technologies
for proj_key, t_list in project_tech_map.items():
    for t_id in t_list:
        add_link(proj_key, t_id, 1, "uses_technology")

print(f"Total Nodes: {len(nodes)}, Total Links: {len(links)}")

graph_data = {"nodes": nodes, "links": links}

json_out_path = os.path.join(OUTPUT_DIR, 'career_graph.json')
with open(json_out_path, 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, indent=2, ensure_ascii=False)
print(f"✅ Generated JSON Graph: {json_out_path}")

html_template = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Muhamad Hendri Febriansyah — Interactive Career Knowledge Graph</title>
  
  <!-- OpenGraph / Social Meta Tags -->
  <meta name="description" content="Jelajahi graf pengetahuan interaktif, arsitektur sistem teknis, dan portofolio proyek rekayasa perangkat lunak Muhamad Hendri Febriansyah (Senior Software Engineer).">
  <meta property="og:title" content="Muhamad Hendri Febriansyah — Career Knowledge Graph">
  <meta property="og:description" content="Visualisasi interaktif D3.js 56+ Node & Relasi: Next.js 15, React 19, Laravel 12, Android Kotlin, Web3 & NTMC Polri Command Center.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://mhendrif.github.io/my-resume/">
  <meta name="theme-color" content="#0f172a">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Muhamad Hendri Febriansyah — Interactive Career Knowledge Graph">
  <meta name="twitter:description" content="Interactive D3.js Knowledge Graph connecting Experience, 37 Production Projects, Frameworks & Tech Stacks.">

  <script src="https://d3js.org/d3.v7.min.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Outfit', sans-serif;
      background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
      color: #f8fafc;
      overflow: hidden;
      width: 100vw;
      height: 100vh;
    }
    .header {
      position: absolute;
      top: 0; left: 0; right: 0;
      padding: 14px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      z-index: 20;
    }
    .title-group { display: flex; align-items: center; gap: 12px; }
    .logo-badge {
      background: linear-gradient(135deg, #38bdf8, #818cf8);
      color: #000;
      font-weight: 700;
      font-size: 13px;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }
    h1 { font-size: 17px; font-weight: 600; }
    .subtitle { font-size: 12px; color: #94a3b8; }
    .controls { display: flex; align-items: center; gap: 10px; }
    .filter-group { display: flex; align-items: center; gap: 6px; }
    .filter-btn {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #94a3b8;
      padding: 6px 11px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    .filter-btn:hover, .filter-btn.active {
      background: #38bdf8;
      color: #000;
      font-weight: 600;
      border-color: #38bdf8;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
    }
    .search-box {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: 7px 12px;
      color: #fff;
      font-size: 13px;
      outline: none;
      transition: all 0.2s;
    }
    .search-box:focus { border-color: #38bdf8; box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2); }
    .btn {
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 13px;
      cursor: pointer;
      font-weight: 500;
      transition: all 0.2s;
    }
    .btn:hover { background: rgba(51, 65, 85, 0.9); border-color: #38bdf8; color: #fff; }
    .legend-bar {
      position: absolute;
      bottom: 20px; left: 24px;
      display: flex; gap: 14px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(10px);
      padding: 8px 16px;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      z-index: 10;
      font-size: 12px;
    }
    .legend-item { display: flex; align-items: center; gap: 6px; }
    .legend-dot { width: 10px; height: 10px; border-radius: 50%; }
    .drawer {
      position: absolute;
      top: 75px; right: -430px;
      width: 410px; bottom: 20px;
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 16px;
      padding: 24px;
      z-index: 30;
      overflow-y: auto;
      transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: -10px 0 30px rgba(0, 0, 0, 0.5);
    }
    .drawer.open { right: 24px; }
    .drawer-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .drawer-tag {
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.8px;
      padding: 3px 8px;
      border-radius: 4px;
      margin-bottom: 8px;
      display: inline-block;
    }
    .drawer-title { font-size: 18px; font-weight: 700; color: #fff; line-height: 1.3; }
    .drawer-close { background: transparent; border: none; color: #94a3b8; font-size: 20px; cursor: pointer; }
    .drawer-close:hover { color: #fff; }
    .drawer-desc { font-size: 14px; color: #cbd5e1; line-height: 1.6; margin-bottom: 18px; }
    .meta-box { background: rgba(30, 41, 59, 0.6); border-radius: 10px; padding: 12px; margin-bottom: 14px; font-size: 13px; }
    .meta-label { color: #94a3b8; font-size: 11px; text-transform: uppercase; font-weight: 600; margin-bottom: 4px; }
    .meta-val { color: #e2e8f0; font-weight: 500; }
    .bullet-list { list-style-type: none; padding: 0; margin-top: 8px; }
    .bullet-list li {
      font-size: 13px; color: #cbd5e1; line-height: 1.5; margin-bottom: 8px;
      padding-left: 16px; position: relative;
    }
    .bullet-list li::before { content: "•"; color: #38bdf8; position: absolute; left: 0; font-size: 16px; }
    svg { width: 100vw; height: 100vh; cursor: grab; }
    svg:active { cursor: grabbing; }
    .link { stroke: rgba(255, 255, 255, 0.12); stroke-width: 1.2px; transition: stroke 0.2s, stroke-width 0.2s; }
    .link.highlighted { stroke: #38bdf8; stroke-width: 2.5px; }
    .node circle { stroke-width: 2.5px; cursor: pointer; transition: transform 0.2s, filter 0.2s; }
    .node circle:hover { transform: scale(1.15); filter: drop-shadow(0 0 12px currentColor); }
    .node text { font-size: 11px; font-weight: 500; fill: #e2e8f0; pointer-events: none; text-shadow: 0 1px 4px rgba(0,0,0,0.9); }
    .node.dimmed circle, .node.dimmed text { opacity: 0.12; }
    .link.dimmed { opacity: 0.04; }
  </style>
</head>
<body>
  <div class="header">
    <div class="title-group">
      <span class="logo-badge">GRAPHIFY</span>
      <div>
        <h1>Muhamad Hendri Febriansyah — Career Knowledge Graph</h1>
        <div class="subtitle">Interactive Knowledge Graph connecting Experience, 37 Production Projects & Tech Stacks</div>
      </div>
    </div>
    <div class="controls">
      <div class="filter-group">
        <button class="filter-btn active" onclick="filterCluster('all', this)">Semua</button>
        <button class="filter-btn" onclick="filterCluster('frontend', this)">🎨 Frontend</button>
        <button class="filter-btn" onclick="filterCluster('backend', this)">⚙️ Backend</button>
        <button class="filter-btn" onclick="filterCluster('web3', this)">🌐 Web3/AI</button>
        <button class="filter-btn" onclick="filterCluster('android', this)">📱 Android</button>
        <button class="filter-btn" onclick="filterCluster('company', this)">🏢 Perusahaan</button>
      </div>
      <input type="text" id="searchInput" class="search-box" placeholder="Cari Proyek, Tech, Skill...">
      <button class="btn" onclick="resetGraph()">Reset</button>
    </div>
  </div>

  <div class="legend-bar">
    <div class="legend-item"><div class="legend-dot" style="background: #38bdf8;"></div> Candidate Root</div>
    <div class="legend-item"><div class="legend-dot" style="background: #60a5fa;"></div> Domain Core</div>
    <div class="legend-item"><div class="legend-dot" style="background: #a855f7;"></div> Companies</div>
    <div class="legend-item"><div class="legend-dot" style="background: #10b981;"></div> Projects</div>
    <div class="legend-item"><div class="legend-dot" style="background: #fbbf24;"></div> Technologies</div>
  </div>

  <div id="drawer" class="drawer">
    <div class="drawer-header">
      <div>
        <span id="drawerTag" class="drawer-tag">PROJECT</span>
        <div id="drawerTitle" class="drawer-title">Project Name</div>
      </div>
      <button class="drawer-close" onclick="closeDrawer()">✕</button>
    </div>
    <div id="drawerDesc" class="drawer-desc">Description will appear here...</div>
    <div id="drawerMeta"></div>
  </div>

  <svg id="graphCanvas"></svg>

  <script>
    const graphData = GRAPH_DATA_PLACEHOLDER;
    const width = window.innerWidth;
    const height = window.innerHeight;

    const svg = d3.select("#graphCanvas");
    const container = svg.append("g");

    const zoom = d3.zoom()
      .scaleExtent([0.2, 4])
      .on("zoom", function(event) {
        container.attr("transform", event.transform);
      });
    svg.call(zoom);

    const simulation = d3.forceSimulation(graphData.nodes)
      .force("link", d3.forceLink(graphData.links).id(function(d) { return d.id; }).distance(function(d) {
        if (d.type === "specializes_in") return 110;
        if (d.type === "worked_at") return 140;
        if (d.type === "built_project") return 90;
        return 70;
      }))
      .force("charge", d3.forceManyBody().strength(-380))
      .force("center", d3.forceCenter(width / 2, height / 2 + 20))
      .force("collision", d3.forceCollide().radius(function(d) { return d.radius + 18; }));

    const link = container.append("g")
      .attr("class", "links")
      .selectAll("line")
      .data(graphData.links)
      .enter().append("line")
      .attr("class", "link");

    const node = container.append("g")
      .attr("class", "nodes")
      .selectAll("g")
      .data(graphData.nodes)
      .enter().append("g")
      .attr("class", "node")
      .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended))
      .on("click", function(event, d) { showDrawer(d); })
      .on("mouseover", function(event, d) { highlightConnections(d); })
      .on("mouseout", resetHighlight);

    node.append("circle")
      .attr("r", function(d) { return d.radius; })
      .attr("fill", function(d) { return d.color; })
      .attr("stroke", function(d) { return d3.color(d.color).brighter(0.8); })
      .attr("stroke-width", function(d) { return d.group === "root" ? 4 : 2; });

    node.append("text")
      .attr("dx", function(d) { return d.radius + 6; })
      .attr("dy", 4)
      .text(function(d) { return d.label; });

    simulation.on("tick", function() {
      link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

      node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    });

    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }
    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }
    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }

    function highlightConnections(d) {
      const connectedNodeIds = new Set();
      connectedNodeIds.add(d.id);

      link.each(function(l) {
        if (l.source.id === d.id || l.target.id === d.id) {
          connectedNodeIds.add(l.source.id);
          connectedNodeIds.add(l.target.id);
          d3.select(this).classed("highlighted", true).classed("dimmed", false);
        } else {
          d3.select(this).classed("highlighted", false).classed("dimmed", true);
        }
      });

      node.each(function(n) {
        if (connectedNodeIds.has(n.id)) {
          d3.select(this).classed("dimmed", false);
        } else {
          d3.select(this).classed("dimmed", true);
        }
      });
    }

    function resetHighlight() {
      node.classed("dimmed", false);
      link.classed("highlighted", false).classed("dimmed", false);
    }

    function filterCluster(category, btnElement) {
      document.querySelectorAll('.filter-btn').forEach(function(b) { b.classList.remove('active'); });
      if (btnElement) btnElement.classList.add('active');

      if (category === 'all') {
        resetGraph();
        return;
      }

      let targetDomainId = '';
      if (category === 'frontend') targetDomainId = 'dom-frontend';
      else if (category === 'backend') targetDomainId = 'dom-backend';
      else if (category === 'web3') targetDomainId = 'dom-web3';
      else if (category === 'android') targetDomainId = 'dom-android';
      else if (category === 'company') {
        node.each(function(n) {
          if (n.group === 'company' || n.group === 'root') {
            d3.select(this).classed('dimmed', false);
          } else {
            d3.select(this).classed('dimmed', true);
          }
        });
        return;
      }

      const matchDomain = graphData.nodes.find(function(n) { return n.id === targetDomainId; });
      if (matchDomain) {
        highlightConnections(matchDomain);
        svg.transition().duration(600).call(
          zoom.transform,
          d3.zoomIdentity.translate(width / 2 - matchDomain.x * 1.3, height / 2 - matchDomain.y * 1.3).scale(1.3)
        );
      }
    }

    function showDrawer(d) {
      const drawer = document.getElementById("drawer");
      const tag = document.getElementById("drawerTag");
      const title = document.getElementById("drawerTitle");
      const desc = document.getElementById("drawerDesc");
      const meta = document.getElementById("drawerMeta");

      tag.innerText = d.group.toUpperCase();
      tag.style.background = d.color + "33";
      tag.style.color = d.color;
      title.innerText = d.label;
      desc.innerText = d.desc || "Tidak ada deskripsi tambahan.";

      let metaHtml = "";
      if (d.meta) {
        if (d.meta.role) {
          metaHtml += '<div class="meta-box"><div class="meta-label">Peran & Periode</div><div class="meta-val">' + d.meta.role + ' (' + d.meta.period + ') - ' + d.meta.location + '</div></div>';
        }
        if (d.meta.bullets && d.meta.bullets.length > 0) {
          metaHtml += '<div class="meta-box"><div class="meta-label">Pencapaian Kunci</div><ul class="bullet-list">' + d.meta.bullets.map(function(b) { return '<li>' + b + '</li>'; }).join('') + '</ul></div>';
        }
        if (d.meta.readme_link) {
          metaHtml += '<div class="meta-box"><div class="meta-label">Dokumentasi Teknis</div><div class="meta-val"><code>' + d.meta.readme_link + '</code></div></div>';
        }
      }
      meta.innerHTML = metaHtml;
      drawer.classList.add("open");
    }

    function closeDrawer() {
      document.getElementById("drawer").classList.remove("open");
    }

    function resetGraph() {
      document.querySelectorAll('.filter-btn').forEach(function(b) { b.classList.remove('active'); });
      document.querySelector('.filter-btn').classList.add('active');
      svg.transition().duration(750).call(
        zoom.transform,
        d3.zoomIdentity.translate(0, 0).scale(1)
      );
      closeDrawer();
      resetHighlight();
    }

    document.getElementById("searchInput").addEventListener("input", function(e) {
      const q = e.target.value.toLowerCase().trim();
      if (!q) {
        resetHighlight();
        return;
      }
      const match = graphData.nodes.find(function(n) {
        return n.label.toLowerCase().indexOf(q) !== -1 || (n.desc && n.desc.toLowerCase().indexOf(q) !== -1);
      });
      if (match) {
        highlightConnections(match);
        svg.transition().duration(500).call(
          zoom.transform,
          d3.zoomIdentity.translate(width / 2 - match.x * 1.5, height / 2 - match.y * 1.5).scale(1.5)
        );
      }
    });

    svg.call(zoom.transform, d3.zoomIdentity.translate(0, 0).scale(0.95));
  </script>
</body>
</html>
"""

html_content = html_template.replace("GRAPH_DATA_PLACEHOLDER", json.dumps(graph_data))

html_out_path = os.path.join(OUTPUT_DIR, 'career_graph.html')
with open(html_out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"✅ Generated Standalone Interactive D3.js Visualizer: {html_out_path}")

root_html_path = os.path.join(BASE_DIR, 'graphify.html')
with open(root_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"✅ Generated Root graphify.html: {root_html_path}")

index_html_path = os.path.join(BASE_DIR, 'index.html')
with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"✅ Generated GitHub Pages index.html: {index_html_path}")
