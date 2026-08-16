# Aku Pintar (Android Native EdTech Platform)

## 📌 Ringkasan Eksekutif
* **Perusahaan:** PT Aku Pintar Indonesia
* **Peran:** Android Developer (Full-time)
* **Periode:** Feb 2021 – May 2024
* **Tipe Aplikasi:** Native Android Application (B2C Education Platform)
* **Skala Pengguna:** 1.500.000+ Total Users (Play Store Rating 4.42/5.00)

---

## 🎯 Masalah & Tujuan Proyek
Aku Pintar adalah platform edukasi digital terkemuka di Indonesia untuk asesmen minat-bakat siswa, materi belajar, dan bimbingan masuk perguruan tinggi. Aplikasi Android sebelumnya mengalami *monolithic bloat* dengan ukuran APK yang besar (69.5 MB), yang memicu tingginya tingkat *churn* / *drop-off* unduhan di daerah dengan keterbatasan kuota internet.

---

## 🛠️ Tech Stack & Arsitektur
| Komponen | Teknologi | Keterangan |
| :--- | :--- | :--- |
| **Bahasa Utama** | Kotlin, Java | Modern idiomatic Kotlin (Coroutines, Flow) |
| **Arsitektur** | Clean Architecture + MVVM | Separation of concerns (Presentation, Domain, Data layer) |
| **Android Jetpack** | ViewModel, LiveData, Navigation, ViewBinding | Standar Google Android Architecture Components |
| **Penyimpanan Lokal**| Room Database, SQLite, EncryptedSharedPreferences | Offline caching & secure token storage |
| **Jaringan & API** | Retrofit2, OkHttp3, Moshi | REST API integration with interceptors |
| **Security & Analytics**| Certificate Pinning, ProGuard/R8, Firebase FCM, Crashlytics | Keamanan jaringan & monitoring crash |

---

## 🚀 Fitur-Fitur Kunci yang Dibangun
1. **Modular Architecture Refactoring:**
   * Memecah monolith app menjadi feature modules terpisah, membuang asset/library redundan, dan mengaktifkan optimasi Android App Bundle (AAB).
2. **Offline-First Assessment & Quiz Engine:**
   * Fitur pengerjaan tes minat bakat yang otomatis menyimpan progress ke Room DB lokal sehingga tidak hilang saat koneksi internet terputus.
3. **Advanced Security Hardening:**
   * Implementasi Certificate Pinning (SSL Pinning) untuk mencegah serangan Man-in-the-Middle (MITM) dan obfuscation kode dengan ProGuard.
4. **Push Notification Campaign:**
   * Integrasi Firebase Cloud Messaging (FCM) dengan deep linking cerdas ke modul belajar siswa.

---

## 📈 Dampak Bisnis & Metrik Pencapaian (Google XYZ Formula)
* **Reduksi Ukuran APK Sebesar 38.6%:** Berhasil memangkas ukuran aplikasi dari **69.5 MB menjadi 42.7 MB**, meningkatkan rasio konversi install Play Store.
* **Crash-Free Rate > 99.42%:** Menjaga stabilitas aplikasi selama 90 hari berturut-turut di atas 99.42% di Google Play Console.
* **Tingkat Kepuasan Pengguna:** Mempertahankan rating **4.42 / 5.00** dari puluhan ribu review pengguna aktif.
