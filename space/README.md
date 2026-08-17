---
title: Emotion Detector
emoji: 😊
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
app_port: 7860
---

# Emotion Detector

AI-based web application that analyzes a statement and returns the emotion
scores (anger, disgust, fear, joy, sadness) and the dominant emotion,
using a real Hugging Face model.

## Setup (one time)

1. Create a free Hugging Face token at https://huggingface.co/settings/tokens
   (type: Read).
2. In this Space: Settings → Variables and secrets → add `HF_TOKEN` with your
   token value.

Then open the app tab and type any English statement.
