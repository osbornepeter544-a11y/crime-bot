"""
Word Counter Module
Handles word count validation for generated scripts.
"""

import re
from app.config import MIN_WORD_COUNT, MAX_WORD_COUNT


class WordCounter:

    @staticmethod
    def count(text: str) -> int:
        """
        Count words in a text block.
        """
        words = re.findall(r"\b\w+\b", text)
        return len(words)

    @staticmethod
    def validate(word_count: int) -> None:
        """
        Validate word count against limits.
        Raises ValueError if outside allowed range.
        """
        if word_count < MIN_WORD_COUNT:
            raise ValueError(
                f"Script too short: {word_count} words (minimum {MIN_WORD_COUNT})"
            )

        if word_count > MAX_WORD_COUNT:
            raise ValueError(
                f"Script too long: {word_count} words (maximum {MAX_WORD_COUNT})"
            )
