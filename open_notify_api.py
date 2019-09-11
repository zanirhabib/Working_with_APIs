import requests
import json

# request = requests.get('http://api.open-notify.org')
# print(request.text)

people = requests.get('http://api.open-notify.org/astros.json')
# print(people.text)

people_json = people.json()
# print(people_json)

print"Number of people in space:",people_json['number']

for p in people_json['people']:
    print(p['name'])