from flask import Flask
from flask_cors import CORS                    # 1. Import the tool
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)                                      # 2. Tell Flask to allow outside requests
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return "Service is Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)         # Use 4000 for analytics service
