cat << 'EOF' > README.md
# Hall Pass 🎟️⏱️

> A lightweight, tamper-proof, bilingual (English / Spanish) classroom kiosk web application designed for high school educators. Replaces disruptive paper hall passes with a streamlined, tablet-optimized check-out system and automated Google Sheets audit logging.

[![Live Demo](https://img.shields.io/badge/Demo-Live_Kiosk-38bdf8?style=for-the-badge&logo=googlechrome&logoColor=white)](https://soniran635.github.io/hall-pass/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-iPad_|_Android_|_Fire_OS_|_Web-blueviolet?style=for-the-badge)](#recommended-hardware--lockdown)

---

## 🌟 Key Features

- **Tablet & Touchscreen Optimized:** Designed with strict anti-zoom constraints (`font-size >= 16px`), zero tap delays (`touch-action: manipulation`), and non-selectable UI elements (`user-select: none`).
- **Fully Bilingual (EN / ES):** Clear English and Spanish labels on all student-facing screens (Reason selection, Period selection, Name search, and Return buttons).
- **Dynamic 3-Stage Smart Timer:**
  - 🟢 **On Time:** Configurable standard countdown (default: 5 minutes).
  - 🟡 **Grace Period:** Configurable grace window (default: +90 seconds) with an amber warning badge.
  - 🔴 **Overdue:** Prominent pulsing red timer tracking exact minutes overdue.
- **Dual-Sync Logging:**
  - **Local Persistence:** Stores timestamped history in browser storage with instant CSV export.
  - **Cloud Webhook:** Seamlessly logs departure time, return time, total duration, and pass status to a connected Google Sheet in real-time.
- **Zero Hardcoded Data / White-Label Architecture:**
  - Teachers have complete administrative control to customize Teacher Name, Room Number, School Name, and Welcome Instructions.
  - Custom pass reasons (Bathroom, Hallway, Nurse, Guidance, etc.) with individual time limits.
  - Flexible period structures (P1–P8, Block schedules, Homeroom, Advisory).
- **Roster Management:**
  - Direct Excel (`.xlsx`, `.xls`) and `.csv` drag-and-drop file imports via SheetJS.
  - Quick copy-paste cell importer directly from Google Sheets.
  - Line-by-line in-app editing and downloadable CSV templates.
- **PIN-Protected Teacher Portal:** Administrative configuration, pass logs, roster management, and JSON backup/restore are shielded behind a customizable security PIN (default: `1234`).

---

## 🚀 Quick Start / Deployment

This app runs entirely client-side with zero external build dependencies or server hosting costs.

### 1. Host via GitHub Pages (Free)
1. Fork or clone this repository:
   ```bash
   git clone [https://github.com/soniran635/hall-pass.git](https://github.com/soniran635/hall-pass.git)
   cd hall-pass
