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
        if largest is None:
            largest = max_diameter        
        if largest > max_diameter:
            pass
        else:
            largest = max_diameter
            name = diameter["name"]
    return(largest, name)

# TODO Function to get the smallest NEO

def get_smallest_neo(neos):
    smallest = None
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

def get_fastest_neo(neos):
    velocity = None
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

# TODO  Write a function to return these calculations
# Declare variables for other units of measure and do the math

largest_diameter_in_armadillos = round(get_largest_neo(neos)[0] / length_of_armadillo)
largest_diameter_in_deloreans = round(get_largest_neo(neos)[0] / length_of_delorean)
smallest_diameter_in_armadillos = round(get_smallest_neo(neos)[0] / length_of_armadillo)
smallest_diameter_in_deloreans = round(get_smallest_neo(neos)[0] / length_of_delorean)

# print("You might ask, 'Are we in danger?' and the answer would be...not at all! Although today is the date of close approach to Earth, it's going to pass at a comfortable {} Kilometers from our planet. You can now exhale.".format(close_approach_distance))

#    print (max_diameter)

#            pass
        
#             largest = neo(max_diameter)
#             return largest

# print find_largest()


# TODO: ...Fastest NEO

# TODO: Any NEO classified as PHA (potentially hazardous)

def asteroidvariables(): 
    asteroid = input("So, do you want to know the fastest, largest, or smallest world ending near Earth object?\n\t> ")
    if asteroid.lower() == "fastest":
        asteroid = "{} is the fastest NEO today, racing towards somwhere at a speed of {} kilometers per second.".format(get_fastest_neo(neos)[1], get_fastest_neo(neos)[0])
    elif asteroid.lower() == "largest":
        asteroid = "{} is the largest NEO today at a whopping {} meters in diameter! \nThat means it's {} armadillos OR {} Deloreans in diameter!".format(get_largest_neo(neos)[1], get_largest_neo(neos)[0], largest_diameter_in_armadillos, largest_diameter_in_deloreans)
    elif asteroid.lower() == "smallest":
        asteroid = "{} is the smallest NEO today. It checks in at a paultry {} meters in diameter. \nThat means it's only {} armadillos OR {} Deloreans in diameter!".format(get_smallest_neo(neos)[1], get_smallest_neo(neos)[0], smallest_diameter_in_armadillos, smallest_diameter_in_deloreans)
    else:
        print("This really wasn't one of the options. Thanks.")
        main()

    return asteroid

def main():
    print("It's time to dispense some bad news about our odds of survival. What's up with that asteroid?")
    asteroidresult = asteroidvariables()
    print(asteroidresult)
    
main()

if __name__ == '__testpage2__':
    main()