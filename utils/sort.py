# Filter and sort incoming booze by type and cheapest first
import json


def filter_and_sort(result, drink_type):
    response = []

    if result and drink_type:
        for drink in result:
            if drink["Type"] == drink_type:
                response.append(drink)
        response.sort(key=lambda x: x["Retail Bottle Price"])  # Sort by Retail Price
        return response

    result.sort(key=lambda x: x["Retail Bottle Price"])  # Sort by Retail Price
    return result
