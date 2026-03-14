"""
Crime Bot - Main Entry Point
Script + Subtitle Timeline + Narration Duration Sync Test.
"""

from app.database.story_loader import StoryLoader
from app.database.case_validator import CaseValidator
from app.scripting.hook_builder import HookBuilder
from app.scripting.setup_builder import SetupBuilder
from app.scripting.escalation_builder import EscalationBuilder
from app.scripting.peak_builder import PeakBuilder
from app.scripting.ending_builder import EndingBuilder
from app.scripting.word_counter import WordCounter
from app.scripting.script_assembler import ScriptAssembler
from app.subtitles.subtitle_segmenter import SubtitleSegmenter
from app.subtitles.subtitle_timing import SubtitleTimingEngine
from app.narration.narration_engine import NarrationEngine


def main():
    print("Initializing Crime Bot...")

    loader = StoryLoader()
    approved_cases = loader.get_approved_cases()

    if not approved_cases:
        print("No approved cases found.")
        return

    for case in approved_cases:
        try:
            CaseValidator.validate(case)

            hook = HookBuilder.build(case)
            setup = SetupBuilder.build(case)
            escalation = EscalationBuilder.build(case)
            peak = PeakBuilder.build(case)
            ending = EndingBuilder.build(case)

            script = ScriptAssembler.assemble(
                case=case,
                hook=hook,
                setup=setup,
                escalation=escalation,
                peak=peak,
                ending=ending
            )

            WordCounter.validate(script["word_count"])

            segmented = SubtitleSegmenter.segment_script(script)
            timeline = SubtitleTimingEngine.generate_timeline(segmented)

            narration = NarrationEngine.generate(script)

            subtitle_duration = timeline[-1]["end"]
            narration_duration = narration["estimated_duration"]

            print("\n✅ SCRIPT READY")
            print("Word Count:", script["word_count"])
            print("Subtitle Duration:", subtitle_duration, "seconds")
            print("Narration Estimated Duration:", narration_duration, "seconds")

            drift = abs(subtitle_duration - narration_duration)
            print("Duration Drift:", round(drift, 2), "seconds")

        except ValueError as e:
            print(f"❌ Validation Error: {e}")


if __name__ == "__main__":
    main()
