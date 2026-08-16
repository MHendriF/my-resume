# Enterprise Assessment, CRM & Payment Integration Systems

## 📌 Ringkasan Eksekutif
* **Perusahaan:** PT Qira Teknologi Indonesia
* **Peran:** Software Developer (Contract / Project-based)
* **Periode:** Nov 2020 – Jan 2024
* **Tipe Aplikasi:** Web-based Back-end Platforms, Online Assessment Systems, E-Commerce, Enterprise CRM & Companion Android Apps

---

## 🎯 Masalah & Tujuan Proyek
Membangun dan mengelola berbagai platform digital kelas enterprise untuk klien korporat, mencakup modul rekrutmen/asesmen online, toko online B2B/B2C, Customer Relationship Management (CRM), serta integrasi payment gateway otomatis untuk rekonsiliasi keuangan tanpa intervensi manual.

---

## 🛠️ Tech Stack & Arsitektur
| Komponen | Teknologi | Keterangan |
| :--- | :--- | :--- |
| **Backend Framework** | PHP, Laravel | RESTful API design, background jobs, queuing |
| **Database & Cache** | MySQL, Redis | Relational data schema with indexing optimization |
| **Payment Gateways** | Midtrans (Snap/Core), Moota | Multi-channel payment (VA, QRIS, E-Wallet, Bank Mutation) |
| **Integrasi Eksternal**| Google APIs, WhatsApp Gateway | OAuth login, automated email notifications & receipts |
| **Mobile Client** | Java, Kotlin, Android Jetpack, Firebase | Companion apps for field staff and customers |
| **Server & Deployment**| Linux/SSH, cPanel, Plesk | Zero-downtime release pipelines & SSL management |

---

## 🚀 Fitur-Fitur Kunci yang Dibangun
1. **Automated Payment Gateway & Mutation Reconciliation:**
   * Integrasi webhook Midtrans dan scraping mutasi otomatis Moota untuk verifikasi pembayaran pesanan dan faktur CRM secara instan.
2. **Online Assessment & Scoring Engine:**
   * Platform tes psikometri dan asesmen kerja online dengan auto-timer, anti-cheat randomized questions, dan auto-scoring PDF report generation.
3. **Companion Native Android Applications:**
   * Aplikasi mobile untuk tracking transaksi dan asesmen berbasis Firebase Realtime Database.
4. **Server Provisioning & Optimization:**
   * Konfigurasi Nginx/Apache, cron jobs, database backup otomatis, dan monitoring server.

---

## 📈 Dampak Bisnis & Metrik Pencapaian
* **Akurasi Pembayaran 99.9%:** Mengotomatiskan 100% verifikasi invoice klien tanpa kesalahan rekonsiliasi manual.
* **Skalabilitas Asesmen:** Mampu menampung ribuan peserta ujian bersamaan dalam satu sesi tanpa lonjakan latensi database.
