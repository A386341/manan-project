FROM python:3.9-slim

# Force Python to send logs straight to terminal (no buffering)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy and install requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

CMD ["python", "app.py"]
