# 📋 Changelog

All notable changes to the **Muhamad Hendri Febriansyah — Resume & Engineering Vault** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-08-18

### 🚀 Added
- **Full Multilingual Pipeline & Indonesian Resume Variants:**
  - Added dedicated Indonesian profile (`data/profile_id.json`) and skills taxonomy (`data/skills_id.json`).
  - Added 4 Indonesian ATS-compliant resume templates (`general_id`, `frontend_id`, `android_id`, `web3_id`).
  - Upgraded `scripts/build_resume.py` to compile all 8 multi-role variants (DOCX, PDF, MD) seamlessly.
- **Interactive Category Filter Pills & OpenGraph Meta Tags (`index.html` & `graphify.html`):**
  - Added one-click domain filters (Frontend, Backend, Web3/AI, Android, Companies) for instant focus in the D3.js career graph.
  - Added comprehensive OpenGraph and Twitter card metadata for professional link sharing.
- **Visual Career Journey Roadmap (Mermaid Gantt Timeline):**
  - Embedded Gantt timeline in root `README.md` showcasing career progression from 2019 to Present.
- **Repository Diagnostic & Health Check Tool (`scripts/verify.py`):**
  - Built diagnostic test suite auditing Markdown link integrity, JSON schemas, blueprints, and build artifacts.
- **Executive Flagship Highlights Section (`README.md`):**
  - Added dedicated 30-second executive summary table showcasing top enterprise systems (KODA NTMC Polri, Superior Agents Web3, Aku Pintar, EPAK Kemdikbudristek).
- **Canonicalized Data References (`data/profile.json`):**
  - Standardized all `project_ref` keys to strict relative filesystem paths for flawless SSOT sync.
- **Expanded Experience Vault with 9 New Production Subprojects (Total: 37 Projects):**
  - **PT Aku Pintar Indonesia:** `aku-pintar-mvp-website` (100+ Liferay/OSGi Micro-Modules, RIASEC, WebRTC, OVO/BCA Payment).
  - **PT Lapantiga Solusi Algoritma:** `ebupot` (Tax Compliance e-Bupot), `a3jni-backend` (Logistics Fleet API), `petrokimia-asuransi` (Petrokimia Gresik Claim Portal), `flondr` (On-Demand Service), `miracle-wish-android` (Native Android Client).
  - **PT Qira Teknologi Indonesia:** `balai-center-android` (Kemdikbud Paud Dikmas Jatim Android), `ezbli-android` (Ezbli Marketplace Android), `tmap-telkom` (PT Telkom Market Analytics).
- **Knowledge Graph Scale Expansion (Graphify):**
  - Expanded graph network to **56 nodes** and **62 links**, dynamically connecting newly integrated subprojects and technology stacks.
- **GitHub Pages Deployment Pipeline (`index.html` & `.github/workflows/deploy-pages.yml`):**
  - Automated CI/CD deployment hosting the interactive D3.js Knowledge Graph publicly at `https://mhendrif.github.io/my-resume/`.
- **Quick-Access Resume Download Badges:**
  - Added one-click PDF download badges at the top of the root `README.md` for instant access to Master and all role-targeted resume variants.
- **Standardized Project Scaffolding Template (`experience/template-project/`):**
  - Upgraded template with modern `README.md` and `ARCHITECTURE.md` blueprints matching 2026 repository standards.
- **Dedicated ARCHITECTURE.md in Every Subproject:**
  - Authored deep system design blueprints (`ARCHITECTURE.md`) across all 28 subprojects with Mermaid component flowcharts, data transmission lifecycles, and security models.
