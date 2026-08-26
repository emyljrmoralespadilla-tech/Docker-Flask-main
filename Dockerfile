FROM python:3.8-slim-buster  # Trivy: Imagen base obsoleta con vulnerabilidades
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["python", "sample_app.py"]