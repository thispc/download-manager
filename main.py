import sys
import json
from pprint import pprint
import os
import wget
import optparse
import time
import signal

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)
def download(ssid):
	try:
		#print "debug1"
		with open('users.dat') as data_file:    
			data = json.load(data_file)
    		#print "debug2"
    		l = data[ssid-1]
    		#print "debug3"
    		print "\n"+str(len(l["url"]))+" downloads to be performed. Download ??y/n\n"
    		inp=str(raw_input())
    		if(inp[0]=='n' or inp[0]=='N'):
    			raise ValueError("Exiting...")
    			sys.exit(2)
    		#signal.signal(signal.SIGINT, signal_handler)
    		for j in l["url"]:
    			os.system("wget "+j)
    		print "Downloaded Successfully. Inform %s" % l["user"]
    	except (IOError, ValueError, KeyError, IndexError, TypeError) as error:
    		raise error
    		print "File is invalid or ssid is incorrect"


def showrequest():
	with open('users.dat') as data_file:
		data = json.load(data_file)
		ss=1
    	for i in data:
    		print "============================================================================="
    		print "id : %s" % str(ss)
    		print "user : %s" % i["user"]
    		sys.stdout.write ("url : ")
    		for j in i["url"]:
    			print j
    		print "volunteered : %s" % i["volun"]
    		print "Done? : %s" % i["done"]
    		ss=ss+1

    	print "============================================================================="
if __name__ == "__main__":

	#os.system("python scraper.py")
	parser = optparse.OptionParser('usage: %prog [options]')
	parser.add_option("--show", "-s", dest="sflag",action="store_true", help="Show Request")
	parser.add_option("--select", "-i", dest="ssid",action="store",type="int", help="Index of link")
	#parser.add_option("--link", "-l", dest="ulink",action="store", help="New Database For Search")
	#parser.add_option("--name", "-n", dest="uname",action="store", help="Name of Database")
	(options, args) = parser.parse_args()
	if(options.sflag):
		showrequest()
	if(options.ssid is not None):
		download(options.ssid)


