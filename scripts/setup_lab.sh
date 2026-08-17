#!/bin/bash
# One-command setup for the Skills Network Labs cloud environment.
# Usage: bash scripts/setup_lab.sh
set -e
pip install --quiet requests flask pylint
echo "Dependencies installed."
echo "Starting the Emotion Detector server..."
python EmotionDetection/server.py