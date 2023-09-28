import json
import requests
import datetime


def fetchLocationIds(location_name, apiKey):
    """ search bite API for locations by location name

    Args:
        location_name (str): location to search for
        apiKey (str): api key for the Sodexo's bite API

    Returns:
        str: json containing the http response
    """
    url = "https://bite-external-api.azure-api.net/extern/accesscodeslocation"
    payload = {"name": location_name, "includeWithoutMenu": False}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return requests.get(url, params=payload, headers=headers).text


def fetchMenu(date, apiKey):
    """ request from the bite API the menu for a specific date

    Args:
        date (datetime.date): date to fetch menu for
        apiKey (str): api key for the Sodexo's bite API

    Returns:
        str: json containing the http response
    """
    url = "https://bite-external-api.azure-api.net/extern/bite-application/location"
    params = {"date": date, "locationid": "75204001"}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return requests.get(url, params=params, headers=headers).text


# open config file with api key
with open("config.json", "r") as file:
    config = json.load(file)

# get info on mines
with open("result.json", "w") as file:
    file.write(fetchLocationIds("mines", config["SODEXO_API_KEY"]))

with open("info.json", "w", encoding="utf-8") as file:
    file.write(fetchMenu(datetime.date.today(), config["SODEXO_API_KEY"]))
