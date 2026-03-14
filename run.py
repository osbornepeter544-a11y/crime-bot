"""
Crime Bot - Main Entry Point
Initial validation and hook generation test.
"""

from app.database.story_loader import StoryLoader
from app.database.case_validator import CaseValidator
from app.scripting.hook_builder import HookBuilder


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

            # Build Hook
            hook = HookBuilder.build(case)
            print("\n🎬 Generated Hook:")
            print(hook)

        except ValueError as e:
            print(f"❌ Case {case.get('case_id')} failed validation: {e}")


if __name__ == "__main__":
    main()
