# Filter and sort incoming booze by type and cheapest first
import json

from flask import Response

def filter_and_sort(result, drink_type):
    response = []

    if result and drink_type:
        for drink in result:
            if drink["Type"] == drink_type:
                response.append(drink)
        response.sort(key=lambda x: x["Retail Bottle Price"])  # Sort by Retail Price
        return Response(response=json.dumps(response), status=200, mimetype="application/json")
    elif result:
        result.sort(key=lambda x: x["Retail Bottle Price"])  # Sort by Retail Price
        return Response(response=json.dumps(result), mimetype="application/json")
    else:
        print("firebase query failed")
        return Response(status=500)
