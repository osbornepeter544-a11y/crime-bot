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
        Construct the setup paragraph.
        """

        year = case.get("year", "")
        location = case.get("location", "")
        summary = case.get("summary", "").strip()

        # More natural introduction structure
        intro_sentence = (
            f"In {year}, over the {location}, a historic disappearance would unfold."
        )

        setup_block = f"{intro_sentence} {summary}"

        return setup_block.strip()
