import json

from __init__ import fetch_location_ids, get_parsed_menu

if __name__ == "__main__":
    # open config file with api key
    with open("mines_market/config.json", "r") as file:
        config = json.load(file)

    # get info on mines
    with open("result.json", "w") as file:
        json.dump(fetch_location_ids("mines", config["SODEXO_API_KEY"]), file)

    parsedMenu = get_parsed_menu(config["SODEXO_API_KEY"], config["LOCATION_ID"])

    mealKeys = parsedMenu.keys()
    for key in mealKeys:
        print(key)
    print("\n")
    selectedMeal = input("SELECT MEALTIME> ")

    courseKeys = parsedMenu[selectedMeal].keys()
    for key in courseKeys:
        print(key)
    print("\n")
    selectedCourse = input("SELECT COURSE> ")

    itemKeys = parsedMenu[selectedMeal][selectedCourse]
    for item in itemKeys:
        print(item)
    print("\n")

    selectedItem = input("SELECT ITEM> ")

    instanceVars = vars(parsedMenu[selectedMeal][selectedCourse][selectedItem])
    for var in instanceVars:
        print(var)
    print("\n")

    selectedVar = input("SELECT INFO> ")
    temp = parsedMenu[selectedMeal][selectedCourse][selectedItem]
    if hasattr(temp, selectedVar):
        value = getattr(temp, selectedVar)
    print(value)
