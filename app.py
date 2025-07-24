# -*- coding: utf-8 -*-
"""
TubeSpire - A professional YouTube video and audio downloader web application.

This Flask application provides a clean, user-friendly interface for downloading
YouTube content. It is built with a focus on clean code, robustness, and
maintainability for a production environment.

Author: TubeSpire Team
Version: 1.2
"""

# --- Standard Library Imports ---
import os
import logging
from typing import Dict, Any, List, Optional

# --- Third-party Imports ---
from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    flash,
    url_for,
    redirect,
    Response,
    make_response,
)
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from dotenv import load_dotenv # Used to load environment variables from .env file

# ==============================================================================
# 1. APPLICATION CONFIGURATION
# ==============================================================================

# Load environment variables from a .env file for local development.
# This must be called before the Config class is defined.
load_dotenv()

class Config:
    """Configuration class for the Flask application."""
    # Secret key for session management (e.g., flash messages).
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key-for-dev")
    # The folder where downloaded files will be temporarily stored.
    DOWNLOAD_FOLDER = "downloads"
    # Load the proxy URL from the environment. It will be None if not set.
    PROXY_URL = os.environ.get("PROXY_URL")


# Initialize the Flask application
app = Flask(__name__)
# Load configuration from the Config class
app.config.from_object(Config)

# Configure professional logging to track application events.
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Log a message indicating whether a proxy is being used.
if app.config["PROXY_URL"]:
    app.logger.info(f"Proxy is configured. All download requests will be routed through the proxy server.")
else:
    app.logger.info("No proxy server is configured. Using direct connection.")

# Ensure the download directory exists on application startup.
try:
    os.makedirs(app.config["DOWNLOAD_FOLDER"], exist_ok=True)
except OSError as e:
    app.logger.critical(f"FATAL: Could not create download folder. Error: {e}")

# ==============================================================================
# 2. SECURITY HEADERS
# ==============================================================================

@app.after_request
def apply_security_headers(response: Response) -> Response:
    """Applies a set of robust security headers to every outgoing response."""
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    csp = (
        "default-src 'self'; "
        "script-src 'self' https://www.googletagmanager.com 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
        "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
        "img-src 'self' data: https://i.ytimg.com; "
        "object-src 'none'; frame-ancestors 'none'; base-uri 'self';"
    )
    response.headers["Content-Security-Policy"] = csp
    return response


# ==============================================================================
# 3. CORE HELPER FUNCTIONS (Business Logic)
# ==============================================================================

def get_base_ydl_opts() -> Dict[str, Any]:
    """
    Constructs the base dictionary of options for yt-dlp, including the proxy if configured.
    """
    opts = {
        "quiet": True,
        "noplaylist": True,
        "ignoreerrors": True,
        "no_check_certificate": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.5",
        },
    }
    # If a PROXY_URL is set in the environment, add it to the yt-dlp options.
    if app.config["PROXY_URL"]:
        opts["proxy"] = app.config["PROXY_URL"]
        
    return opts


def fetch_video_info(url: str) -> Optional[Dict[str, Any]]:
    """Fetches comprehensive video information using yt-dlp."""
    ydl_opts = get_base_ydl_opts()
    ydl_opts["dump_single_json"] = True

    try:
        with YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
    except (DownloadError, Exception) as e:
        app.logger.error(f"Failed to fetch video info for '{url}': {e}")
        return None


