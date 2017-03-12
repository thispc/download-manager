import json
from pprint import pprint
import os

with open('data.json') as data_file:    
    data = json.load(data_file)

print("Download Choices")

i = 0

for user, link in data.iteritems():
    i = i + 1
    print i, user, link

ch = int(input("Enter your choice: "))

i = 0

for user, link in data.iteritems():
    i = i + 1
    if (ch == i):
        print i, user, link
        os.system("wget " + link)