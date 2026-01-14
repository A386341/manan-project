from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics  # <-- ADD THIS

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # <-- ADD THIS (Initializes /metrics endpoint)

@app.route('/')
def index():
    return "Link Service is Running"

# ... rest of your existing code ...
