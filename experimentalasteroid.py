import json
import requests
from dictor import dictor
from neokey import apiKey

api_url = "https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key="
response = requests.get(api_url + apiKey)
data = response.text
parsed = json.loads(data)

neos = parsed["near_earth_objects"]["2019-10-25"]

for diameter in neos:
    max_diameter = round(diameter["estimated_diameter"]["meters"]["estimated_diameter_max"])
    """print(max_diameter)"""



def max(diameter):
    largest = None
    for bigdog in diameter:
        if largest is None:
            largest = bigdog
        pass
    else bigdog["max_diameter"] > largest:
        largest = bigdog
        pass
    return largest
