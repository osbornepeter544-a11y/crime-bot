"""
Case Validator Module
Ensures cases meet minimum requirements before script generation.
"""

from typing import Dict

from app.config import (
    MIN_EVERGREEN_SCORE,
    REQUIRED_STATUS_FOR_SCRIPT
)


class CaseValidator:
    """
    Validates whether a case is eligible for script generation.
    """

    REQUIRED_FIELDS = [
        "case_id",
        "title",
        "year",
        "location",
        "category",
        "summary",
        "hook_angle_options",
        "open_loop_question",
        "evergreen_score",
        "status"
    ]

    @classmethod
    def validate(cls, case: Dict) -> None:
        """
        Validate a case. Raises ValueError if invalid.
        """

        # Check required fields exist
        for field in cls.REQUIRED_FIELDS:
            if field not in case or case.get(field) in [None, "", []]:
                raise ValueError(f"Missing or empty required field: {field}")

        # Check evergreen score
        if case.get("evergreen_score", 0) < MIN_EVERGREEN_SCORE:
            raise ValueError("Case does not meet minimum evergreen score requirement.")

        # Check approval status
        if case.get("status") != REQUIRED_STATUS_FOR_SCRIPT:
            raise ValueError("Case is not approved for script generation.")
