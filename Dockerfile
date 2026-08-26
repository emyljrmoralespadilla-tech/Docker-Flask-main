FROM python:3.12-slim

WORKDIR /app

# Actualizar paquetes del sistema operativo para corregir fallos reportados por Trivy
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050
CMD ["python", "sample_app.py"]