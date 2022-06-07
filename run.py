import requests
response_API = requests.get("https://random-word-api.herokuapp.com/all")
print(response_API.status_code)