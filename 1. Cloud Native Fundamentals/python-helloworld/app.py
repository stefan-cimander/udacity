from flask import Flask, json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    return app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype = "application/json"
    );

@app.route("/metrics")
def metrics():
    return app.response_class(
        response = json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status = 200,
        mimetype = "application/json"
    );

if __name__ == "__main__":
    app.run(host='0.0.0.0')
