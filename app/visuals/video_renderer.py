"""
Video Renderer Module
Generates 1080x1920 vertical video with burned subtitles.
"""

from typing import List, Dict
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
import os

from app.config import VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS


class VideoRenderer:

    OUTPUT_DIR = "assets/final"

    @classmethod
    def ensure_output_dir(cls):
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

    @classmethod
    def render(cls, timeline: List[Dict], case_id: str) -> str:
        """
        Render video from subtitle timeline.
        """

        cls.ensure_output_dir()

        total_duration = timeline[-1]["end"]

        # Black background
        background = ColorClip(
            size=(VIDEO_WIDTH, VIDEO_HEIGHT),
            color=(0, 0, 0),
            duration=total_duration
        )

        clips = [background]

        for entry in timeline:
            txt = TextClip(
                entry["text"],
                fontsize=60,
                color="white",
                size=(VIDEO_WIDTH * 0.9, None),
                method="caption",
                align="center"
            ).set_position(("center", VIDEO_HEIGHT * 0.75)
            ).set_start(entry["start"]
            ).set_end(entry["end"])

            clips.append(txt)

        final = CompositeVideoClip(clips)

        output_path = os.path.join(cls.OUTPUT_DIR, f"{case_id}.mp4")

        final.write_videofile(
            output_path,
            fps=VIDEO_FPS,
            codec="libx264",
            audio=False
        )

        return output_path
