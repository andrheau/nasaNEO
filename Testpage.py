# Let's build a python application to pull some info on Near Earth Objects and give it back to people in interesting ways

import requests
import json
import datetime
import random


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

# Function to generate a random mild insult to insert in the greeting

def generate_random_insult(i):
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
    return(insult)




# TODO  Write a function to return these calculations
# Declare variables for other units of measure and do the math

largest_diameter_in_armadillos = round(get_largest_neo(neos)[0] / length_of_armadillo)
largest_diameter_in_deloreans = round(get_largest_neo(neos)[0] / length_of_delorean)
smallest_diameter_in_armadillos = round(get_smallest_neo(neos)[0] / length_of_armadillo)
smallest_diameter_in_deloreans = round(get_smallest_neo(neos)[0] / length_of_delorean)


# All the "print" statements

print("Well hello you {}! Since you asked, there are {} Near Earth Objects on close approach today. \nNever fear, though, only {} of them are potentially hazardous. Wait, {} of them are potentially hazardous?!!? \nEverybody run for your lives!!!! ".format(generate_random_insult(i), total_neos_today, get_total_phas(neos), get_total_phas(neos)))
print("\nWell, since we're here anyway...")

# Define the "main" function

def asteroidvariables(x): 
    asteroid =("This is an error.")
    if x.lower() == "fastest":
        asteroid = "{} is the fastest NEO today, racing towards somwhere at a speed of {} kilometers per second.".format(get_fastest_neo(neos)[1], get_fastest_neo(neos)[0])
    elif x.lower() == "largest":
        asteroid = "{} is the largest NEO today at a whopping {} meters in diameter! \nThat means it's {} armadillos OR {} Deloreans in diameter!".format(get_largest_neo(neos)[1], get_largest_neo(neos)[0], largest_diameter_in_armadillos, largest_diameter_in_deloreans)
    elif x.lower() == "smallest":
        asteroid = "{} is the smallest NEO today. It checks in at a paultry {} meters in diameter. \nThat means it's only {} armadillos OR {} Deloreans in diameter!".format(get_smallest_neo(neos)[1], get_smallest_neo(neos)[0], smallest_diameter_in_armadillos, smallest_diameter_in_deloreans)
    else:
        print("\nOkay, you silly trickster. You and both know that {} is not any of the things I said you could ask for. \nHow's about we try that again?".format(x))
        main()
    return asteroid

def main():
    x = input("So, do you want to know the fastest, largest, or smallest world ending near Earth object?\n\t> ")
    asteroidresult = asteroidvariables(x)
    print(asteroidresult)
    all_done()

def all_done():
    finished = input("\nWell now aren't we all more informed? \nDid you want to know anything else today? (Yes/No): ")
    if finished.lower() == "yes":
        main()
    elif finished.lower() == "no":
        print("Okay then. I hope you enjoyed learning about whether or not we're all gonna die today. Come back anytime!")
    else:
        print("Ummm...it was a yes or no question friend. \nLast time I checked, {} is not yes OR no. Let's try it again, shall we?".format(finished))
        all_done()

main()



# print("You might ask, 'Are we in danger?' and the answer would be...not at all! Although today is the date of close approach to Earth, it's going to pass at a comfortable {} Kilometers from our planet. You can now exhale.".format(close_approach_distance))

#    print (max_diameter)

#            pass
        
#             largest = neo(max_diameter)
#             return largest

# print find_largest()


# TODO: ...Fastest NEO

# TODO: Any NEO classified as PHA (potentially hazardous)