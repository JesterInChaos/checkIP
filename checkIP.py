import urllib
import re
import time
import os

wan_range = "178.132" # The starting IPv4 range of the VPN provider
ip_url_check = "http://checkip.dyndns.org"


def getIP(ip_url_check):
    request = urllib.urlopen(ip_url_check).read()
    remote_ip = ''.join(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request))
    return remote_ip

def checkIP(wan_range):
    if getIP(ip_url_check).startswith(wan_range):
        return True
    else:
        return False

while True:
    if not checkIP(wan_range):
        os.system("taskkill /im utorrent.exe /f")
    time.sleep(60)