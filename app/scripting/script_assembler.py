"""
Script Assembler Module
Combines all script blocks into a structured script object.
"""

from typing import Dict

from app.scripting.word_counter import WordCounter


class ScriptAssembler:
    """
    Assembles structured script output.
    """

    @staticmethod
    def assemble(
        case: Dict,
        hook: str,
        setup: str,
        escalation: str,
        peak: str,
        ending: str
    ) -> Dict:
        """
        Build final structured script object.
        """

        full_text = " ".join([
            hook,
            setup,
            escalation,
            peak,
            ending
        ])

        word_count = WordCounter.count(full_text)

        return {
            "case_id": case.get("case_id"),
            "title": case.get("title"),
            "blocks": {
                "hook": hook,
                "setup": setup,
                "escalation": escalation,
                "peak": peak,
                "ending": ending
            },
            "full_text": full_text,
            "word_count": word_count
        }
