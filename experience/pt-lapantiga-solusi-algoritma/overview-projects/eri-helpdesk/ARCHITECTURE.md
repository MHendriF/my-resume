# 🏛️ ERI Helpdesk System — Modern Full-Stack Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Monolithic_SPA_via_Inertia.js_2.0_with_Native_Laravel_Reverb_WebSockets-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-lapantiga-solusi-algoritma-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-eri-helpdesk-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta pertimbangan keamanan dan skalabilitas untuk **`eri-helpdesk`**.

* **Pola Arsitektur Utama:** `Monolithic SPA via Inertia.js 2.0 with Native Laravel Reverb WebSockets`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph BrowserUI ["Inertia Client View (Vue 3.4 + Tailwind CSS)"]
        VueComp["Vue 3 Composition API Components"]
        FullCalendar["FullCalendar Schedule View"]
        QuillEditor["VueQuill Rich Text Ticket Editor"]
        LiveEcho["Laravel Echo WebSocket Listener"]
    end

    subgraph MonolithCore ["Laravel 12 Enterprise Monolith"]
        InertiaAdapter["Inertia.js Protocol Adapter"]
        TicketEngine["Ticket State Machine & Assignment Service"]
        ReverbServer["Laravel Reverb Native WebSockets (Port 8080)"]
        QueueWorker["Redis Queue Background Worker"]
    end

    subgraph StorageInfra ["Data & Notification Infrastructure"]
        MySQL_DB[(MySQL 8.0 Primary DB)]
        RedisQueue[(Redis Cache & Event Bus)]
        FirebaseFCM["Firebase Cloud Messaging (Mobile Alerts)"]
    end

    VueComp --> InertiaAdapter
    LiveEcho <--> ReverbServer
    InertiaAdapter --> TicketEngine
    TicketEngine --> MySQL_DB
    TicketEngine --> QueueWorker
    QueueWorker --> FirebaseFCM
    QueueWorker --> ReverbServer
```

---

## 🔄 Lifecycle & Data Flow
1. **Ticket Creation:** Operator submits a technical ticket with rich text formatting (VueQuill) via Inertia client visit.
2. **State Machine Transition:** Laravel 12 assigns the ticket according to priority and notifies technical staff.
3. **WebSocket Event Dispatch:** Laravel Reverb dispatches a private channel broadcast without requiring external third-party services.
4. **Instant UI Reaction:** Laravel Echo catches the event on the client, updating ticket statuses and comment feeds in real time.

---

## 🔒 Security & Access Control
- **Private Channel Authorization:** Laravel Reverb enforces channel-level authorization policies.
- **CSRF Token Synchronization:** Automatically handled by Inertia.js on all mutating visits.

---

## ⚡ Performance & Scalability Considerations
- **Native Reverb Architecture:** Capable of handling thousands of simultaneous open socket connections on minimal server resources.
