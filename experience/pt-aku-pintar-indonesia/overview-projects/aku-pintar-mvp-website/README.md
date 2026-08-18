# 🎓 Aku Pintar MVP Web Platform — Technical Overview

[![System Status](https://img.shields.io/badge/Status-Production_Active-brightgreen?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-PT_Aku_Pintar_Indonesia-blue?style=for-the-badge&logo=android)](#)
[![Role](https://img.shields.io/badge/Role-Software_Developer-purple?style=for-the-badge)](#)
[![Scale](https://img.shields.io/badge/Scale-100+_Micro_Modules_/_Liferay_Portal-orange?style=for-the-badge)](#)

---

## 📌 Ringkasan Eksekutif (Executive Summary)
* **Perusahaan / Klien:** PT Aku Pintar Indonesia
* **Peran:** Software Developer
* **Periode:** Feb 2021 – May 2024
* **Tipe Sistem:** Enterprise Modular EdTech Web Portal (100+ Micro-Modules)

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Platform Aku Pintar membutuhkan arsitektur portal web skala besar yang mampu mengintegrasikan puluhan layanan pendidikan sekaligus—mulai dari tes minat bakat psikometri (RIASEC & Multiple Intelligence), learning management system (LMS) latihan soal tryout UTBK, direktori kampus dan beasiswa, konseling online berbayar via WebRTC video stream, hingga integrasi multi-payment gateway (OVO, BCA, dan KoinWorks Pinjaman Pendidikan).

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Mengembangkan dan mengelola arsitektur modular enterprise berbasis Liferay / Java OSGi dan Gradle multi-module project yang memecah layanan menjadi lebih dari 100 micro-module mandiri (`minatbakat-web`, `tryout-web`, `konseling-rest`, `koinworks-web`, `gamification-web`, `webrtc`), memastikan skalabilitas tinggi dan isolasi fitur antar modul.

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 📦 Versi Framework & Runtime Utama (Core Technology Versions)
| Komponen / Framework | Versi Standar | Keterangan & Peran Arsitektural |
| :--- | :--- | :--- |
| **Java Platform** | `Java 8 / 11` | Core Enterprise Backend Engine |
| **Portal Framework** | `Liferay / OSGi` | Modular Component Architecture & Service Builder |
| **Build Automation** | `Gradle Multi-Module` | Dependency Management & Artifact Bundling |
| **Real-Time WebRTC** | `WebRTC Native Stream` | Low-Latency Live Video/Audio Tele-Counseling |
| **Payment Gateway** | `BCA API & OVO Gateway` | Automated Digital Top-up & Coin Purchases |
| **Fintech Lending** | `KoinWorks P2P API` | Educational Student Loan Calculator & Submission |

| Layer / Kategori | Teknologi | Deskripsi Implementasi |
| :--- | :--- | :--- |
| **Frontend UI** | JSP, Liferay AlloyUI / Web Components | Responsive Student & Counselor Portals |
| **Backend Services** | Java, OSGi Modules, REST APIs | Modular Service Layer & Business Logic |
| **Database & Cache** | MySQL RDBMS, Redis | Relational User Records & Session Storage |

---

## 📈 Metrik Dampak Terukur (Google XYZ Formula)
* **Penyajian 100+ Modul Edukasi:** Membangun dan memelihara arsitektur 100+ micro-module independen yang melayani ratusan ribu pengguna web secara stabil.
* **Otomasi Penjurusan Siswa:** Mengotomatisasi pemrosesan tes RIASEC dan Multiple Intelligence dengan akurasi 100% dan rekomendasi jurusan instan.
* **Integrasi Multi-Payment & Fintech:** Mengintegrasikan pembayaran digital (BCA, OVO) dan pinjaman pendidikan KoinWorks dengan tingkat keberhasilan transaksi **> 99.8%**.

---

## 💬 STAR Story untuk Wawancara Kerja (Interview Cheat Sheet)
* **Situation:** Aku Pintar memerlukan sistem portal web terpadu dengan puluhan fitur kompleks yang harus dapat di-maintain oleh tim engineer secara paralel tanpa saling mengganggu.
* **Task:** Bertanggung jawab atas pengembangan dan pemeliharaan modul-modul inti web portal (tes minat bakat, tryout, gamifikasi, konseling, dan integrasi payment).
* **Action:** Memanfaatkan arsitektur modular OSGi/Gradle untuk memisahkan domain logic ke dalam modul-modul independen (`konseling-web`, `minatbakat-web`, `tryout-web`, `gamification-web`) serta menghubungkan REST API backend secara seamless.
* **Result:** Platform berhasil beroperasi dengan performa tinggi, mendukung jutaan sesi latihan soal dan tes psikometri siswa se-Indonesia.