def process_video_formats(video_info: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Parses video info to extract and sort clean video format options."""
    video_formats: List[Dict[str, Any]] = []
    seen_resolutions: set[int] = set()
    target_resolutions: set[int] = {4320, 2160, 1440, 1080, 720}
    resolution_labels = {4320: "8K", 2160: "4K", 1440: "2K", 1080: "FHD", 720: "HD"}

    for f in video_info.get("formats", []):
        height = f.get("height")
        if height in target_resolutions and height not in seen_resolutions:
            if (
                f.get("vcodec") != "none"
                and f.get("acodec") == "none"
                and f.get("ext") == "mp4"
            ):
                label = resolution_labels.get(height, "")
                display_resolution = f"{height}p ({label})" if label else f"{height}p"
                video_formats.append({
                    "resolution": display_resolution,
                    "format_id": f["format_id"],
                    "height": height,
                    "note": "MP4",
                })
                seen_resolutions.add(height)

    video_formats.sort(key=lambda x: -x["height"])
    return video_formats


def get_audio_formats() -> List[Dict[str, str]]:
    """Returns a predefined list of audio quality options."""
    return [
        {"quality": "320 kbps (Highest)", "bitrate": "320"},
        {"quality": "192 kbps (Standard)", "bitrate": "192"},
    ]


def sanitize_filename(title: str) -> str:
    """Removes characters from a title that are unsafe for filenames."""
    return "".join(c for c in title if c.isalnum() or c in " ._-").rstrip()


def format_duration(seconds: Optional[float]) -> str:
    """Formats seconds into a human-readable HH:MM:SS string."""
    if not isinstance(seconds, (int, float)):
        return "N/A"
    try:
        seconds = int(seconds)
        h, m, s = seconds // 3600, (seconds % 3600) // 60, seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}" if h > 0 else f"{m:02d}:{s:02d}"
    except (ValueError, TypeError):
        return "N/A"


def build_download_options(
    download_type: str, selection: str, safe_title: str
) -> Dict[str, Any]:
    """Builds the final yt-dlp options dictionary based on user selection."""
    base_opts = get_base_ydl_opts()

    if download_type == "audio":
        base_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": selection,
            }],
            "outtmpl": os.path.join(
                app.config["DOWNLOAD_FOLDER"],
                f"{safe_title} [{selection}kbps].%(ext)s",
            ),
        })
        return base_opts

    if download_type == "video":
        if "_" not in selection:
            raise ValueError("Invalid video selection format")
        format_id, res_str = selection.split("_", 1)
        base_opts.update({
            "format": f"{format_id}+bestaudio/bestvideo[height={res_str}]+bestaudio/best",
            "outtmpl": os.path.join(
                app.config["DOWNLOAD_FOLDER"], f"{safe_title} [{res_str}p].%(ext)s"
            ),
            "merge_output_format": "mp4",
        })
        return base_opts

    raise ValueError(f"Invalid download type specified: {download_type}")


# ==============================================================================
# 4. FLASK WEB ROUTES (Controllers)
# ==============================================================================

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles the main page for fetching video info."""
    if request.method == "GET":
        return render_template("index.html", video_info=None)

    video_url = request.form.get("url")
    if not video_url:
        flash("Please paste a YouTube URL to get started.")
        return redirect(url_for("index"))

    video_info = fetch_video_info(video_url)
    if not video_info:
        flash("❌ Could not retrieve video information. The URL may be invalid or the video is private.")
        return redirect(url_for("index"))

    return render_template(
        "index.html",
        video_info=video_info,
        formatted_duration=format_duration(video_info.get("duration")),
        video_formats=process_video_formats(video_info),
        audio_formats=get_audio_formats(),
    )


@app.route("/download", methods=["POST"])
def download():
    """Handles the file download logic."""
    video_url = request.form.get("video_url")
    download_type = request.form.get("type")
    selection = request.form.get("selection")

    try:
        if not all([video_url, download_type, selection]):
            flash("Invalid download request. Please select a format.")
            return redirect(url_for("index"))

        info = fetch_video_info(video_url)
        if not info:
            raise ValueError("Failed to re-verify video info before download.")

        safe_title = sanitize_filename(info.get("title", "video"))
        ydl_opts = build_download_options(download_type, selection, safe_title)

        with YoutubeDL(ydl_opts) as ydl:
            app.logger.info(f"Starting download for '{safe_title}'")
            download_info = ydl.extract_info(video_url, download=True)

            final_filename = ydl.prepare_filename(download_info)
            if not final_filename or not os.path.exists(final_filename):
                raise FileNotFoundError("Downloaded file could not be found on the server.")
            
            app.logger.info(f"Download finished. Sending file: '{os.path.basename(final_filename)}'")

        response = make_response(send_from_directory(
            os.path.dirname(final_filename),
            os.path.basename(final_filename),
            as_attachment=True,
        ))
        response.set_cookie('downloadComplete', 'true', max_age=20, path='/')
        return response

    except (DownloadError, ValueError, FileNotFoundError) as e:
        app.logger.error(f"A user-facing error occurred for '{video_url}': {e}")
        flash(f"❌ Download failed. This can happen with private or age-restricted videos. Error: {e}")
        return redirect(url_for("index"))
    except Exception as e:
        app.logger.error(f"An unexpected server error occurred for '{video_url}': {e}")
        flash("❌ An unexpected server error occurred. Please try again later.")
        return redirect(url_for("index"))


# --- Static Pages & SEO Files ---
@app.route("/terms")
def terms():
    """Renders the Terms of Service page."""
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    """Renders the Privacy Policy page."""
    return render_template("privacy.html")

@app.route("/about")
def about():
    """Renders the About Us page."""
    return render_template("about.html")


# ==============================================================================
# 5. ERROR HANDLERS
# ==============================================================================

@app.errorhandler(403)
def forbidden_error(error):
    """Handles 403 Forbidden errors."""
    return render_template("errors/403.html"), 403

@app.errorhandler(404)
def not_found_error(error):
    """Handles 404 Not Found errors."""
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Handles 500 Internal Server errors."""
    return render_template("errors/500.html"), 500


# ==============================================================================
# 6. APPLICATION LAUNCH
# ==============================================================================

if __name__ == "__main__":
    # Runs the Flask development server.
    app.run(debug=False, host="0.0.0.0")