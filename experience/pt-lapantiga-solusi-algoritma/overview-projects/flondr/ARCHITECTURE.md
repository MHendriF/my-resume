# 🏛️ Flondr Marketplace — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-On_Demand_Marketplace_Core-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-lapantiga-solusi-algoritma-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-flondr-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini menguraikan arsitektur sistem marketplace on-demand Flondr.

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Library | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | `laravel/framework` | `v5.3.x` | On-Demand Order Dispatcher & Vendor Core |
| **Push Alerts** | `brozot/laravel-fcm` | `v1.x` | Real-time Customer & Courier Push Notifications |
| **DataTables** | `yajra/laravel-datatables-oracle` | `v5.x` | Server-Side Order History Grid |
| **Business Analytics** | `consoletvs/charts` | `v5.x` | Vendor Revenue & Order Completion Metrics |
