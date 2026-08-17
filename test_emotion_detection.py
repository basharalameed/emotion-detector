"""Unit tests for the Emotion Detection application."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


def mock_response(status_code=200, emotions=None):
    """Build a fake requests.Response object."""
    emotions = emotions or {
        "anger": 0.5,
        "disgust": 0.1,
        "fear": 0.1,
        "joy": 0.2,
        "sadness": 0.1,
    }
    response = Mock(status_code=status_code)
    response.json.return_value = {
        "emotionPredictions": [{"emotion": emotions}]
    }
    return response


class TestEmotionDetector(unittest.TestCase):
    """Test suite for the emotion_detector function."""

    def assert_dominant_emotion(self, statement, emotions, expected):
        """Assert the dominant emotion for a mocked service response."""
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=mock_response(emotions=emotions),
        ):
            result = emotion_detector(statement)
        self.assertEqual(result["dominant_emotion"], expected)

    def test_emotion_detector_joy(self):
        """The dominant emotion should be joy for a happy statement."""
        self.assert_dominant_emotion(
            "I am glad this happened",
            {
                "anger": 0.02,
                "disgust": 0.01,
                "fear": 0.01,
                "joy": 0.93,
                "sadness": 0.03,
            },
            "joy",
        )

    def test_emotion_detector_anger(self):
        """The dominant emotion should be anger for an angry statement."""
        self.assert_dominant_emotion(
            "I am really mad about this",
            {
                "anger": 0.91,
                "disgust": 0.03,
                "fear": 0.02,
                "joy": 0.01,
                "sadness": 0.03,
            },
            "anger",
        )

    def test_emotion_detector_disgust(self):
        """The dominant emotion should be disgust for a disgusting statement."""
        self.assert_dominant_emotion(
            "I feel disgusted just hearing about this",
            {
                "anger": 0.05,
                "disgust": 0.88,
                "fear": 0.02,
                "joy": 0.01,
                "sadness": 0.04,
            },
            "disgust",
        )

    def test_emotion_detector_sadness(self):
        """The dominant emotion should be sadness for a sad statement."""
        self.assert_dominant_emotion(
            "I am so sad about this",
            {
                "anger": 0.02,
                "disgust": 0.01,
                "fear": 0.02,
                "joy": 0.01,
                "sadness": 0.94,
            },
            "sadness",
        )

    def test_emotion_detector_fear(self):
        """The dominant emotion should be fear for a fearful statement."""
        self.assert_dominant_emotion(
            "I am really afraid that this will happen",
            {
                "anger": 0.03,
                "disgust": 0.01,
                "fear": 0.89,
                "joy": 0.01,
                "sadness": 0.06,
            },
            "fear",
        )

    def test_emotion_detector_status_400(self):
        """All scores should be None when the service returns status 400."""
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=mock_response(status_code=400),
        ):
            result = emotion_detector("I am really mad about this")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])
        self.assertIsNone(result["disgust"])
        self.assertIsNone(result["fear"])
        self.assertIsNone(result["joy"])
        self.assertIsNone(result["sadness"])


if __name__ == "__main__":
    unittest.main()