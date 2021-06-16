import requests

r = requests.get('http://localhost:5000/health')

if r.status_code == 200:
    print(r.json())
