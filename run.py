"""
Crime Bot - Main Entry Point
Full script generation with word count validation.
"""

from app.database.story_loader import StoryLoader
from app.database.case_validator import CaseValidator
from app.scripting.hook_builder import HookBuilder
from app.scripting.setup_builder import SetupBuilder
from app.scripting.escalation_builder import EscalationBuilder
from app.scripting.peak_builder import PeakBuilder
from app.scripting.ending_builder import EndingBuilder
from app.scripting.word_counter import WordCounter


def main():
    print("Initializing Crime Bot...")

    loader = StoryLoader()
    approved_cases = loader.get_approved_cases()

    if not approved_cases:
        print("No approved cases found.")
        return

    print(f"Found {len(approved_cases)} approved case(s).")

    for case in approved_cases:
        try:
            CaseValidator.validate(case)
            print(f"✅ Case {case['case_id']} is valid and ready.")

            hook = HookBuilder.build(case)
            setup = SetupBuilder.build(case)
            escalation = EscalationBuilder.build(case)
            peak = PeakBuilder.build(case)
            ending = EndingBuilder.build(case)

            full_script = " ".join([
                hook,
                setup,
                escalation,
                peak,
                ending
            ])

            word_count = WordCounter.count(full_script)

            print("\n🎬 FULL GENERATED SCRIPT:\n")
            print(full_script)
            print("\n📊 WORD COUNT:", word_count)

            # Validate word count
            WordCounter.validate(word_count)
            print("✅ Word count within target range.")

        except ValueError as e:
            print(f"❌ Validation Error: {e}")


if __name__ == "__main__":
    main()
