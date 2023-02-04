#!/bin/bash

# URL of the file to download
url="https://svn.nmap.org/nmap/nmap-os-db"

# Destination location
destination="/usr/share/honeyd/"

# Download the file
wget -P "$destination" "$url"

# Confirm the file was downloaded
if [ -f "$destination/nmap-os-db" ]; then
  echo "File successfully downloaded and placed in $destination"
else
  echo "Failed to download the file."
fi
