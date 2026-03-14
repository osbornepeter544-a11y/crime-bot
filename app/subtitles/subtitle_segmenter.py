"""
Subtitle Segmenter Module
Improved cinematic segmentation logic.
"""

import re
from typing import Dict, List


class SubtitleSegmenter:

    BLOCK_WORD_LIMITS = {
        "hook": 6,
        "setup": 8,
        "escalation": 6,
        "peak": 5,
        "ending": 6
    }

    @staticmethod
    def split_into_sentences(text: str) -> List[str]:
        sentences = re.split(r'(?<=[.!?]) +', text.strip())
        return [s.strip() for s in sentences if s.strip()]

    @staticmethod
    def split_by_word_limit(sentence: str, max_words: int) -> List[str]:
        words = sentence.split()
        lines = []
        current = []

        for word in words:
            current.append(word)

            if len(current) >= max_words:
                lines.append(" ".join(current))
                current = []

        if current:
            lines.append(" ".join(current))

        return lines

    @classmethod
    def segment_block(cls, block_name: str, text: str) -> List[str]:
        sentences = cls.split_into_sentences(text)
        lines = []
        max_words = cls.BLOCK_WORD_LIMITS.get(block_name, 6)

        for sentence in sentences:
            split_lines = cls.split_by_word_limit(sentence, max_words)
            lines.extend(split_lines)

        return lines

    @classmethod
    def segment_script(cls, script: Dict) -> Dict:
        segmented = {}

        for block_name, block_text in script["blocks"].items():
            segmented[block_name] = cls.segment_block(block_name, block_text)

        return segmented
