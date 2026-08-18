"""
Repository Health & Integrity Diagnostic Tool
Usage:
    python scripts/verify.py
"""

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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
EXP_DIR = os.path.join(BASE_DIR, 'experience')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

def check_json_files():
    print("🔍 [1/4] Checking JSON Schema & Data Integrity...")
    json_errors = []
    
    # 1. profile.json
    prof_path = os.path.join(DATA_DIR, 'profile.json')
    try:
        with open(prof_path, 'r', encoding='utf-8') as f:
            prof = json.load(f)
            assert 'name' in prof and 'experiences' in prof
            for exp in prof.get('experiences', []):
                ref = exp.get('project_ref', '')
                if not os.path.exists(os.path.join(BASE_DIR, ref)):
                    json_errors.append(f"Broken project_ref in profile.json: '{ref}'")
        print("  ✅ profile.json is valid and synchronized.")
    except Exception as e:
        json_errors.append(f"profile.json invalid: {e}")
        
    # 2. skills.json
    skills_path = os.path.join(DATA_DIR, 'skills.json')
    if os.path.exists(skills_path):
        try:
            with open(skills_path, 'r', encoding='utf-8') as f:
                skills = json.load(f)
                assert isinstance(skills, (dict, list))
            print("  ✅ skills.json is valid.")
        except Exception as e:
            json_errors.append(f"skills.json invalid: {e}")

    # 3. templates
    tpl_dir = os.path.join(DATA_DIR, 'templates')
    for t in os.listdir(tpl_dir):
        if t.endswith('.json'):
            try:
                with open(os.path.join(tpl_dir, t), 'r', encoding='utf-8') as tf:
                    json.load(tf)
                print(f"  ✅ Template '{t}' is valid JSON.")
            except Exception as e:
                json_errors.append(f"Template '{t}' error: {e}")

    return json_errors

def check_markdown_links():
    print("\n🔍 [2/4] Verifying Markdown Links & Documentation Integrity...")
    broken_links = []
    md_count = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ['code', '.git', 'node_modules', 'vendor', '.gradle', 'build', 'storage', 'output']]
        for f in files:
            if f.endswith('.md'):
                md_count += 1
                fp = os.path.join(root, f)
                with open(fp, 'r', encoding='utf-8', errors='ignore') as mdf:
                    txt = mdf.read()
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', txt)
                for text, link in links:
                    if link.startswith('http') or link.startswith('#') or link.startswith('mailto:'):
                        continue
                    target_path = os.path.normpath(os.path.join(root, link))
                    if not os.path.exists(target_path):
                        broken_links.append(f"{os.path.relpath(fp, BASE_DIR)} -> [{text}]('{link}')")

    print(f"  ✅ Scanned {md_count} Markdown files. Broken links found: {len(broken_links)}")
    return broken_links

def check_subproject_blueprints():
    print("\n🔍 [3/4] Auditing Subproject Blueprints (README & ARCHITECTURE)...")
    missing_docs = []
    total_projects = 0
    
    for comp in os.listdir(EXP_DIR):
        cp = os.path.join(EXP_DIR, comp)
        if not os.path.isdir(cp) or comp == 'template-project': continue
        op = os.path.join(cp, 'overview-projects')
        if os.path.exists(op):
            for sub in os.listdir(op):
                sp = os.path.join(op, sub)
                if not os.path.isdir(sp): continue
                total_projects += 1
                if not os.path.exists(os.path.join(sp, 'README.md')):
                    missing_docs.append(f"Missing README.md: {comp}/{sub}")
                if not os.path.exists(os.path.join(sp, 'ARCHITECTURE.md')):
                    missing_docs.append(f"Missing ARCHITECTURE.md: {comp}/{sub}")
                    
    print(f"  ✅ Verified {total_projects} total subprojects. Missing docs: {len(missing_docs)}")
    return missing_docs

def check_graphify_build():
    print("\n🔍 [4/4] Checking Graphify Artifacts & Web Assets...")
    graph_errors = []
    g_json = os.path.join(OUTPUT_DIR, 'career_graph.json')
    g_html = os.path.join(OUTPUT_DIR, 'career_graph.html')
    idx_html = os.path.join(BASE_DIR, 'index.html')
    
    for item, label in [(g_json, 'career_graph.json'), (g_html, 'career_graph.html'), (idx_html, 'index.html')]:
        if not os.path.exists(item):
            graph_errors.append(f"Missing graph asset: {label}")
        else:
            print(f"  ✅ Found {label} ({os.path.getsize(item):,} bytes)")
            
    return graph_errors

def main():
    print("=" * 60)
    print("🚀 MUHAMAD HENDRI FEBRIANSYAH — REPO HEALTH CHECK")
    print("=" * 60)
    
    e1 = check_json_files()
    e2 = check_markdown_links()
    e3 = check_subproject_blueprints()
    e4 = check_graphify_build()
    
    total_issues = len(e1) + len(e2) + len(e3) + len(e4)
    print("\n" + "=" * 60)
    if total_issues == 0:
        print("🌟 REPOSITORY HEALTH SCORE: 100/100 (PERFECT GRADE A+)")
        print("All schemas, markdown links, blueprints, and build assets are 100% healthy!")
    else:
        print(f"⚠️ FOUND {total_issues} ISSUE(S):")
        for err in e1 + e2 + e3 + e4:
            print(f"  ❌ {err}")
    print("=" * 60)

if __name__ == '__main__':
    main()
