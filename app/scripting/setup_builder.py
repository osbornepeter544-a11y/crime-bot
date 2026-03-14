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

        title = case.get("title", "")
        year = case.get("year", "")
        location = case.get("location", "")
        summary = case.get("summary", "").strip()

        # Basic structured setup sentence
        intro_sentence = (
            f"In {year}, {title} occurred over {location}."
        )

        # Combine with condensed summary
        setup_block = f"{intro_sentence} {summary}"

        return setup_block.strip()
