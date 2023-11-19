class MenuItem:
    def __init__(self, formalName, description, calories, ingredients):
        self.formalName = formalName
        self.description = description
        self.calories = calories
        self.ingredients = ingredients


def parse_menu(fullMenuDict):
    # Initialize variables
    parsedMenu = {}  # dict storing Meal : {Course : Item}
    course = {}  # dict storing Course: Item
    item = {}  # stores item formal names
    for i in range(len(fullMenuDict["Menus"][0]["OrderDays"][0]["MenuItems"])):
        # load menu item
        menuItem = fullMenuDict["Menus"][0]["OrderDays"][0]["MenuItems"][i]["BiteMenuItemSizes"][0]

        # check if course or description missing from keys
        if not {"Course", "Description"}.issubset(menuItem.keys()):
            continue

        # construct menu item object
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
    return parsedMenu
