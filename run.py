"""
Crime Bot - Main Entry Point
Full 5-block script generation test.
"""

from app.database.story_loader import StoryLoader
from app.database.case_validator import CaseValidator
from app.scripting.hook_builder import HookBuilder
from app.scripting.setup_builder import SetupBuilder
from app.scripting.escalation_builder import EscalationBuilder
from app.scripting.peak_builder import PeakBuilder
from app.scripting.ending_builder import EndingBuilder


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

            print("\n🎬 FULL GENERATED SCRIPT:\n")

            print(hook)
            print()
            print(setup)
            print()
            print(escalation)
            print()
            print(peak)
            print()
            print(ending)

        except ValueError as e:
            print(f"❌ Case {case.get('case_id')} failed validation: {e}")


if __name__ == "__main__":
    main()
