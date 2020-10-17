#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Enter the Host to scan: ")
#port = int(raw_input("[*] Enter the Port to scan: "))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("Port %d is closed" % (port),'red'))
	else:
		print(colored("Port %d is open" % (port),'cyan'))

for port in range(1,150):
	portscanner(port)
