import json
with open('jsonproba.json') as file_object:
    adatok=json.load(file_object)
print(adatok)