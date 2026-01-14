# Use a lightweight Python image
FROM python:3.9-slim

# Set the directory where the app will live
WORKDIR /app

# 1. Copy the requirements file first (Best Practice for caching)
COPY requirements.txt .

# 2. Install all dependencies from the file
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of your application code
COPY . .

# Start the application
CMD ["python", "app.py"]
