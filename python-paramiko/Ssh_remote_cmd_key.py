#!/usr/bin/env python
#coding:utf8
#author:luodi


import paramiko

hostname="192.168.2.147"
port=22

#初始化SSH对象
ssh = paramiko.SSHClient()

#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#指定私钥进行连接
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

#连接到对应的服务器
ssh.connect(hostname=hostname,port=port,username='root',pkey=private_key)

#执行命令
stdin,stdout,stderr = ssh.exec_command('df -h')

#判断执行情况
out,error = stdout.read(),stderr.read()

if error: 
    print "Result ERROR:%s" %error
else:
    print "Result:%s" %out

ssh.close()
