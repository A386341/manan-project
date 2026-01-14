from flask import Flask
import os
from prometheus_flask_exporter import PrometheusMetrics  # Correctly imported

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # Initialized before the app runs

@app.route('/')
def hello():
    return f"<h1>Service {os.getenv('SERVICE_NAME')} is LIVE!</h1>"

if __name__ == '__main__':
    # CHANGE: Changed port from 80 to 4000 to match your docker-compose
    app.run(host='0.0.0.0', port=4000)
