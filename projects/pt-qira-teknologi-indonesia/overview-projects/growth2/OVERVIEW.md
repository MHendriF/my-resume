# Growth SFA & Outlet Map Geotagging System

## 📌 Ringkasan Eksekutif & Identitas Proyek
- **Perusahaan / Organisasi:** PT Qira Teknologi Indonesia
- **Peran & Tanggung Jawab:** Full Stack Developer
- **Tipe Sistem:** Outlet Mapping & Sales Performance Management System

---

## 🎯 Latar Belakang & Masalah (Problem Statement)
Manajemen memerlukan sistem pemetaan visual outlet toko ritel pada peta digital dan pemantauan kinerja sales terpadu.

## 💡 Solusi & Nilai Bisnis (Solution & Business Value)
Mengembangkan sistem admin Laravel dengan integrasi Google Maps picker, export laporan Excel otomatis (`maatwebsite/excel`), grafik LavaCharts, dan push notifikasi FCM.

---

## 🛠️ Tech Stack & Arsitektur Lengkap
| Layer / Domain | Teknologi / Library | Keterangan Arsitektural |
| :--- | :--- | :--- |
| **Backend & Admin** | `Laravel, PHP, MySQL, Laravel Elixir / Gulp` | Implementasi arsitektural |
| **Reporting & Export** | `Maatwebsite Excel, Khill LavaCharts` | Implementasi arsitektural |
| **Maps & Location** | `Google Maps Coordinate Picker, FCM Notifications (`brozot/laravel-fcm`)` | Implementasi arsitektural |
| **Styling** | `Bootstrap-SASS, Toastr, Intervention Image` | Implementasi arsitektural |

---

## 🚀 Fitur-Fitur Kunci & Rekayasa Teknis
- Interactive Map coordinate picker untuk registrasi outlet ritel baru.
- Generator laporan performa penjualan dalam format Excel spreadsheet.
- Grafik analitik pencapaian omset bulanan menggunakan LavaCharts.

---

## 📈 Metrik, Dampak & Hasil Terukur (Google XYZ Formula)
- **Memetakan ribuan titik outlet toko ritel secara presisi pada peta digital.**
- **Ekspor laporan penjualan ribuan baris data dalam format Excel dalam < 3 detik.**

---

## 🌟 Poin Resume Siap Pakai (Resume Ready Bullets)
* *Developed outlet management and visual map-tagging system using Laravel and Google Maps API.*
* *Implemented automated spreadsheet export workflows utilizing Maatwebsite Excel package.*
* *Integrated visual performance analytics with LavaCharts and automated push alerts via Firebase FCM.*
