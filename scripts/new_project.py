"""
Scaffold a New Project in Experience Vault
Usage:
    python scripts/new_project.py --company "<company-kebab-name>" --name "<project-name>"
    python scripts/new_project.py "Nama Proyek Baru"
"""

import os
import sys
import re
import shutil

# Fix Windows console UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPERIENCE_DIR = os.path.join(BASE_DIR, 'experience')
TEMPLATE_DIR = os.path.join(EXPERIENCE_DIR, 'template-project')

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def main():
    company_name = None
    project_name = None

    args = sys.argv[1:]
    if '--company' in args:
        idx = args.index('--company')
        if idx + 1 < len(args):
            company_name = args[idx + 1]
    if '--name' in args:
        idx = args.index('--name')
        if idx + 1 < len(args):
            project_name = args[idx + 1]

    if not project_name:
        if len(args) > 0 and not args[0].startswith('--'):
            project_name = " ".join(args).strip()
        else:
            project_name = input("Masukkan nama subproyek baru: ").strip()

    if not project_name:
        print("❌ Nama proyek tidak boleh kosong.")
        return

    proj_slug = slugify(project_name)

    if not company_name:
        companies = [d for d in os.listdir(EXPERIENCE_DIR) if os.path.isdir(os.path.join(EXPERIENCE_DIR, d)) and d != 'template-project']
        print("\nPilih Perusahaan:")
        for i, c in enumerate(companies, 1):
            print(f"  [{i}] {c}")
        choice = input("Pilihan (nomor atau nama folder): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(companies):
            company_name = companies[int(choice) - 1]
        elif choice in companies:
            company_name = choice
        else:
            company_name = slugify(choice)

    comp_dir = os.path.join(EXPERIENCE_DIR, company_name)
    op_dir = os.path.join(comp_dir, 'overview-projects')
    os.makedirs(op_dir, exist_ok=True)

    target_path = os.path.join(op_dir, proj_slug)

    if os.path.exists(target_path):
        print(f"❌ Subproyek '{proj_slug}' sudah ada di {op_dir}.")
        return

    os.makedirs(target_path, exist_ok=True)
    print(f"🚀 Membuat subproyek baru: {target_path}")

    # Copy template files (README.md, ARCHITECTURE.md, resume_bullets.md)
    for fname in os.listdir(TEMPLATE_DIR):
        src = os.path.join(TEMPLATE_DIR, fname)
        dst = os.path.join(target_path, fname)
        if os.path.isfile(src):
            with open(src, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('[Nama Proyek / Sistem]', project_name)
            content = content.replace('[Nama Proyek]', project_name)
            content = content.replace('[Nama_Perusahaan]', company_name)
            content = content.replace('[Nama Perusahaan]', company_name.replace('-', ' ').title())
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  📄 Dibuat: {fname}")

    print(f"\n✅ Berhasil membuat subproyek '{proj_slug}' di bawah '{company_name}'!")
    print(f"👉 Silakan lengkapi {os.path.join(target_path, 'README.md')} dan {os.path.join(target_path, 'ARCHITECTURE.md')}")

if __name__ == '__main__':
    main()
