# Let's build a python application to pull some info on Near Earth Objects and give it back to people in interesting ways

import requests
import json

# TODO: Build a method to pull the feed data based on user input start/end dates

"""
Defined variables for start/end date
"""
start_date = input("Please enter a starting date (Format: YYYY-MM-DD): ")
while start_date is not int:
    start_date = input("Ouch, reading instructions isn't your favorite eh? Let's make sure that date is in this format \n (YYYY-MM-DD): ")

end_date = input("Now enter an end date (Format: YYYY-MM-DD): ")

while end_date is not int:
    end_date = input("Ouch, reading instructions isn't your favorite eh? Let's make sure that date is in this format \n (YYYY-MM-DD): ")

print("Start Date: {} | End Date: {}").format(start_date, end_date)
# TODO: Parse the data to return data for...

# TODO: ...Furthest NEO

# TODO: ...Nearest NEO

# TODO: ...Largest (diameter) NEO

# TODO: ...Fastest NEO

# TODO: Any NEO classified as PHA (potentially hazardous)



