# download-manager
Manages download requests for data sharer and download files without hassle.  
## Options
```sh
Usage: dmanage.py [options]

Options:
  -h, --help            show this help message and exit
  -s, --start           Start server
  -m, --manage          Manage servers
  -c, --configure       Make configuration file
  -S, --show            Show All DC Request
  -q, --queue           Download queue
  -x, --stop            Stop Server
  -u, --usermanage      User Management

  Add Links directly:
    -a LINK, --link=LINK
                        Links
    -n NAME, --name=NAME
                        Name of the links group

  Add Links by DC request id shown by dmanage.py -S command:
    -i SSID, --ssid=SSID
                        Add download links by ids

  Deleting downloads by ID. View queue by running dmanage.py -q:
    -f FID, --fid=FID   Delete download links by queue file ids
    -p PID, --pid=PID   Delete download links by queue package ids
```

## Example Usage:

1) Clone the repo
```sh
git clone https://github.com/thispc/download-manager.git
```
2) Change directory to the repo
```sh
cd download-manager
```
3) Run the following command to create a config file (Initial Step)
```sh
python dmanage.py -c
```
4) Follow all the steps and create a configuration file

5) Start the download server
```sh
python dmanage.py -s
```
6) Try to add a link to start the download ()
```sh
python dmanage.py -a <link> -n <username_of_requested_person>
```
ex:
```sh
python dmanage.py -a http://speedtest.atlanta.linode.com/100MB-atlanta.bin -n user1
```
7) Manage the downloads
```sh
python dmanage.py -m
```
8) See the queue
```sh
python dmanage.py -q
```
9) Stop the server
```sh
python dmanage.py -x
```
