# 🏛️ Sistem Asuransi PT Petrokimia Gresik — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Enterprise_Reactive_Healthcare_Claim_Portal-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-lapantiga-solusi-algoritma-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-petrokimia-asuransi-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini menguraikan arsitektur sistem klaim asuransi kesehatan karyawan berbasis Laravel 10 dan Livewire.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph EmployeeUI ["Employee & Verifier Portal (Livewire + Tailwind v3)"]
        ClaimForm["Livewire Dynamic Claim Form"]
        HospitalSelect["IndoRegion Healthcare Facility Selector"]
        ReviewDashboard["Multi-Tier Verifier Approval Grid"]
    end

    subgraph ApplicationCore ["Petrokimia Core (Laravel 10.x + PHP 8.1+)"]
        SanctumAuth["Laravel Sanctum Session & Auth"]
        ClaimStateMachine["Claim State Transition Engine"]
        S3Storage["AWS S3 Flysystem v3 Vault"]
        CaptchaSecurity["Mews Captcha Verification"]
    end

    subgraph StorageInfra ["Data Storage Layer"]
        MySQL_DB[(MySQL 8.0 Primary DB)]
        S3Bucket[(Encrypted AWS S3 Medical Vault)]
    end

    ClaimForm --> SanctumAuth --> ClaimStateMachine
    HospitalSelect --> ClaimStateMachine
    ClaimStateMachine --> MySQL_DB
    ClaimStateMachine --> S3Storage --> S3Bucket
    ReviewDashboard --> ClaimStateMachine
```

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Library | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | `laravel/framework` | `v10.x` | Enterprise Claim Processing & Business Logic |
| **Reactive UI** | `livewire/livewire` | `v2.x` | Server-Driven Real-time Dynamic UI Components |
| **Frontend Bundler** | `vite + laravel-vite-plugin` | `v4.x` | Modern ESM Asset Pipeline |
| **Cloud Storage** | `league/flysystem-aws-s3-v3` | `v3.x` | S3 Encrypted Medical Document Storage |
| **Regional Service** | `azishapidin/indoregion` | `v3.x` | Indonesia Province/City Health Facility Service |
| **Role-Based Access** | `spatie/laravel-permission` | `v5.x` | Employee, Verifier, and Medical Board Roles |
