
import json

# .loads example

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car["name"])
    print(car["engine"])

path_to_json = "example.json"
json = json.load(open(path_to_json))
value = json["name"]

print(value)

# jason.load takes a file
# json.loads takes a string
