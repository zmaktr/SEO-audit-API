import requests

endpoint = "http://localhost:8000/auth/users/"

headers = {
    "Content-Type": "application/json"
}

data = {
    "email" : "contact120@admin.com",
    "username":"admin4",
    "password":"howsezq-1"
    }

get_response = requests.post(endpoint, headers=headers, json=data)

print(get_response.json())
print(get_response.status_code)