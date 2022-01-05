import requests
 
url = "http://localhost:3500/v1.0/state/statestore"
 
data = [{
    "key": "food",
    "value": ["Rice","Beans","Yam","Cassava"]
  }]

 
response = requests.post(url, json=data)

print(response)