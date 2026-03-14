"""
Crime Bot - Main Entry Point
Full pipeline: Script → Timeline → Video Render.
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
from app.visuals.video_renderer import VideoRenderer


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

            print("Rendering video...")

            output_path = VideoRenderer.render(
                timeline=timeline,
                case_id=script["case_id"]
            )

            print("✅ Video generated successfully!")
            print("Output:", output_path)

        except ValueError as e:
            print(f"❌ Validation Error: {e}")


if __name__ == "__main__":
    main()
