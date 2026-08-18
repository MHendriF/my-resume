# 🏛️ ERI Helpdesk Ticketing System (`eri-helpdesk`) — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Monolithic_SPA_via_Inertia.js_2.0_with_Native_Laravel_Reverb_WebSockets-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-lapantiga-solusi-algoritma-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-eri-helpdesk-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta manifest dependensi terverifikasi yang diambil langsung dari file manifest proyek (`package.json` & `composer.json`).

* **Pola Arsitektur Utama:** `Monolithic SPA via Inertia.js 2.0 with Native Laravel Reverb WebSockets`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph InertiaClient ["Client Application (Vue 3.4 + Tailwind CSS)"]
        VueComp["Vue 3 Composition API Components"]
        CalendarView["FullCalendar (Schedule & Maintenance Planner)"]
        Quill["VueQuill (Rich Text Ticket Body & Attachments)"]
        EchoListener["laravel-echo (Reverb WebSocket Client)"]
    end

    subgraph LaravelCore ["Backend Framework (Laravel 12.0 + PHP 8.2+)"]
        InertiaAdapter["inertiajs/inertia-laravel v2.0 Protocol Bridge"]
        ReverbDaemon["laravel/reverb v1.4 Native WebSockets Server (:8080)"]
        SanctumAuth["laravel/sanctum API & Session Authenticator"]
        ImageOptimizer["intervention/image Ticket Attachment Pipeline"]
        DocGenerator["knuckleswtf/scribe OpenAPI / Swagger Docs"]
    end

    subgraph ExternalAndData ["Database & Push Notification Layer"]
        FirebaseAlerts["kreait/laravel-firebase FCM Push Alerts"]
        MySQL_DB[(MySQL 8.0 Primary DB)]
    end

    VueComp --> InertiaAdapter
    EchoListener <--> ReverbDaemon
    InertiaAdapter --> SanctumAuth --> MySQL_DB
    InertiaAdapter --> ImageOptimizer --> MySQL_DB
    InertiaAdapter --> FirebaseAlerts
```

---

## 🔄 Lifecycle & Data Flow
1. **Ticket Submission:** User drafts ticket with rich formatted text via `VueQuill` and submits through `inertiajs/inertia-laravel`.
2. **Attachment Processing:** `intervention/image` resizes and optimizes evidence screenshots before disk storage.
3. **Real-time Event Broadcast:** `laravel/reverb` broadcasts state changes on private channels to connected operators.
4. **Push Notification:** `kreait/laravel-firebase` dispatches mobile notifications to assigned field engineers.

---

### 📦 Manifest Dependensi Terverifikasi (Direct from Codebase Manifests)
| Manifest Source | Package / Library | Version Constraint | Category & Architectural Role |
| :--- | :--- | :--- | :--- |
| `package.json` (`package.json`) | **`@fullcalendar/core`** | `^6.1.15` | Production Dependency |
| `package.json` (`package.json`) | **`@fullcalendar/daygrid`** | `^6.1.15` | Production Dependency |
| `package.json` (`package.json`) | **`@fullcalendar/interaction`** | `^6.1.15` | Production Dependency |
| `package.json` (`package.json`) | **`@fullcalendar/vue3`** | `^6.1.15` | Production Dependency |
| `package.json` (`package.json`) | **`@hcaptcha/vue3-hcaptcha`** | `^1.3.0` | Production Dependency |
| `package.json` (`package.json`) | **`@railway/cli`** | `^4.6.3` | Production Dependency |
| `package.json` (`package.json`) | **`@vueup/vue-quill`** | `^1.2.0` | Production Dependency |
| `package.json` (`package.json`) | **`date-fns`** | `^4.1.0` | Production Dependency |
| `package.json` (`package.json`) | **`flowbite`** | `^3.0.0` | Production Dependency |
| `package.json` (`package.json`) | **`moment`** | `^2.30.1` | Production Dependency |
| `package.json` (`package.json`) | **`npm`** | `^11.5.2` | Production Dependency |
| `package.json` (`package.json`) | **`pdfjs-dist`** | `^5.4.54` | Production Dependency |
| `package.json` (`package.json`) | **`preline`** | `^2.7.0` | Production Dependency |
| `package.json` (`package.json`) | **`sweetalert2`** | `^11.15.10` | Production Dependency |
| `package.json` (`package.json`) | **`trix`** | `^2.1.15` | Production Dependency |
| `package.json` (`package.json`) | **`vue3-apexcharts`** | `^1.8.0` | Production Dependency |
| `package.json` (`package.json`) | **`@inertiajs/vue3`** | `^2.0.0` | Dev Tool / Bundler |
| `package.json` (`package.json`) | **`@prettier/plugin-php`** | `^0.24.0` | Dev Tool / Bundler |
| `package.json` (`package.json`) | **`@tailwindcss/forms`** | `^0.5.3` | Dev Tool / Bundler |
| `package.json` (`package.json`) | **`@vitejs/plugin-vue`** | `^5.0.0` | Dev Tool / Bundler |
| `package.json` (`package.json`) | **`autoprefixer`** | `^10.4.12` | Dev Tool / Bundler |
| `package.json` (`package.json`) | **`axios`** | `^1.7.9` | Dev Tool / Bundler |
| `package.json` (`package.json`) | **`concurrently`** | `^9.0.1` | Dev Tool / Bundler |
| `package.json` (`package.json`) | **`laravel-echo`** | `^2.1.6` | Dev Tool / Bundler |
| `composer.json` (`composer.json`) | **`php`** | `^8.2` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`illuminate/broadcasting`** | `*` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`inertiajs/inertia-laravel`** | `^2.0` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`intervention/image`** | `^3.11` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`knuckleswtf/scribe`** | `^5.2` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`kreait/laravel-firebase`** | `^6.1` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`laravel/framework`** | `^12.0` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`laravel/reverb`** | `^1.4` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`laravel/sanctum`** | `^4.0` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`laravel/tinker`** | `^2.9` | Backend Framework Component |
| `composer.json` (`composer.json`) | **`league/flysystem-aws-s3-v3`** | `^3.29` | Backend Framework Component |

---

## 🔒 Security & Access Control
- **Laravel Sanctum Authentication:** Token-based security and cookie session guard.
- **Private Channel Authorization:** Reverb validates broadcast channel access per user role.

---

## ⚡ Performance & Scalability Considerations
- **Native Reverb WebSockets:** Eliminates external pusher costs while maintaining high-concurrency socket channels.
