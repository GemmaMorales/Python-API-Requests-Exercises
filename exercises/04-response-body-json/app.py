import requests, json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
#print(response.text)

time = json.loads(response.text)
#hours = time.hours
#minute = time.minutes
#seconds = time.seconds
#print(time)
print("Current time: " + str(time["hours"]) + " hrs "+ str(time["minutes"]) +" min and " + str(time["seconds"]) + " sec")