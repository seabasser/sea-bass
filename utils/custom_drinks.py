# List of Custom drinks
CUSTOM_DRINK_LIST = ['Shots']

# Custom Drink Recipe Definitions
shots_recipe = {
    'strInstructions': 'SHOTS SHOTS SHOTS!!',
    'strMeasure1': 'Way too much',
    'strIngredient1': 'Grain alcohol'
}

# Custom Drink Definitions
shots = {
    'strDrink': 'Shots',
    'strDrinkThumb': 'not available',
    'idDrink': 'custom'
}


def add_custom_drinks(drink_list, booze):
    '''
    Add custom drinks to the list of drinks returned from cocktailDB
    '''
    if booze == "Grain Alcohol":
        drink_list['drinks'].append(shots)

    return drink_list

def add_custom_recipe(drink_name):
    '''
    Creates recipe for custom drinks
    '''
    recipe = {}

    if drink_name == 'Shots':
        recipe['drinks'] = [shots_recipe]
        return recipe

    return None
