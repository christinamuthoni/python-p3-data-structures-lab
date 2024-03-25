spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        name = food["name"]
        names.append(name)
    return names
#return [food["name"] for food in spicy_foods] is a more concise way to write the function

#print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    #return [food for food in spicy_foods if food.get("heat_level", 0) > 5]
    spiciest_foods = []
    for food in spicy_foods:
        heat_level = food.get("heat_level")
        if heat_level > 5:
            spiciest_foods.append(food)
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food.get("heat_level")
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    return None
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get("heat_level", 0) > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = "🌶" * food.get("heat_level")
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
    total_level = sum(food.get("heat_level", 0) for food in spicy_foods)
    count = len(spicy_foods)
    average_level = total_level / count
    return round(average_level)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food == [
            
            {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            },
        ]
    spicy_foods.append(spicy_food)
    return spicy_foods



