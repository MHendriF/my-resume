# 📜 RULES & DEVELOPMENT GUIDELINES

> **Repository:** `MHendriF/my-resume`  
> **Purpose:** Centralized Career Hub, Automated Multi-Variant Resume Engine, and Architectural Project Vault for **Muhamad Hendri Febriansyah**.  
> **Last Updated:** August 2026

---

## 🎯 1. Core Principles & Terminology

1. **Terminology Standard:**
   - Always use the term **"Resume"** across all documents, templates, file names, and commit messages (e.g., `Muhamad_Hendri_Febriansyah_Resume.docx`, `Resume_Frontend_Engineer.pdf`). Do not use "CV" unless referring to legacy source archives.
2. **Single Source of Truth (SSOT):**
   - Profile data, employment history, certifications, and skills reside strictly in `data/profile.json` and `data/skills.json`.
   - Never hardcode candidate credentials or experiences inside python build scripts or markdown generators.
3. **Decoupled Architecture:**
   - **Data Layer (`data/`):** JSON structured state.
   - **Project Vault (`experience/`):** Technical documentation and architecture diagrams.
   - **Build Engine (`scripts/`):** Automated compiler generating `.docx`, `.pdf`, and `.md`.
   - **Distribution Layer (`output/`):** Ready-to-use artifacts.

---

## 📁 2. Directory Structure & File Naming Conventions

### 2.1 Company Folders
* Located directly under `experience/` (strictly lowercase `kebab-case`):
  - `experience/kipley-pte-ltd/`
  - `experience/pt-lapantiga-solusi-algoritma/`
  - `experience/pt-qira-teknologi-indonesia/`
  - `experience/pt-aku-pintar-indonesia/`
* Each company directory must contain:
  - `README.md` — Comprehensive company engineering showcase, subproject catalog table, metrics & STAR story (auto-rendered by GitHub).
  - `overview-experience/` — Vault containing subproject folders.

### 2.2 Subproject Folders (Mandatory `kebab-case`)
* Subproject folders inside `overview-experience/` **MUST ALWAYS** use lowercase **`kebab-case`** (hyphen-separated, no spaces, no underscores, no uppercase):
  - ✅ Correct: `koda-fe-utama`, `superior-agents`, `epak-dev`, `digipor-bank-bmpdjatim`
  - ❌ Forbidden: `Koda_FE_Utama`, `superiorAgents`, `Epak_Dev`, `pmp smart backend`

### 2.3 Subproject Internal Structure
Each subproject folder must strictly follow this 2-item hierarchy:
```text
experience/<Company Name>/overview-experience/<project-kebab-name>/
├── 📁 code/           <-- Source code repository (ignored by Git)
└── 📄 README.md     <-- Rich technical documentation & architecture
```

---

## 📝 3. `README.md` Documentation Standard

Every `README.md` file within a subproject folder must contain the following standardized sections:

1. **# Project Title & Status Badge:** (e.g., Live App, Production, Mission-Critical, Government).
2. **## 📌 Ringkasan Eksekutif & Identitas Proyek:** Company, Role, System Type.
3. **## 🎯 Latar Belakang & Masalah (Problem Statement):** Real-world challenge addressed.
4. **## 💡 Solusi & Nilai Bisnis (Solution & Business Value):** Software engineering solution and business impact.
5. **## 🛠️ Tech Stack & Arsitektur Lengkap:** Markdown table categorizing UI, State, Backend, Database, Protocols, Cloud.
6. **### 🏛️ Diagram Alur Arsitektur Sistem (System Architecture):** Clean **Mermaid.js flowchart** for flagship projects.
7. **## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis:** Core functional modules.
8. **## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula):** Quantifiable performance/business outcomes.
9. **## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets):** English STAR-formula bullet points.

---

## ✍️ 4. Resume Writing & Content Rules (Google XYZ Formula)

All bullet points in `data/profile.json`, `resume_bullets.md`, and `README.md` must strictly adhere to **Google's XYZ Formula**:
$$\text{"Accomplished [X] as measured by [Y], by doing [Z]"}$$

* **Action Verbs:** Start every bullet point with strong, precise technical action verbs:
  - *Past Roles:* `Architected`, `Engineered`, `Developed`, `Integrated`, `Optimized`, `Refactored`, `Deployed`, `Scaled`.
  - *Current Role:* `Architecting`, `Leading`, `Engineering`, `Developing`.
* **Quantifiable Metrics:** Include hard numbers, latencies, percentages, and user scales:
  - *Examples:* *"reduced latency by 45%"*, *"processed 1.5M+ active users"*, *"sub-500ms real-time delivery"*, *"achieved 99.9% uptime"*.
* **Concrete Stack Naming:** Explicitly mention modern technologies instead of generic terms (e.g., write *"React 19, Pusher WebSockets, and TanStack Table v8"* instead of *"modern frontend libraries"*).
* **Strict ATS-Compatibility:** Avoid tables, multi-column text frames, images, or special character icons inside compiled Word/PDF resume documents to ensure 100% Applicant Tracking System (ATS) parsing accuracy.

---

## ⚙️ 5. Build Engine & Tooling Guidelines (`scripts/`)

1. **Python Console Encoding:**
   - Always include `sys.stdout.reconfigure(encoding='utf-8')` at the beginning of any Python CLI script to prevent Windows `cp1252` encoding exceptions on emojis and special characters.
2. **Resume Compilation (`scripts/build_resume.py`):**
   - Run compilation using:
     ```powershell
     python scripts/build_resume.py --target all
     ```
   - Supported targets: `general`, `frontend`, `android`, `web3`, `all`.
   - Outputs are placed into `output/` and `output/variants/` (as `.docx`, `.pdf`, and `.md`).
3. **Project Scaffolding (`scripts/new_project.py`):**
   - Always use the helper script to scaffold new projects:
     ```powershell
     python scripts/new_project.py --company "<Company Name>" --name "<project-kebab-name>"
     ```

---

## 🛡️ 6. Git Hygiene & Security Rules

1. **Git Remote Repository:**
   - Origin URL: `git@github.com:MHendriF/my-resume.git`
   - Target Branch: `main`
2. **Git Ignore Protections (`.gitignore`):**
   - **NEVER** commit source code repositories inside `overview-experience/**/code/`.
   - **NEVER** commit `node_modules/`, `vendor/`, `.next/`, `.react-router/`, `build/`, `dist/`, `.venv/`, or `.env*` files.
   - Only markdown documentation, configuration JSONs, build scripts, and official output PDFs/DOCXs should be tracked in Git.
3. **Commit Conventions:**
   - Follow standard **Conventional Commits**:
     - `feat:` New resume template, script, or project vault entry.
     - `docs:` Updates to `README.md`, `README.md`, or `RULES.md`.
     - `refactor:` Restructuring folders or optimizing build scripts.
     - `fix:` Correcting typos, JSON formatting, or build issues.
     - `build:` Re-compiling output resume variants.

---

## 🤖 7. AI Agent Guidelines (For Antigravity / AI Coding Assistants)

When interacting with this repository, AI agents MUST:
1. Adhere strictly to the `kebab-case` naming rule for all subproject folders.
2. Never revert "Resume" back to "CV".
3. Use UTF-8 encoding configuration on all Python script outputs.
4. Verify that `python scripts/build_resume.py --target all` succeeds before committing structural changes.
5. Keep `.gitignore` intact so raw nested repositories in `code/` folders are never tracked.
