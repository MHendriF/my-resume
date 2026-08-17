# E-Budgeting — Regional Government Budget Planning & QR Sign-Off

[![Municipal Budgeting](https://img.shields.io/badge/Gov_Fintech-E--Budgeting_Regional-green?style=for-the-badge)](https://qiratek.com)


## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** PT Qira Teknologi Indonesia
- **Peran & Tanggung Jawab:** Software Developer
- **Tipe Sistem:** Enterprise Municipal Budgeting & Approval System

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Penyusunan anggaran daerah memerlukan alur pengajuan dan persetujuan bertingkat yang transparan dengan proteksi tanda tangan digital.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun sistem E-Budgeting berbasis Laravel dengan tabel data berkinerja tinggi (`yajra/laravel-datatables-oracle`), autentikasi peran kompleks (`zizaco/entrust`), dan verifikasi dokumen via QR Code (`simplesoftwareio/simple-qrcode`).

---

## 🛠️ Tech Stack & Arsitektur Lengkap

### 🏛️ Diagram Alur Arsitektur Sistem (System Architecture)
```mermaid
flowchart TD
    SKPD([Dinas / Satuan Kerja]) --> InputBudget[Input Usulan Anggaran Belanja]
    InputBudget --> YajraTable[Server-Side DataTables (>50K Rows)]
    YajraTable --> MultiAuth{Verifikasi Bertingkat (Entrust RBAC)}
    MultiAuth -->|Disetujui| QRSign[Digital Signature via QR Code]
    MultiAuth -->|Ditolak / Revisi| NoteRevisi[Catatan Revisi Pos Anggaran]
    QRSign --> DocumentPDF[Dokumen Pengesahan Anggaran Resmi Ber-QR]
```

| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Framework & DB** | `Laravel, PHP, MySQL / Oracle DB support` | Implementasi arsitektural |
| **High-Performance Tables** | `Yajra Laravel DataTables & Oracle DataTables` | Implementasi arsitektural |
| **Security & RBAC** | `Zizaco Entrust Role-Based Access Control` | Implementasi arsitektural |
| **Digital Signatures** | `SimpleSoftwareIO Simple QRCode` | Implementasi arsitektural |
| **Developer Tooling** | `Laravel Debugbar, Laravel Tinker, Laravel Collective` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- **Multi-Level Budget Approval:** Alur persetujuan usulan anggaran dari level dinas, verifikator, hingga kepala daerah.
- **Fast DataTables:** Pemrosesan puluhan ribu baris pos anggaran dengan Yajra DataTables sisi server.
- **QR Code Verification:** Tanda tangan digital dinamis pada lembar dokumen anggaran pengesahan.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Pencarian dan pemfilteran data anggaran instan pada dataset >50.000 baris belanja.**
- **Mencegah manipulasi dokumen anggaran melalui verifikasi QR Code terenkripsi.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Developed enterprise regional government budgeting system using Laravel and Yajra DataTables.*
* *Implemented multi-tier hierarchical approval workflows with granular Role-Based Access Control (Entrust).*
* *Engineered digital sign-off and document authenticity verification utilizing dynamic QR codes.*