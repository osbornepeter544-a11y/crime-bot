"""
Escalation Builder Module
Generates the escalation block of the script.
"""

from typing import Dict


class EscalationBuilder:
    """
    Builds the escalation section from key events and unresolved elements.
    """

    @staticmethod
    def clean_sentence(text: str) -> str:
        """
        Remove trailing periods and clean formatting.
        """
        return text.strip().rstrip(".")

    @classmethod
    def build(cls, case: Dict) -> str:
        """
        Construct the escalation paragraph with stronger narrative rhythm.
        """

        key_events = case.get("key_events", [])
        unresolved = case.get("unresolved_elements", [])

        parts = []

        # First key event
        if key_events:
            first_event = cls.clean_sentence(key_events[0])
            parts.append(first_event + ".")

        # Second key event with tension shift
        if len(key_events) > 1:
            second_event = cls.clean_sentence(key_events[1])
            parts.append("But soon, " + second_event.lower() + ".")

        # First unresolved element
        if unresolved:
            first_unresolved = cls.clean_sentence(unresolved[0])
            parts.append(first_unresolved + ".")

        # Second unresolved element as emphasis line
        if len(unresolved) > 1:
            second_unresolved = cls.clean_sentence(unresolved[1])
            parts.append("And the reports only deepened the mystery.")

        escalation_block = " ".join(parts)

        return escalation_block.strip()
