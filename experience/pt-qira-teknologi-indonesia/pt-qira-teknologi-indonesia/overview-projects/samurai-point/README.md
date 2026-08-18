# Samurai Point — Customer Loyalty Rewards & Token System

## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** PT Qira Teknologi Indonesia
- **Peran & Tanggung Jawab:** Software Developer
- **Tipe Sistem:** Customer Loyalty & Reward Points Redemption Platform

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Jaringan ritel memerlukan sistem program loyalitas poin terpadu untuk pelanggan dengan alur penukaran hadiah (*rewards redemption*) yang aman dan real-time.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun platform loyalitas berbasis Laravel dengan Laravel Sanctum API authentication, shopping cart khusus penukaran poin (`darryldecode/cart`), dan sistem proteksi anti-fraud.

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 📦 Versi Framework & Runtime Utama (Core Technology Versions)
| Komponen / Framework | Versi Spesifik | Keterangan & Peran Arsitektural |
| :--- | :--- | :--- |
| **Laravel Framework** | `v8.75.x` | Customer Loyalty Points Redemption Hub |
| **PHP Runtime** | `v7.3 / v8.0+` | Tamper-Proof Ledger Transaction Logic |
| **API Authentication** | `Laravel Sanctum v2.x` | Tokenized REST API for Mobile Applications |
| **Point Cart** | `darryldecode/cart v4.x` | Specialized Reward Point Deduction Engine |

| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Backend Framework** | `Laravel, PHP, MySQL` | Implementasi arsitektural |
| **API Authentication** | `Laravel Sanctum` | Implementasi arsitektural |
| **Point Cart Engine** | `Darryldecode Cart, Laravel Collective` | Implementasi arsitektural |
| **Security & Config** | `JackieDo DotEnv Editor, Google NoCaptcha, GuzzleHttp` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- **Points Accumulation & Redemption:** Kalkulasi poin reward dari setiap transaksi belanja ritel.
- **Reward Catalog & Cart:** Katalog hadiah online dengan checkout penukaran saldo poin.
- **Secure Token API:** Endpoint REST API terenkripsi berbasis Laravel Sanctum untuk aplikasi mobile pelanggan.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Memproses ribuan transaksi penukaran poin bulanan tanpa kesalahan pembukuan saldo.**
- **Kecepatan respon API penukaran poin < 200ms.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Engineered customer loyalty and rewards redemption system using Laravel and Laravel Sanctum.*
* *Developed secure point-deduction shopping cart workflows utilizing Darryldecode Cart package.*
* *Implemented tamper-proof ledger tracking member points earning and reward claims.*
