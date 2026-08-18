# Miracle Wish Backend — E-Commerce & Gifting Order Processing API

## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** PT Lapantiga Solusi Algoritma
- **Peran & Tanggung Jawab:** Backend Engineer
- **Tipe Sistem:** E-Commerce & Gifting Order Backend API

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Platform gifting dan merchandise custom memerlukan API pemrosesan order cepat dengan pembuatan invoice otomatis dan push notification status pengiriman.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun REST API Laravel dengan integrasi Firebase FCM (`apility/laravel-fcm`), auto-generate invoice PDF (`barryvdh/dompdf`), dan analitik transaksi Chart.js.

---

## 🛠️ Tech Stack & Arsitektur Lengkap
| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Backend** | `Laravel, PHP, MySQL` | Implementasi arsitektural |
| **Notifications** | `Apility Laravel FCM` | Implementasi arsitektural |
| **Document Engine** | `Barryvdh DomPDF` | Implementasi arsitektural |
| **Charts** | `FX3Costa LaravelChartJS, Fruitcake CORS` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- API pemrosesan pesanan custom gift dan tracking nomor resi.
- Penerbitan otomatis faktur / invoice PDF berbarcode.
- Notifikasi push status pengiriman pesanan ke aplikasi pembeli.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Generasi invoice PDF instan dalam waktu < 800ms.**
- **Tingkat keberhasilan push notification status pesanan 99.8%.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Developed RESTful order processing API with Laravel and MySQL for custom e-commerce platform.*
* *Integrated Firebase Cloud Messaging for automated order status and shipment push notifications.*
* *Engineered automated PDF invoice generation pipeline with Barcode and QR tracking.*
