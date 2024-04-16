import os, json, sys, yaml

# if len(sys.argv) > 1: # do we have more than 1 argument?
#     if os.path.exists(sys.argv[1]): # is the filename passed actually present?
#         file = open(sys.argv[1], "r")
#         json.load(file)
#         file.close()
#         print("JSON is valid!")
#     else:
#         print(sys.argv[1] + " not found")
# else:
#     print("Usage: python check_json.py <file>")
#

# with open('input_json.json', 'r') as file:
#   configuration = json.load(file)
#
# with open('config.yaml', 'w') as yaml_file:
#   yaml.dump(configuration, yaml_file)
#
# with open('config.yaml', 'r') as yaml_file:
#   print(yaml_file.read())

if len(sys.argv) > 1: # do we have more than 1 argument?
    if os.path.exists(sys.argv[1]): # is the filename passed actually present?
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is valid! Now the file will be converted.")
        with open(sys.argv[1], 'r') as file:
            configuration = json.load(file)
    else:
        print(sys.argv[1] + "not found")
else:
    print("Usage: python json_2_yaml.py <file>")

with open(sys.argv[2], "w") as yaml_file:
    yaml.dump(configuration, yaml_file)

with open(sys.argv[2], 'r') as yaml_file:
    print(yaml_file.read())
