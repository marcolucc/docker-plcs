import requests
from os import getcwd

url = "https://raw.githubusercontent.com/marcolucc/Honeyd/master/ext/extend"

r = requests.get(url)

with open("/usr/share/honeyd/nmap-os-db", "a") as file_object:
    file_object.write(r.content)
