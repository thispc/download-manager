import requests
import sys
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import json
import optparse
import lxml.html
from lxml import etree
#from lxml.cssselect import CSSSelector
#rr='\b(magnet):?[-A-Z0-9+&@#()\/%?=~_|!:,.;]*[-A-Z0-9+&@#()\/%=~_|]'
#N= re.compile(rr)
nn="""\b(https?|ftp|file):\/\/[-A-Z0-9+&@#(\/%?=~_|!:,.;]*[-A-Z0-9+&@#)\/%=~_|]"""
M=re.compile(nn)
url="http://172.16.86.222/dchub/request&page="
userlinks =[]
for i in range(1,6):
	tempurl=url+str(i)
	html_page = urllib2.urlopen(tempurl)
	soup = BeautifulSoup(html_page,"lxml")
	sys.stdout.write(".")
	for j in range(1,11):
		link=soup.select('body > div.container > div.row > div.span7 > div:nth-of-type('+str(j)+') > div.post')
		user=soup.select('body > div.container > div.row > div.span7 > div:nth-of-type('+str(j)+') > h4 > a')
		if(len(link)):
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(link[0].text))
		else:
			continue
		#urls=M.findall(str(link))
		if(len(user)!=0):	
			#print user[0].text
			temp=dict()
			temp["user"]=user[0].text
			temp["url"]=[]
			temp["done"]="No"
			temp["volun"]="false"
			for k in urls:
				temp["url"].append(k)
			if(len(temp["url"])!=0):
				userlinks.append(temp)
		
		#	for f in k:
		#		pos=pos+1
		#		if f=='\\':
		#			break
			#print k[:pos-1]
print "\n"
json.dump(userlinks, open('users.dat', 'w'))

		#sel=CSSSelector('body div.container div.row div.span7 div:nth-child(10) div.post a')
		#print sel()