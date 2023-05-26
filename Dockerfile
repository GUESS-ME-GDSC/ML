FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip \
  && apt-get update \
  && apt-get -y install libgl1-mesa-glx \
  && apt-get -y install libglib2.0-0 \
  && pip install --no-cache-dir -r requirements.txt
COPY ./app.py .
COPY ./structural_similarity.py .

# Run with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]