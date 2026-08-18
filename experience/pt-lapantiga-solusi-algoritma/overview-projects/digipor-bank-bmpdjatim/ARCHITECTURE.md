# 🏛️ Digipor Bank BMPD Jatim — Architecture

[![Architecture Pattern](https://img.shields.io/badge/Pattern-OAuth2_Health_Sync_&_Automated_Document_Generation_Architecture-blue?style=for-the-badge)](#)
[![Company](https://img.shields.io/badge/Company-pt-lapantiga-solusi-algoritma-purple?style=for-the-badge)](#)
[![Project](https://img.shields.io/badge/Project-digipor-bank-bmpdjatim-green?style=for-the-badge)](#)

---

## 📌 Executive Architecture Summary
Dokumen ini memaparkan cetak biru arsitektur teknis (*system design blueprint*), pemisahan tanggung jawab komponen (*separation of concerns*), alur transmisi data (*data lifecycle*), serta pertimbangan keamanan dan skalabilitas untuk **`digipor-bank-bmpdjatim`**.

* **Pola Arsitektur Utama:** `OAuth2 Health Sync & Automated Document Generation Architecture`
* **Fokus Rekayasa:** Keandalan sistem, latensi rendah, integritas data, dan keamanan transaksi.

---

## 🏛️ System Architecture Diagram

```mermaid
flowchart TD
    subgraph UserMobile ["Athlete / Bank Employee Client"]
        StravaApp["Strava Mobile App (GPS Tracker)"]
        WebPortal["Digipor Web Dashboard (Blade + jQuery)"]
    end

    subgraph LaravelApp ["Digipor Engine (Laravel 8.0)"]
        OAuthHandler["Strava OAuth2 Token Controller"]
        ActivitySync["Activity Ingestion & Filter Engine"]
        LeaderboardEngine["Real-time Category Leaderboard Calculator"]
        CertGenerator["Barryvdh DomPDF Certificate Engine"]
    end

    subgraph ExternalServices ["External Endpoints & Stores"]
        StravaAPI["Strava v3 Athlete API"]
        MySQL[(MySQL Relational DB)]
        CertStorage[(Encrypted PDF Certificate Vault)]
    end

    StravaApp --> StravaAPI
    WebPortal --> OAuthHandler --> StravaAPI
    OAuthHandler --> ActivitySync --> MySQL
    LeaderboardEngine --> MySQL
    LeaderboardEngine --> CertGenerator --> CertStorage
```

---

## 🔄 Lifecycle & Data Flow
1. **Athlete Authorization:** Users link their personal Strava accounts via Strava OAuth2 exchange.
2. **Activity Synchronization:** Ingests distance, elevation, and duration metrics for running and cycling activities.
3. **Fair-Play Verification:** Automated validation filters out invalid speeds and non-qualifying workouts.
4. **Instant E-Certificate:** DomPDF dynamically renders verified completion certificates with unique verification hashes.

---

## 🔒 Security & Access Control
- **Encrypted Strava Tokens:** Access and refresh tokens stored with AES-256 encryption in MySQL.
- **Anti-Cheat Validation:** Algorithmic speed ceilings filter motorized activities.

---

## ⚡ Performance & Scalability Considerations
- **Batched Sync Jobs:** Chunked queue workers prevent hitting Strava API 15-minute rate limits.
