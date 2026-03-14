"""
FFmpeg Renderer Module
Generates 1080x1920 vertical video with burned SRT subtitles.
"""

import os
import subprocess

from app.config import VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS


class FFmpegRenderer:

    OUTPUT_DIR = "assets/final"
    SRT_DIR = "assets/subtitles"

    @classmethod
    def ensure_dirs(cls):
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)
        os.makedirs(cls.SRT_DIR, exist_ok=True)

    @classmethod
    def render(cls, case_id: str, duration: float, srt_content: str) -> str:
        cls.ensure_dirs()

        srt_path = os.path.join(cls.SRT_DIR, f"{case_id}.srt")
        output_path = os.path.join(cls.OUTPUT_DIR, f"{case_id}.mp4")

        # Write SRT file
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write(srt_content)

        # FFmpeg command
        command = [
            "ffmpeg",
            "-y",
            "-f", "lavfi",
            "-i", f"color=c=black:s={VIDEO_WIDTH}x{VIDEO_HEIGHT}:d={duration}",
            "-vf", f"subtitles={srt_path}:force_style='Fontsize=36,PrimaryColour=&HFFFFFF&,Alignment=2'",
            "-r", str(VIDEO_FPS),
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            output_path
        ]

        subprocess.run(command, check=True)

        return output_path
