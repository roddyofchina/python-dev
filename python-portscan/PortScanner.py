#!/usr/bin/env python
#coding:utf8
__author__ =  'luodi'

from socket import *
import threading

def Scanports(serverHost,port):
    try:
        socketobj= socket(AF_INET, SOCK_STREAM)
        sresult=socketobj.connect_ex((serverHost, port))
        if sresult ==0:
            print "Server %s open %s" %(serverHost,port)
    except:
        print "socket异常!!!!"
    socketobj.close()


if __name__ == '__main__':
    hostip="192.168.2.232"
    for port in range(0,65535):
        t=threading.Thread(target=Scanports,args=(hostip,port))
        t.start()












