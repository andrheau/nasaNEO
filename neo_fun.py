# Let's build a python application to pull some info on Near Earth Objects and give it back to people in interesting ways

import requests
import json

# TODO: Build a method to pull the feed data based on user input start/end dates

# API Endpoint

api_url = "https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key="
apiKey = "13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"

# Get and return data
response = requests.get(api_url + apiKey)

# Set variables based on data
data = response.text
parsed = json.loads(data)
neos = parsed["near_earth_objects"]["2019-10-25"]

# Set global variables

length_of_armadillo = 1.5
length_of_delorean = 4.2

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

# Write a function to return the largest NEO in diameter
def get_largest_neo(neos):
    largest = None
    for diameter in neos:
        max_diameter = round(diameter["estimated_diameter"]["meters"]["estimated_diameter_max"])
#        name = diameter["name"]
        if largest is None:
            largest = max_diameter
        if largest > max_diameter:
            pass
        else:
            largest = max_diameter
    return(largest)

# Write a function to get the name of the NEO

def get_name(neos):
    for name in neos:
        name = name["name"]
    return(name)

# TODO  Write a function to return these calculations

diameter_in_armadillos = round(get_largest_neo(neos) / length_of_armadillo)
diameter_in_deloreans = round(get_largest_neo(neos) / length_of_delorean)

print("{} is the largest NEO today at a whopping {} meters in diameter! \nThat means it's {} armadillos OR {} Deloreans in diameter!".format(get_name(neos), get_largest_neo(neos), diameter_in_armadillos, diameter_in_deloreans))

# print("You might ask, 'Are we in danger?' and the answer would be...not at all! Although today is the date of close approach to Earth, it's going to pass at a comfortable {} Kilometers from our planet. You can now exhale.".format(close_approach_distance))

#    print (max_diameter)

#            pass
        
#             largest = neo(max_diameter)
#             return largest

# print find_largest()


# TODO: ...Fastest NEO

# TODO: Any NEO classified as PHA (potentially hazardous)



