import requests, json

def get_titles():
    # your code here
    r = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response = r.json()
    new_list = []
    for x in response["posts"]:
        new_list.append(x["title"])
    return new_list
print(get_titles())