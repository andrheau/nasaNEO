# Let's build a python application to pull some info on Near Earth Objects and give it back to people in interesting ways

import requests
import json
import datetime
import random

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
i = random.randint(1,8)

    # Functions

# Function to calculate the total number of potentially hazardous asteriods

def get_total_phas(neos):
    total_phas = 0
    for pha in neos:
        if pha["is_potentially_hazardous_asteroid"] is True:
            total_phas = total_phas + 1
            pass
    return(total_phas)

# Function to get the largest NEO
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

# Function to get the smallest NEO

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

# Declare variables for comparitive units of measure and do the math

largest_diameter_in_armadillos = round(get_largest_neo(neos)[0] / length_of_armadillo)
largest_diameter_in_deloreans = round(get_largest_neo(neos)[0] / length_of_delorean)
smallest_diameter_in_armadillos = round(get_smallest_neo(neos)[0] / length_of_armadillo)
smallest_diameter_in_deloreans = round(get_smallest_neo(neos)[0] / length_of_delorean)

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
    elif i == 6:
        insult = "flaky Firefly fiend"
    elif i == 7:
        insult = "genuine gentleperson"
    elif i == 8:
        insult = "spacey spheroid spelunker"
    return(insult)

# Function to get the user's chosen NEO

def which_neo(x): 
    if x.lower() == "fastest":
        this_neo = "\n{} is the fastest NEO today, racing towards somewhere at a speed of {} kilometers per second.".format(get_fastest_neo(neos)[1], get_fastest_neo(neos)[0])
    elif x.lower() == "largest":
        this_neo = "\n{} is the largest NEO today at a whopping {} meters in diameter! \nThat means it's {} armadillos OR {} Deloreans in diameter!".format(get_largest_neo(neos)[1], get_largest_neo(neos)[0], largest_diameter_in_armadillos, largest_diameter_in_deloreans)
    elif x.lower() == "smallest":
        this_neo = "\n{} is the smallest NEO today. It checks in at a paultry {} meters in diameter. \nThat means it's only {} armadillos OR {} Deloreans in diameter!".format(get_smallest_neo(neos)[1], get_smallest_neo(neos)[0], smallest_diameter_in_armadillos, smallest_diameter_in_deloreans)
    elif x.lower() == "the matrix":
        print("\nYou should have taken the blue pill.")
        x = input("Try fastest, largest, or smallest.\n\t> ")
        return which_neo(x)
    elif x.lower() == "trinity":
        print("\nNeo, I'm not afraid anymore. The Oracle told me that I would fall in love and that that man... \nthe man that I loved would be The One. So you see, you can't be dead. \nYou can't be... because I love you. You hear me? I love you. \nNow get up.")
        x = input("Try fastest, largest, or smallest.\n\t> ")
        return which_neo(x)
    else:
        print("\nOkay, you silly trickster. You and both know that {} is not any of the things I said you could ask for. \nHow's about we try that again?".format(x))
        x = input("Try fastest, largest, or smallest.\n\t> ")
        return which_neo(x)
    return this_neo

# Function to check if the user wants more info on other NEOs

def all_done():
    finished = input("\nWell now aren't we all more informed? \nDid you want to know anything else today? (Yes/No): ")
    if finished.lower() == "yes":
        main()
    elif finished.lower() == "no":
        print("\nOkay then. I hope you enjoyed learning about whether or not we're all gonna die today. Come back anytime!")
    else:
        print("\nUmmm...it was a yes or no question friend. \nLast time I checked, {} is not yes OR no. Let's try it again, shall we?".format(finished))
        all_done()

# Function to initiate the greeting

def greeting_message():
    print("Well hello you {}! Since you asked, there are {} Near Earth Objects on close approach today. \nNever fear, though, only {} of them are potentially hazardous. Wait, {} of them are potentially hazardous?!!? \nEverybody run for your lives!!!! ".format(generate_random_insult(i), total_neos_today, get_total_phas(neos), get_total_phas(neos)))
    print("\nWell, since we're here anyway...")

# Main function

def main(): 
    x = input("\nSo, do you want to know the fastest, largest, or smallest world ending near Earth object?\n\t> ")
    this_asteroid = which_neo(x)
    print(this_asteroid)
    return all_done()


# Call the greeting and main functions

greeting_message()
main()