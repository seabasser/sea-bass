import json

from flask import Flask

from app.handlers.routes import configure_routes

def test_root():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/"
    
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == b"lubdub"
    

def test_ping():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/ping"
    
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == b"PONG"
    

def test_booze():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/booze"
    
    response = client.get(url)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) > 0
    assert data[0].keys() == {"Type",
                              "Retail Bottle Price",
                              "Brand Name",
                              "Supplier",
                              "Proof",
                              "Bottle Size"
    }