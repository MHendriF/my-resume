# 🏛️ NTMC Korlantas Polri Dashboard — Mission-Critical System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-High-Throughput_Reactive_Command_Center_with_WebSocket_Event_Bus-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-lapantiga-solusi-algoritma-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-koda-fe-utama-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta pertimbangan keamanan dan skalabilitas untuk **`koda-fe-utama`**.

* **Pola Arsitektur Utama:** `High-Throughput Reactive Command Center with WebSocket Event Bus`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph OperationalView ["Command Center Operator View (React 19.2 + Bun)"]
        RouterView["React Router v7 Config-Based Routing"]
        CCTVGrid["Multi-Channel CCTV Live Grid (HLS/WebRTC)"]
        DataTable["TanStack Table v8 Server-Side Grid (>50k Records)"]
        AlertBanner["Audio-Visual Emergency Alert Modal"]
    end

    subgraph StateAndCache ["Reactive Client State Bus"]
        TanStackQuery["TanStack Query v5 Cache & Mutation Bus"]
        PusherClient["Pusher JS WebSocket Listener (wss://)"]
        OptimisticStore["Optimistic UI Dispatcher"]
    end

    subgraph BackendCore ["NTMC Core Cluster (Laravel 12 / Reverb / Redis)"]
        API_Cluster["Load-Balanced RESTful API Gateway"]
        EventBroadcaster["Real-time Incident Event Broadcaster"]
        RedisPubSub[(Redis Pub/Sub Message Bus)]
        MySQLMaster[(MySQL Relational Data Store)]
    end

    subgraph EdgeStreams ["National Edge Streaming Network"]
        CCTVMediaServer["National CCTV Video Streaming Relays"]
    end

    PusherClient --> AlertBanner
    PusherClient --> TanStackQuery
    TanStackQuery --> DataTable
    CCTVGrid --> CCTVMediaServer
    RouterView --> API_Cluster
    EventBroadcaster --> RedisPubSub --> PusherClient
    API_Cluster --> MySQLMaster
```

---

## 🔄 Lifecycle & Data Flow
1. **Live Emergency Incident Broadcast:** When an incident occurs anywhere in Indonesia, Korlantas backend publishes an event to Redis Pub/Sub.
2. **WebSocket Broadcast:** The Pusher/Reverb server pushes the incident payload to all connected command center operators within `< 500ms`.
3. **Optimistic Cache Invalidation:** TanStack Query intercepts the event and selectively invalidates only the relevant table query keys.
4. **Data Rendering:** TanStack Table v8 performs virtualization and server-side pagination, ensuring zero UI lag even with 50,000+ records.

---

## 🔒 Security & Access Control
- **JWT + Refresh Token Protocol:** Secure token rotation stored in HttpOnly cookies.
- **Role-Based Access Control (RBAC):** Granular permissions for Operator, Supervisor, and National Administrator.
- **XSS & CSRF Protection:** Strict CSP headers and zero raw `dangerouslySetInnerHTML` usage.

---

## ⚡ Performance & Scalability Considerations
- **Virtualization:** High-density CCTV grids and tables render only viewport DOM elements.
- **Bun Runtime:** Sub-second bundling and hot-module replacement for enterprise reliability.
