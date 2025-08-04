FROM python:3.9-slim

# Gerekli paketleri yükler
RUN pip install --upgrade pip
RUN pip install cassandra-driver

WORKDIR /app

COPY . /app

CMD ["python", "cassandra_read.py"]

