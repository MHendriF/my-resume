# PMP Smart Backend — Online Assessment & Psychometric Scoring Engine

[![Psychometrics](https://img.shields.io/badge/Online_Testing-PMP_Smart_Psychometrics-blue?style=for-the-badge)](http://www.pmpsmart.com)


## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** PT Qira Teknologi Indonesia
- **Peran & Tanggung Jawab:** Lead Backend Developer
- **Tipe Sistem:** Psychometric Testing & Online Assessment Engine

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Institusi asesmen membutuhkan platform tes psikometri online yang mampu menyajikan ribuan variasi soal acak, mengukur waktu pengerjaan secara ketat, dan menghasilkan laporan interpretasi skor instan.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun backend Laravel berkinerja tinggi yang terhubung dengan cloud storage S3 (KilatStorage), generator laporan psikogram PDF (`barryvdh/dompdf`), dan push notification FCM.

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 📦 Versi Framework & Runtime Utama (Core Technology Versions)
| Komponen / Framework | Versi Spesifik | Keterangan & Peran Arsitektural |
| :--- | :--- | :--- |
| **Laravel Framework** | `v8.12.x` | Online Psychometric Examination Engine |
| **PHP Runtime** | `v7.3 / v8.0.2+` | Anti-Cheat Timer & Scoring Algorithmic Pipeline |
| **Object Storage** | `KilatStorage S3 (AWS S3 Protocol)` | Cloud Storage for Answer Vaults & Assets |
| **DomPDF Engine** | `barryvdh/laravel-dompdf v0.9+` | Instant Radar Chart & Psychogram PDF Generator |

### 🏛️ Diagram Alur Arsitektur Sistem (System Architecture)
```mermaid
flowchart TD
    TestTaker([Peserta Asesmen Online]) --> AntiCheat[Anti-Cheat Session Lock & Countdown Timer]
    AntiCheat --> Randomizer[Dynamic Question Item Randomizer]
    Randomizer --> AnswerVault[(KilatStorage S3 / Database Sesi)]
    AnswerVault --> ScoreMatrix[Psychometric Scoring Engine (DISC, MBTI, Papikostik, IQ)]
    ScoreMatrix --> RadarPlot[Radar Chart Generator (Chart.js)]
    RadarPlot --> PsychogramDoc[Instant PDF Psychogram Report (DomPDF)]
```

| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Backend Framework** | `Laravel, PHP, MySQL` | Implementasi arsitektural |
| **Cloud Object Storage** | `AWS S3 Protocol / KilatStorage S3` | Implementasi arsitektural |
| **Reporting Engine** | `Barryvdh DomPDF, FX3Costa LaravelChartJS` | Implementasi arsitektural |
| **Push Notifications** | `Code-LTS Laravel FCM` | Implementasi arsitektural |
| **Networking & Security** | `Fruitcake CORS, GuzzleHttp, Intervention Image` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- **Automated Psychometric Scoring:** Kalkulasi otomatis formula skor tes psikologi (DISC, MBTI, Papikostik, IQ).
- **Anti-Cheat Timer & Question Randomization:** Penyajian butir soal teracak dan penguncian sesi otomatis saat batas waktu habis.
- **Instant Psychogram PDF:** Generator laporan psikogram visual lengkap dengan grafik radar kepribadian peserta.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Menangani ribuan peserta asesmen online bersamaan tanpa kegagalan sinkronisasi jawaban.**
- **Penerbitan laporan hasil psikotes PDF otomatis dalam waktu < 1.5 detik pasca ujian.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Architected online psychometric assessment engine using Laravel, MySQL, and KilatStorage S3.*
* *Engineered automated scoring algorithms for complex psychological testing instruments (DISC, IQ, MBTI).*
* *Implemented instant PDF psychogram report generation with visual radar charts using DomPDF and Chart.js.*