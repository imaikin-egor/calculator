import requests
import json

url = 'http://127.0.0.1:5000/calculate'
data = {
    'expression': '5 + 2 * (4 - 1) - 8'
}

response = requests.post(url, json=data)
result = response.json()

print(result)
