import requests
import json
import datetime
import random
import pytz

api_url = "https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key="
apiKey = "13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"

response = requests.get(api_url + apiKey)
data = response.text
parsed = json.loads(data)

# Set variables based on data
# Sets a variable to dynamically pull today's date and then turns it into a string
todays_date = str(datetime.datetime.utcnow().date())

# Sets "neos" as a variable which is the entirety of the API data along with some other global variables
neos = parsed["near_earth_objects"][todays_date]
total_neos_today = parsed["element_count"]
length_of_armadillo = 1.5
length_of_delorean = 4.2
i = random.randint(1,5)

# max_diameter = neos["estimated_diameter"]["meters"]["estimated_diameter_max"]

# TODO: Parse the data to return data for...

# TODO: ...Furthest NEO


# Function to calculate the total number of potentially hazardous asteriods

def get_total_phas(neos):
    total_phas = 0
    for pha in neos:
        if pha["is_potentially_hazardous_asteroid"] is True:
            total_phas = total_phas + 1
            pass
    return(total_phas)

# Write a function to return the largest NEO in diameter
def get_largest_neo():
    largest = None
    neos = parsed["near_earth_objects"][todays_date]
    for diameter in neos:
        max_diameter = round(diameter["estimated_diameter"]["meters"]["estimated_diameter_max"])
        if largest is None:
            largest = max_diameter        
        if largest > max_diameter:
            pass
        else:
            largest = max_diameter
            name = diameter["name"]

    return(largest, name)

# TODO Function to get the smallest NEO

def get_smallest_neo():
    smallest = None
    neos = parsed["near_earth_objects"][todays_date]
    for diameter in neos:
        min_diameter = round(diameter["estimated_diameter"]["meters"]["estimated_diameter_min"])
        if smallest is None:
            smallest = min_diameter
        if smallest < min_diameter:
            pass
        else:
            smallest = min_diameter
            name = diameter["name"]
    return(smallest, name)

# Function to get the fastest NEO

def get_fastest_neo():
    velocity = None
    neos = parsed["near_earth_objects"][todays_date]
    for speed in neos:
        km_per_second = speed["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]
        km_per_second = float(km_per_second)
        if velocity is None:
            velocity = km_per_second
        if velocity > km_per_second:
            pass
        else:
            velocity = km_per_second
            name = speed["name"]
    return(round(velocity), name)

def largest_diameter_in_armadillos(): 
    length_of_armadillo = 1.5
    largest_armadillo = round(get_largest_neo()[0] / length_of_armadillo)
    return largest_armadillo

def smallest_diameter_in_armadillos(): 
    length_of_armadillo = 1.5
    smallest_armadillo = round(get_smallest_neo()[0] / length_of_armadillo)
    return smallest_armadillo

def smallest_diameter_in_deloreans(): 
    length_of_delorean = 4.2
    smallest_delorean = round(get_smallest_neo()[0] / length_of_delorean)
    return smallest_delorean

def largest_diameter_in_deloreans(): 
    length_of_delorean = 4.2
    largest_delorean= round(get_largest_neo()[0] / length_of_delorean)
    return largest_delorean
