import requests
import json

data = {"name": "Uzair Test", "roll": 1000, "city": "Lhr"}
json_data = json.dump(data)
response = requests.post('http://127.0.0.1:8000/create-student', json_data)

print(response.json())
