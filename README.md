# Emotion Detector

**Emotion Detector** is an AI-based web application that analyzes a statement
and returns the detected emotion scores (anger, disgust, fear, joy, sadness)
together with the dominant emotion, using the IBM Watson NLP
EmotionPredict service and Flask.

**كاشف المشاعر** تطبيق ويب يعتمد على الذكاء الاصطناعي يحلل النص ويعيد درجات
العواطف الخمس (الغضب، الاشمئزاز، الخوف، الفرح، الحزن) مع العاطفة السائدة،
باستخدام خدمة IBM Watson NLP وإطار Flask.

## Project Name
`Emotion Detector`

## Project Details

| Feature | Detail |
|---|---|
| Project name | Emotion Detector |
| Language | Python 3 |
| AI service | IBM Watson NLP (EmotionPredict API) |
| Web framework | Flask |
| Static analysis | pylint (10.00/10) |
| Unit tests | 6 tests, all passing |

## Project Structure

```
emotion-detector/
├── EmotionDetection/
│   ├── emotion_detection.py   # Watson NLP emotion detection function
│   ├── server.py              # Flask web server
│   ├── __init__.py            # Package import of the application module
│   ├── templates/index.html   # Web interface
│   └── static/mywebscript.js  # Front-end script
├── test_emotion_detection.py  # Unit tests
├── Task_1_repository/         # Repository details
├── Task_2_watson_app/         # Application code + test output
├── Task_3_output_format/      # Output formatting code + test output
├── Task_4_package/            # Package validation output
├── Task_5_unit_tests/         # Unit tests code + result
├── Task_6_flask_deployment/   # Server code + deployment screenshot
├── Task_7_error_handling/     # Error handling code + screenshot
├── Task_8_static_analysis/    # Static analysis code + pylint score
└── requirements.txt
```

## How to Run

```bash
pip install -r requirements.txt
python EmotionDetection/server.py
```

Then open `http://127.0.0.1:5000/` in your browser.