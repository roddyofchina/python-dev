#!/usr/bin/env python
#coding:utf8
__author__ = 'LUODI'

#静态方法
class Static_Function(object):
    names = 'LUODI'
    
    def __init__(self):
        self.name = 'LUODI'
        self.job = 'IT'

    @staticmethod
    def PrintStatic():
        print "this is a static function"
        #print self.names,self.job 静态无法访问类方法和实例方法

    def PrintJob(self):
        print self.name,self.job

#直接调用类里的静态方法
Static_Function.PrintStatic()

#非静态方法需要实例化该类
a=Static_Function()
a.PrintStatic()


