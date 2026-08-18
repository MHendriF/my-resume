# 🏛️ Epak Widyaprada Kemdikbudristek RI (`epak-dev`) — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-National_Civil_Servant_Credit_Scoring_Platform_&_Document_Security_Pipeline-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-epak-dev-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta manifest dependensi terverifikasi yang diambil langsung dari file manifest proyek (`package.json` & `composer.json`).

* **Pola Arsitektur Utama:** `National Civil Servant Credit Scoring Platform & Document Security Pipeline`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph GovernmentClients ["Government User Portals"]
        WidyapradaOfficer["Widyaprada Civil Servant"]
        SecretariatTeam["Secretariat Document Verifier"]
        AssessorBoard["Certified Assessor Board (Tim Penilai)"]
    end

    subgraph EpakCore ["Epak Core Engine (Laravel 8.0 + PHP ^7.3)"]
        FileVault["alexusmai/laravel-file-manager v2.5 + league/flysystem-aws-s3-v3"]
        PAK_Calc["Official PAK Scoring Formula Engine (Permenpan-RB)"]
        DataTableOracle["yajra/laravel-datatables-oracle v9.0 Grid Engine"]
        AuditLogging["spatie/laravel-activitylog v3.17 Immutable Trail"]
        PermissionRBAC["spatie/laravel-permission v3.17"]
        DomPDFCert["barryvdh/laravel-dompdf v0.8.7 + phpoffice/phpword v0.17"]
        BarcodeGen["milon/barcode v8.0 Official Verification Stamp"]
        ZoomIntegration["macsidigital/laravel-zoom v4.1 Assessment Meetings"]
        BackupDaemon["spatie/laravel-backup v6.16"]
    end

    subgraph SecureStorage ["Government Document Storage Layer"]
        MySQL_DB[(MySQL 8.0 Primary DB)]
        S3Vault[(Encrypted Portfolio Cloud S3 Storage)]
    end

    WidyapradaOfficer --> FileVault --> S3Vault
    SecretariatTeam --> DataTableOracle --> PAK_Calc
    AssessorBoard --> PAK_Calc --> AuditLogging --> MySQL_DB
    PAK_Calc --> DomPDFCert --> BarcodeGen --> MySQL_DB
```

---

## 🔄 Lifecycle & Data Flow
1. **Portfolio Evidence Upload:** Civil servants upload promotion evidence via `alexusmai/laravel-file-manager` to cloud S3 storage (`league/flysystem-aws-s3-v3`).
2. **Secretariat Pre-screening:** Verifiers filter submissions using high-performance `yajra/laravel-datatables-oracle` server-side tables.
3. **Assessment Scoring:** Certified assessors evaluate portfolio points; every score mutation is immutably logged via `spatie/laravel-activitylog`.
4. **Legal Document Issuance:** Generates official Penetapan Angka Kredit (PAK) PDF via `barryvdh/laravel-dompdf` stamped with unique QR barcodes (`milon/barcode`).

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Library | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | `laravel/framework` | `v8.x` | Government Assessment Core Engine |
| **Secure Document Vault** | `alexusmai/laravel-file-manager + S3` | `v2.x` | Cloud Portfolio Evidence Vault |
| **High-Performance Grid** | `yajra/laravel-datatables-oracle` | `v9.x` | Server-Side Table Engine for Large Cohorts |
| **Immutable Audit Trail** | `spatie/laravel-activitylog` | `v3.x+` | Assessor Activity & Point Mutation Logging |
| **Official PAK Generator** | `barryvdh/laravel-dompdf + phpword` | `v0.8+` | Legally Binding Government Certificate Generator |
| **Digital Verification Stamp** | `milon/barcode` | `v8.x` | Security QR Stamp & Certificate Validation |
| **Virtual Assessment Meet** | `macsidigital/laravel-zoom` | `v4.x` | Zoom Integration for Candidate Oral Exams |
| **Role-Based Access (RBAC)** | `spatie/laravel-permission` | `v3.x+` | Multi-Tier Separation of Duties |

---

## 🔒 Security & Access Control
- **Spatie Multi-Tier RBAC:** Strict separation of duties between candidate, secretariat, and assessor.
- **Spatie Activity Log:** Complete audit trail tracking user ID, IP address (`torann/geoip`), and exact point changes.

---

## ⚡ Performance & Scalability Considerations
- **Yajra DataTables:** Server-side pagination handles tens of thousands of educator submissions smoothly.
