"""
Crime Bot - Main Entry Point
Script + Timeline JSON Export (Render-safe mode).
"""

import json
import os

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


OUTPUT_DIR = "assets/output"


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def main():
    print("Initializing Crime Bot...")

    loader = StoryLoader()
    approved_cases = loader.get_approved_cases()

    if not approved_cases:
        print("No approved cases found.")
        return

    ensure_output_dir()

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

            output_data = {
                "script": script,
                "timeline": timeline
            }

            output_path = os.path.join(OUTPUT_DIR, f"{script['case_id']}.json")

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2)

            print("✅ JSON export generated successfully.")
            print("Output:", output_path)

        except ValueError as e:
            print(f"❌ Validation Error: {e}")


if __name__ == "__main__":
    main()