- **Graphify Interactive Career Knowledge Graph:**
  - Interactive D3.js Force-Directed Network Graph visualizer ([`graphify.html`](./graphify.html) & `output/career_graph.html`).
  - Graph generator engine (`scripts/graphify.py`) mapping **47 Nodes & 49 Relations** across Candidate, Core Domains, Companies, 28 Subprojects, and Framework Technologies.
  - Cyberpunk / Glassmorphism dark mode UI with real-time search, zoom/pan controls, connection hover highlighting, and slide-over detail drawer.
  - Tree-Sitter AST codebase analysis AI Skill at [`.agents/skills/graphify/SKILL.md`](./.agents/skills/graphify/SKILL.md).
- **Company Showcase Landing Pages:**
  - Authored rich, badge-enhanced `README.md` files for all 4 company directories (`experience/kipley-pte-ltd/`, `experience/pt-lapantiga-solusi-algoritma/`, `experience/pt-qira-teknologi-indonesia/`, `experience/pt-aku-pintar-indonesia/`).
  - Added direct subproject catalogs, quantitative Google XYZ impact metrics, and curated English resume bullet points.
- **Specific Framework & Runtime Version Specifications:**
  - Added dedicated `📦 Versi Framework & Runtime Utama` tables across all 28 subproject `README.md` files (highlighting modern stacks like **Next.js 15.1.6, React 19.2.6, React Router v7, Laravel 12.0, TypeScript 5.9, Tailwind CSS v4, Bun 1.0+**, to enterprise legacy frameworks **Laravel 5.x/6.x/8.x, Vue 2, PHP 7.x/8.x**).
- **Single Source of Truth (SSOT) Guidelines:**
  - Authored [`RULES.md`](./RULES.md) outlining strict architectural rules, kebab-case directory conventions, ATS resume writing standards (STAR & Google XYZ formulas), build tooling, and AI agent guardrails.

### 🔄 Changed
- **Directory Hierarchy Refactoring:**
  - Renamed root `projects/` directory to [`experience/`](./experience/) to more accurately reflect a career-based portfolio and experience vault.
  - Standardized all 4 company folders to strict lowercase `kebab-case` (`kipley-pte-ltd`, `pt-lapantiga-solusi-algoritma`, `pt-qira-teknologi-indonesia`, `pt-aku-pintar-indonesia`).
  - Standardized all 28 subproject folders under `overview-projects/` to strict `kebab-case`.
  - Renamed all subproject documentation files from `OVERVIEW.md` to `README.md` for seamless automatic landing page rendering on GitHub.
- **Synchronized System References:**
  - Updated all `project_ref` paths in `data/profile.json`, `scripts/new_project.py`, `experience/README.md`, `README.md`, and `RULES.md`.

### 🧹 Removed & Cleaned
- **Eliminated Redundant Bullet Point Files:**
  - Removed all `resume_bullets.md` files across company directories as their contents are permanently integrated into company `README.md` files and centralized in `data/profile.json`.
- **Cleaned Redundant Files:**
  - Removed duplicate root resume builds (`Muhamad Hendri Febriansyah - Resume.docx/pdf`) to centralize all outputs strictly under `output/`.
  - Removed legacy company-level `overview.md` files as their contents have been completely absorbed into the richer, auto-rendered `README.md` showcases.
- **Disk Footprint Optimization:**
  - Recursively removed 15 `node_modules` and 95 `vendor` folders across subproject codebases.
  - Updated `.gitignore` to prevent vendor artifacts, node modules, and raw source directories from cluttering repository history.

---

## [1.1.0] - 2026-08-17

### 🚀 Added
- **Full Multilingual Pipeline & Indonesian Resume Variants:**
  - Added dedicated Indonesian profile (`data/profile_id.json`) and skills taxonomy (`data/skills_id.json`).
  - Added 4 Indonesian ATS-compliant resume templates (`general_id`, `frontend_id`, `android_id`, `web3_id`).
  - Upgraded `scripts/build_resume.py` to compile all 8 multi-role variants (DOCX, PDF, MD) seamlessly.
- **Interactive Category Filter Pills & OpenGraph Meta Tags (`index.html` & `graphify.html`):**
  - Added one-click domain filters (Frontend, Backend, Web3/AI, Android, Companies) for instant focus in the D3.js career graph.
  - Added comprehensive OpenGraph and Twitter card metadata for professional link sharing.
