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
        Construct the escalation paragraph with improved narrative flow.
        """

        key_events = case.get("key_events", [])
        unresolved = case.get("unresolved_elements", [])

        escalation_parts = []

        # First key event
        if key_events:
            first_event = cls.clean_sentence(key_events[0])
            escalation_parts.append(first_event + ".")

        # Second key event (shorter emphasis)
        if len(key_events) > 1:
            second_event = cls.clean_sentence(key_events[1])
            escalation_parts.append(second_event + ".")

        # Add unresolved tension
        if unresolved:
            first_unresolved = cls.clean_sentence(unresolved[0])
            escalation_parts.append(first_unresolved + ".")

        if len(unresolved) > 1:
            second_unresolved = cls.clean_sentence(unresolved[1])
            escalation_parts.append(second_unresolved + ".")

        escalation_block = " ".join(escalation_parts)

        return escalation_block.strip()
