import requests
import datetime


# return info on mines
def fetchLocationIds(location_name, apiKey):
    url = "https://bite-external-api.azure-api.net/extern/accesscodeslocation"
    payload = {"name": location_name, "includeWithoutMenu": False}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return requests.get(url, params=payload, headers=headers).text


# get menu
def getMenu(apiKey, date=datetime.date.today()):
    url = "https://bite-external-api.azure-api.net/extern/bite-application/location"
    params = {"date": date, "locationid": "75204001"}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return requests.get(url, params=params, headers=headers).text


def get_menu_info(menu_dict, x, key):
    return menu_dict["Menus"][0]["OrderDays"][0]["MenuItems"][x]["BiteMenuItemSizes"][0][key]
