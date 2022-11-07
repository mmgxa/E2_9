import requests
import base64
import json

with open("img/cat.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    

encoded_string = str(encoded_string)[1:]
encoded_string = "data:image/jpeg;base64," + encoded_string
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'body': encoded_string}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=data, headers=headers).json()
loaded_j = json.loads(response['body'])
print(loaded_j[0])