import json
import requests
from recursivejson import extract_values

def neo_api_matrix():
    endpoint = "https://api.nasa.gov/neo/rest/v1/feed/today?api_key=13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"
    params = {

       "near_earth_objects": {}

    }

    miss_distance = extract_values(response.json(), 'text')
    return miss_distance

