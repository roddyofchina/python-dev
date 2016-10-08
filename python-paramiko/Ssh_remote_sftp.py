#!/usr/bin/env python
#coding:utf8
#author:luodi

import paramiko

transfile = paramiko.Transport(('192.168.2.147',22))

transfile.connect(username='root',password='123456')

sftp = paramiko.SFTPClient.from_transport(transfile)


#上传当前目前下的文件到远端/tmp/下，文件名为test.py
sftp.put('./Ssh_remote_sftp.py','/tmp/test.py')

sftp.get('/etc/hosts','/tmp/hosts')

transfile.close()
