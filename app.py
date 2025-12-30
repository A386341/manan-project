from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def hello():
    return f"<h1>Service {os.getenv('SERVICE_NAME')} is LIVE!</h1>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
