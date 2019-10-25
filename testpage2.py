import json
import requests
from recursivejson import extract_values

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key=13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"
)
data = response.text
parsed = json.loads(data)
""" velocity = parsed["near_earth_objects"]["2019-10-25"][0]["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]
diameter = parsed["near_earth_objects"]["2019-10-25"][1]["estimated_diameter"]["feet"]["estimated_diameter_max"] """

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(parsed)