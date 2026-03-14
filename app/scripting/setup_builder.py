"""
Setup Builder Module
Generates the setup block of the script.
"""

from typing import Dict


class SetupBuilder:
    """
    Builds the setup section from case core information.
    """

    @staticmethod
    def build(case: Dict) -> str:
        """
        Construct a tighter, more natural setup paragraph.
        """

        year = case.get("year", "")
        location = case.get("location", "")
        summary = case.get("summary", "").strip()

        intro_sentence = (
            f"In {year}, over the {location}, a disappearance shocked the world."
        )

        setup_block = f"{intro_sentence} {summary}"

        return setup_block.strip()
