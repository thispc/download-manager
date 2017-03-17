import json
import requests

username = input('Enter your username: ')
#test123

password = input('Enter your password: ')
#123456

secret = "qwerty"

url = "172.16.86.222:13000/login?nick="
url += username
url += "&password="
url += password
url += "&secret="
url += secret

r = requests.get(url)

js = json.loads(r.text)

print js