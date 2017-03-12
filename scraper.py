import requests
import sys
from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
import re
import json
import optparse
import lxml.html
from lxml import etree
#from lxml.cssselect import CSSSelector

url="http://172.16.86.222/dchub/request&page="

for i in range(1,2):
	tempurl=url+str(i)
	r = requests.get(tempurl)
	html_page = urllib2.urlopen(tempurl)
	soup = BeautifulSoup(html_page)
	link=soup.select('body')
	print link.text
	#sel=CSSSelector('body div.container div.row div.span7 div:nth-child(10) div.post a')
	#print sel()