# Filter and sort incoming booze by type and cheapest first

def filter_and_sort(result, drink_type):
    response = []

    if result and drink_type:
        for drink in result:
            if drink["Type"] == drink_type:
                response.append(drink)
        response.sort(key=lambda x: x["Retail Bottle Price"])  # Sort by Retail Price
        for i in response:
            i["Retail Bottle Price"] = fix_decimals(i["Retail Bottle Price"])
        return response

    for i in result:
        i["Retail Bottle Price"] = fix_decimals(i["Retail Bottle Price"])
    result.sort(key=lambda x: x["Retail Bottle Price"])  # Sort by Retail Price
    return result


def fix_decimals(value):
    """
    Fix the decimals in a value to 2 decimal places
    """
    value = format(value, '.2f')
    return value
