# 🏛️ QiSales Sales Force Automation (`qisales-backend`) — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Polyglot_Persistence_Architecture_with_GPS_Geo-Fencing_&_SFA_Mobile_Backend-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-qisales-backend-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta manifest dependensi terverifikasi yang diambil langsung dari file manifest proyek (`package.json` & `composer.json`).

* **Pola Arsitektur Utama:** `Polyglot Persistence Architecture with GPS Geo-Fencing & SFA Mobile Backend`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph MobileSalesApp ["Field Sales Representative Mobile App"]
        GPSCheckIn["Mobile Check-in (GPS Coordinates + Photo)"]
        OrderTaking["Field Order Taking & Stock Audit"]
    end

    subgraph SFABackendCore ["QiSales Gateway (Laravel 6.18 LTS + PHP ^7.3)"]
        GeoFence["Haversine Formula Geo-Radius Proximity Validator"]
        IndoRegion["azishapidin/indoregion v3.0 (Hierarchy: Prov/Kab/Kec/Kel)"]
        MongoDBDriver["jenssegers/mongodb v3.6.8 + mostafamaklad/laravel-permission-mongodb"]
        FCMAlerts["brozot/laravel-fcm v1.3 Target Push Notifications"]
        ExcelReport["maatwebsite/excel v3.1 Sales Route Exporter"]
        ChartsEngine["consoletvs/charts v6.* Regional Performance Analytics"]
        BackupRoutine["spatie/laravel-backup v6.16"]
    end

    subgraph DualDataStore ["Polyglot Storage Architecture"]
        MySQL_DB[(MySQL RDBMS - Master Retail Outlets, Users, Orders)]
        MongoDB_Cluster[(MongoDB NoSQL - High-Volume GPS Telemetry & Check-in Logs)]
    end

    GPSCheckIn --> GeoFence
    GeoFence --> MongoDBDriver --> MongoDB_Cluster
    OrderTaking --> IndoRegion --> MySQL_DB
    SFABackendCore --> FCMAlerts
    SFABackendCore --> ExcelReport
```

---

## 🔄 Lifecycle & Data Flow
1. **Field GPS Check-in:** Sales agent submits GPS coordinates and outlet visit photo from mobile app.
2. **Proximity Validation:** Backend verifies location against registered outlet master coordinates using the Haversine formula.
3. **Polyglot Storage:** High-volume time-series GPS trails persist directly into `jenssegers/mongodb`; sales transactions persist into MySQL.
4. **Territory Reporting:** `azishapidin/indoregion` structures sales performance across Indonesian administrative hierarchies.

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Library | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | `laravel/framework` | `v6.x LTS` | Sales Force Automation Gateway |
| **Polyglot NoSQL Logging** | `jenssegers/mongodb` | `v3.x` | High-Volume GPS Check-in & Route Telemetry |
| **Regional Hierarchy** | `azishapidin/indoregion` | `v3.x` | Indonesian Administrative Hierarchy Service |
| **Push Notifications** | `brozot/laravel-fcm` | `v1.x` | Field Route & Target Push Notifications |
| **Analytics & Reports** | `consoletvs/charts + excel` | `v6.x / v3.x` | Outlet Coverage & Territory Sales Reports |

---

## 🔒 Security & Access Control
- **Mock GPS Coordinate Filtering:** Jitter and speed validation to detect spoofed locations.
- **Role Management on MongoDB:** `mostafamaklad/laravel-permission-mongodb` enforces document-level permissions.

---

## ⚡ Performance & Scalability Considerations
- **Polyglot Separation:** Uncouples heavy telemetry logging from core financial order tables.
