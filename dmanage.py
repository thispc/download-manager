import os
from os.path import exists
import __builtin__
import sys
from os import makedirs, path, chdir
from os.path import join
from sys import argv, platform
import shutil
import optparse
import json

def wdir():
	__builtin__.owd = path.abspath("") 
	__builtin__.pypath = path.abspath(path.join(__file__, "..", ".."))

	sys.path.append(join(pypath, "module", "lib"))

	homedir = ""

	if platform == 'nt':
	    homedir = path.expanduser("~")
	    if homedir == "~":
	        import ctypes

	        CSIDL_APPDATA = 26
	        _SHGetFolderPath = ctypes.windll.shell32.SHGetFolderPathW
	        _SHGetFolderPath.argtypes = [ctypes.wintypes.HWND,
	                                     ctypes.c_int,
	                                     ctypes.wintypes.HANDLE,
	                                     ctypes.wintypes.DWORD, ctypes.wintypes.LPCWSTR]

	        path_buf = ctypes.wintypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
	        result = _SHGetFolderPath(0, CSIDL_APPDATA, 0, 0, path_buf)
	        homedir = path_buf.value
	else:
	    homedir = path.expanduser("~")

	__builtin__.homedir = homedir

	args = " ".join(argv[1:])

	if "--configdir=" in args:
	    pos = args.find("--configdir=")
	    end = args.find("-", pos + 12)

	    if end == -1:
	        configdir = args[pos + 12:].strip()
	    else:
	        configdir = args[pos + 12:end].strip()
	elif path.exists(path.join(pypath, "module", "config", "configdir")):
	    f = open(path.join(pypath, "module", "config", "configdir"), "rb")
	    c = f.read().strip()
	    f.close()
	    configdir = path.join(pypath, c)
	else:
	    if platform in ("posix", "linux2"):
	        configdir = path.join(homedir, ".pyload")
	    else:
	        configdir = path.join(homedir, "pyload")

	if not path.exists(configdir):
	    makedirs(configdir, 0700)

	__builtin__.configdir = configdir
	return configdir




if __name__ == "__main__":
	wpath=wdir()
	parser = optparse.OptionParser('usage: %prog [options]')
	parser.add_option("--start", "-s", dest="sflag",action="store_true", help="Start server")
	parser.add_option("--manage", "-m", dest="mflag",action="store_true", help="Manage servers")
	parser.add_option("--configure", "-c", dest="cflag",action="store_true", help="Make configuration file")
	parser.add_option("--show", "-S", dest="Sflag",action="store_true", help="Show All DC Request")
	parser.add_option("--queue", "-q", dest="qflag",action="store_true", help="Download queue")
	parser.add_option("--stop", "-x", dest="xflag",action="store_true", help="Stop Server")
	parser.add_option("--usermanage", "-u", dest="uflag",action="store_true", help="User Management")
	group1 = optparse.OptionGroup(parser, 'Add Links directly')
	group2 = optparse.OptionGroup(parser, 'Add Links by DC request id shown by ' +argv[0]+ ' -S command')
	group3 = optparse.OptionGroup(parser, 'Deleting downloads by ID. View queue by running '+argv[0]+' -q')
	group1.add_option("--link", "-a", action="append", help="Links")
	group1.add_option("--name","-n", action="store",dest="name",help="Name of the links group")
	group2.add_option("--ssid", "-i", action="append",help="Add download links by ids")
	group3.add_option("--fid", "-f", action="append",help="Delete download links by queue file ids")
	group3.add_option("--pid", "-p", action="append",help="Delete download links by queue package ids")
	parser.add_option_group(group1)
	parser.add_option_group(group2)
	parser.add_option_group(group3)

	(options, args) = parser.parse_args()
	#print options
	linksid=options.ssid
	links=options.link
	deleteids=options.fid
	deleteidsp=options.pid
	if(options.sflag):
		if not exists(wpath+"/pyload.conf"):
			print "\nConfig File does not exists. \nFirst run '%s -c' command to make configuration file\n" % sys.argv[0]
		else:
			if exists(wpath+"/pyload.pid"):
				print "Server is already UP!!"
				pid=open(wpath+"/pyload.pid").read()
				print "pid %s" %pid
				sys.exit(2)
			os.system('python pyLoadCore.py --daemon')
			print "Server UP!!"
		sys.exit(2)
	if(options.cflag):
		if not exists(wpath+"/pyload.conf"):
			os.system('python pyLoadCore.py')
			sys.exit(2)
		else:
			print "\nConfiguration file exist!!!!. Overwrite existing config file? y/n\n"
			inp=str(raw_input())
			if(inp[0]=='n' or inp[0]=='N'):
				print("Abort...")
				sys.exit(2)
			else:
				shutil.rmtree(wpath)
				os.system('python pyLoadCore.py')
				sys.exit(2)
	if(options.mflag):
		os.system("python pyLoadCli.py")
		sys.exit(2)
	if(options.qflag):
		os.system("python pyLoadCli.py queue")
		sys.exit(2)
	if(options.Sflag):
		os.system("python scraper.py")
		with open('users.dat') as data_file:
			data = json.load(data_file)
			ss=1
	    	for i in data:
	    		print "=============================================================================="
	    		print "id : %s" % str(ss)
	    		print "user : %s" % i["user"]
	    		sys.stdout.write ("url : ")
	    		for j in i["url"]:
	    			print j
	    		print "volunteered : %s" % i["volun"]
	    		print "Done? : %s" % i["done"]
	    		ss=ss+1

	    	print "==============================================================================" 
		
	
	if(options.xflag):
		try:
			pid=open(wpath+"/pyload.pid").read()
		except Exception:
			print "Server is already DOWN!!"
			sys.exit(0)
		os.system("python pyLoadCli.py kill")
		#os.remove(wpath+"/pyload.pid")
		print "Server Down!!"
	if(options.uflag):
		os.system("python pyLoadCore.py -u")
	if (linksid is not None):
		with open('users.dat') as data_file:
			data = json.load(data_file)
			for i in linksid:
				l = data[int(i)-1]
				linkappend=""
				for j in l["url"]:
					linkappend=linkappend+" "+j
				try:
					os.system("python pyLoadCli.py add "+l["user"]+linkappend)
					
				except Exception:
					print "Error in adding...Abort!"
					sys.exit(2)
			print "Download(s) added successfully"
	if (links is not None):
		if(options.name is None):
			print "\nSpecify the name of the download group by -n flag. Aborting.....\n"
			sys.exit(2)
		linkappend=""
		for j in links:
			linkappend=linkappend+" "+j
		try:
			os.system("python pyLoadCli.py add "+options.name+linkappend)
			print "Download(s) added successfully"
		except Exception:
			print "Error in adding...Abort!"
			raise Exception
			sys.exit(2)

	if (deleteids is not None):
		idappend=""
		for j in deleteids:
			idappend=idappend+" "+j
		try:
			os.system("python pyLoadCli.py del_file "+idappend)
			print "Deleted file(s) successfully"
		except Exception:
			print "Error in deletion...Abort!"
			raise Exception
			sys.exit(2)
	if (deleteidsp is not None):
		idappend=""
		for j in deleteidsp:
			idappend=idappend+" "+j
		try:
			os.system("python pyLoadCli.py del_package "+idappend)
			print "Deleted packages(s) successfully"
		except Exception:
			print "Error in deletion...Abort!"
			raise Exception
			sys.exit(2)