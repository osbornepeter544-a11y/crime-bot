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
        Construct the peak paragraph with strong rhythmic emphasis.
        """

        unresolved = case.get("unresolved_elements", [])
        theories = case.get("known_theories", [])

        parts = []

        # Strong unresolved element
        if unresolved:
            main_mystery = cls.clean_sentence(unresolved[0])
            parts.append(main_mystery + ".")

        # Brief theory contrast
        if theories:
            theory = cls.clean_sentence(theories[0])
            parts.append("Some believe " + theory.lower() + ".")
            parts.append("Others disagree.")

        # Strong punch ending
        parts.append("But no confirmed wreckage was ever found.")

        peak_block = " ".join(parts)

        return peak_block.strip()
