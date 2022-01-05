import requests
 
url = "http://localhost:3500/v1.0/state/statestore/pp"
 
res = requests.get(url)
print(res)