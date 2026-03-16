"""
Shotstack Renderer Module
Sends render request to Shotstack Sandbox.
"""

import os
import time
import requests


class ShotstackRenderer:

    BASE_URL = "https://api.shotstack.io/stage"
    HEADERS = {
        "Content-Type": "application/json",
        "x-api-key": os.getenv("SHOTSTACK_API_KEY")
    }

    @classmethod
    def render(cls, timeline, case_id, duration):

        # Convert timeline into Shotstack clip structure
        clips = []

        for entry in timeline:
            clips.append({
                "asset": {
                    "type": "text",
                    "text": entry["text"],
                    "font": {
                        "family": "Montserrat",
                        "size": 52,
                        "color": "#ffffff"
                    },
                    "alignment": "center"
                },
                "start": entry["start"],
                "length": round(entry["end"] - entry["start"], 2),
                "position": "bottom"
            })

        payload = {
            "timeline": {
                "background": "#000000",
                "tracks": [
                    {
                        "clips": clips
                    }
                ]
            },
            "output": {
                "format": "mp4",
                "resolution": "hd",
                "aspectRatio": "9:16"
            }
        }

        response = requests.post(
            f"{cls.BASE_URL}/render",
            json=payload,
            headers=cls.HEADERS
        )

        response.raise_for_status()

        render_id = response.json()["response"]["id"]

        print("Render submitted. ID:", render_id)

        # Poll for completion
        while True:
            status_response = requests.get(
                f"{cls.BASE_URL}/render/{render_id}",
                headers=cls.HEADERS
            )

            status_data = status_response.json()["response"]

            if status_data["status"] == "done":
                print("✅ Render complete.")
                return status_data["url"]

            elif status_data["status"] == "failed":
                raise Exception("Render failed.")

            print("Rendering...")
            time.sleep(3)
