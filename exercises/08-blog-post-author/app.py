import requests, json

# your code here
r = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
response = r.json()
print(response["posts"][0]["author"]["name"])