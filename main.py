import json
import requests
import datetime


# return info on mines
def fetchLocationIds(location_name, apiKey):
    url = "https://bite-external-api.azure-api.net/extern/accesscodeslocation"
    payload = {"name": location_name, "includeWithoutMenu": False}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return requests.get(url, params=payload, headers=headers).text


# get menu
def getMenu(apiKey):
    url = "https://bite-external-api.azure-api.net/extern/bite-application/location"
    today = datetime.date.today()
    params = {"date": today, "locationid": "75204001"}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return requests.get(url, params=params, headers=headers).text


# open config file with api key
with open("config.json", "r") as file:
    config = json.load(file)

# get info on mines
with open("result.json", "w") as file:
    file.write(fetchLocationIds("mines", config["SODEXO_API_KEY"]))

with open("info.json", "w", encoding="utf-8") as file:
    file.write(getMenu(config["SODEXO_API_KEY"]))
