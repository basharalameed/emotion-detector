"""Live server using the Hugging Face Inference API (real AI model).

Same web interface as the assignment, but the emotion scores come from a
real model (j-hartmann/emotion-english-distilroberta-base) hosted by
Hugging Face. No heavy local installs - only requests + flask.

Usage:
    set HF_TOKEN=your_token
    python scripts/run_live_hf.py
"""
# pylint: disable=wrong-import-position,unused-argument
import os
import sys
from unittest.mock import Mock, patch

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import requests  # noqa: E402

HF_URL = (
    "https://api-inference.huggingface.co/models/"
    "j-hartmann/emotion-english-distilroberta-base"
)
EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]
ALL_LABELS = EMOTIONS + ["surprise", "neutral"]


def analyze_real(text):
    """Call the real Hugging Face model and return score dict."""
    token = os.environ.get("HF_TOKEN", "")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        HF_URL, json={"inputs": text}, headers=headers, timeout=45
    )
    response.raise_for_status()
    items = response.json()[0]
    scores = {item["label"]: round(item["score"], 3) for item in items}
    return {emotion: scores.get(emotion, 0.0) for emotion in EMOTIONS}


def fake_post(url, json=None, headers=None, timeout=None):
    """Real HTTP call through a Mock wrapper (same interface as the app)."""
    text = json["raw_document"]["text"].strip()
    scores = analyze_real(text)
    response = Mock(status_code=200)
    response.json.return_value = {
        "emotionPredictions": [{"emotion": scores}]
    }
    return response


import EmotionDetection.emotion_detection as module  # noqa: E402

_patcher = patch.object(module.requests, "post", side_effect=fake_post)
_patcher.start()

from EmotionDetection.server import app  # noqa: E402

if __name__ == "__main__":
    print("Live mode: real scores from Hugging Face Inference API.")
    app.run(host="127.0.0.1", port=5000, debug=False)