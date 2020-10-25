#!usr/bin/python

import hashlib

hashval = input("Enter a string to hash: ")

hashobj1 = hashlib.md5()
hashobj1.update(hashval.encode())
print("[+] MD5 hash: " + hashobj1.hexdigest())

hashobj2 = hashlib.sha1()
hashobj2.update(hashval.encode())
print("[+] SHA1 hash: " + hashobj2.hexdigest())

hashobj3 = hashlib.sha224()
hashobj3.update(hashval.encode())
print("[+] SHA224 hash: " + hashobj3.hexdigest())

hashobj4 = hashlib.sha256()
hashobj4.update(hashval.encode())
print("[+] SHA256 hash: " + hashobj4.hexdigest())

hashobj5 = hashlib.sha512()
hashobj5.update(hashval.encode())
print("[+] SHA512 hash: " + hashobj5.hexdigest())
