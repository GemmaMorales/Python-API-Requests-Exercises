import requests, json

# your code here
r = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")
r = r.json()
print(r["name"])