import requests, json

# your code here
r = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
response = r.json()
print(response[1]["name"])
#print(response)