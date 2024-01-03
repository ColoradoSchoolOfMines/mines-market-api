# Mines Market API
---------------------------------------------------------------------------
This 'mines_market' python package allows users to see menu options for any sodexo sponsored dining option. The package was made for Mines Market located at the Colorado School of Mines, but has the ability to work for other locations through a unique location id assigned to each dining option.

## Requirements
---------------------------------------------------------------------------

This module requires the following modules:
- [requests]

## Installation
---------------------------------------------------------------------------
Install this package as you normally would via 'pip install mines_market'

## Usage
---------------------------------------------------------------------------
**NOTE: Package requires the use of an API key for sodexo's bite API**
- Link to register found here: [Sodexo's Bite API](https://bite-external-api.portal.azure-api.net/)

#### Users can use this API via two main functions:
##### 1. fetch_location_ids(location, apiKey, url)
###### Parameters
    - location: Location name of the place you are trying to access. For Mines Market, this is 'mines'
    - apiKey: Use the API key given once you register for Sodexo's Bite API
    - url: Link to request URL of sodexo's bite API that gets location ids. Use default argument for link

###### Returns
    - 'str': A string containing the location id
##### 2. get_parsed_menu(apiKey, locationId, date, url)
###### Parameters
    - apiKey: Same parameter as used in fetch_location_ids
    - locationId: Location id of chosen place. Use fetch_location_ids to get id
    - date: Specify which date's menu you are trying to access. Default argument given as today
    - url: Link to request URL of sodexo's bite API that gets menu. Use default argument for link
###### Returns
    -  'dict': Full menu for given date
