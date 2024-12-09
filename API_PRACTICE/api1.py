import requests

data={"key": "value"}
response=requests.post("https://httpbin.org/post", data)
json_response = response.json()
print(response)