- **Visual Career Journey Roadmap (Mermaid Gantt Timeline):**
  - Embedded Gantt timeline in root `README.md` showcasing career progression from 2019 to Present.
- **Repository Diagnostic & Health Check Tool (`scripts/verify.py`):**
  - Built diagnostic test suite auditing Markdown link integrity, JSON schemas, blueprints, and build artifacts.
- **Executive Flagship Highlights Section (`README.md`):**
  - Added dedicated 30-second executive summary table showcasing top enterprise systems (KODA NTMC Polri, Superior Agents Web3, Aku Pintar, EPAK Kemdikbudristek).
- **Canonicalized Data References (`data/profile.json`):**
  - Standardized all `project_ref` keys to strict relative filesystem paths for flawless SSOT sync.
- **Expanded Experience Vault with 9 New Production Subprojects (Total: 37 Projects):**
  - **PT Aku Pintar Indonesia:** `aku-pintar-mvp-website` (100+ Liferay/OSGi Micro-Modules, RIASEC, WebRTC, OVO/BCA Payment).
  - **PT Lapantiga Solusi Algoritma:** `ebupot` (Tax Compliance e-Bupot), `a3jni-backend` (Logistics Fleet API), `petrokimia-asuransi` (Petrokimia Gresik Claim Portal), `flondr` (On-Demand Service), `miracle-wish-android` (Native Android Client).
  - **PT Qira Teknologi Indonesia:** `balai-center-android` (Kemdikbud Paud Dikmas Jatim Android), `ezbli-android` (Ezbli Marketplace Android), `tmap-telkom` (PT Telkom Market Analytics).
- **Knowledge Graph Scale Expansion (Graphify):**
  - Expanded graph network to **56 nodes** and **62 links**, dynamically connecting newly integrated subprojects and technology stacks.
- **GitHub Pages Deployment Pipeline (`index.html` & `.github/workflows/deploy-pages.yml`):**
  - Automated CI/CD deployment hosting the interactive D3.js Knowledge Graph publicly at `https://mhendrif.github.io/my-resume/`.
- **Quick-Access Resume Download Badges:**
  - Added one-click PDF download badges at the top of the root `README.md` for instant access to Master and all role-targeted resume variants.
- **Standardized Project Scaffolding Template (`experience/template-project/`):**
  - Upgraded template with modern `README.md` and `ARCHITECTURE.md` blueprints matching 2026 repository standards.
- **Dedicated ARCHITECTURE.md in Every Subproject:**
  - Authored deep system design blueprints (`ARCHITECTURE.md`) across all 28 subprojects with Mermaid component flowcharts, data transmission lifecycles, and security models.
- **Mermaid Architecture Diagrams:**
  - Embedded Mermaid.js system flowcharts, database architecture diagrams, and sequence flows across flagship subproject documentations (NTMC Polri Command Center, Voxi AI Girlfriend, Epak Kemdikbudristek, ERI Helpdesk Reverb, etc.).
- **Subproject Scaffolding Tool:**
  - Created `scripts/new_project.py` for automated creation of new company and project documentation from standardized templates.

### 🔄 Changed
- Reorganized project vaults into structured `overview-projects/` hierarchy per employer.
- Polished bullet points in `resume_bullets.md` using strong action verbs and STAR interview frameworks.

---

## [1.0.0] - 2026-08-16

### 🚀 Added
- **Full Multilingual Pipeline & Indonesian Resume Variants:**
  - Added dedicated Indonesian profile (`data/profile_id.json`) and skills taxonomy (`data/skills_id.json`).
  - Added 4 Indonesian ATS-compliant resume templates (`general_id`, `frontend_id`, `android_id`, `web3_id`).
  - Upgraded `scripts/build_resume.py` to compile all 8 multi-role variants (DOCX, PDF, MD) seamlessly.
