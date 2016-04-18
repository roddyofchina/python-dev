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
    message = 'Hello this is client2'
    socketobj.send(message)
    data = socketobj.recv(1024)
    time.sleep(2)
    print('client received:',data)

socketobj.close()
