# Like eyeing fish in a barrel!

import requests

URL = "www.thecocktaildb.com/api/json/v1/1/"

def get_drinks_by_booze(booze):
    # Gets a list of drinks from TheCocktailDB based on given type of booze

    r = requests.get(f'{URL}filter.php?i={booze}')
    r.raise_for_status()
    drink_list = r.json()
    drink_list["count"] = len(drink_list.get("drinks"))
    return drink_list

def get_recipe_by_id(id):
    # Gets the recipe for a given drink from TheCocktailDB

    r = requests.get(f'{URL}lookup.php?i={id}')
    r.raise_for_status()
    recipe = r.json()
    return recipe