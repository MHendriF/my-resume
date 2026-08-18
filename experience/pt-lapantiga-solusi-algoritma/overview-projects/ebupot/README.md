# 📑 Sistem e-Bupot (Elektronik Bukti Potong Pajak) — Technical Overview

[![System Status](https://img.shields.io/badge/Status-Production_Active-brightgreen?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-PT_Lapantiga_Solusi_Algoritma-red?style=for-the-badge)](#)
[![Role](https://img.shields.io/badge/Role-Full_Stack_Engineer-blue?style=for-the-badge)](#)

---

## 📌 Ringkasan Eksekutif (Executive Summary)
* **Perusahaan / Klien:** PT Lapantiga Solusi Algoritma
* **Peran:** Full Stack Engineer
* **Tipe Sistem:** Tax Compliance & Withholding Tax Electronic Management System

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Pengelolaan bukti pemotongan pajak penghasilan (PPh 23/26/Final) perusahaan membutuhkan kepatuhan regulasi perpajakan yang ketat, verifikasi NPWP otomatis, serta pengelolaan dokumen pemotongan ribuan transaksi vendor tanpa kesalahan hitung.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun platform sistem e-Bupot berbasis Laravel 8.x, Tailwind CSS, Flowbite, Yajra DataTables, dan AWS S3 untuk mengotomatisasi pembuatan bukti potong pajak, validasi NPWP, penghitungan tarif otomatis, serta ekspor format pelaporan DJP.

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 📦 Versi Framework & Runtime Utama (Core Technology Versions)
| Komponen / Framework | Versi Standar | Keterangan & Peran Arsitektural |
| :--- | :--- | :--- |
| **Backend Framework** | `Laravel v8.x` | Core Tax Calculation & Ledger Engine |
| **Authentication** | `Laravel Sanctum v2.x` | Token-based API Authentication Guard |
| **Data Grid** | `Yajra DataTables v9.x` | Server-Side Heavy Dataset Grid Processing |
| **Cloud Storage** | `Flysystem AWS S3 v1.x` | Encrypted Tax Certificate Storage Vault |
| **UI Components** | `Tailwind CSS v3.x + Flowbite` | Modern Accounting Theme & Modal Dialogs |
| **Spreadsheet Exporter** | `Maatwebsite Excel v3.x` | DJP Tax Report Reconciliation Exporter |

---

## 📈 Metrik Dampak Terukur (Google XYZ Formula)
* **Otomasi Penghitungan Pajak:** Mengotomatisasi **100%** penghitungan tarif PPh berdasarkan jenis objek pajak dengan akurasi formula compliance penuh.
* **Efisiensi Penerbitan Dokumen:** Mempercepat penerbitan ribuan bukti potong bulanan dari beberapa hari menjadi **hitungan menit**.
* **Keamanan Dokumen Bukti Potong:** Seluruh dokumen tersimpan aman terenkripsi di AWS S3 dengan token download berbatas waktu.

---

## 💬 STAR Story untuk Wawancara Kerja (Interview Cheat Sheet)
* **Situation:** Perusahaan membutuhkan sistem internal untuk menerbitkan dan mengarsipkan bukti potong pajak secara digital sesuai format DJP.
* **Task:** Merancang backend kalkulasi pajak, manajemen hak akses multi-role (Akuntan, Reviewer, Tax Manager), dan antarmuka input yang cepat.
* **Action:** Menggunakan Laravel 8.x dengan Yajra DataTables untuk pengolahan ribuan transaksi pemotongan, serta Tailwind CSS + Flowbite untuk interface akuntansi yang intuitif.
* **Result:** Sistem berhasil memangkas waktu rekonsiliasi pajak bulanan dan mencegah potensi denda keterlambatan pelaporan.
