import requests
import json

# parameter = {"rel_rhy":"jingle"}
# rquest = requests.get('https://api.datamuse.com/words',parameter)

# rhyme_json = request.json()
# for i in rhyme_json[0:3]:
#     print(i['word'])



parameter = {"ml":"ringing+up"}
request = requests.get('https://api.datamuse.com/words',parameter)

related_json = request.json()
for i in related_json[0:16]:
    print(i['word'])
    
param = {"sp":"dadike"}
request1 = requests.get('https://api.datamuse.com/words',param)

a = request1.json()
print
for b in a[0:16]:
    print(b['word'])
