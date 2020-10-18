#!/usr/bin/python
# CMD: python3 vulscan.py vulbanners.txt

import socket
import os
import sys
import retbanner

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return str(banner)
    except:
        return

def checkVulns(banner,filename):
    f = open(filename,"r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable: " + banner.strip("\n"))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] File doesn\'t exist!")
        if not os.access(filename, os.R_OK):
            print("[-] Access Denied!")
            exit(0)
    else:
        print("[-] Please input: " + str(sys.argv[0])+ " <vuln filename>")

    portlist = [21,22,25,80,110,443,450]
    for ips in range(1,255):
        ip = "192.168.1." + str(ips)
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                print("[+] " + ip + " | " +str(port) + " : " + str(banner))
                checkVulns(banner, filename)

main()
