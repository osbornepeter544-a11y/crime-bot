"""
Hook Builder Module
Generates the hook block for the script.
"""

from typing import Dict


class HookBuilder:
    """
    Builds the hook section from stored hook angle options.
    """

    @staticmethod
    def build(case: Dict) -> str:
        """
        Select and return the strongest (longest) hook for stability.
        """

        hook_options = case.get("hook_angle_options", [])

        if not hook_options:
            raise ValueError("No hook angles available for this case.")

        # Select longest hook to stabilize word count
        selected_hook = max(hook_options, key=lambda h: len(h.split()))

        selected_hook = selected_hook.strip()
        selected_hook = selected_hook[0].upper() + selected_hook[1:]

        return selected_hook
