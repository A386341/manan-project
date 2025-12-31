from flask import Flask
import os
import requests  # Added to talk to other services
from prometheus_flask_exporter import PrometheusMetrics # Added for Monitoring

app = Flask(__name__)
metrics = PrometheusMetrics(app) # Enable metrics on /metrics

# Get service names from environment variables
SERVICE_NAME = os.getenv('SERVICE_NAME', 'Frontend')
LINK_SERVICE_URL = os.getenv('LINK_SERVICE_URL', 'http://link-service:80')
ANALYTICS_SERVICE_URL = os.getenv('ANALYTICS_SERVICE_URL', 'http://analytics-service:80')

@app.route('/')
def hello():
    # Check if other services are up
    status_summary = ""
    for name, url in [("Link Service", LINK_SERVICE_URL), ("Analytics Service", ANALYTICS_SERVICE_URL)]:
        try:
            resp = requests.get(url, timeout=2)
            if resp.status_code == 200:
                status_summary += f"<br>✅ {name} is reachable!"
            else:
                status_summary += f"<br>⚠️ {name} returned status {resp.status_code}"
        except Exception:
            status_summary += f"<br>❌ {name} is UNREACHABLE"

    return f"""
    <h1>Service {SERVICE_NAME} is LIVE!</h1>
    <p><b>Microservices Status:</b>{status_summary}</p>
    <hr>
    <p><a href='/metrics'>View Prometheus Metrics</a></p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
