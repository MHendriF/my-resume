# PT Aku Pintar Indonesia - Project Portfolio & Overview

## 📌 Ringkasan Perusahaan & Peran
* **Perusahaan:** PT Aku Pintar Indonesia
* **Peran:** Android Developer (Full-time)
* **Periode:** Feb 2021 – May 2024
* **Tipe Sistem:** Native Android Application (EdTech Education Platform)
* **Skala Pengguna:** 1.500.000+ Total Users (Play Store Rating 4.42/5.00)

---

## 🎯 Masalah & Solusi
Aplikasi Android Aku Pintar yang memiliki 1.5 juta pengguna mengalami kendala ukuran bundle APK yang terlalu besar (69.5 MB), yang memicu tingginya tingkat *drop-off* unduhan bagi pengguna dengan kuota terbatas. Diperlukan refactoring arsitektur modular untuk memangkas ukuran APK dan meningkatkan performa runtime.

---

## 🛠️ Tech Stack & Arsitektur
| Komponen | Teknologi | Keterangan |
| :--- | :--- | :--- |
| **Bahasa Utama** | Kotlin, Java | Kotlin Coroutines & Flow |
| **Arsitektur** | Clean Architecture + MVVM | Modular architecture separation |
| **Android Jetpack** | ViewModel, LiveData, Navigation, ViewBinding | Modern Android components |
| **Penyimpanan Lokal**| Room Database, SQLite | Local offline caching |
| **Jaringan & API** | Retrofit2, OkHttp3, Moshi | REST API integration |
| **Keamanan & Tools** | Certificate Pinning, ProGuard/R8, Firebase FCM, Crashlytics | Security hardening & monitoring |

---

## 🚀 Fitur-Fitur Kunci yang Dibangun
1. **Modular Architecture & Size Reduction:** Memecah monolit menjadi feature modules, membersihkan aset tak terpakai, dan optimasi AAB/ProGuard.
2. **Offline-First Assessment:** Menyimpan progress tes asesmen ke Room DB lokal secara otomatis.
3. **Security Hardening:** Implementasi SSL Certificate Pinning untuk proteksi mitigasi serangan MITM.

---

## 📈 Metrik Pencapaian (Google XYZ Formula)
* **38.6% App Size Reduction:** Memangkas ukuran APK dari **69.5 MB menjadi 42.7 MB**.
* **99.42%+ Crash-Free Rate:** Mempertahankan kestabilan aplikasi >99.42% selama 90 hari berturut-turut di Google Play Console.
* **Tingkat Kepuasan:** Mempertahankan rating **4.42 / 5.00** di Google Play Store.
