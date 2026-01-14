from flask import Flask
import os
from flask_cors import CORS                          # <--- 1. ADD THIS
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)                                            # <--- 2. ADD THIS
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return f"<h1>Service {os.getenv('SERVICE_NAME')} is LIVE!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
