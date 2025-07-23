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

**TubeSpire** is not just another downloader—it's a robust, self-hosted engine engineered for elite media archiving. Forged with a focus on raw performance, absolute privacy, and a minimalist user experience, it provides a clean, powerful gateway to YouTube's media library, free from ads and trackers. This is a professional-grade tool for creators, researchers, and archivists who demand control and reliability.

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

- **🚀 UNCOMPROMISING SPEED:** Engineered for pure velocity. A lightweight Flask backend and efficient processing pipeline mean your downloads are handled with minimal overhead. No waiting. No excuses.

- **✨ RADICAL SIMPLICITY:** Power doesn't require complexity. The UI is brutally efficient and intuitive, designed to serve your needs and then get out of the way.

- **🛡️ ABSOLUTE PRIVACY:** Your operations are your own. TubeSpire's core application operates on a zero-log policy for user downloads. No user accounts, no download history. Period.

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 📸 Live Demo

A glimpse into the clean, focused, and powerful user interface of TubeSpire.

<p align="center">
  <img src="https://i.imgur.com/your-ui-preview.png" alt="TubeSpire UI Preview">
  </p>

<div align="center">
  <video width="90%" controls>
    <source src="extras/demo.mp4" type="video/mp4">
    Your browser does not support the video tag. 
  </video>
</div>

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 💎 Core Features

| Feature                   | The Arsenal                                                                                                             |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| 💿 **4K & 8K Video**      | Archive video in resolutions up to pristine 8K UHD. Your media, preserved in its highest form.                          |
| 🎵 **High-Bitrate Audio** | Rip and convert audio streams directly to high-bitrate MP3. Perfect for music, podcasts, and critical audio analysis.   |
| ⚡ **Efficient Backend**  | Built on a high-throughput Flask architecture that handles requests with ruthless efficiency for a zero-lag experience. |
| 🕶️ **Minimalist UI/UX**   | A sleek, fully responsive interface with a native dark mode that's easy on the eyes and hard on distractions.           |
| 🔒 **Zero-Log Privacy**   | With zero user tracking and no request logging in its core, TubeSpire is your secure, private media archiving vault.    |

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 🧠 Technical Architecture

TubeSpire is engineered with a clean, decoupled architecture for maximum performance and maintainability.

1.  **Frontend (Client-Side):**

    - The user interacts with a responsive UI built with semantic **HTML5** and styled with modern **CSS3**.
    - All pages inherit from a central `base.html` template, including SEO optimizations and the core layout.
    - Interactive elements are powered by lightweight, vanilla **JavaScript** for maximum performance.

2.  **Backend (Server-Side):**

    - The **Flask** application (`app.py`) serves as the central nervous system, handling all routing and business logic.
    - When a URL is submitted, the `index` route calls the `fetch_video_info` helper to retrieve metadata using **`yt-dlp`**.
    - The `process_video_formats` helper sanitizes and organizes the available streams into a user-friendly list.

3.  **Download Process:**
    - A POST request to the `/download` endpoint triggers the download.
    - The backend builds a precise `yt-dlp` command. For high-resolution video, it downloads separate video and audio streams.
    - **FFmpeg** is automatically invoked by `yt-dlp` to merge ("mux") these streams into a single, high-quality MP4 file.
    - The final file is served to the user, triggering a browser download.

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 🛠️ Technology Stack

TubeSpire is built with a stack of battle-tested, high-performance technologies.

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

Get your own instance of TubeSpire operational in minutes. For a complete guide on local setup, dependencies, and deployment, consult the **[Administrator's Guide](guide/ADMIN_GUIDE.md)**.

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>Is using this software legal?</strong></summary>
<br>
This software is a powerful tool, and you are responsible for using it ethically. It is intended for the legitimate archival of public content (e.g., your own creations, public domain media, research materials). Do not use this tool for piracy or copyright infringement. Always respect the content creators and the law.
</details>
<br>
<details>
<summary><strong>Why is FFmpeg required?</strong></summary>
<br>
Quality demands it. For most high-resolution content (1080p and above), YouTube delivers video and audio as separate streams. FFmpeg is the industry-standard tool required to merge—or "mux"—these streams into a single, flawless file. Without FFmpeg, you cannot achieve the highest quality downloads.
</details>
<br>
<details>
<summary><strong>How is this better than online downloader websites?</strong></summary>
<br>
Online sites are often filled with ads, trackers, and malware, and they typically throttle your download speeds. TubeSpire is your own private, self-hosted instance. It is faster, infinitely safer, and respects your privacy. You control the hardware and the code. It's the difference between a public payphone and an encrypted satellite phone.
</details>

<p align="right"><a href="#-table-of-contents">↑ back to top</a></p>

---

## 🤝 Contributing

This project is built for elite operators. If you have the skills to enhance the arsenal, we welcome your contributions. Please consult the **[Contributing Guide](CONTRIBUTING.md)** for mission parameters and code of conduct.

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
