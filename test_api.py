import requests

# request = requests.get('http://api.open-notify.org')
# print(request.text)

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)