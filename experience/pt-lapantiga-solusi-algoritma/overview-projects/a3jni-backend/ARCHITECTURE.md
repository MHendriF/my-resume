# 🏛️ A3 JNI Logistics Backend — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Supply_Chain_%26_Logistics_Gateway-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-lapantiga-solusi-algoritma-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-a3jni-backend-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini menguraikan cetak biru arsitektur RESTful API gateway untuk armada pengiriman logistik A3 JNI.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph DriverAndClients ["Mobile Driver & Client Portals"]
        DriverApp["Mobile Courier App"]
        AdminPortal["Logistics Admin & Fleet Dashboard"]
    end

    subgraph APIGateway ["A3 JNI Core Gateway (Laravel 8.x)"]
        SanctumAuth["Laravel Sanctum API Guard"]
        RecaptchaDefense["Google Recaptcha v3 Shield"]
        DeliveryEngine["Order Tracking & POD State Machine"]
        S3Storage["AWS S3 Media Pipeline"]
        AnalyticsService["ChartJS Performance Metrics"]
    end

    subgraph DataInfra ["Storage Layer"]
        MySQL_DB[(MySQL Relational Data Store)]
        S3Bucket[(AWS S3 POD Image Vault)]
    end

    DriverApp --> SanctumAuth --> DeliveryEngine
    AdminPortal --> RecaptchaDefense --> DeliveryEngine
    DeliveryEngine --> MySQL_DB
    DeliveryEngine --> S3Storage --> S3Bucket
    AdminPortal --> AnalyticsService --> MySQL_DB
```

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Library | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | `laravel/framework` | `v8.x` | Logistics REST API & State Machine |
| **Bot Protection** | `josiasmontag/laravel-recaptchav3` | `v1.x` | Invisible Anti-Scraping Protection |
| **Cloud Storage** | `league/flysystem-aws-s3-v3` | `v1.x` | High-Resolution POD Image Archival |
| **API Authentication** | `laravel/sanctum` | `v2.x` | Device-tied Courier Token Auth |
| **Performance Charts** | `fx3costa/laravelchartjs` | `v3.x` | Fleet On-Time Delivery Analytics |
