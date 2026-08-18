# 🏛️ E-Budgeting Regional Government Core (`e-budgeting`) — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-High-Volume_Municipal_Financial_Approval_Platform_with_Oracle_DataTables-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-e-budgeting-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta manifest dependensi terverifikasi yang diambil langsung dari file manifest proyek (`package.json` & `composer.json`).

* **Pola Arsitektur Utama:** `High-Volume Municipal Financial Approval Platform with Oracle DataTables`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph BudgetAdmin ["Government Agency / SKPD Users"]
        BudgetEntry["Budget Line Item Entry & Expense Mapping"]
        SignOffModal["Official Document Sign-off & Verification"]
    end

    subgraph EBudgetingCore ["E-Budgeting Core (Laravel 5.4 + PHP >=5.6.4)"]
        YajraEngine["yajra/laravel-datatables-oracle Large Dataset Grid (>50k Rows)"]
        EntrustRBAC["zizaco/entrust v5.2 Hierarchical Approval Roles"]
        QRValidator["simplesoftwareio/simple-qrcode Digital Signatures"]
        FormBuilder["laravelcollective/html v5.4 Dynamic Form Generator"]
        DebugMonitor["barryvdh/laravel-debugbar Performance Profiler"]
    end

    subgraph MunicipalDB ["Municipal Database Layer"]
        MySQL_DB[(MySQL 8.0 / Oracle Financial Data Store)]
    end

    BudgetEntry --> FormBuilder --> YajraEngine --> MySQL_DB
    SignOffModal --> EntrustRBAC --> QRValidator --> MySQL_DB
```

---

## 🔄 Lifecycle & Data Flow
1. **Budget Line Input:** SKPD operators input detailed municipal budget allocations.
2. **High-Performance Grid Rendering:** `yajra/laravel-datatables-oracle` performs server-side queries on datasets exceeding 50,000 budget items.
3. **Tiered Approval Workflow:** `zizaco/entrust` validates approval hierarchy from Staff, Head of Subdivision, to Head of Agency.
4. **Digital Signature Verification:** `simplesoftwareio/simple-qrcode` embeds dynamic QR validation tokens on signed municipal budget receipts.

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Library | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | `laravel/framework` | `v5.x` | Municipal Budgeting Core Engine |
| **Large Dataset Tables** | `yajra/laravel-datatables-oracle` | `v8.x` | High-Performance Grid for >50k Line Items |
| **Hierarchical RBAC** | `zizaco/entrust` | `v5.x` | Government Agency Approval Hierarchy |
| **Digital Sign-off QR** | `simplesoftwareio/simple-qrcode` | `v2.x` | Dynamic QR Document Validation |

---

## 🔒 Security & Access Control
- **Entrust RBAC Hierarchy:** Enforces strict government separation of approval powers.
- **Tamper-Evident QR Hashes:** Authenticates printed budget documents against live database records.

---

## ⚡ Performance & Scalability Considerations
- **Server-Side DataTables:** Zero browser freeze when paging through massive municipal budget books.
