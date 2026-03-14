"""
SRT Generator Module
Converts subtitle timeline into SRT format.
"""

from typing import List, Dict


class SRTGenerator:

    @staticmethod
    def format_time(seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)

        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

    @classmethod
    def generate(cls, timeline: List[Dict]) -> str:
        srt_lines = []

        for i, entry in enumerate(timeline, start=1):
            start = cls.format_time(entry["start"])
            end = cls.format_time(entry["end"])

            srt_lines.append(str(i))
            srt_lines.append(f"{start} --> {end}")
            srt_lines.append(entry["text"])
            srt_lines.append("")

        return "\n".join(srt_lines)
