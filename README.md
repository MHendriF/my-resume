# 🚀 Muhamad Hendri Febriansyah — Resume & Engineering Vault

<div align="center">

[![Live Interactive Career Graph](https://img.shields.io/badge/🌐_Live_Career_Graph-GitHub_Pages-2563eb?style=for-the-badge&logo=googlechrome&logoColor=white)](https://mhendrif.github.io/my-resume/)
[![Download Master Resume (PDF)](https://img.shields.io/badge/📄_Download_Master_Resume-PDF-dc2626?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](./output/Muhamad_Hendri_Febriansyah_Resume.pdf)

<br/>

[![Frontend Resume](https://img.shields.io/badge/🎨_Frontend_Resume-PDF-0284c7?style=for-the-badge&logo=react&logoColor=white)](./output/variants/Resume_Frontend_Engineer.pdf)
[![Android Resume](https://img.shields.io/badge/📱_Android_Resume-PDF-16a34a?style=for-the-badge&logo=android&logoColor=white)](./output/variants/Resume_Android_Engineer.pdf)
[![Web3 Resume](https://img.shields.io/badge/🌐_Web3_Resume-PDF-7c3aed?style=for-the-badge&logo=ethereum&logoColor=white)](./output/variants/Resume_Web3_Engineer.pdf)

</div>

---

## 🌟 Rekayasa Unggulan & Proyek Flagship (Executive Highlights)

Untuk kemudahan peninjauan cepat (*Quick 30-Second Overview*), berikut adalah 4 proyek rekayasa perangkat lunak terpilih:

| Proyek Unggulan | Institusi / Klien | Peran & Skala Sistem | Tech Stack Kunci | Arsitektur & Showcase |
| :--- | :--- | :--- | :--- | :---: |
| **KODA NTMC Polri** | NTMC Korlantas Polri | Real-Time Traffic & Incident Monitoring Command Center (< 500ms latency) | `React 19`, `React Router v7`, `Tailwind v4`, `TanStack Query`, `Pusher WS` | [🏛️ C4 Blueprint](./experience/pt-lapantiga-solusi-algoritma/overview-projects/koda-fe-utama/ARCHITECTURE.md) • [📖 Showcase](./experience/pt-lapantiga-solusi-algoritma/overview-projects/koda-fe-utama/README.md) |
| **Superior Agents** | Kipley Pte. Ltd. | Autonomous Multi-Agent Web3 & AI Portal | `Next.js 15`, `App Router`, `Turbopack`, `RainbowKit`, `Ethers`, `Stripe API` | [🏛️ C4 Blueprint](./experience/kipley-pte-ltd/overview-projects/superior-agents/ARCHITECTURE.md) • [📖 Showcase](./experience/kipley-pte-ltd/overview-projects/superior-agents/README.md) |
| **Aku Pintar EdTech** | PT Aku Pintar Indonesia | Enterprise Modular EdTech Portal (100+ Micro-Modules, 1.5M+ Siswa) | `Java OSGi / Liferay`, `WebRTC Video Stream`, `RIASEC Psychometrics`, `BCA/OVO` | [🏛️ C4 Blueprint](./experience/pt-aku-pintar-indonesia/overview-projects/aku-pintar-mvp-website/ARCHITECTURE.md) • [📖 Showcase](./experience/pt-aku-pintar-indonesia/overview-projects/aku-pintar-mvp-website/README.md) |
| **EPAK Widyaprada** | Kemdikbudristek RI | Sistem Penilaian Angka Kredit Pejabat Fungsional Nasional | `Laravel 8`, `AWS S3 Flysystem`, `Yajra DataTables`, `DomPDF`, `Milon Barcode` | [🏛️ C4 Blueprint](./experience/pt-qira-teknologi-indonesia/overview-projects/epak-dev/ARCHITECTURE.md) • [📖 Showcase](./experience/pt-qira-teknologi-indonesia/overview-projects/epak-dev/README.md) |

---

## 🌟 Gambaran Arsitektur Sistem

Repositori ini adalah **Resume Generation Pipeline & Career Knowledge Vault** modular yang dikelola secara profesional berbasis data (*Single Source of Truth*). Sistem ini mengintegrasikan otomasi kompilasi dokumen multi-varian (`.docx`, `.pdf`, `.md`), lemari arsip rekam jejak teknis per perusahaan (**Experience Vault**), dan **Interactive Knowledge Graph Engine (Graphify)**.

```text
My Resume/
│
├── 📁 .agents/                          <-- AI Skills & Customizations (Graphify AST Skill)
├── 📁 .github/workflows/               <-- GitHub Actions (Automated Pages Deployment)
├── 📁 data/                             <-- Single Source of Truth
│   ├── profile.json                     <-- Data profil, pengalaman kerja, kontak, edukasi
│   ├── skills.json                      <-- Taksonomi keahlian teknis (Web3, Frontend, Backend, Mobile)
│   └── templates/                       <-- Template resume DOCX & Markdown
│
├── 📁 experience/                       <-- Experience Vault (Rekam Jejak per Perusahaan)
│   ├── 📄 README.md                     <-- Katalog seluruh perusahaan & panduan
│   ├── 📁 kipley-pte-ltd/               <-- Kipley Pte. Ltd. (Web3 & AI dApps)
│   ├── 📁 pt-lapantiga-solusi-algoritma/<-- PT Lapantiga Solusi Algoritma (NTMC Polri Command Center)
│   ├── 📁 pt-qira-teknologi-indonesia/  <-- PT Qira Teknologi Indonesia (Kemdikbudristek, Fintech, SFA)
│   ├── 📁 pt-aku-pintar-indonesia/      <-- PT Aku Pintar Indonesia (Android Native MVVM 1.5M Users)
│   └── 📁 template-project/             <-- Template scaffolding subproyek baru (README & ARCHITECTURE)
│
├── 📁 output/                           <-- Production Output (Hasil Build Terkompilasi)
│   ├── 📄 Muhamad_Hendri_Febriansyah_Resume.pdf
│   ├── 📄 Muhamad_Hendri_Febriansyah_Resume.docx
│   ├── 📄 Muhamad_Hendri_Febriansyah_Resume.md
│   ├── 📄 career_graph.html             <-- Standalone D3.js Knowledge Graph Visualizer
│   └── 📁 variants/                     <-- Varian resume tertarget (Frontend, Android, Web3)
│
├── 📁 scripts/                          <-- Automation Engine
│   ├── build_resume.py                  <-- Generator multi-format (.docx, .pdf via MS Word COM, .md)
│   ├── graphify.py                      <-- D3.js interactive career knowledge graph generator
│   └── new_project.py                   <-- Scaffolding otomatis dokumentasi proyek baru
│
├── 📄 CHANGELOG.md                      <-- Riwayat rilis & Semantic Versioning (SemVer)
├── 📄 graphify.html / index.html        <-- Web App Knowledge Graph (GitHub Pages Entrypoint)
├── 📄 README.md                         <-- Panduan utama repositori ini
└── 📄 RULES.md                          <-- Single Source of Truth (SSOT) aturan & konvensi sistem
```

---

## 🌐 Graphify — Interactive Career & Code Knowledge Graph

Repositori ini dilengkapi dengan **Graphify Engine** (D3.js Force-Directed Interactive Network Graph & Tree-Sitter AST Skill):
* 🕸️ **Live Web Demo:** Kunjungi [**`https://mhendrif.github.io/my-resume/`**](https://mhendrif.github.io/my-resume/) untuk menjelajahi graf hubungan interaktif antara **Perusahaan ➔ Proyek ➔ Framework & Versi ➔ Kategori Keahlian**.
* 🤖 **AI AST Skill:** Tersedia di [`.agents/skills/graphify/SKILL.md`](./.agents/skills/graphify/SKILL.md) untuk pemetaan dependensi codebase lintas-proyek secara deterministik.
* ⚡ **Regenerate Graph:** Jalankan `python scripts/graphify.py` kapan saja untuk memperbarui visualisasi graf.

---

## 🚀 Quick Start / Cara Penggunaan

### 1. Build Semua Varian Resume (DOCX, PDF & Markdown)
```powershell
# Generate semua 4 target peran sekaligus
python scripts/build_resume.py --target all
```

### 2. Build Varian Peran Tertentu
```powershell
python scripts/build_resume.py --target frontend    # Senior Frontend Engineer
python scripts/build_resume.py --target android     # Senior Android Engineer
python scripts/build_resume.py --target web3        # Full Stack Web3 Engineer
python scripts/build_resume.py --target general     # Senior Software Engineer (Master)
```

### 3. Generate Interactive Knowledge Graph
```powershell
python scripts/graphify.py
```

### 4. Tambah Proyek Baru dari Template
```powershell
python scripts/new_project.py --company "pt-lapantiga-solusi-algoritma" --name "nama-proyek-baru"
```

---

## 📋 Varian Resume yang Tersedia

| Varian Resume | Target Posisi | Highlight Proyek & Stack Utama | Output File |
| :--- | :--- | :--- | :--- |
| **Master / General** | Senior Software Engineer | Full Stack (React 19, Laravel 12, Android Kotlin, Web3, NTMC Polri) | [`Resume.pdf`](./output/Muhamad_Hendri_Febriansyah_Resume.pdf) |
| **Frontend Track** | Senior Frontend / Web Lead | React 19, React Router v7, Next.js 15, Tailwind v4, Pusher WS | [`Frontend.pdf`](./output/variants/Resume_Frontend_Engineer.pdf) |
| **Android Track** | Senior Android Engineer | Kotlin, MVVM, Clean Architecture, Jetpack, Coroutines, Room DB | [`Android.pdf`](./output/variants/Resume_Android_Engineer.pdf) |
| **Web3 & AI Track** | Full Stack Web3 / AI Engineer | Next.js 15, Telegram TMA SDK, Solidity, Ethers, SSE Streaming | [`Web3.pdf`](./output/variants/Resume_Web3_Engineer.pdf) |

---

## 📝 Format Penulisan Resume (Standar Google XYZ & STAR Method)

Semua pencapaian dalam resume disusun dengan formula terukur:

$$\text{Accomplished } [X] \text{ as measured by } [Y] \text{ by doing } [Z]$$

* **Situation & Task:** Masalah nyata yang dihadapi sistem / bisnis klien.
* **Action:** Pilihan arsitektur, teknologi spesifik, dan langkah implementasi teknis konkret.
* **Result & Metric:** Peningkatan performa kuantitatif (latensi < 500ms, reduksi ukuran bundle 38.6%, zero failure rate).
