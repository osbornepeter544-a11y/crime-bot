"""
Subtitle Timing Engine
Assigns timing to segmented subtitle lines.
"""

from typing import Dict, List


class SubtitleTimingEngine:

    BASE_WORDS_PER_SECOND = 2.7

    BLOCK_SPEED_MULTIPLIER = {
        "hook": 1.0,
        "setup": 1.1,
        "escalation": 1.0,
        "peak": 0.9,
        "ending": 0.9
    }

    @classmethod
    def estimate_duration(cls, text: str, block: str) -> float:
        word_count = len(text.split())
        base_duration = word_count / cls.BASE_WORDS_PER_SECOND

        multiplier = cls.BLOCK_SPEED_MULTIPLIER.get(block, 1.0)

        return round(base_duration * multiplier, 2)

    @classmethod
    def generate_timeline(cls, segmented_script: Dict) -> List[Dict]:
        timeline = []
        current_time = 0.0

        for block_name, lines in segmented_script.items():
            for line in lines:
                duration = cls.estimate_duration(line, block_name)

                entry = {
                    "text": line,
                    "start": round(current_time, 2),
                    "end": round(current_time + duration, 2),
                    "block": block_name
                }

                timeline.append(entry)
                current_time += duration

        return timeline
