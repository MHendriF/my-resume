# 🏛️ Epak Widyaprada (Kemdikbudristek RI) — Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Multi-Tier_Government_Audit_Trail_&_Legal_Document_Pipeline-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-epak-dev-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta pertimbangan keamanan dan skalabilitas untuk **`epak-dev`**.

* **Pola Arsitektur Utama:** `Multi-Tier Government Audit Trail & Legal Document Pipeline`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph AssessorClients ["Government User Interfaces"]
        WidyapradaUser["Widyaprada Officer (Civil Servant)"]
        SecretariatTeam["Secretariat Verifier"]
        AssessorTeam["Official Assessor (Tim Penilai)"]
    end

    subgraph EpakPlatform ["Epak Core System (Laravel 8.0)"]
        AuthRBAC["Multi-Level RBAC & Profile Validator"]
        PAK_Calculator["Precise Credit Formula Engine (Permenpan-RB)"]
        DocVault["Alexusmai File Manager Secure Document Store"]
        AuditTrail["Immutable Action Audit Logging Engine"]
        PDF_Engine["Official PAK Legal PDF Generator (DomPDF)"]
    end

    subgraph StorageLayer ["Database & Secure Document Vault"]
        MySQL_DB[(MySQL 8.0 Primary DB)]
        PDF_Vault[(Encrypted Government Document Vault)]
    end

    WidyapradaUser --> AuthRBAC --> DocVault
    SecretariatTeam --> AuthRBAC --> PAK_Calculator
    AssessorTeam --> AuthRBAC --> PAK_Calculator
    PAK_Calculator --> AuditTrail --> MySQL_DB
    PAK_Calculator --> PDF_Engine --> PDF_Vault
```

---

## 🔄 Lifecycle & Data Flow
1. **Portfolio Submission:** Civil servant officers upload work evidence portfolios into the secured document manager.
2. **Secretariat Pre-Screening:** Verifiers check document completeness before forwarding to certified assessors.
3. **Assessment & Credit Scoring:** Evaluators score criteria according to official ministerial scoring matrices.
4. **Official PAK Issuance:** Generates legally binding PDF Penetapan Angka Kredit (PAK) with digital signature stamps.

---

## 🔒 Security & Access Control
- **Multi-Tier Separation of Duties:** Assessors cannot evaluate candidates without prior secretariat clearance.
- **Comprehensive Audit Trail:** Logs every point modification with timestamp and assessor ID.

---

## ⚡ Performance & Scalability Considerations
- **Database Indexing:** Indexed candidate records ensure rapid calculation across nationwide cohorts.
