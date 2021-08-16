import json

from flask import Flask, Response, request
from app.db.fb import Firebase

import barreleye

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
    return Response(response=json.dumps(result), mimetype='application/json')


@app.route("/drinks", methods=["GET"])
def drinks():
    booze = request.args.get('base')
    result = barreleye.get_drinks_by_booze(booze)
    return Response(response=result, mimetype='application/json')


@app.route("/spec", methods=["GET"])
def spec():
    drink_id = request.args.get('id')
    result = barreleye.get_recipe_by_id(drink_id)
    return Response(response=result, mimetype='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
