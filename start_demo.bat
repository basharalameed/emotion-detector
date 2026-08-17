@echo off
chcp 65001 >nul
title Emotion Detector - Demo Server (offline)
cd /d "%~dp0"
set "PY=..\land-classification-exam\.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"
echo Starting Emotion Detector (offline demo)...
echo Open your browser at: http://127.0.0.1:5000/
echo Press Ctrl+C to stop.
echo.
"%PY%" scripts\run_demo_server.py
pause