<div align="center">

<a href="https://github.com/KartikeyaPandey313/TubeSpire">
  <img src="https://placehold.co/1000x250/121212/6a11cb/png?text=TubeSpire&font=raleway" alt="TubeSpire Banner">
</a>

<br/>

### **A High-Performance Engine for Seamless YouTube Media Archiving.**

<p>
  <a href="https://github.com/KartikeyaPandey313/TubeSpire/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/KartikeyaPandey313/TubeSpire?style=for-the-badge&logo=github&color=1e1e1e&logoColor=white&labelColor=121212"></a>
  <img alt="Status" src="https://img.shields.io/badge/status-production_ready-brightgreen?style=for-the-badge&logo=serverless&logoColor=white&labelColor=121212">
  <img alt="Python" src="https://img.shields.io/badge/python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=121212">
  <a href="#-license"><img alt="License" src="https://img.shields.io/badge/License-Proprietary-B80F0A?style=for-the-badge&labelColor=121212"></a>
</p>
</div>

**TubeSpire** is not just another downloader—it's a robust, self-hosted engine engineered for elite media archiving. Forged with a focus on raw performance, absolute privacy, and a minimalist user experience, it provides a clean, powerful gateway to YouTube's media library, free from ads and trackers.

---

### 📚 Table of Contents
1. [**The Philosophy**](#-the-philosophy)
2. [**Live Demo**](#-live-demo)
3. [**Core Features**](#-core-features)
4. [**Technical Architecture**](#-technical-architecture)
5. [**Technology Stack**](#-technology-stack)
6. [**Deployment & Setup**](#-deployment--setup)
7. [**Frequently Asked Questions**](#-frequently-asked-questions)
8. [**Contributing**](#-contributing)
9. [**License**](#-license)

---

> _A tool forged in the fires of digital sovereignty._

## 🔥 The Philosophy

This project is built on an uncompromising foundation.

- **🚀 UNCOMPROMISING SPEED:** Engineered for pure velocity. A lightweight Flask backend and efficient processing pipeline mean your downloads are handled with minimal overhead.
- **✨ RADICAL SIMPLICITY:** Power doesn't require complexity. The UI is brutally efficient and intuitive, designed to serve your needs and then get out of the way.
- **🛡️ ABSOLUTE PRIVACY:** Your operations are your own. TubeSpire's core application operates on a zero-log policy for user downloads. No user accounts, no download history.

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 📸 Live Demo

A glimpse into the clean, focused, and powerful user interface of TubeSpire.

<p align="center">
  <img src="extras/preview_ui.png" alt="TubeSpire UI Preview" width="90%">
</p>

<div align="center">

**Watch the Video Demo**

<a href="https://tubespire.onrender.com">
  <img src="extras/Demo.mp4" alt="Watch the TubeSpire Video Demo" width="90%">
</a>

</div>

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 💎 Core Features

| Feature                 | The Arsenal                                                                                                             |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| 💿 **2K & 4K Video** | Archive video in resolutions up to pristine 4K UHD. Your media, preserved in its highest form.                          |
| 🎵 **High-Bitrate Audio** | Rip and convert audio streams directly to high-bitrate MP3. Perfect for music, podcasts, and critical audio analysis.   |
| ⚡ **Efficient Backend** | Built on a high-throughput Flask architecture that handles requests with ruthless efficiency for a zero-lag experience. |
| 🕶️ **Minimalist UI/UX** | A sleek, fully responsive interface with a native dark mode that's easy on the eyes and hard on distractions.         |
| 🔒 **Zero-Log Privacy** | With zero user tracking and no request logging, TubeSpire is your secure, private media archiving vault.                |

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 🧠 Technical Architecture

TubeSpire is engineered with a clean, decoupled architecture for maximum performance and maintainability.

1.  **Frontend:** A responsive UI built with semantic **HTML5** and modern **CSS3**, powered by lightweight, vanilla **JavaScript**.
2.  **Backend:** A **Flask** application (`app.py`) serves as the central nervous system, handling all routing and business logic.
3.  **Download Engine:** The powerful **`yt-dlp`** library retrieves metadata and media streams, while **FFmpeg** handles the merging and conversion of files into high-quality MP4s and MP3s.

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 🛠️ Technology Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=121212" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-FFFFFF?style=for-the-badge&logo=flask&logoColor=black&labelColor=121212" alt="Flask"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black&labelColor=121212" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white&labelColor=121212" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white&labelColor=121212" alt="CSS3"/>
  <br>
  <img src="https://img.shields.io/badge/yt--dlp-8A2BE2?style=for-the-badge&labelColor=121212" alt="yt-dlp"/>
  <img src="https://img.shields.io/badge/FFmpeg-007800?style=for-the-badge&logo=ffmpeg&logoColor=white&labelColor=121212" alt="FFmpeg"/>
  <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white&labelColor=121212" alt="Gunicorn"/>
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white&labelColor=121212" alt="GitHub Actions"/>
</p>

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 🚀 Deployment & Setup
For a complete guide on local setup, dependencies, and deployment, consult the **[Administrator's Guide](guide/ADMIN_GUIDE.md)**.

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>Is using this software legal?</strong></summary>
<br>
This software is a tool, and you are responsible for using it ethically. It is intended for the legitimate archival of public content (e.g., your own creations, public domain media). Do not use this tool for piracy or copyright infringement.
</details>
<br>
<details>
<summary><strong>Why is FFmpeg required?</strong></summary>
<br>
For high-resolution content (1080p and above), YouTube delivers video and audio as separate streams. FFmpeg is the industry-standard tool required to merge ("mux") these streams into a single, flawless file.
</details>
<br>
<details>
<summary><strong>How is this better than online downloader websites?</strong></summary>
<br>
Online sites are often filled with ads, trackers, and malware. TubeSpire is your own private, self-hosted instance. It is faster, safer, and respects your privacy.
</details>

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 🤝 Contributing
We welcome contributions. Please consult the **[Contributing Guide](CONTRIBUTING.md)** for mission parameters and code of conduct.

<div align="center">
  <h3>Project Architect</h3>
  <a href="https://github.com/KartikeyaPandey313">
    <img src="extras/profile_picture.png" width="120" alt="Kartikeya Pandey" style="border-radius:50%; border: 2px solid #30363D;"/>
    <br/>
    <sub><b>Kartikeya Pandey</b></sub>
  </a>
</div>

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 📜 License
This project is governed by a **Proprietary License**. Access and use are granted exclusively by the author. Please review the full [LICENSE](LICENSE) file for details.

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

<div align="center">
  <em>“The best way to predict the future is to build it.”</em>
  <br>
  <strong>© 2025 TubeSpire</strong>
</div>