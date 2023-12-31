import requests
import datetime
import json

from mines_market.menu import parse_menu


# return info on mines
def fetch_location_ids(location_name, apiKey, url="https://bite-external-api.azure-api.net/extern/accesscodeslocation"):
    payload = {"name": location_name, "includeWithoutMenu": False}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return json.loads(requests.get(url, params=payload, headers=headers).text)


# get menu
def get_menu(apiKey, locationId, date=datetime.date.today(), url="https://bite-external-api.azure-api.net/extern/bite-application/location"):
    params = {"date": date, "locationid": str(locationId)}
    headers = {"Ocp-Apim-Subscription-Key": apiKey}
    return json.loads(requests.get(url, params=params, headers=headers).text)


def get_parsed_menu(apiKey, locationId, date=datetime.date.today(), url="https://bite-external-api.azure-api.net/extern/bite-application/location"):
    fullMenuDict = get_menu(apiKey, locationId, date=date, url=url)
    return parse_menu(fullMenuDict)
