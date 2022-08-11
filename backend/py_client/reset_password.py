import requests

endpoint = "http://localhost:8000/auth/users/reset_password/"

headers = {
    "Content-Type": "application/json"
}

data = {
    "email" : "my.nifty.solutions@gmail.com"
    }

get_response = requests.post(endpoint, headers=headers, json=data)

print(get_response.text)
print(get_response.status_code)