import json
import requests
from neokey import apiKey

api_url = "https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key="
response = requests.get(api_url + apiKey)
data = response.text
parsed = json.loads(data)

neos = parsed["near_earth_objects"]["2019-10-25"]

for diameter in neos:
    max_diameter = round(diameter["estimated_diameter"]["meters"]["estimated_diameter_max"])

def max(neos):
    largest = None
    for diameter in neos:
        max_diameter = round(diameter["estimated_diameter"]["meters"]["estimated_diameter_max"])
        name = diameter["name"]
        
        if largest is None:
            largest = max_diameter
        if largest > max_diameter:
            pass
        else:
            largest = max_diameter

    return(largest)

print(max(neos))