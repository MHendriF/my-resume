# 🗂️ Direktori Proyek & Portofolio (Project Vault)

Selamat datang di **Project Vault**. Folder ini adalah repositori dokumentasi mendalam untuk setiap proyek rekayasa perangkat lunak yang pernah dikerjakan oleh **Muhamad Hendri Febriansyah**, terorganisir rapi berdasarkan **Perusahaan / Organisasi**.

Dokumentasi di sini dirancang untuk 2 tujuan utama:
1. **Sumber Data Resume:** Kumpulan *bullet points* terukur siap pakai untuk resume.
2. **Cheat Sheet Interview:** Panduan menjawab pertanyaan teknis / *system design* menggunakan metode **STAR (Situation, Task, Action, Result)**.

---

## 📋 Daftar Perusahaan & Portofolio Proyek

| Perusahaan / Organisasi | Peran Utama | Proyek & Fokus Teknologi | Status |
| :--- | :--- | :--- | :---: |
| **[PT Lapantiga Solusi Algoritma](./pt-lapantiga-solusi-algoritma/)** | Lead Frontend / Software Engineer | **NTMC Dashboard Utama** (`koda-fe-utama`), NTMC Client, ERI Helpdesk, Digipor Strava (React 19, React Router v7, TanStack, Pusher WebSockets, Laravel Reverb) | 🟢 Active |
| **[Kipley Pte. Ltd](./kipley-pte-ltd/)** | Full Stack Web3 & AI Engineer | **Superior Agents, Telegram Mini Apps (Voxi), KnowledgeFi** (Next.js, RainbowKit, Solidity, Telegram TMA SDK, SSE Streaming, AWS S3) | ⚪ Completed |
| **[PT Aku Pintar Indonesia](./pt-aku-pintar-indonesia/)** | Android Developer | **Aku Pintar EdTech Android Platform** (Native Android Kotlin, MVVM, Jetpack, Room DB, 1.5M Users) | ⚪ Completed |
| **[PT Qira Teknologi Indonesia](./pt-qira-teknologi-indonesia/)** | Software Developer | **Epak Kemdikbudristek, E-Budgeting, FixAutoMart (Midtrans), QiSales (MongoDB)** (Laravel, PHP, Midtrans, MySQL, MongoDB) | ⚪ Completed |

---

## 🏗️ Struktur Setiap Folder Perusahaan

Setiap folder perusahaan memiliki struktur standar:
```text
projects/<company-kebab-name>/
├── 📄 overview.md          <-- Ringkasan tingkat perusahaan & peran
├── 📄 resume_bullets.md    <-- Bullet points resume pilihan (STAR & Google XYZ)
└── 📁 overview-projects/   <-- Vault subproyek (masing-masing memiliki README.md & diagram)
    ├── 📁 <project-kebab-1>/
    │   └── 📄 README.md    <-- Dokumentasi teknis & arsitektur proyek
    └── 📁 <project-kebab-2>/
        └── 📄 README.md
```

---

## ➕ Cara Menambahkan Dokumentasi Proyek Baru

Gunakan helper script otomatis:
```powershell
python scripts/new_project.py --company "<company-kebab-name>" --name "<project-kebab-name>"
```
