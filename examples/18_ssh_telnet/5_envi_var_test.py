import subprocess
from getpass import getpass
from pprint import pprint
import os
import pexpect
import sys


#Version_1


ssh = pexpect.spawn(f'/bin/bash -c "ssh cisco@192.168.100.1 "', encoding='utf-8' )

try:
    ssh.expect('Passw')
    ssh.sendline('cisco')
    ssh.expect('[>#]')
    ssh.sendline('enable')
    ssh.expect('Pass')
    ssh.sendline('cisco')
    ssh.expect('#')
    ssh.sendline('sh arp')
    ssh.expect(pexpect.EOF, timeout=2)
    
except pexpect.exceptions.TIMEOUT:
    print(ssh.before)
        
        
        

'''
#Version_2

ssh = pexpect.spawn("ssh cisco@192.168.100.1",encoding='utf-8')

#ssh.logfile = sys.stdout
#ssh.logfile_read = sys.stdout
#ssh.logfile_send = sys.stdout

ssh.expect('Passw')
ssh.sendline('cisco')
ssh.expect('[>#]')
ssh.sendline('enable')
ssh.expect('Pass')
ssh.sendline('cisco')
ssh.expect('#')
ssh.sendline('sh run')
while True:
    try:
        if ssh.expect('--More--', timeout=1)==0:
            print(ssh.before)
            ssh.send(" ")
    except pexpect.exceptions.TIMEOUT:break
ssh.expect('#')
print(ssh.before)
ssh.close()
'''
