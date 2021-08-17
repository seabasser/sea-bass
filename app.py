import json

from flask import Flask, Response
from app.handlers.routes import configure_routes
from app.db.fb import Firebase

app = Flask(__name__)
firebase = Firebase()


configure_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
