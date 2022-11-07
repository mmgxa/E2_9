import requests
import base64
import json

with open("img/cat.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    

encoded_string = str(encoded_string)[2:-1]
print(encoded_string)
encoded_string = "data:image/jpeg;base64," + encoded_string
print(encoded_string)
url = 'https://hv6egfvgwctna6wz54qk7eiw6i0yablo.lambda-url.us-east-2.on.aws'

data = {'body': encoded_string}
headers = {'Content-Type': 'application/json'}
# response = requests.post(url, json=data, headers=headers)
# print(response)
response = requests.post(url, json=data, headers=headers).json()
# loaded_j = json.loads(response)
# print(loaded_j[0])
print(response[0])