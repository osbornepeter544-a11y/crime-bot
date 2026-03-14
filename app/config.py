"""
Crime Bot Configuration Module
Central configuration and constants for the Crime Bot system.
"""

from pathlib import Path


# =========================
# Project Base Paths
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"

EVERGREEN_DB_PATH = DATA_DIR / "evergreen_cases.json"


# =========================
# Case Status Rules
# =========================

ALLOWED_STATUSES = [
    "pending",
    "approved",
    "rejected",
    "produced"
]

REQUIRED_STATUS_FOR_SCRIPT = "approved"


# =========================
# Script Constraints
# =========================

MIN_WORD_COUNT = 135
MAX_WORD_COUNT = 165
TARGET_WORD_COUNT = 150

MIN_EVERGREEN_SCORE = 7


# =========================
# Video Output Standards
# =========================

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30
VIDEO_FORMAT = "mp4"
VIDEO_BITRATE_MBPS = 4.5


# =========================
# Audio Standards
# =========================

AUDIO_SAMPLE_RATE = 48000
AUDIO_BITRATE_KBPS = 160


# =========================
# Subtitle Style
# =========================

SUBTITLE_STYLE = "cinematic_line_by_line"
