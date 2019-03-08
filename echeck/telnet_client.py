# -*- coding: utf-8 -*-

import getpass
import telnetlib


def do_telnet(host,username,password,finish,commands):
    tn = telnetlib.Telnet(host,port=23,timeout=10)
    tn.set_debuglevel(2)
    tn.read_until('login:')
    tn.write(username + '\n')
    tn.read_until('password:')
    tn.write(password + '\n')
    tn.read_until(finish)
    for command in commands:
        tn.write('%s\n' % command)
    tn.read_until(finish)
    tn.close()

if __name__=='__main__':
    host = 'localhost'
    username = ''
    password = ''
    finish = ':~$ '  #  命令提示符
    commands = ['echo "test"']
    do_telnet(host,username,password,finish,commands)

# HOST = "localhost"
# user = input("Enter your remote account: ")
# password = getpass.getpass()
#
# tn = telnetlib.Telnet(HOST)
#
# tn.read_until(b"login: ")
# tn.write(user.encode('ascii') + b"\n")
# if password:
#     tn.read_until(b"Password: ")
#     tn.write(password.encode('ascii') + b"\n")
#
# tn.write(b"ls\n")
# tn.write(b"exit\n")
#
# print(tn.read_all().decode('ascii'))