import json

from app.db.fb import Firebase
from utils import barreleye, sort

from flask import Response, request


firebase = Firebase()

RESPONSE_META = {
    "mimetype": "application/json",
    "headers": {
        "Access-Control-Allow-Origin": "*"
    }
}


def configure_routes(app):
    @app.route("/ping", methods=["GET"])
    def ping():
        return "PONG"

    @app.route("/", methods=["GET"])
    def root():
        return "lubdub"

    @app.route("/booze", methods=["GET"])
    def booze():
        result = firebase.fb.get("/", None)
        drink_type = request.args.get("type")
        sorted_result = sort.filter_and_sort(result, drink_type)

        if result and drink_type:
            return Response(response=json.dumps(sorted_result), **RESPONSE_META)
        elif result:
            return Response(response=json.dumps(sorted_result), **RESPONSE_META)
        else:
            print("firebase query failed")
            return Response(status=500, **RESPONSE_META)

    @app.route("/drinks", methods=["GET"])
    def drinks():
        """Get drinks based on provided spirit.

        @api {get} /drinks/   Get a drink based on spirit
        @apiName getDrinks
        @apiVersion 1.0.0
        @apiDescription Get drinks from base spirit

        @apiParam (Query) {String} spirit Base spirit of desired drinks

        @apiSuccess {int} count Number of drinks returned
        @apiSuccess {Array} drinks Array of drink dicts based on spirit
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 SUCCESS
            {
                "count": 3,
                "drinks": [
                    {
                        "strDrink": "Damned if you do",
                        "strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/ql7bmx1503565106.jpg",
                        "idDrink": "13194"
                    },
                    {
                        "strDrink": "Hot Toddy",`
                        "strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/ggx0lv1613942306.jpg",
                        "idDrink": "178345"
                    },
                    {
                        "strDrink": "Owen's Grandmother's Revenge",
                        "strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/0wt4uo1503565321.jpg",
                        "idDrink": "13200"
                    }
                ]
            }
        """
        spirit = request.args.get("spirit")
        if spirit:
            result = barreleye.get_drinks_by_booze(spirit)
            return Response(response=json.dumps(result), **RESPONSE_META)
        response = Response(response="Please supply a base spirit with ?spirit=",
                            status=400,
                            headers={"Access-Control-Allow-Origin": "*"}
                            )
        return response

    @app.route("/spec", methods=["GET"])
    def spec():
        """Get drink spec from cocktailDB drink name.

        @api {get} /spec/   Get a spec based on drink name
        @apiName getSpec
        @apiVersion 1.0.0
        @apiDescription Get drink spec by cocktailDB drink name

        @apiParam (Query) {String} name cocktailDB drink id to find spec

        @apiSuccess {Array} drinks Array of drink details based on name
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 SUCCESS
            {
                "drinks": [
                    {
                        "idDrink": "13194",
                        "strDrink": "Damned if you do",
                        "strDrinkAlternate": null,
                        "strTags": null,
                        "strVideo": null,
                        "strCategory": "Shot",
                        "strIBA": null,
                        "strAlcoholic": "Alcoholic",
                        "strGlass": "Shot glass",
                        "strInstructions": "Pour into shot glass. Put in mouth. Repeat as deemed necessary.",
                        "strInstructionsES": null,
                        "strInstructionsDE": "In das Schnapsglas gießen. In den Mund nehmen. Bei Bedarf wiederholen.",
                        "strInstructionsFR": null,
                        "strInstructionsIT": "Versare nel bicchiere da shot.\r\nVersa in bocca.",
                        "strInstructionsZH-HANS": null,
                        "strInstructionsZH-HANT": null,
                        "strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/ql7bmx1503565106.jpg",
                        "strIngredient1": "Whiskey",
                        "strIngredient2": "Hot Damn",
                        "strIngredient3": null,
                        "strIngredient4": null,
                        "strIngredient5": null,
                        "strIngredient6": null,
                        "strIngredient7": null,
                        "strIngredient8": null,
                        "strIngredient9": null,
                        "strIngredient10": null,
                        "strIngredient11": null,
                        "strIngredient12": null,
                        "strIngredient13": null,
                        "strIngredient14": null,
                        "strIngredient15": null,
                        "strMeasure1": "0.75 oz ",
                        "strMeasure2": "0.25 oz ",
                        "strMeasure3": null,
                        "strMeasure4": null,
                        "strMeasure5": null,
                        "strMeasure6": null,
                        "strMeasure7": null,
                        "strMeasure8": null,
                        "strMeasure9": null,
                        "strMeasure10": null,
                        "strMeasure11": null,
                        "strMeasure12": null,
                        "strMeasure13": null,
                        "strMeasure14": null,
                        "strMeasure15": null,
                        "strImageSource": null,
                        "strImageAttribution": null,
                        "strCreativeCommonsConfirmed": "No",
                        "dateModified": "2017-08-24 09:58:26"
                    }
                ]
            }
        """
        drink_name = request.args.get("name")
        if drink_name:
            result = barreleye.get_recipe_by_name(drink_name)
            response = Response(response=json.dumps(result), **RESPONSE_META)
            return response
        response = Response(response="Please supply a drink name with ?name=",
                            status=400,
                            headers={"Access-Control-Allow-Origin": "*"}
                            )
        return response
