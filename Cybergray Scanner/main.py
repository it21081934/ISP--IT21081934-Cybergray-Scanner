import os
import socket
import pyfiglet
from tabulate import tabulate
import nmap3
import nmap
import pyfiglet
from contextlib import redirect_stderr
from ipaddress import ip_address
import sys
import webbrowser
from urllib.request import urlopen
import datetime
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

ascii_banner = pyfiglet.figlet_format("CYBERGRAY!!!")
print(ascii_banner)

print("Welcome to Cybergray Vulnerability Scanning Tool")
print("<------------Made by Kulika Padmika------------->")
print (" ")
# Table
data = [["ClickJacking Tester", 1],
        ["Network Scanner", 2],
        ["XSS Scanner", 3],
        ["WP Scanner", 4]
        ]

# define header names
col_names = ["Type of Scanner", "Program ID"]

# display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

programID = int(input("Enter Program ID : "))

if (programID == 1):
    
    os.system("python ISPClick.py")

elif (programID == 2):

    os.system("python Network.py")

elif (programID == 3):

    os.system("python XSSscanner.py")

elif (programID == 4):

    os.system("python WP_Scanner.py")

else:
    print("Wrong ID !!!")
