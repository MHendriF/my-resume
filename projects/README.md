# 🗂️ Direktori Proyek & Portofolio (Project Vault)

Selamat datang di **Project Vault**. Folder ini adalah repositori dokumentasi mendalam untuk setiap proyek rekayasa perangkat lunak yang pernah dikerjakan oleh **Muhamad Hendri Febriansyah**.

Dokumentasi di sini dirancang untuk 2 tujuan utama:
1. **Sumber Data Resume:** Kumpulan *bullet points* terukur siap pakai untuk resume.
2. **Cheat Sheet Interview:** Panduan menjawab pertanyaan teknis / *system design* menggunakan metode **STAR (Situation, Task, Action, Result)**.

---

## 📋 Daftar Proyek Terdata

| No | Folder Proyek | Perusahaan / Klien | Peran Utama | Tech Stack Kunci | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | [01-ntmc-dashboard-utama](./01-ntmc-dashboard-utama/) | NTMC Korlantas Polri / Lapantiga | Frontend Lead / SE | React 19, React Router v7, TanStack Query/Table, Tailwind v4, Pusher JS | 🟢 Active |
| 2 | [02-telegram-ai-crypto-bot](./02-telegram-ai-crypto-bot/) | Kipley Pte. Ltd. (Singapore) | Full Stack Web3 & AI | Next.js, TON SDK, Solidity, Telegram Bot SDK, USDT/Stars | ⚪ Completed |
| 3 | [03-aku-pintar-edtech-app](./03-aku-pintar-edtech-app/) | PT Aku Pintar Indonesia | Android Developer | Kotlin, Java, Jetpack, MVVM, Room DB, Retrofit | ⚪ Completed |
| 4 | [04-qira-enterprise-crm-cms](./04-qira-enterprise-crm-cms/) | PT Qira Teknologi Indonesia | Software Developer | Laravel, PHP, MySQL, Midtrans, Moota, Android | ⚪ Completed |
| 5 | [05-lapantiga-virtual-events](./05-lapantiga-virtual-events/) | PT Lapantiga Solusi Algoritma | Software Engineer | Laravel, Node.js, MongoDB, Virtual Event Streaming, Swagger | ⚪ Completed |

---

## ➕ Cara Menambahkan Proyek Baru

Untuk menambahkan proyek baru ke dalam sistem pipeline ini:
1. **Otomatis via Script CLI:**
   ```bash
   python scripts/new_project.py "nama-proyek-baru"
   ```
2. **Atau Manual:**
   Salin folder [`template-project/`](./template-project/) dan ubah namanya menjadi nomor urut berikutnya (misal: `06-nama-proyek`). Kemudian isi file `overview.md` dan `resume_bullets.md`.
