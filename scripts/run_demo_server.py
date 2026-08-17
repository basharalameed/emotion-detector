"""Local demo server with a smart mocked Watson response (no internet needed).

Runs the real Flask application but replaces the Watson POST with a
keyword-based mock that detects the emotion from the statement (Arabic and
English) and returns realistic scores. The production code in
EmotionDetection/ is untouched.

Usage:
    python scripts/run_demo_server.py
"""
# pylint: disable=wrong-import-position,unused-argument
import os
import sys
from unittest.mock import Mock, patch

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import EmotionDetection.emotion_detection as module  # noqa: E402

EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]

KEYWORDS = {
    "joy": [
        "glad", "happy", "joy", "great", "love", "wonderful", "awesome",
        "سعيد", "سعيدة", "فرح", "رائع", "مبسوط", "احب", "أحب",
    ],
    "anger": [
        "mad", "angry", "anger", "hate", "rage", "furious", "annoyed",
        "غاضب", "غاضبة", "غضب", "اكره", "أكره", "مستاء", "مستاءة",
    ],
    "sadness": [
        "sad", "sorrow", "cry", "crying", "unhappy", "miserable", "upset",
        "حزين", "حزينة", "حزن", "باكي", "تعيس", "متضايق",
    ],
    "fear": [
        "afraid", "fear", "scared", "terrified", "frightened", "anxious",
        "خائف", "خايف", "خوف", "مذعور", "مرعوب", "قلق",
    ],
    "disgust": [
        "disgust", "disgusted", "repulsive", "revolting", "gross",
        "اشمئزاز", "مقرف", "مقزز", "كريه", "مقرف جدا",
    ],
}

TAIL = {
    "anger": 0.012,
    "disgust": 0.034,
    "fear": 0.021,
    "joy": 0.043,
    "sadness": 0.031,
}


def detect_emotion(text):
    """Return the detected emotion keyword for the statement, or None."""
    lowered = text.lower()
    for emotion, words in KEYWORDS.items():
        if any(word in lowered for word in words):
            return emotion
    return None


def fake_post(url, json=None, headers=None, timeout=None):
    """Return a fake Watson response with keyword-detected emotion scores."""
    text = json["raw_document"]["text"].strip()
    dominant = detect_emotion(text) or "joy"
    scores = {emotion: TAIL[emotion] for emotion in EMOTIONS}
    scores[dominant] = 0.89
    response = Mock(status_code=200)
    response.json.return_value = {
        "emotionPredictions": [{"emotion": scores}]
    }
    return response


_patcher = patch.object(module.requests, "post", side_effect=fake_post)
_patcher.start()

from EmotionDetection.server import app  # noqa: E402

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)