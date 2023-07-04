import requests

user = {"phone_number": 1234567890, "password": "password1"}
jwt_token = requests.post("http://127.0.0.1:8000/login", json=user).json()
# print(jwt_token)
