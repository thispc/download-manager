import requests
import sys
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import json
import optparse
import lxml.html


exp1="(https?|ftp|file):\/\/[-A-Z0-9+&@#(\/%?=~_|!:,.;]*[-A-Z0-9+&@#)\/%=~_|]"
exp2="(magnet):?[-A-Z0-9+&@#()\/%?=~_|!:,.;]*[-A-Z0-9+&@#()\/%=~_|]"
exp="(magnet):?[-A-Z0-9+&@#()\/%?=~_|!:,.;]*[-A-Z0-9+&@#()\/%=~_|]|(https?|ftp|file):\/\/[-A-Z0-9+&@#(\/%?=~_|!:,.;]*[-A-Z0-9+&@#)\/%=~_|]"
url="http://172.16.86.222/dchub/request&page="
userlinks =[]
for i in range(1,6):
	tempurl=url+str(i)
	html_page = urllib2.urlopen(tempurl)
	soup = BeautifulSoup(html_page,"lxml")
	sys.stdout.write(".")
	for j in range(1,11):
		link=soup.select('body > div.container > div.row > div.span7 > div:nth-of-type('+str(j)+') > div.post')
		box = link[0].text
		user=soup.select('body > div.container > div.row > div.span7 > div:nth-of-type('+str(j)+') > h4 > a')
		user = user[0].text
		#print user
		
		urls=re.search(exp,box,re.IGNORECASE)
		temp=dict()
		temp["user"]=user
		temp["url"]=[]
		temp["done"]="No"
		temp["volun"]="No"
		while urls is not None:
			#print urls.group(0)
			temp["url"].append(urls.group(0))
			box=box[box.find(urls.group(0))+len(urls.group(0)):]
			urls=re.search(exp,box,re.IGNORECASE)
			pass
		if(len(temp["url"])!=0):
			userlinks.append(temp)
		
print "\n"
json.dump(userlinks, open('users.dat', 'w'))

		#sel=CSSSelector('body div.container div.row div.span7 div:nth-child(10) div.post a')
		#print sel()