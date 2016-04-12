#!/usr/bin/env python
__author__ = "luodi"


from socket import *

myHost=''
myPort=50007

socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.bind((myHost, myPort))
socketobj.listen(5)


while True:
    connection, address = socketobj.accept()
    print('Server connected by ', address)
    while True:
        data = connection.recv(1024)
        if not data: break
        if 'df' in data:
            print "data df"
        connection.send(b'Echo=>' + data )
    connection.close()

