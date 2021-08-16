import json

from flask import Flask
from app.db.fb import Firebase

app = Flask(__name__)
firebase = Firebase()


@app.route("/ping", methods=["GET"])
def ping():
    return "PONG"


@app.route("/", methods=["GET"])
def root():
    return "lubdub"


@app.route("/booze", methods=["GET"])
def booze():
    result = firebase.fb.get('/', None)
    return json.dumps(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
