This is based off the tutorial: https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236

OPEN-NOTIFY API

people_json = people.json()
print(people_json)

returns: {u'message': u'success', u'number': 6, u'people': [{u'craft': u'ISS', u'name': u'Alexey Ovchinin'}, {u'craft': u'ISS', u'name': u'Nick Hague'}, {u'craft': u'ISS', u'name': u'Christina Koch'}, {u'craft': u'ISS', u'name': u'Alexander Skvortsov'}, {u'craft': u'ISS', u'name': u'Luca Parmitano'}, {u'craft': u'ISS', u'name': u'Andrew Morgan'}]}

u means the output is a unicode string - https://stackoverflow.com/questions/13940272/python-json-loads-returns-items-prefixing-with-u

test



