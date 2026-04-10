FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir ultralytics opencv-python numpy

CMD ["python", "project/main.py"]