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

for i in range(1,6):
	tempurl=url+str(i)
	html_page = urllib2.urlopen(tempurl)
	soup = BeautifulSoup(html_page,"lxml")
	print "============="
	for j in range(1,11):
		link=soup.select('body > div.container > div.row > div.span7 > div:nth-of-type('+str(j)+') > div.post')
		user=soup.select('body > div.container > div.row > div.span7 > div:nth-of-type('+str(j)+') > h4 > a')
		#urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(link))
		urls=M.findall(str(link))
		print urls
		for k in urls:
			pos=0
			for f in k:
				pos=pos+1
				if f=='\\':
					break
			#print k[:pos-1]
		if(len(user)!=0):	
			print user[0].text
		else:
			print "Nil"

		#sel=CSSSelector('body div.container div.row div.span7 div:nth-child(10) div.post a')
		#print sel()