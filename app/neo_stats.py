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

todays_date = str(datetime.datetime.utcnow().date())

neos = parsed["near_earth_objects"][todays_date]
total_neos_today = parsed["element_count"]
length_of_armadillo = 1.5
length_of_delorean = 4.2
i = random.randint(1,8)

def get_total_phas():
    neos = parsed["near_earth_objects"][todays_date]
    total_phas = 0
    for pha in neos:
        if pha["is_potentially_hazardous_asteroid"] is True:
            total_phas = total_phas + 1
            pass
    return(total_phas)

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
            nasa_url = diameter["nasa_jpl_url"]
    return(largest, name, nasa_url)

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
            nasa_url = diameter["nasa_jpl_url"]
    return(smallest, name, nasa_url)

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
            nasa_url = speed["nasa_jpl_url"]
    return(round(velocity), name, nasa_url)

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

def generate_random_insult(i):
    i = random.randint(1,8)
    if i == 1:
        insult = "worry wart"
    elif i == 2:
        insult = "high level hypochondriac"
    elif i == 3:
        insult = "inquisitive interstellar instigator"
    elif i == 4:
        insult = "celestial conjurer of ceaseless candor"
    elif i == 5:
        insult = "laser-brained luddite"
    elif i == 6:
        insult = "flaky Firefly fiend"
    elif i == 7:
        insult = "genuine gentleperson"
    elif i == 8:
        insult = "spacey spheroid spelunker"
    return (insult)