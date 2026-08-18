# 🏛️ FixAutoMart E-Commerce — Payment Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Fintech_E-Commerce_Gateway_with_Cryptographic_Webhook_Reconciliation-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-fixautomart-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta pertimbangan keamanan dan skalabilitas untuk **`fixautomart`**.

* **Pola Arsitektur Utama:** `Fintech E-Commerce Gateway with Cryptographic Webhook Reconciliation`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph BuyerClient ["Customer Web & Mobile Interface"]
        Storefront["FixCore Automotive Catalog UI"]
        Cart["Session-Based Shopping Cart Engine"]
        SnapUI["Midtrans Snap Modal Gateway"]
    end

    subgraph CoreBackend ["FixAutoMart Core (Laravel 5.5 LTS)"]
        OrderManager["Order Processing State Machine"]
        PaymentController["Midtrans API & Charge Requester"]
        WebhookHandler["Cryptographic Signature Webhook Validator"]
        NotificationEngine["Brozot FCM Push & Email Alert Dispatcher"]
    end

    subgraph PaymentGateway ["Midtrans Payment Infrastructure"]
        MidtransAPI["Midtrans Snap / Core API"]
        PaymentRails["Virtual Accounts / QRIS / GoPay"]
    end

    subgraph DataStore ["Database & Cache"]
        MySQL_DB[(MySQL 8.0 Transactional DB)]
    end

    Storefront --> Cart --> OrderManager
    OrderManager --> PaymentController --> MidtransAPI
    MidtransAPI --> SnapUI
    PaymentRails --> MidtransAPI --> WebhookHandler
    WebhookHandler --> OrderManager --> MySQL_DB
    OrderManager --> NotificationEngine
```

---

## 🔄 Lifecycle & Data Flow
1. **Order Checkout:** Buyer items are compiled from the shopping cart into an unpaid order record.
2. **Payment Token Request:** Backend requests a Snap token from Midtrans with order details and price breakdown.
3. **Customer Payment:** Buyer settles payment via Bank Transfer (VA), QRIS, or e-Wallet.
4. **Webhook Verification:** Midtrans calls the webhook URL; backend computes SHA-512 `hash(order_id + status_code + gross_amount + server_key)` to verify authenticity before unlocking order fulfillment.

---

## 🔒 Security & Access Control
- **SHA-512 Signature Hash Verification:** Protects against fake webhook payment injection attacks.
- **Idempotent Webhook Processing:** Prevents duplicate order fulfillment on network retries.

---

## ⚡ Performance & Scalability Considerations
- **Database Transactions:** ACID-compliant database locking guarantees inventory consistency during peak sales.
