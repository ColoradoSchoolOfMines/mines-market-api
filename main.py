import json
import APIFunctions


class MenuItem:
    def __init__(self, formalName, description, calories, ingredients):
        self.formalName = formalName
        self.description = description
        self.calories = calories
        self.ingredients = ingredients

# open config file with api key
with open("config.json", "r") as file:
    config = json.load(file)

# get info on mines
with open("result.json", "w") as file:
    file.write(APIFunctions.fetchLocationIds("mines", config["SODEXO_API_KEY"]))

with open("full_menu_info.json", "w", encoding="utf-8") as file:
    file.write(APIFunctions.getMenu(config["SODEXO_API_KEY"]))

menu = open("full_menu_info.json")
menu = menu.read()
fullMenuDict = json.loads(menu)

# Initialize variables
parsedMenu = {}  # dict storing Meal : {Course : Item}
course = {}  # dict storing Course: Item
item = {}  # stores item formal names
for i in range(len(fullMenuDict["Menus"][0]["OrderDays"][0]["MenuItems"])):
    try:
        time = APIFunctions.get_menu_info(fullMenuDict, i, "StartTime")
        # only get today
        if time[:10] == str(APIFunctions.datetime.date.today()):
            menuItem = fullMenuDict["Menus"][0]["OrderDays"][0]["MenuItems"][i]["BiteMenuItemSizes"][0]
            menuItem["FormalName"] = MenuItem(menuItem["FormalName"], menuItem["Description"], menuItem["Calories"], menuItem["Ingredients"])

            # create meal times
            if menuItem["Meal"] not in parsedMenu:
                # delete course dict so course names can repeat depending on meal time
                course = {}
                parsedMenu[menuItem["Meal"]] = menuItem["Meal"]
            # add course names to respective meal time
            if menuItem["Course"] not in course:
                # delete item so different menu item's can appear in each course
                item = {}
                if menuItem["Course"] == "MISCELLANEOUS":  # unneccesary course name
                    continue
                course[menuItem["Course"]] = menuItem["Course"]
            # make a list of all menu item's in a specific course
            if menuItem["FormalName"] not in item:
                item[menuItem["FormalName"].formalName] = menuItem["FormalName"]
                course[menuItem["Course"]] = item
                # create parsedMenu dict
                parsedMenu[menuItem["Meal"]] = course
    except KeyError:
        pass

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
