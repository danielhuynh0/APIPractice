import requests

url = 'http://localhost:5000/hello'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['content'])

