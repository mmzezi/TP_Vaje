import json

podatki = {
        "name" : "John",
        "age" : 30,
        "city" : "New York"
        }
json = json.dumps(podatki, indent = 4)
print(json)
