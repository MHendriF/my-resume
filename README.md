# 🚀 Resume & Portfolio Management Pipeline
**Author:** Muhamad Hendri Febriansyah  
**Stack:** Python, python-docx, Word COM (PDF Export), Markdown, JSON  

---

## 🌟 Gambaran Arsitektur Sistem

Pipeline ini dirancang untuk mengorganisir, memperbarui, dan men-generate **Resume profesional & ATS-friendly** secara modular dan otomatis berbasis data (*Single Source of Truth*), lengkap dengan **Experience Vault** untuk menyimpan dokumentasi proyek dan bank kalimat *STAR method* untuk interview.

```
Formal CV/
│
├── 📄 README.md                          <-- Panduan lengkap ini
├── 📄 Muhamad Hendri Febriansyah - Resume.pdf   <-- Output Resume Utama (PDF)
├── 📄 Muhamad Hendri Febriansyah - Resume.docx  <-- Output Resume Utama (Word)
│
├── 📂 data/                              <-- Single Source of Truth
│   ├── profile.json                      <-- Data profil, kontak, pengalaman kerja, edukasi
│   ├── skills.json                       <-- Inventaris skills terkategori per spesialisasi
│   └── templates/                        <-- Konfigurasi target role
│       ├── general.json                  <-- Target: Senior Software Engineer
│       ├── frontend.json                 <-- Target: Senior Frontend Engineer
│       ├── android.json                  <-- Target: Senior Android Engineer
│       └── web3.json                     <-- Target: Full Stack Web3 Engineer
│
├── 📂 experience/                          <-- 🗂️ Experience Vault (Koleksi Dokumentasi Proyek)
│   ├── README.md                         <-- Katalog & indeks seluruh proyek
│   ├── 01-ntmc-dashboard-utama/          <-- NTMC Korlantas Polri (React 19, Pusher, TanStack)
│   │   ├── overview.md                   <-- Gambaran arsitektur, tech stack, metrik, peran
│   │   └── resume_bullets.md             <-- Bullet points siap pakai & STAR interview story
│   ├── 02-telegram-ai-crypto-bot/        <-- Kipley (Web3, TON, Solidity, AI)
│   ├── 03-aku-pintar-edtech-app/         <-- Aku Pintar (Android Native, 1.5M Users, MVVM)
│   ├── 04-qira-enterprise-crm-cms/       <-- Qira (Laravel, Midtrans/Moota, Assessment)
│   ├── 05-lapantiga-virtual-events/      <-- Lapantiga (Virtual Events, Node.js, MongoDB)
│   └── template-project/                 <-- Template starter proyek baru
│
├── 📂 scripts/                           <-- ⚙️ Mesin Otomasi & CLI
│   ├── build_resume.py                   <-- Script build Resume (DOCX, PDF, Markdown)
│   └── new_project.py                    <-- Script scaffolding proyek baru
│
├── 📂 output/                            <-- 📦 Output Build Hasil Render
│   ├── Muhamad_Hendri_Febriansyah_Resume.pdf
│   ├── Muhamad_Hendri_Febriansyah_Resume.docx
│   ├── Muhamad_Hendri_Febriansyah_Resume.md
│   └── variants/                         <-- Hasil build per spesialisasi
│       ├── Resume_Frontend_Engineer.pdf
│       ├── Resume_Android_Engineer.pdf
│       └── Resume_Web3_Engineer.pdf
│
└── 📂 archive/                           <-- 🗄️ Arsip file & draf versi lama
```

---

## ⚡ Cara Menggunakan Pipeline

### 1. 🔨 Mem-build Resume (Generate DOCX, PDF, MD)

Cukup jalankan script `build_resume.py` di terminal:

```bash
# 1. Build Resume Utama (General / Full Stack)
python scripts/build_resume.py

# 2. Build SEMUA Varian Sekaligus (General, Frontend, Android, Web3)
python scripts/build_resume.py --target all

# 3. Build Varian Spesifik
python scripts/build_resume.py --target frontend
python scripts/build_resume.py --target android
python scripts/build_resume.py --target web3
```

Setiap kali script dijalankan, sistem akan otomatis:
1. Membaca data dari `data/profile.json` dan `data/skills.json`.
2. Menyusun layout ATS-compliant single-column berstandar internasional.
3. Menghasilkan file **`.docx`**, **`.pdf`** (via native Word renderer), dan **`.md`** ke dalam folder `output/`.

---

### 2. ➕ Menambahkan Proyek Baru ke Experience Vault

Jalankan perintah berikut:
```bash
python scripts/new_project.py "Nama Proyek Baru Anda"
```

Contoh:
```bash
python scripts/new_project.py "E-Commerce Microservices Platform"
```
* Folder `experience/06-e-commerce-microservices-platform/` akan otomatis dibuatkan dari template.
* Anda tinggal mengisi file `overview.md` dan `resume_bullets.md` di dalam folder tersebut.

---

### 3. ✏️ Memperbarui Data Diri, Pengalaman, atau Skill

* **Ubah Kontak / Bio / Pengalaman / Pendidikan / Sertifikasi:**  
  Edit file **[`data/profile.json`](./data/profile.json)**.
* **Ubah Daftar Skill / Kategori Keahlian:**  
  Edit file **[`data/skills.json`](./data/skills.json)**.
* **Sesuaikan Urutan Pengalaman / Template Baru:**  
  Edit file di dalam folder **[`data/templates/`](./data/templates/)**.

Setelah mengubah data di atas, cukup jalankan `python scripts/build_resume.py --target all` untuk memperbarui seluruh file Word, PDF, dan Markdown dalam sekejap!
