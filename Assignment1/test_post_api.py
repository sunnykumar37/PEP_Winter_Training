import requests
import json

url = 'http://localhost:8000/api/students/'

student_data = {
    'name': 'Vinay',
    'age': 22,
    'email': 'vinay@example.com'
}

response = requests.post(url, json=student_data)

print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")


if response.status_code == 201:
    print("\n Student created successfully!")
else: 
    print("\n Error creating student")