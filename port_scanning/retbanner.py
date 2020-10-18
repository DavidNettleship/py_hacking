#!usr/bin/python
#"192.168.1.7" metasploitable ip

import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return str(banner)
    except:
        return

def main():
    ip = "192.168.1.7" #metasploitable
    for port in range(1,1000):
        banner = retBanner(ip,port)
        if banner:
            print("[+]" +"IP:" + ip + " | Port: "+ str(port) + ": " + banner)

main()
