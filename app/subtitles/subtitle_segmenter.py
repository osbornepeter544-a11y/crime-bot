"""
Subtitle Segmenter Module
Splits structured script blocks into cinematic subtitle lines.
"""

import re
from typing import Dict, List


class SubtitleSegmenter:
    """
    Handles subtitle line segmentation per script block.
    """

    MAX_WORDS_PER_LINE = 6
    MIN_WORDS_PER_LINE = 3

    @staticmethod
    def split_into_sentences(text: str) -> List[str]:
        """
        Split text into sentences.
        """
        sentences = re.split(r'(?<=[.!?]) +', text.strip())
        return [s.strip() for s in sentences if s.strip()]

    @classmethod
    def split_sentence_into_lines(cls, sentence: str) -> List[str]:
        """
        Split a single sentence into cinematic subtitle lines.
        """
        words = sentence.split()
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)

            if len(current_line) >= cls.MAX_WORDS_PER_LINE:
                lines.append(" ".join(current_line))
                current_line = []

        if current_line:
            lines.append(" ".join(current_line))

        return lines

    @classmethod
    def segment_block(cls, text: str) -> List[str]:
        """
        Segment full block into subtitle lines.
        """
        sentences = cls.split_into_sentences(text)
        all_lines = []

        for sentence in sentences:
            lines = cls.split_sentence_into_lines(sentence)
            all_lines.extend(lines)

        return all_lines

    @classmethod
    def segment_script(cls, script: Dict) -> Dict:
        """
        Segment entire structured script.
        """
        segmented = {}

        for block_name, block_text in script["blocks"].items():
            segmented[block_name] = cls.segment_block(block_text)

        return segmented
