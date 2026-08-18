# Digipor Bank BMPD Jatim — Digital Sports & Strava Integration Platform

[![Strava Integration](https://img.shields.io/badge/Strava_API-Digital_Sports_Platform-FC4C02?style=for-the-badge&logo=strava)](https://strava.com)


## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** PT Lapantiga Solusi Algoritma / Bank BMPD Jatim
- **Peran & Tanggung Jawab:** Full Stack Developer
- **Tipe Sistem:** Digital Sports Competition & Leaderboard System

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Bank BMPD Jawa Timur mengadakan kompetisi olahraga virtual antar-bank (lari & sepeda) dan memerlukan sistem otomatisasi tracking jarak dan validasi aktivitas tanpa input manual.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun web platform Laravel yang terintegrasi langsung dengan Strava API (`iamstuartwilson/strava`), mengotomatisasi sinkronisasi aktivitas, perhitungan skor leaderboard, dan penerbitan sertifikat digital PDF.

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 🏛️ Diagram Alur Arsitektur Sistem (System Architecture)
```mermaid
flowchart TD
    Athlete([Bank Employee / Participant]) --> StravaAuth[Strava OAuth2 Authorization]
    StravaAuth --> StravaAPI[(Strava Cloud Servers)]
    StravaAPI --> WebhookSync[Activity Webhook / Auto-Sync Listener]
    WebhookSync --> DistanceEngine[Anti-Cheating & Distance Validation Engine]
    DistanceEngine --> Leaderboard[(Live Banking Leaderboard Database)]
    Leaderboard --> CertificateEngine[Automated PDF Certificate Generator (DomPDF)]
    CertificateEngine --> DownloadCert([Download Verified E-Certificate])
```

| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Backend Framework** | `PHP, Laravel, MySQL` | Implementasi arsitektural |
| **Third-Party API** | `Strava OAuth & Activity API (`iamstuartwilson/strava`)` | Implementasi arsitektural |
| **Security & Anti-Bot** | `Google NoCaptcha (`anhskohbo/no-captcha`), CORS` | Implementasi arsitektural |
| **PDF & Analytics** | `Barryvdh DomPDF, Laravel Chart.js (`fx3costa/laravelchartjs`)` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- **Strava OAuth & Auto-Sync:** Peserta menghubungkan akun Strava dan aktivitas lari/sepeda otomatis tersinkronisasi.
- **Live Leaderboard:** Papan peringkat klasemen per bank dan perorangan real-time.
- **Automated E-Certificate:** Generator sertifikat prestasi PDF dinamis dengan barcode verifikasi.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Otomasi 100% verifikasi jarak olahraga bagi ribuan karyawan perbankan se-Jawa Timur.**
- **Menghemat ratusan jam kerja panitia dalam merekap data aktivitas manual.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Developed digital sports competition platform for Bank BMPD Jatim integrating the Strava API.*
* *Engineered automated activity sync and distance verification algorithms calculating real-time leaderboards.*
* *Implemented dynamic PDF certificate generation pipeline utilizing Barryvdh DomPDF.*