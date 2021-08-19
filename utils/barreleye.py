# Like eyeing fish in a barrel!

import requests
from utils.custom_drinks import add_custom_drinks, add_custom_recipe, CUSTOM_DRINK_LIST

URL = "https://thecocktaildb.com/api/json/v1/1/"


def get_drinks_by_booze(booze):
    # Gets a list of drinks from TheCocktailDB based on given type of booze

    r = requests.get(f"{URL}filter.php?i={booze}")
    r.raise_for_status()
    drink_list = r.json()

    # Add Custom Drinks
    drink_list = add_custom_drinks(drink_list, booze)

    drink_list["count"] = len(drink_list.get("drinks"))
    return drink_list


def get_recipe_by_name(drink_name):
    # Gets the recipe for a given drink from TheCocktailDB
    if drink_name in CUSTOM_DRINK_LIST:
        recipe = add_custom_recipe(drink_name)
    else:
        r = requests.get(f"{URL}search.php?s={drink_name}")
        r.raise_for_status()
        recipe = r.json()

    return recipe
