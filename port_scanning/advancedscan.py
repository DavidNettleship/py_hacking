#!/usr/bin/python
# Example usage:
# python3 advancedscan.py -H 192.168.56.1 -p 135,443
# python3 advancedscan.py -H google.com -p 443,80,22

from socket import *
from threading import *
from termcolor import colored
import optparse

def connScan(tgtHost, tgtPort):
    #attempt connection
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print(colored("[+]%d/tcp open" % tgtPort,'cyan'))
    except:
        print(colored("[-] %d/tcp closed" %tgtPort,'red'))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Unable to resolve host %s" %tgtHost)
    try:
        tgtName = gethostbyaddress(tgtIP)
        print("[+]Scan Results for: " + tgtName[0])
    except:
        print("[+] Scan Results for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', help='Specify target ports seperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')
    if(tgtHost == None) | (tgtPorts[0] == None):
            print(parser.usage)
            exit(0)
    portScan(tgtHost,tgtPorts)

main()
