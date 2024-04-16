import requests

postcodes_req = requests.get("http://api.postcodes.io/postcodes/se120nb")
# print(postcodes_req)
# print(type(postcodes_req.status_code))
# print(postcodes_req.headers)
# print(postcodes_req.content)
# print(postcodes_req.json())

data_dict = postcodes_req.json()["result"]
print(data_dict)
print(data_dict["region"])
