#!/usr/bin/env python
#coding:utf8
#description:this is a test socket clinet
__author__ = 'luodi'

import sys
import time
from socket import *
serverHost = '127.0.0.1'
serverPort = 50007

socketobj= socket(AF_INET, SOCK_STREAM)
socketobj.connect((serverHost, serverPort))
while True:
    cmd=raw_input("input a shell commands:").strip()
    if not cmd: continue
    socketobj.send(cmd)
    data = socketobj.recv(1024)
    print(data)
socketobj.close()
