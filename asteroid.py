import requests
import json


response = requests.get("https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key=13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx", params=parameters)

jprint(response.json())

parameters = {
   "is_potentially_hazardous_asteroid": true
}