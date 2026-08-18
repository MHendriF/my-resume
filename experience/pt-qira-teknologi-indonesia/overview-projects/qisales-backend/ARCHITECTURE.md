# 🏛️ QiSales Sales Force Automation (SFA) — Polyglot Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Polyglot_Persistence_Architecture_with_GPS_Radius_Validation-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-qisales-backend-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta pertimbangan keamanan dan skalabilitas untuk **`qisales-backend`**.

* **Pola Arsitektur Utama:** `Polyglot Persistence Architecture with GPS Radius Validation`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph MobileApp ["Field Sales Representative Mobile App"]
        SalesAgent["Field Sales Representative (Android GPS)"]
        CheckInAction["Outlet Check-in & Geo-Stamp Action"]
    end

    subgraph SFABackend ["QiSales Engine (Laravel 6.18 LTS)"]
        GeoValidator["Haversine Formula GPS Radius Validator"]
        SalesOrderService["Sales Order & Inventory Manager"]
        IndoRegionService["Administrative Hierarchy Service (Prov/Kab/Kec)"]
    end

    subgraph PolyglotDB ["Dual-Database Storage Architecture"]
        MySQL_DB[(MySQL RDBMS - Master Outlets, Users, Orders)]
        MongoDB[(MongoDB NoSQL - High-Volume GPS Trails & Check-in Logs)]
    end

    SalesAgent --> CheckInAction --> GeoValidator
    GeoValidator --> MySQL_DB
    GeoValidator --> MongoDB
    CheckInAction --> SalesOrderService --> MySQL_DB
    SalesOrderService --> IndoRegionService
```

---

## 🔄 Lifecycle & Data Flow
1. **Field Check-in:** Sales agent taps check-in on the Android app, transmitting current GPS coordinates and device timestamp.
2. **Geo-Fence Validation:** Backend executes the Haversine formula against the registered outlet coordinates to verify physical proximity (< 100m).
3. **Polyglot Storage:** Verified transaction and order data persist in MySQL; high-volume GPS telemetry paths append to MongoDB collections without locking relational tables.
4. **Analytics Reporting:** Supervisors visualize regional sales routes and real-time outlet coverage heatmaps.

---

## 🔒 Security & Access Control
- **Mock Location Detection:** Backend timestamp and coordinate jitter analysis to prevent GPS spoofing.
- **Sanctum API Token Authentication:** Revocable device-tied API tokens.

---

## ⚡ Performance & Scalability Considerations
- **Polyglot Separation:** Isolating time-series GPS pings to MongoDB preserves MySQL throughput for financial transactions.
