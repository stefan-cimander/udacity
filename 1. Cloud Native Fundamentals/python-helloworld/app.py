from flask import Flask, json
import logging
app = Flask(__name__)

logging.basicConfig(filename="app.log", level=logging.DEBUG, format=f"%(asctime)s, %(message)s")

@app.route("/")
def hello():
    logging.debug("/ was reached")
    return "Hello World!"

@app.route("/status")
def status():
    logging.debug("/status was reached")
    return app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json"
    );

@app.route("/metrics")
def metrics():
    logging.debug("/metrics was reached")
    return app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype="application/json"
    );

if __name__ == "__main__":
    app.run(host='0.0.0.0')
