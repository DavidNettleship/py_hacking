#!usr/bin/python
# 3dbcf8078a52e0d449f4d2ab0be13235 = msfadmin

from termcolor import colored
import hashlib

def tryOpen(pw_list):
    global pw_file
    try:
        pw_file = open(pw_list, "r")
    except:
        print("[!] No file at path!")

    for word in pw_file:
        print(colored("[-] Trying: " + word.strip("\n"), 'red'))
        enc_wrd = word.encode('utf-8')
        md5_digest = hashlib.md5(enc_wrd.strip()).hexdigest()

        if md5_digest == md5hash:
            print(colored("[+] Password Found: " + word,'green'))
            exit(0)
        else:
            print(colored("[-] Password not in List!",'red'))

md5hash = input("[+] Enter MD5 Hash Value: ")
pw_list = "passwords.txt"
tryOpen(pw_list)
