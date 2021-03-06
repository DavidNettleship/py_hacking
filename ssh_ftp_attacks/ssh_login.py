#!usr/bin/python

import pexpect

PROMPT = ['# ','>>> ','> ','\$ ']

def send_command(shell,command):
    shell.sendline(command)
    shell.expect(PROMPT)
    print(shell.before)

def connect(user,host,password):
    ssh_new_key = 'Are you sure you want to continue connecting?'
    connStr = 'ssh ' + user + '@' + host
    shell = pexpect.spawn(connStr)
    ret = shell.expect([pexpect.TIMEOUT,ssh_new_key,'[P|p]assword: '])
    if ret == 0:
        print("[-] Error Connecting")
        return
    if ret == 1:
        shell.sendline('yes')
        ret = shell.expect([pexpect.TIMEOUT,'[P|p]assword: '])
        if ret == 0:
            print("[-] Error Connecting")
            return
    shell.sendline(password)
    shell.expect(PROMPT) #successful login, expecting to be in terminal (prompt)
    return shell

def main():
    host = "192.168.1.7"
    user = "msfadmin"
    password = "msfadmin"
    shell = connect(user,host,password)
    send_command(shell, 'ls;ps')

main()
