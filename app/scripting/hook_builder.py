"""
Hook Builder Module
Generates the hook block for the script.
"""

from typing import Dict
import random


class HookBuilder:
    """
    Builds the hook section from stored hook angle options.
    """

    @staticmethod
    def build(case: Dict) -> str:
        """
        Select and return a hook from available hook angles.
        """

        hook_options = case.get("hook_angle_options", [])

        if not hook_options:
            raise ValueError("No hook angles available for this case.")

        # Select one hook randomly for now
        selected_hook = random.choice(hook_options)

        # Ensure formatting is clean
        selected_hook = selected_hook.strip()

        # Capitalize first letter properly
        selected_hook = selected_hook[0].upper() + selected_hook[1:]

        return selected_hook
