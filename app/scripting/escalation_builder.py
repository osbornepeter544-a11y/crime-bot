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
    def build(case: Dict) -> str:
        """
        Construct the escalation paragraph.
        """

        key_events = case.get("key_events", [])
        unresolved = case.get("unresolved_elements", [])

        escalation_sentences = []

        # Add key events (limited for pacing)
        for event in key_events[:2]:
            escalation_sentences.append(event.strip() + ".")

        # Add unresolved tension points
        for item in unresolved[:2]:
            escalation_sentences.append(item.strip() + ".")

        escalation_block = " ".join(escalation_sentences)

        return escalation_block.strip()
