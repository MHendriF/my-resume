# Milei — Real-time Web3 Analytics & WebSocket Dashboard

## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** Kipley Pte. Ltd. (Singapore / Remote)
- **Peran & Tanggung Jawab:** Frontend Developer
- **Tipe Sistem:** Real-time Crypto Analytics Web App

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Menampilkan analitik dan fluktuasi pergerakan data aset kripto secara live dengan latensi nol.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Membangun dashboard Next.js dengan koneksi WebSocket aktif (`react-use-websocket`), parsing data berkecepatan tinggi, dan visualisasi grafik.

---

## 🛠️ Tech Stack & Arsitektur Lengkap
| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Framework** | `Next.js, React, TypeScript` | Implementasi arsitektural |
| **Real-Time** | `react-use-websocket, Axios` | Implementasi arsitektural |
| **Utilities** | `Moment.js, UUID, Tailwind CSS` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- Real-time WebSocket data stream listener with auto-reconnect.
- Live market metric cards & price ticker.
- Event log activity tracking.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Update data real-time < 100ms melalui WebSocket channel.**
- **Zero memory leak pada long-running dashboard session.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Developed live analytics dashboard utilizing Next.js and react-use-websocket.*
* *Engineered auto-reconnecting WebSocket handlers ensuring uninterrupted market data streams.*
* *Designed clean, responsive analytical UI components with Tailwind CSS.*
