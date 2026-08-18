# 🏛️ Ezbli Marketplace Android Client — System Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-Native_Android_Marketplace_Client-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-qira-teknologi-indonesia-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-ezbli-android-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini menguraikan arsitektur native Android mobile client untuk Ezbli Marketplace.

---

### 📦 Komponen & Library Arsitektur Utama (Core Architectural Stack)
| Kategori Arsitektural | Package / Dependency | Versi Standar | Peran & Tanggung Jawab Sistem |
| :--- | :--- | :--- | :--- |
| **Android Core** | `com.android.support:appcompat-v7` | `v28.0.0` | Core Android UI Framework |
| **Custom Module** | `simplenavigationbar (Custom Library)` | `Internal` | Modular Animated Bottom Navigation Bar |
| **Responsive Layout** | `com.android.support.constraint:constraint-layout` | `v1.1.2` | High-Performance Flat UI Hierarchy |
| **Image Presentation** | `de.hdodenhof:circleimageview` | `v2.2.0` | Circular Merchant & User Avatar Rendering |
