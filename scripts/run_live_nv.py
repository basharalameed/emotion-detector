"""Live server using the NVIDIA NIM API (real AI model).

Same web interface as the assignment, but the emotion scores come from a
real LLM (meta/llama-3.3-70b-instruct) hosted by NVIDIA. No heavy local
installs - only requests + flask.

Usage:
    set NV_API_KEY=your_key   (or place it in a local .env file)
    python scripts/run_live_nv.py
"""
# pylint: disable=wrong-import-position,unused-argument,import-error
# pylint: disable=duplicate-code
import json
import os
import re
import sys
from unittest.mock import Mock, patch

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import requests  # noqa: E402

NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "meta/llama-3.3-70b-instruct"
EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]

_real_post = requests.post

SYSTEM_PROMPT = (
    "You are an emotion detection classifier. Analyze the user's statement "
    "and return ONLY a compact JSON object with five emotion scores "
    f"({', '.join(EMOTIONS)}) as floats between 0 and 1 that sum to "
    "approximately 1, plus a 'dominant_emotion' key holding the emotion "
    "with the highest score. "
    'Example: {"anger":0.05,"disgust":0.02,"fear":0.1,"joy":0.8,'
    '"sadness":0.03,"dominant_emotion":"joy"}. No explanation, no markdown.'
)


def _api_key():
    """Read the NVIDIA key from the environment or a local .env file."""
    key = os.environ.get("NV_API_KEY", "")
    if key:
        return key
    env_path = os.path.join(PROJECT_ROOT, ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as env_file:
            for line in env_file:
                if line.strip().startswith("NV_API_KEY="):
                    return line.strip().split("=", 1)[1].strip()
    return ""


def _extract_json(text):
    """Pull the first JSON object out of a model response."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in model response")
    return json.loads(match.group(0))


def analyze_real(text):
    """Call the real NVIDIA model and return the emotion score dict."""
    response = _real_post(
        NVIDIA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
            "temperature": 0.1,
            "max_tokens": 300,
        },
        headers={
            "Authorization": f"Bearer {_api_key()}",
            "Content-Type": "application/json",
        },
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()["choices"][0]["message"]["content"]
    data = _extract_json(payload)
    return {
        emotion: round(float(data.get(emotion, 0.0)), 3)
        for emotion in EMOTIONS
    }


def fake_post(url, json=None, headers=None, timeout=None):  # pylint: disable=redefined-outer-name
    """Real NVIDIA call wrapped as the app's expected response shape."""
    text = json["raw_document"]["text"].strip()
    scores = analyze_real(text)
    scores["dominant_emotion"] = max(scores, key=scores.get)
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
    print("Live mode: real scores from NVIDIA NIM API (Llama 3.3 70B).")
    app.run(
        host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False
    )
