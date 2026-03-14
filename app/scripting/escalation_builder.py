"""
Escalation Builder Module
Generates the escalation block of the script.
"""

from typing import Dict


class EscalationBuilder:

    @staticmethod
    def clean_sentence(text: str) -> str:
        return text.strip().rstrip(".")

    @classmethod
    def build(cls, case: Dict) -> str:
        key_events = case.get("key_events", [])
        unresolved = case.get("unresolved_elements", [])

        parts = []

        if key_events:
            parts.append(cls.clean_sentence(key_events[0]) + ".")

        if len(key_events) > 1:
            parts.append("But soon, " + cls.clean_sentence(key_events[1]).lower() + ".")

        if len(unresolved) > 1:
            parts.append(cls.clean_sentence(unresolved[1]) + ".")

        parts.append("The search efforts revealed nothing.")

        return " ".join(parts).strip()
