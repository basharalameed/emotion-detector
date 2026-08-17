"""Local demo server with a mocked Watson response (no internet needed).

Runs the real Flask application but replaces the Watson POST with a
deterministic mock so the web interface works fully offline. The
production code in EmotionDetection/ is untouched.

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

SAMPLES = {
    "I am so glad this happened": {
        "anger": 0.012, "disgust": 0.008, "fear": 0.012,
        "joy": 0.902, "sadness": 0.066,
    },
    "I am really mad about this": {
        "anger": 0.871, "disgust": 0.099, "fear": 0.008,
        "joy": 0.004, "sadness": 0.018,
    },
    "I feel disgusted just hearing about this": {
        "anger": 0.041, "disgust": 0.798, "fear": 0.011,
        "joy": 0.006, "sadness": 0.144,
    },
    "I am so sad about this": {
        "anger": 0.022, "disgust": 0.016, "fear": 0.019,
        "joy": 0.003, "sadness": 0.94,
    },
    "I am really afraid that this will happen": {
        "anger": 0.031, "disgust": 0.055, "fear": 0.811,
        "joy": 0.022, "sadness": 0.081,
    },
}


def fake_post(url, json=None, headers=None, timeout=None):
    """Return a fake response using the sample emotions for the text."""
    text = json["raw_document"]["text"].strip()
    emotions = SAMPLES.get(
        text,
        {"anger": 0.2, "disgust": 0.2, "fear": 0.2, "joy": 0.2, "sadness": 0.2},
    )
    response = Mock(status_code=200)
    response.json.return_value = {
        "emotionPredictions": [{"emotion": emotions}]
    }
    return response


_patcher = patch.object(module.requests, "post", side_effect=fake_post)
_patcher.start()

from EmotionDetection.server import app  # noqa: E402

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
