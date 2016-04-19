#!/usr/bin/env python
__author__ = 'Luodi'



import socket,os,sys
from socket import *
serverHost = '127.0.0.1'
serverPort = 50007

socketobj= socket(AF_INET, SOCK_STREAM)
socketobj.connect((serverHost, serverPort))

def pullfile(localfilename):
    with open(localfilename, 'wb') as f: 
        while True: 
            data = socketobj.recv(4096) 
            if data == 'EOF': 
                print "file pull success!"
                break
            f.write(data) 

def pushfile(localfilename):
    with open(localfilename, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data: break
            socketobj.send(data)
    print "send file success!"


def connect_server(action,message):
    if action == 'pull':
        localfile= sys.argv[3]
        socketobj.send(message)
        pullfile(localfile)

    elif action == 'push':
        filename = sys.argv[2]
        socketobj.send(message)
        data=socketobj.recv(4096)
        if data == 'conRead':
            pushfile(filename)

if __name__  == '__main__':
    action= sys.argv[1]
    filename = sys.argv[2]
    data = action + ' ' + filename
    connect_server(action,data)
    socketobj.close()

