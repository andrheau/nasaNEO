# Let's build a python application to pull some info on Near Earth Objects and give it back to people in interesting ways

import requests
import json
import datetime


# TODO: Build a method to pull the feed data based on user input start/end dates

# API Endpoint

api_url = "https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key="
apiKey = "13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"

# Get and return data
response = requests.get(api_url + apiKey)
data = response.text
parsed = json.loads(data)

# Set variables based on data
# Sets a variable to dynamically pull today's date and then turns it into a string
todays_date = str(datetime.date.today())

# Sets "neos" as a variable which is the entirety of the API data
neos = parsed["near_earth_objects"][todays_date]

# Set global variables

length_of_armadillo = 1.5
length_of_delorean = 4.2

# max_diameter = neos["estimated_diameter"]["meters"]["estimated_diameter_max"]

# TODO: Parse the data to return data for...

# TODO: ...Furthest NEO


# Write a function to return the largest NEO in diameter
def get_largest_neo(neos):
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
    return(largest, name)

# TODO  Write a function to return these calculations
# Declare variables for other units of measure and do the math

diameter_in_armadillos = round(get_largest_neo(neos)[0] / length_of_armadillo)
diameter_in_deloreans = round(get_largest_neo(neos)[0] / length_of_delorean)

print("{} is the largest NEO today at a whopping {} meters in diameter! \nThat means it's {} armadillos OR {} Deloreans in diameter!".format(get_largest_neo(neos)[1], get_largest_neo(neos)[0], diameter_in_armadillos, diameter_in_deloreans))

# print("You might ask, 'Are we in danger?' and the answer would be...not at all! Although today is the date of close approach to Earth, it's going to pass at a comfortable {} Kilometers from our planet. You can now exhale.".format(close_approach_distance))

#    print (max_diameter)

#            pass
        
#             largest = neo(max_diameter)
#             return largest

# print find_largest()


# TODO: ...Fastest NEO

# TODO: Any NEO classified as PHA (potentially hazardous)



