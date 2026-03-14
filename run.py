"""
Crime Bot - Main Entry Point
Hook, Setup, Escalation, and Peak generation test.
"""

from app.database.story_loader import StoryLoader
from app.database.case_validator import CaseValidator
from app.scripting.hook_builder import HookBuilder
from app.scripting.setup_builder import SetupBuilder
from app.scripting.escalation_builder import EscalationBuilder
from app.scripting.peak_builder import PeakBuilder


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

            print("\n🎬 Generated Script Blocks:\n")

            print("HOOK:")
            print(hook)

            print("\nSETUP:")
            print(setup)

            print("\nESCALATION:")
            print(escalation)

            print("\nPEAK:")
            print(peak)

        except ValueError as e:
            print(f"❌ Case {case.get('case_id')} failed validation: {e}")


if __name__ == "__main__":
    main()
