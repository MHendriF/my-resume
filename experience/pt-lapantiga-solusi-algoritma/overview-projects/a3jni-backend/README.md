# 🚚 A3 JNI Logistics & Supply Chain Backend — Technical Overview

[![System Status](https://img.shields.io/badge/Status-Production_Active-brightgreen?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-PT_Lapantiga_Solusi_Algoritma-red?style=for-the-badge)](#)
[![Role](https://img.shields.io/badge/Role-Backend_Developer-blue?style=for-the-badge)](#)

---

## 📌 Ringkasan Eksekutif (Executive Summary)
* **Perusahaan / Klien:** PT Lapantiga Solusi Algoritma (A3 JNI)
* **Peran:** Backend Developer
* **Tipe Sistem:** High-Throughput Logistics & Supply Chain Fleet Tracking API Gateway

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Operasional armada logistik membutuhkan gateway backend yang tangguh untuk memantau status pengiriman kargo, memvalidasi bukti serah terima barang (POD), dan mengamankan endpoint dari serangan bot.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun backend RESTful API berbasis Laravel 8.x yang dilengkapi dengan Google Recaptcha v3, AWS S3 untuk penyimpanan foto POD, Yajra DataTables, dan Spatie Permissions.

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 📦 Versi Framework & Runtime Utama (Core Technology Versions)
| Komponen / Framework | Versi Standar | Keterangan & Peran Arsitektural |
| :--- | :--- | :--- |
| **Backend Framework** | `Laravel v8.x` | Core RESTful API Gateway & Fleet State Machine |
| **Security Shield** | `Google Recaptcha v3` | Invisible Bot & Automated Scraping Shield |
| **Cloud Storage** | `AWS S3 (Flysystem)` | Proof of Delivery (POD) Image Vault |
| **Authentication** | `Laravel Sanctum v2.x` | Mobile Driver & Dispatcher Token Guard |
| **Data Analytics** | `Laravel ChartJS` | Fleet Performance & Delivery Velocity Analytics |

---

## 📈 Metrik Dampak Terukur (Google XYZ Formula)
* **Penyimpanan Bukti Kirim (POD):** Mengelola puluhan ribu foto bukti serah terima kargo langsung ke AWS S3 tanpa membebani server backend.
* **Keamanan Endpoint API:** Menekan request bot ilegal sebesar **99%** menggunakan Recaptcha v3 invisible verification.

---

## 💬 STAR Story untuk Wawancara Kerja (Interview Cheat Sheet)
* **Situation:** Diperlukan backend API logistik yang aman dan cepat untuk melayani aplikasi kurir dan portal monitoring armada.
* **Task:** Mengembangkan API tracking, endpoint upload foto POD ke AWS S3, dan dashboard analisis performa kurir.
* **Action:** Mengintegrasikan Laravel Sanctum untuk otentikasi driver mobile, Recaptcha v3 untuk proteksi endpoint publik, dan S3 Flysystem untuk media handling.
* **Result:** Waktu respons API terjaga di bawah 200ms pada beban pengiriman harian yang tinggi.
