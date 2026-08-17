"""Emotion detection module using the IBM Watson NLP EmotionPredict API.

This module exposes the emotion_detector function, which sends a statement
to the Watson NLP emotion prediction service and returns the detected
emotion scores together with the dominant emotion.
"""

import requests

from requests.exceptions import RequestException


def _empty_response():
    """Build a response with None values (invalid input or HTTP 400)."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyse):
    """Return emotion scores and the dominant emotion for the given text.

    Args:
        text_to_analyse (str): The statement to analyze.

    Returns:
        dict: Emotion scores for anger, disgust, fear, joy and sadness,
            plus a 'dominant_emotion' key. All values are None when the
            service answers with status code 400.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(
            url, json=input_json, headers=headers, timeout=10
        )
    except RequestException:
        return _empty_response()

    if response.status_code == 400:
        return _empty_response()

    emotions = response.json()["emotionPredictions"][0]["emotion"]
    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores
