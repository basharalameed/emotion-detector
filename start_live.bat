@echo off
rem Emotion Detector - Live mode (real NVIDIA AI model)
chcp 65001 >nul
cd /d %~dp0
set PY=
if exist ".venv\Scripts\python.exe" set PY=.venv\Scripts\python.exe
if "%PY%"=="" if exist "..\land-classification-exam\.venv\Scripts\python.exe" set PY=..\land-classification-exam\.venv\Scripts\python.exe
if "%PY%"=="" set PY=python
echo Starting live server (real NVIDIA AI model)...
echo Open http://127.0.0.1:5000/ in your browser
"%PY%" scripts\run_live_nv.py
pause