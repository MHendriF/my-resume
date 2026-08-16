# PT Lapantiga Solusi Algoritma - Project Portfolio & Overview

## 📌 Ringkasan Perusahaan & Peran
* **Perusahaan:** PT Lapantiga Solusi Algoritma
* **Peran:** Frontend Developer / Software Engineer
* **Periode:** Jan 2019 – Present (Aktif)
* **Klien Utama:** Korps Lalu Lintas Kepolisian Negara Republik Indonesia (Korlantas Polri / NTMC)

---

## 📂 Daftar Proyek & Sistem

### 1. NTMC Dashboard Utama (`koda-fe-utama`)
* **Tipe Sistem:** Real-time Traffic Monitoring & Operational Management Dashboard (Korlantas Polri).
* **Tech Stack:** React 19, React Router v7 (config-based declarative routing), TypeScript 5.9, Tailwind CSS v4, shadcn/ui, TanStack Query v5, TanStack Table v8, Pusher JS (WebSockets), Recharts, React Hook Form, Zod v4, Bun 1.0+, Vite.
* **Fitur Utama:**
  - **Live Incident Streaming:** Integrasi WebSockets (Pusher JS) untuk alert penyiaran insiden real-time ke seluruh operator.
  - **Server-Side Data Tables:** Table arsitektur berbasis TanStack Table v8 dengan URL-synced multi-column sorting, debounce search, dan server pagination.
  - **Cascading Master Data:** Form manajemen CCTV/Channel dengan dependent dropdown (Provinsi ➔ Kota) dan validasi Zod.
  - **Idempotent Broadcast Tool:** Penyiaran pengumuman darurat nasional dengan `crypto.randomUUID` idempotency key.

### 2. NTMC Client App (`koda-fe-client`)
* **Tipe Sistem:** Client-facing & Field Operator Monitoring Web App.
* **Tech Stack:** React 19, TypeScript, Tailwind CSS v4, TanStack Query v5.

### 3. Virtual Event Platform & Enterprise CMS
* **Tipe Sistem:** High-traffic Virtual Expo, Live Polling, Interactive Streaming & Custom CMS.
* **Tech Stack:** PHP (Laravel), Node.js, Express, MySQL, MongoDB, Vanilla JS, Bootstrap, Swagger/OpenAPI.
* **Fitur Utama:**
  - Streaming portal interaktif dengan polyglot persistence (MySQL untuk ticketing, MongoDB untuk logs).
  - Standarisasi dokumentasi API (Swagger/Postman) yang mempercepat onboarding developer hingga 40%.

---

## 📈 Metrik & Dampak Utama
* **Real-time Latency:** Latensi alert operasional <500ms via WebSockets.
* **Modularity:** Pola arsitektur 3-file feature structure (`index.tsx`, `columns.tsx`, `form-dialog.tsx`) memangkas waktu dev fitur baru sebesar 50%.
* **Type Safety:** 100% type-safe strict mode tanpa `any` di seluruh layer API dan form.
