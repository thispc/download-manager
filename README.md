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