import requests, json

# your code here
#url = "https://image.shutterstock.com/image-vector/trophy-cup-award-vector-icon-260nw-592525184.jpg"
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

data = response.json()
curr_data = data[-1]
print(curr_data['images'][-1])
