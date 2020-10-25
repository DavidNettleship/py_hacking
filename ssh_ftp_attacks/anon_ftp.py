#!usr/bin/python

import ftplib

def anonLogin(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anon','anon')
        print("[*] " + host + " FTP anonymous login succeeded.")
        ftp.quit()
        return True
    except:
        print("[-] " + host + " FTP anonymous login failed.")

host = "192.168.1.7"
anonLogin(host)
