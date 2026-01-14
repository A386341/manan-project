from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics  # <-- ADD THIS

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # <-- ADD THIS (Initializes /metrics endpoint)

@app.route('/')
def index():
    return "Link Service is Running"

# ... rest of your existing code ...
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return "Link Service is Running"

# --- ADD THIS AT THE VERY BOTTOM ---
if __name__ == '__main__':
    # host='0.0.0.0' allows connections from outside the container
    # port=3000 must match your docker-compose file
    app.run(host='0.0.0.0', port=3000)
