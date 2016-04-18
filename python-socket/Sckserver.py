#!/usr/bin/env python
#coding:utf8
#description: this is a test socketserver program 
__author__ = "luodi"


import SocketServer
import commands


class HandleServer(SocketServer.BaseRequestHandler):

    def handle(self):
        print("Client connection:",self.client_address)
        while True:
            self.c_data = self.request.recv(1024)
            if not self.c_data: 
                break
            ExecCMDstatus, ExecCMDresult=commands.getstatusoutput(self.c_data)
            self.request.sendall(ExecCMDresult)
            print("connection closed:",self.client_address)

if __name__ == "__main__":
    HOST,PORT = "",50007
    server = SocketServer.ThreadingTCPServer((HOST,PORT),HandleServer)
    server.serve_forever()
