import requests

#This is saperate application it may be out of dir OR Any other programming languages
URL = 'http://127.0.0.1:8000/stu_info/'
req = requests.get(url = URL)
data = req.json()
print(data)