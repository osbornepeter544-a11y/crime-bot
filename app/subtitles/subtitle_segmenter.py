"""
Subtitle Segmenter Module
Cinematic segmentation with special peak handling.
"""

import re
from typing import Dict, List


class SubtitleSegmenter:

    BLOCK_WORD_LIMITS = {
        "hook": 6,
        "setup": 8,
        "escalation": 6,
        "peak": 4,
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
    def segment_peak(cls, text: str) -> List[str]:
        """
        Special cinematic handling for peak block.
        """
        sentences = cls.split_into_sentences(text)
        lines = []

        for sentence in sentences:
            # Force split at comma for dramatic pause
            if "," in sentence:
                parts = sentence.split(",", 1)
                lines.append(parts[0].strip() + ",")
                remainder = parts[1].strip()
                lines.extend(cls.split_by_word_limit(remainder, 4))
            else:
                lines.extend(cls.split_by_word_limit(sentence, 4))

        return lines

    @classmethod
    def segment_block(cls, block_name: str, text: str) -> List[str]:
        if block_name == "peak":
            return cls.segment_peak(text)

        sentences = cls.split_into_sentences(text)
        lines = []
        max_words = cls.BLOCK_WORD_LIMITS.get(block_name, 6)

        for sentence in sentences:
            lines.extend(cls.split_by_word_limit(sentence, max_words))

        return lines

    @classmethod
    def segment_script(cls, script: Dict) -> Dict:
        segmented = {}

        for block_name, block_text in script["blocks"].items():
            segmented[block_name] = cls.segment_block(block_name, block_text)

        return segmented
