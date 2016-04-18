#!/usr/bin/env python
#coding:utf8
#description: this is a test socket server 
__author__ = "luodi"


from socket import *

import multiprocessing

myHost=''
myPort=50007
socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.bind((myHost, myPort))
socketobj.listen(5)

def socketserver(socketobj):
    while True:
        connec, address = socketobj.accept()
        print('Server connected by:', address)
        while True:
            data = connec.recv(1024)
            if not data: break
            connec.sendall(data)
        connec.close()

if __name__ == '__main__':
    jobs = []
    numclients = 8
    for client in range(numclients):
        p = multiprocessing.Process(target=socketserver, args=(socketobj,))
        jobs.append(p)
        p.start()