- **Interactive Category Filter Pills & OpenGraph Meta Tags (`index.html` & `graphify.html`):**
  - Added one-click domain filters (Frontend, Backend, Web3/AI, Android, Companies) for instant focus in the D3.js career graph.
  - Added comprehensive OpenGraph and Twitter card metadata for professional link sharing.
- **Visual Career Journey Roadmap (Mermaid Gantt Timeline):**
  - Embedded Gantt timeline in root `README.md` showcasing career progression from 2019 to Present.
- **Repository Diagnostic & Health Check Tool (`scripts/verify.py`):**
  - Built diagnostic test suite auditing Markdown link integrity, JSON schemas, blueprints, and build artifacts.
- **Executive Flagship Highlights Section (`README.md`):**
  - Added dedicated 30-second executive summary table showcasing top enterprise systems (KODA NTMC Polri, Superior Agents Web3, Aku Pintar, EPAK Kemdikbudristek).
- **Canonicalized Data References (`data/profile.json`):**
  - Standardized all `project_ref` keys to strict relative filesystem paths for flawless SSOT sync.
- **Expanded Experience Vault with 9 New Production Subprojects (Total: 37 Projects):**
  - **PT Aku Pintar Indonesia:** `aku-pintar-mvp-website` (100+ Liferay/OSGi Micro-Modules, RIASEC, WebRTC, OVO/BCA Payment).
  - **PT Lapantiga Solusi Algoritma:** `ebupot` (Tax Compliance e-Bupot), `a3jni-backend` (Logistics Fleet API), `petrokimia-asuransi` (Petrokimia Gresik Claim Portal), `flondr` (On-Demand Service), `miracle-wish-android` (Native Android Client).
  - **PT Qira Teknologi Indonesia:** `balai-center-android` (Kemdikbud Paud Dikmas Jatim Android), `ezbli-android` (Ezbli Marketplace Android), `tmap-telkom` (PT Telkom Market Analytics).
- **Knowledge Graph Scale Expansion (Graphify):**
  - Expanded graph network to **56 nodes** and **62 links**, dynamically connecting newly integrated subprojects and technology stacks.
- **GitHub Pages Deployment Pipeline (`index.html` & `.github/workflows/deploy-pages.yml`):**
  - Automated CI/CD deployment hosting the interactive D3.js Knowledge Graph publicly at `https://mhendrif.github.io/my-resume/`.
- **Quick-Access Resume Download Badges:**
  - Added one-click PDF download badges at the top of the root `README.md` for instant access to Master and all role-targeted resume variants.
- **Standardized Project Scaffolding Template (`experience/template-project/`):**
  - Upgraded template with modern `README.md` and `ARCHITECTURE.md` blueprints matching 2026 repository standards.
- **Dedicated ARCHITECTURE.md in Every Subproject:**
  - Authored deep system design blueprints (`ARCHITECTURE.md`) across all 28 subprojects with Mermaid component flowcharts, data transmission lifecycles, and security models.
- **Multi-Variant Resume Generation Engine:**
  - Automated Python build script (`scripts/build_resume.py`) with support for targeted role compilation via `--target` CLI parameter.
  - Supported variants:
    1. `Senior Software Engineer` (Master 2-page resume)
    2. `Senior Frontend Engineer` (Tailored for modern React/Next.js/UI roles)
    3. `Senior Android Engineer` (Tailored for Kotlin/Jetpack/MVVM roles)
    4. `Full Stack Web3 Engineer` (Tailored for Next.js/Solidity/Telegram dApps)
- **Multi-Format Export Pipeline:**
  - Simultaneous compilation to `.docx` (custom typographic styling & table borders), `.pdf` (via Microsoft Word COM Automation), and `.md` formats.
- **Centralized Data Sources:**
  - Structured profile data in `data/profile.json` and skills categorization in `data/skills.json`.
