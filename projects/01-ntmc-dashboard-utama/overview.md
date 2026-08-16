# NTMC Dashboard Utama (Traffic & Operational Monitoring System)

## 📌 Ringkasan Eksekutif
* **Organisasi / Klien:** Korps Lalu Lintas Kepolisian Negara Republik Indonesia (Korlantas Polri / NTMC)
* **Perusahaan:** PT Lapantiga Solusi Algoritma
* **Peran:** Frontend Developer / Software Engineer
* **Periode:** 2024 – Sekarang (Active)
* **Tipe Aplikasi:** Enterprise Single Page Application (SPA) & Real-time Operational Monitoring Dashboard

---

## 🎯 Masalah & Tujuan Proyek
NTMC Polri membutuhkan sistem terpusat untuk memantau arus lalu lintas nasional, mengelola ribuan channel kamera CCTV/IoT, memonitor status kesehatan server, dan melakukan penyiaran pengumuman darurat secara instan kepada operator di seluruh polda dan polres di Indonesia.

---

## 🛠️ Tech Stack & Arsitektur
| Komponen | Teknologi | Keterangan |
| :--- | :--- | :--- |
| **Framework UI** | React 19 + React Router v7 | Modern config-based routing declarative di `app/routes.ts` |
| **Bahasa** | TypeScript 5.9 | Strict type-safety, zero `any` policy |
| **Styling & Design System** | Tailwind CSS v4 + shadcn/ui | Design tokens semantik, tema Dark/Light (`next-themes`) |
| **State & Data Caching** | TanStack Query v5 + TanStack Table v8 | Server-side pagination, multi-column sort, query invalidation |
| **Real-Time Streaming** | Pusher JS (WebSockets) | Live alert & incident notifications broadcasting |
| **Form & Validasi** | React Hook Form + Zod v4 | Type-safe form validation, dependent dropdowns (Provinsi ➔ Kota) |
| **Visualisasi Data** | Recharts | Grafik utilisasi resource server & throughput |
| **Runtime & Tooling** | Bun 1.0+, Vite, Docker | Superfast local bundling, containerized deployment |

---

## 🚀 Fitur-Fitur Kunci yang Dibangun
1. **Real-time Incident & Alert Broadcasting:**
   * Integrasi WebSocket dengan Pusher JS dan custom React hook `usePusherEvent`.
   * Menampilkan toast notification via Sonner dan panel slide-over (Sheet) untuk update insiden lalu lintas real-time.
2. **Server-side Data Tables:**
   * Wrapper reusable `DataTable` berbasis TanStack Table v8 dengan URL-synced search, multi-field filter, debounce input, dan status badges.
3. **Cascading Master Data (Geografis & Perangkat):**
   * Form dinamis penambahan CCTV/Channel dengan dependent select (Provinsi ➔ Kota) dan validasi skema Zod.
4. **Idempotent Broadcast System:**
   * Modul compose broadcast pengumuman darurat dengan `crypto.randomUUID` sebagai idempotency key untuk mencegah pengiriman pesan ganda saat gangguan jaringan.

---

## 📈 Dampak Bisnis & Metrik Pencapaian
* **Real-time Latency:** Mengurangi delay penerimaan alert operasional dari hitungan menit menjadi sub-detik (<500ms) menggunakan WebSockets.
* **Developer Experience:** Arsitektur modular 3-file pattern (`index.tsx`, `columns.tsx`, `form-dialog.tsx`) mempercepat penambahan modul baru hingga 50%.
* **Zero Runtime Type Error:** Penerapan TypeScript strict + Zod validation di seluruh layer API dan form.
