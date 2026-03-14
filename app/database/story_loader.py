"""
Story Loader Module
Handles loading and filtering cases from the evergreen database.
"""

import json
from typing import List, Dict

from app.config import EVERGREEN_DB_PATH, REQUIRED_STATUS_FOR_SCRIPT


class StoryLoader:
    """
    Loads and filters evergreen cases from the JSON database.
    """

    def __init__(self):
        self.db_path = EVERGREEN_DB_PATH

    def load_all_cases(self) -> List[Dict]:
        """
        Load all cases from the JSON database.
        """
        if not self.db_path.exists():
            raise FileNotFoundError(f"Database file not found at {self.db_path}")

        with open(self.db_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("cases", [])

    def get_approved_cases(self) -> List[Dict]:
        """
        Return only cases that are approved for script generation.
        """
        all_cases = self.load_all_cases()
        return [
            case for case in all_cases
            if case.get("status") == REQUIRED_STATUS_FOR_SCRIPT
        ]

    def get_case_by_id(self, case_id: str) -> Dict:
        """
        Retrieve a specific case by case_id.
        """
        all_cases = self.load_all_cases()
        for case in all_cases:
            if case.get("case_id") == case_id:
                return case

        raise ValueError(f"Case with ID {case_id} not found.")
