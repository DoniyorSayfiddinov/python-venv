import requests
import json


response = requests.get('https://randomuser.me/api/')
    
if response.status_code == 200:
        content = response.content
        data = json.loads(content.decode())
        print(data)
{
    "fullname": "fadsfsad",
    "email":"dffdgdctr",
    "phone": "fadsfsad",
    "age":215
}