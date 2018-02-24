#!/usr/bin/env python3

import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect('52.15.116.112', username='ec2-user')

sftp = client.open_sftp()
with open('file.csv') as file:
    sftp.putfo(file, '/home/ec2-user/robinsfile.csv')

stdin, stdout, stderr = client.exec_command('ls /home/ec2-user')
for line in stdout:
    print(line.strip(''))

client.close()