FROM python:3.11-slim

RUN pip install --no-cache-dir requests flask pylint

COPY . /app
WORKDIR /app

EXPOSE 7860

CMD ["python", "scripts/run_live_hf.py"]