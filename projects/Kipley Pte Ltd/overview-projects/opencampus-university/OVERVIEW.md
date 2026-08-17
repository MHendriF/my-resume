# OpenCampus University — Decentralized Education Portal

[![Web3 Education](https://img.shields.io/badge/Web3-Open_Campus_OCID-orange?style=for-the-badge)](https://opencampus.xyz)


## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** Kipley Pte. Ltd. (Singapore / Remote)
- **Peran & Tanggung Jawab:** Frontend Web3 Engineer
- **Tipe Sistem:** EdTech Web3 Portal with OCID Integration

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Menghubungkan platform pembelajaran online dengan identitas terdesentralisasi Open Campus (OCID) dan kurikulum interaktif.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun portal Next.js dengan integrasi `@opencampus/ocid-connect-js`, sistem drag-and-drop course builder `@dnd-kit/core`, dan integrasi AWS S3.

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 🏛️ Diagram Alur Arsitektur Sistem (System Architecture)
```mermaid
flowchart LR
    Student([Learner / Educator]) --> OCIDAuth[Open Campus ID Login (@opencampus/ocid-connect-js)]
    OCIDAuth --> CourseBuilder[Drag-and-Drop Curriculum Builder (@dnd-kit/core)]
    CourseBuilder --> S3Upload[Direct-to-S3 Presigned Content Upload]
    S3Upload --> CertNFT[On-chain Education Credentials]
```

| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Framework** | `Next.js, React, TypeScript` | Implementasi arsitektural |
| **Decentralized ID** | `@opencampus/ocid-connect-js (Open Campus ID)` | Implementasi arsitektural |
| **Interactive UI** | `@dnd-kit/core, @dnd-kit/sortable, @dnd-kit/utilities, Emoji Mart` | Implementasi arsitektural |
| **Cloud & Storage** | `AWS S3 SDK, Presigned URLs` | Implementasi arsitektural |
| **Styling** | `Headless UI, Tailwind CSS, Emotion` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- **OCID Single Sign-On:** Login Web3 resmi via Open Campus ID.
- **Drag-and-Drop Course Builder:** Penyusunan modul kursus interaktif dengan DnD Kit.
- **Decentralized Certificates:** Penerbitan kredensial edukasi on-chain.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Integrasi OCID tanpa hambatan dengan waktu autentikasi < 1 detik.**
- **Mendukung penyusunan ratusan modul kurikulum interaktif.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Built Web3 educational portal integrating Open Campus Decentralized Identity (@opencampus/ocid-connect-js).*
* *Engineered smooth drag-and-drop curriculum builder utilizing @dnd-kit/core and sortable primitives.*
* *Implemented cloud asset storage pipeline via AWS S3 SDK for educational multimedia content.*