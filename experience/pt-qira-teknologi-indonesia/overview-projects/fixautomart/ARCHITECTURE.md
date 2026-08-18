# 🏛️ FixAutoMart Automotive E-Commerce (`fixautomart`) — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Fintech_E-Commerce_Gateway_with_Cryptographic_Midtrans_Reconciliation-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-fixautomart-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta manifest dependensi terverifikasi yang diambil langsung dari file manifest proyek (`package.json` & `composer.json`).

* **Pola Arsitektur Utama:** `Fintech E-Commerce Gateway with Cryptographic Midtrans Reconciliation`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph BuyerStorefront ["Buyer Web & Mobile Storefront (FixCore)"]
        CatalogView["Automotive Catalog & Search"]
        CartEngine["gloudemans/shoppingcart v2.6 Session Cart"]
        MidtransSnap["Midtrans Snap Checkout Modal"]
    end

    subgraph BackendCore ["FixAutoMart Core Engine (Laravel 5.5 LTS)"]
        OrderStateMachine["Order State Machine & Invoicing"]
        MidtransBridge["firmantr3/laravel-midtrans + midtrans/midtrans-php v2.3"]
        WebhookCrypto["SHA-512 Signature Hash Verifier"]
        PushDispatcher["brozot/laravel-fcm v1.3 Mobile Notification Engine"]
        BarcodeLabel["milon/barcode v6.0 Shipping Waybill Generator"]
        ImageProcessing["intervention/image v2.5 Product Optimizer"]
    end

    subgraph PaymentRail ["Midtrans Payment Infrastructure"]
        MidtransCore["Midtrans Snap / Core API (VA, QRIS, GoPay)"]
    end

    subgraph DBStore ["Database Layer"]
        MySQL_DB[(MySQL 8.0 Primary DB)]
    end

    CatalogView --> CartEngine --> OrderStateMachine
    OrderStateMachine --> MidtransBridge --> MidtransCore
    MidtransCore --> MidtransSnap
    MidtransCore --> WebhookCrypto --> OrderStateMachine --> MySQL_DB
    OrderStateMachine --> PushDispatcher
    OrderStateMachine --> BarcodeLabel
```

---

## 🔄 Lifecycle & Data Flow
1. **Cart & Checkout:** `gloudemans/shoppingcart` manages buyer cart items and calculates subtotal with tax and shipping.
2. **Payment Token Request:** `firmantr3/laravel-midtrans` calls Midtrans API to acquire a Snap payment token.
3. **Payment Settlement:** Buyer settles invoice via Bank Virtual Account, QRIS, or GoPay.
4. **Cryptographic Webhook Handshake:** Midtrans sends payment notification; backend verifies SHA-512 signature before unlocking order fulfillment and dispatching FCM notifications (`brozot/laravel-fcm`).

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Library | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | `laravel/framework` | `v5.x LTS` | Automotive E-Commerce Core Engine |
| **Payment Gateway Bridge** | `firmantr3/laravel-midtrans` | `v1.x` | Midtrans Snap & Core API Integration |
| **Shopping Cart Engine** | `gloudemans/shoppingcart` | `v2.x` | Session-Based Persistent Multi-Item Cart |
| **Push Notification** | `brozot/laravel-fcm` | `v1.x` | Automated Order & Settlement Push Alerts |
| **Shipping Label Engine** | `milon/barcode` | `v6.x` | Automated Barcode Waybill Generator |

---

## 🔒 Security & Access Control
- **SHA-512 Signature Verification:** Eliminates fake webhook payment exploits.
- **Idempotent Order Handling:** Guards against double processing during payment gateway retries.

---

## ⚡ Performance & Scalability Considerations
- **Database Transaction Locks:** ACID guarantees prevent inventory race conditions during flash sales.
