#!/usr/bin/env python
#coding:utf8
#description: this is a test socketserver program 
__author__ = "luodi"


import SocketServer
import commands
import time
import os


class HandleServer(SocketServer.BaseRequestHandler):
    #客户端下载文件(将文件下发给客户端)
    def send_file(self,filepath):
        with open(filepath,'rb') as f:
            while True:
                data = f.read(4096) 
                if not data: 
                    break
                self.request.send(data) 
        time.sleep(1) 
        self.request.send('EOF') 
        print "send file success!"

    #客户端上传文件
    def push_file(self,localpath):
        self.request.sendall('conRead')
        with open(localpath,'wb') as f:
            while True:
                data = self.request.recv(4096)
                if not data: break
                f.write(data)

    def handle(self):
        print("Client connection:",self.client_address)
        localpath='/tmp/'
        while True:
            self.c_data = self.request.recv(1024)
            if not self.c_data: 
                break
            actions,filepath = self.c_data.split()
            if actions == 'pull':
                self.send_file(filepath)
            elif actions == 'push':
                filename=os.path.basename(filepath)
                filepath=os.path.join(localpath,filename) #/tmp/file.txt
                self.push_file(filepath)
            else:
                print "input error"
            print("connection closed:",self.client_address)


if __name__ == "__main__":
    HOST,PORT = "",50007
    server = SocketServer.ThreadingTCPServer((HOST,PORT),HandleServer)
    server.serve_forever()
