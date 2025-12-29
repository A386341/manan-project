from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return "<h1>Frontend is Running on EC2!</h1>"

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=80)
