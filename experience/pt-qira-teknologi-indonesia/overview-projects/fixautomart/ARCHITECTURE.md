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

### 📦 Manifest Dependensi Terverifikasi (Direct from Codebase Manifests)
| Manifest Source | Package / Library | Version Constraint | Category & Architectural Role |
| :--- | :--- | :--- | :--- |
| `package.json` (`FixCore\package.json`) | **`axios`** | `^0.17` | Dev Tool / Bundler |
| `package.json` (`FixCore\package.json`) | **`bootstrap-sass`** | `^3.3.7` | Dev Tool / Bundler |
| `package.json` (`FixCore\package.json`) | **`cross-env`** | `^5.1` | Dev Tool / Bundler |
| `package.json` (`FixCore\package.json`) | **`jquery`** | `^3.2` | Dev Tool / Bundler |
| `package.json` (`FixCore\package.json`) | **`laravel-mix`** | `^1.0` | Dev Tool / Bundler |
| `package.json` (`FixCore\package.json`) | **`lodash`** | `^4.17.4` | Dev Tool / Bundler |
| `package.json` (`FixCore\package.json`) | **`vue`** | `^2.5.7` | Dev Tool / Bundler |
| `composer.json` (`FixCore\composer.json`) | **`php`** | `>=7.0.0` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`anhskohbo/no-captcha`** | `^3.2` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`brozot/laravel-fcm`** | `^1.3` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`consoletvs/charts`** | `5.*` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`doctrine/dbal`** | `^2.11` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`fideloper/proxy`** | `~3.3` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`firmantr3/laravel-midtrans`** | `^1.0` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`gloudemans/shoppingcart`** | `^2.6` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`intervention/image`** | `^2.5` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`laravel/framework`** | `5.5.*` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`laravel/tinker`** | `~1.0` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`laravelcollective/html`** | `^5.3.0` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`midtrans/midtrans-php`** | `^2.3` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`milon/barcode`** | `6.0` | Backend Framework Component |
| `composer.json` (`FixCore\composer.json`) | **`barryvdh/laravel-debugbar`** | `^3.3` | Dev / Testing Tool |
| `composer.json` (`FixCore\composer.json`) | **`filp/whoops`** | `~2.0` | Dev / Testing Tool |
| `composer.json` (`FixCore\composer.json`) | **`fzaninotto/faker`** | `~1.4` | Dev / Testing Tool |
| `composer.json` (`FixCore\composer.json`) | **`mockery/mockery`** | `~1.0` | Dev / Testing Tool |
| `composer.json` (`FixCore\composer.json`) | **`phpunit/phpunit`** | `~6.0` | Dev / Testing Tool |
| `composer.json` (`FixCore\composer.json`) | **`symfony/thanks`** | `^1.0` | Dev / Testing Tool |

---

## 🔒 Security & Access Control
- **SHA-512 Signature Verification:** Eliminates fake webhook payment exploits.
- **Idempotent Order Handling:** Guards against double processing during payment gateway retries.

---

## ⚡ Performance & Scalability Considerations
- **Database Transaction Locks:** ACID guarantees prevent inventory race conditions during flash sales.
