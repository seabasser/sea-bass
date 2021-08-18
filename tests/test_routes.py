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
    assert data[0].keys() == {
        "Type",
        "Retail Bottle Price",
        "Brand Name",
        "Supplier",
        "Proof",
        "Bottle Size",
    }
    assert response.headers["Access-Control-Allow-Origin"] == "*"


def test_drinks():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/drinks?spirit=whiskey"

    response = client.get(url)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['count'] != 0
    assert len(data['drinks']) > 0
    assert data['drinks'][0].keys() == {
        "strDrink",
        "strDrinkThumb",
        "idDrink"
    }


def test_spec():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/spec?name=Damned if you do"

    response = client.get(url)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data['drinks']) > 0
    assert data['drinks'][0].keys() == {
        "idDrink",
        "strDrink",
        "strDrinkAlternate",
        "strTags",
        "strVideo",
        "strCategory",
        "strIBA",
        "strAlcoholic",
        "strGlass",
        "strInstructions",
        "strInstructionsES",
        "strInstructionsDE",
        "strInstructionsFR",
        "strInstructionsIT",
        "strInstructionsZH-HANS",
        "strInstructionsZH-HANT",
        "strDrinkThumb",
        "strIngredient1",
        "strIngredient2",
        "strIngredient3",
        "strIngredient4",
        "strIngredient5",
        "strIngredient6",
        "strIngredient7",
        "strIngredient8",
        "strIngredient9",
        "strIngredient10",
        "strIngredient11",
        "strIngredient12",
        "strIngredient13",
        "strIngredient14",
        "strIngredient15",
        "strMeasure1",
        "strMeasure2",
        "strMeasure3",
        "strMeasure4",
        "strMeasure5",
        "strMeasure6",
        "strMeasure7",
        "strMeasure8",
        "strMeasure9",
        "strMeasure10",
        "strMeasure11",
        "strMeasure12",
        "strMeasure13",
        "strMeasure14",
        "strMeasure15",
        "strImageSource",
        "strImageAttribution",
        "strCreativeCommonsConfirmed",
        "dateModified"
    }
