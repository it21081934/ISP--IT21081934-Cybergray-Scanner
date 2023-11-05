from ipaddress import ip_address
import nmap
import sys
import pyfiglet
import socket
import datetime
import os
from tabulate import tabulate

print('\n ------------------- [Cybergray Network Scanner] --------------------')
print('\n ----------------- ------------------------------- -----------------')

scanner = nmap.PortScanner()

# Table
data = [["UDP Scan", 1],
        ["TCP SYN Scan", 2],
        ["TCP ACK Scan", 3],
        ["TCP FIN Scan", 4],
        ["TCP Connect Scan", 5],
        ["Service Scan", 6],
        ["Port Scan", 7]]

# define header names
col_names = ["Type of Scanner", "Selection Number"]

# display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

resp = input("Enter Your Choice:")
if resp == '1':
    
    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sU')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['udp'].keys())
    

elif resp == '2':
    
    ip_addr = input("please enter IP Address: ")
    print("The ip address you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sS')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '3':

    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sA')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '4':
    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sF')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '5':

    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sT')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '6':

    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sS')
    print(scanner.scaninfo())
    print("Ip status: ", scanner.csv())

    # new portion
elif resp == '7':

    ip_addr1 = input("please enter the IP: ")
    target = socket.gethostbyname(ip_addr1)  # translate hostname to IPv4

    start = int(input("Enter the starting port number: "))
    end = int(input("Enter the ending port number: "))

    try:
        for port in range(start, end):  # max range of port is from 0 to 65535
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))  # returns an error indicator
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting Program....")
        sys.exit()

    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()

    except socket.error:
        print("\n Server not responding !!!!")
        sys.exit()
