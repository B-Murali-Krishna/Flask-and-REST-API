import requests
BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1",{"likes": 10,'name':"tim","views":10000})
print(response.json())
