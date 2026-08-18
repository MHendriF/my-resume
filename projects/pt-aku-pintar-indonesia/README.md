# 🏢 PT Aku Pintar Indonesia — Career Portfolio & Engineering Showcase

[![Company](https://img.shields.io/badge/Company-PT_Aku_Pintar_Indonesia-blue?style=for-the-badge&logo=android)](https://akupintar.id)
[![Role](https://img.shields.io/badge/Role-Android_Developer-brightgreen?style=for-the-badge&logo=android)](https://github.com/MHendriF)
[![Period](https://img.shields.io/badge/Period-Feb_2021_--_May_2024-orange?style=for-the-badge)](https://github.com/MHendriF)
[![User Base](https://img.shields.io/badge/Scale-1.5M+_Users_/_4.42_Rating-yellow?style=for-the-badge&logo=googleplay)](https://play.google.com/store/apps/details?id=id.akupintar.app)

---

## 📌 Ringkasan Eksekutif & Lingkup Tanggung Jawab
Di **PT Aku Pintar Indonesia**, saya berperan sebagai **Android Developer (Full-time)** yang memegang tanggung jawab penuh atas pengembangan dan optimasi aplikasi native Android *Aku Pintar* — platform edtech terkemuka di Indonesia dengan lebih dari **1.500.000+ total unduhan** di Google Play Store.

* **Domain Keahlian:** Native Android Architecture (MVVM, Clean Architecture), Performance Optimization, APK Size Reduction, Memory Leak Profiling, Offline-First Database.
* **Tech Stack Utama:** Kotlin, Java, Android Jetpack, Coroutines, Flow, Retrofit 2, Room DB, Dagger / Hilt, SharedPreferences, Chucker, Firebase Crashlytics.

---

## 🗂️ Fokus Modul & Arsitektur Rekayasa

### 🏛️ Arsitektur Aplikasi (MVVM & Modularization)
```mermaid
flowchart TD
    subgraph ViewLayer ["UI / View Layer (Kotlin)"]
        Activity["Activities & Fragments (Jetpack Navigation)"]
        DataBinding["ViewBinding & DataBinding"]
    end

    subgraph ViewModelLayer ["State & ViewModel Layer"]
        VM["Android ViewModel"]
        StateFlow["StateFlow & LiveData"]
        Coroutines["Kotlin Coroutines (Dispatchers.IO / Main)"]
    end

    subgraph DomainDataLayer ["Repository & Data Source Layer"]
        Repo["Data Repository (Single Source of Truth)"]
        RemoteSource["Remote Data Source (Retrofit 2 + OkHttp3)"]
        LocalSource["Local Offline DB (Room Database + SQLite)"]
    end

    Activity --> DataBinding --> VM
    VM --> StateFlow --> Coroutines
    Coroutines --> Repo
    Repo --> RemoteSource --> REST_API[(Aku Pintar Cloud Backend)]
    Repo --> LocalSource --> RoomDB[(Device Local Storage)]
```

### 📱 Modul Fungsional Utama:
1. **Minat Pintar (Tes Minat & Bakat):** Modul tes psikometri interaktif untuk penjurusan karir dan kuliah siswa.
2. **Belajar Pintar (LMS & Latihan Soal):** Modul latihan soal ujian UTBK/SNBT, tryout online, dan video pembelajaran interaktif.
3. **Kampus Pintar (Informasi Universitas & Beasiswa):** Direktori ribuan program studi perguruan tinggi di Indonesia.
4. **Offline-First Synchronization:** Sinkronisasi materi soal dan catatan belajar ke database lokal (Room DB).

---

## 📈 Metrik Dampak & Pencapaian Terukur (Google XYZ Formula)
* **Reduksi Ukuran Bundle APK:** Memangkas ukuran file instalasi APK sebesar **38.6% (dari 69.5 MB menjadi 42.7 MB)** melalui optimasi asset vector drawable, ProGuard/R8 code shrinking, dan modularisasi arsitektur.
* **Stabilitas & Crash-Free Rate:** Mempertahankan tingkat *crash-free sessions* sebesar **99.42%+** pada basis pengguna aktif harian berskala besar.
* **Kepuasan Pengguna:** Menjaga rating aplikasi tetap tinggi di angka **4.42 / 5.00** pada lebih dari puluhan ribu ulasan di Google Play Store.
* **Efisiensi Waktu Build:** Mempercepat waktu kompilasi *Gradle build time* sebesar **30%** dengan implementasi Gradle caching dan pemisahan modul dependensi.

---

## 🌟 Pilihan Bullet Point Resume Siap Pakai (English)
* *Spearheaded native Android development for a flagship education platform with 1.5M+ active users and a 4.42/5.00 rating on the Google Play Store.*
* *Architected and refactored the codebase into a modular MVVM structure using Android Jetpack, reducing the APK application size by 38.6% (from 69.5 MB to 42.7 MB).*
* *Optimized core UI components, network caching (Retrofit 2), and local persistence (Room DB) achieving a consistent 99.42%+ crash-free session rate.*
* *Implemented responsive multi-screen layouts with Jetpack ViewBinding and managed asynchronous data pipelines using Kotlin Coroutines and Flow.*
