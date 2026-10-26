# Hall Pass 🎟️⏱️

> A lightweight, tamper-proof, bilingual (English / Spanish) classroom kiosk web application designed for high school educators. Replaces disruptive paper hall passes with a streamlined, tablet-optimized check-out system, multi-student timer tracking, and automated Google Sheets audit logging.

[![Live Demo](https://img.shields.io/badge/Demo-Live_Kiosk-38bdf8?style=for-the-badge&logo=googlechrome&logoColor=white)](https://soniran635.github.io/hall-pass/)
[![License: Proprietary](https://img.shields.io/badge/License-All_Rights_Reserved-red.svg?style=for-the-badge)](#copyright--intellectual-property)
[![Platform](https://img.shields.io/badge/Platform-iPad_|_Android_|_Fire_OS_|_Web-blueviolet?style=for-the-badge)](#recommended-hardware--lockdown)

---

## 🔒 Teacher-First Startup Security

The kiosk features an **Authorized Teacher Activation Gate**:
- When the tablet or browser loads `https://soniran635.github.io/hall-pass/`, the kiosk remains locked.
- Students cannot browse rosters, select periods, or check out until the teacher enters their PIN (default: `1234`) to activate the session.
- Once activated, the teacher can launch **Kiosk Lockdown Mode** to lock the hardware screen.
- At the end of the day or period, the teacher can tap **"Lock Session / Cerrar Kiosco"** to freeze student input again.

---

## 🌟 Key Features

- **Tablet & Touchscreen Optimized:** Designed with strict anti-zoom constraints (`font-size >= 16px`), zero tap delays (`touch-action: manipulation`), and non-selectable UI elements (`user-select: none`).
- **Fully Bilingual (EN / ES):** English and Spanish labels on all student-facing screens (Reason selection, Period selection, Name search, Overdue explanations, and Return buttons).
- **Multi-Student Live Pass Management:** Configurable concurrent pass limits (1 to 10 students out at once) with independent live timers and check-in buttons.
- **Dynamic 3-Stage Smart Timer & Overdue Gate:**
  - 🟢 **On Time:** Configurable standard countdown (default: 5 minutes).
  - 🟡 **Grace Period:** Configurable grace window (default: +90 seconds) with an amber warning badge.
  - 🔴 **Overdue (+2m Explanation):** If a student exceeds the grace period by more than 2 minutes, the app prompts for an explanation upon return (*"Long line at restroom"*, *"Spoke with staff"*, *"Nurse visit"*, or custom reason).
- **Dual-Sync Logging:**
  - **Local Persistence:** Stores timestamped history in browser storage with instant CSV export.
  - **Cloud Webhook:** Seamlessly logs departure time, return time, overdue explanations, and security events directly to Google Sheets in real-time.
- **Dynamic Period Roster Control:** Teachers can dynamically add/remove periods (1–7, 8, Advisory, Homeroom), import Excel/CSV sheets, or paste roster columns directly.

---

## 🚀 How to Launch the Live Kiosk

The application is deployed live via GitHub Pages at:
**[https://soniran635.github.io/hall-pass/](https://soniran635.github.io/hall-pass/)**

### Daily Classroom Startup:
1. Open **[https://soniran635.github.io/hall-pass/](https://soniran635.github.io/hall-pass/)** on the classroom tablet or browser.
2. Enter the Teacher PIN (**`1234`**) and click **"Unlock Class Kiosk / Activar Kiosco"**.
3. (Optional) In the Teacher Area, tap **"🔒 LAUNCH KIOSK LOCKDOWN MODE"** to enter full-screen mode.
4. Place the tablet on the stand for student check-outs.

---

## 📱 Hardware & Kiosk Lockdown

| Platform | Recommended Device | Recommended Lockdown Method |
| :--- | :--- | :--- |
| **Amazon Fire OS** | Amazon Fire HD 8 / 10 | **Fully Kiosk Browser** (Sets start URL, disables status bar, home, and back buttons behind PIN) |
| **iOS / iPadOS** | iPad (9th Gen or newer) | **Guided Access** (Triple-click lock with passcode protection) |
| **Android** | Samsung Galaxy Tab / Lenovo | **App Pinning** (Enforces device PIN before unpinning browser) |

---

## ⚖️ Copyright & Intellectual Property

**Copyright © 2026 Sonia Rahman. All Rights Reserved.**

This software, source code, user interface design, and related documentation are the proprietary intellectual property of Sonia Rahman. 

- **No Unauthorized Distribution:** No part of this software may be copied, reproduced, modified, reverse engineered, decompiled, distributed, sublicensed, or published in any form without prior express written permission from the copyright owner.
- **Commercial Protection:** This repository is published strictly for direct classroom deployment. Any commercial reproduction, resale, or unauthorized deployment is strictly prohibited.
