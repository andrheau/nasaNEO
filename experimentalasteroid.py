import urllib.request
import json
import pprint
contents = urllib.request.urlopen("https://api.nasa.gov/neo/rest/v1/neo/3879283?api_key=13L6o25sYaUm7Ac1Op2e09FrWudmH6N0rRhVBoCx").read()
varab = json.loads(contents)
pprint.pprint(varab)