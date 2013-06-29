import urllib
import re
import time
import os
from Tkinter import *
import tkMessageBox

wan_range = "178.132" # The starting IPv4 range of the VPN provider
shutdown_program = "utorrent.exe" # The program you want to shut down, remember to include .exe
ip_url_check = "http://checkip.dyndns.org" # Don't edit if you're unsure ;)

def getIP(ip_url_check):
    request = urllib.urlopen(ip_url_check).read()
    remote_ip = ''.join(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request))
    return remote_ip

while True:
    if not getIP(ip_url_check).startswith(wan_range):
        window = Tk()
        window.wm_withdraw()
        os.system("taskkill /im " + shutdown_program + " /f")
        tkMessageBox.showerror("IP Error", "The starting range " + wan_range + " doesn't match the external IP: " + getIP(ip_url_check) + "\nShutting down " + shutdown_program)
        break
    time.sleep(60)
