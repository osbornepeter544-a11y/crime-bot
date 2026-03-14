"""
Peak Builder Module
Generates the core mystery peak block of the script.
"""

from typing import Dict


class PeakBuilder:
    """
    Builds the peak section focusing on the strongest unresolved element.
    """

    @staticmethod
    def clean_sentence(text: str) -> str:
        return text.strip().rstrip(".")

    @classmethod
    def build(cls, case: Dict) -> str:
        """
        Construct the peak paragraph with stronger emphasis.
        """

        unresolved = case.get("unresolved_elements", [])
        theories = case.get("known_theories", [])

        parts = []

        # Main unresolved element
        if unresolved:
            main_mystery = cls.clean_sentence(unresolved[0])
            parts.append(main_mystery + ".")

        # Add theory tension in shorter form
        if theories:
            theory = cls.clean_sentence(theories[0])
            parts.append("One theory suggests " + theory.lower() + ".")

        # Short emphasis line
        parts.append("But no definitive proof was ever found.")

        peak_block = " ".join(parts)

        return peak_block.strip()
