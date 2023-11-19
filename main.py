import json
import APIFunctions
import menu

# open config file with api key
with open("config.json", "r") as file:
    config = json.load(file)

# get info on mines
with open("result.json", "w") as file:
    file.write(APIFunctions.fetchLocationIds("mines", config["SODEXO_API_KEY"]))

with open("full_menu_info.json", "w", encoding="utf-8") as file:
    file.write(APIFunctions.getMenu(config["SODEXO_API_KEY"]))

with open("full_menu_info.json", 'r') as file:
    # menu = menu.read()
    fullMenuDict = json.load(file)

parsedMenu = menu.parse_menu(fullMenuDict)

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
