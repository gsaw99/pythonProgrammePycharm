import requests
import pytest
class API:

 def test_api(self):
  BASE_URL="https://reqres.in/api/users?page=2"
  response=requests.get(BASE_URL)
  print(response)
  print(response.content)
  print(response.headers)
  print(response.headers.get("Date"))
  print(response.cookies)
  print(response.status_code)
  assert response.status_code == 201
  print(response.encoding)
  print(response.elapsed)

obj=API()
obj.test_api()





