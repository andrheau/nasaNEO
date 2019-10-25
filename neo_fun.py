# Let's build a python application to pull some info on Near Earth Objects and give it back to people in interesting ways

import requests
import json

# TODO: Build a method to pull the feed data based on user input start/end dates

# API Endpoint

api_url = "https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key="
apiKey = "13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"

# Get and return data
response = requests.get(api_url + apiKey)

data = response.text
parsed = json.loads(data)
neos = parsed["near_earth_objects"]["2019-10-25"]
# max_diameter = neos["estimated_diameter"]["meters"]["estimated_diameter_max"]

# TODO: Parse the data to return data for...

# TODO: ...Furthest NEO

# TODO: ...Closest miss NEO
# def closest_miss(neos):
#    closest = None
#    for neo in neos:
#        if closest is None:
#            closest = neo
#            pass
#        if neo["miss_distance"]

# TODO: ...Largest (diameter) NEO

# def find_largest():


#def get_largest_neo():
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
print("{} is the largest NEO today at a whopping {} meters in diameter!".format(name, largest))


#    print (max_diameter)

#            pass
        
#             largest = neo(max_diameter)
#             return largest

# print find_largest()


# TODO: ...Fastest NEO

# TODO: Any NEO classified as PHA (potentially hazardous)



