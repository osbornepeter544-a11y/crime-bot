"""
Peak Builder Module
Generates the core mystery peak block of the script.
"""

from typing import Dict


class PeakBuilder:

    @staticmethod
    def clean_sentence(text: str) -> str:
        return text.strip().rstrip(".")

    @classmethod
    def build(cls, case: Dict) -> str:
        unresolved = case.get("unresolved_elements", [])
        theories = case.get("known_theories", [])

        parts = []

        if unresolved:
            parts.append("To this day, the aircraft has never been recovered.")

        if theories:
            theory = cls.clean_sentence(theories[0])
            parts.append("Some believe " + theory.lower() + ".")

        parts.append("But no definitive evidence confirms any theory.")

        return " ".join(parts).strip()
