# Welcome to Asteroids v. Aardvarks, courtesy of Nasa's NEO API (https://api.nasa.gov/api.html)
import json, requests, time

api_url = "https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key=13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"
apiKey = "13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx"

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed/today?detailed=true&api_key=13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx")
data = response.json()
today = time.strftime('%Y-%m-%d', time.gmtime())

# To print the number of NEOs hear earth today
print("Today " + str(data["element_count"]) + " asteroids will be passing close to planet Earth.")
print('Good god, send help.')

# This is to print today's date in a yyyy-mm-dd format. Now we just have to figure out how to put it into the parsed JSON maybe?
print("Date: " + today)