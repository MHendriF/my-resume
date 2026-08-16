#!/usr/bin/env python3
"""
Scaffold a New Project in Project Vault
======================================
Usage:
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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
PROJECTS_DIR = os.path.join(BASE_DIR, 'projects')
TEMPLATE_DIR = os.path.join(PROJECTS_DIR, 'template-project')


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text


def main():
    if len(sys.argv) < 2:
        project_name = input("Masukkan nama proyek baru: ").strip()
    else:
        project_name = " ".join(sys.argv[1:]).strip()

    if not project_name:
        print("Error: Nama proyek tidak boleh kosong.")
        sys.exit(1)

    # Find next sequence number
    existing_dirs = [d for d in os.listdir(PROJECTS_DIR) if os.path.isdir(os.path.join(PROJECTS_DIR, d))]
    seq_nums = []
    for d in existing_dirs:
        match = re.match(r'^(\d+)-', d)
        if match:
            seq_nums.append(int(match.group(1)))

    next_seq = (max(seq_nums) + 1) if seq_nums else 1
    folder_name = f"{next_seq:02d}-{slugify(project_name)}"
    target_path = os.path.join(PROJECTS_DIR, folder_name)

    if os.path.exists(target_path):
        print(f"Error: Folder {folder_name} sudah ada.")
        sys.exit(1)

    shutil.copytree(TEMPLATE_DIR, target_path)

    # Update template placeholders in overview.md
    overview_file = os.path.join(target_path, 'overview.md')
    if os.path.exists(overview_file):
        with open(overview_file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('[Nama Proyek / Sistem]', project_name)
        with open(overview_file, 'w', encoding='utf-8') as f:
            f.write(content)

    bullets_file = os.path.join(target_path, 'resume_bullets.md')
    if os.path.exists(bullets_file):
        with open(bullets_file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('[Nama Proyek]', project_name)
        with open(bullets_file, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"\n🎉 Berhasil membuat proyek baru di:")
    print(f"📁 {target_path}")
    print(f"  - {os.path.join(target_path, 'overview.md')}")
    print(f"  - {os.path.join(target_path, 'resume_bullets.md')}")
    print("\nSilakan isi detail overview dan bullet points pada file tersebut!")


if __name__ == '__main__':
    main()
