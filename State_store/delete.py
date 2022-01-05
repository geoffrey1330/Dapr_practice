import requests
 
url = "http://localhost:3500/v1.0/state/statestore/food"
 
res = requests.delete(url)
