"""
Ending Builder Module
Generates the open-loop ending block of the script.
"""

from typing import Dict


class EndingBuilder:
    """
    Builds the final reflective open-loop ending.
    """

    @staticmethod
    def build(case: Dict) -> str:
        """
        Construct the ending paragraph with slight rhythmic padding.
        """

        open_question = case.get("open_loop_question", "").strip()

        if not open_question:
            raise ValueError("Missing open loop question in case data.")

        ending_parts = [
            "To this day, the mystery remains unsolved.",
            "No clear answers.",
            open_question
        ]

        ending_block = " ".join(ending_parts)

        return ending_block.strip()
