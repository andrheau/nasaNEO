import json
import requests

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key=13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"
)
data = response.text
parsed = json.loads(data)
velocity = parsed["near_earth_objects"]["2019-10-25"][0]["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]
diameter = parsed["near_earth_objects"]["2019-10-25"][1]["estimated_diameter"]["feet"]["estimated_diameter_max"]

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint("Jeepers, this thing is moving fast! It's moving at " + velocity + " kilometers per hour. We ded for sure.")

print("And it's pretty big. It's roughly " + str(diameter) + " feet wide. Pretty sure it could be elected president in 2020")