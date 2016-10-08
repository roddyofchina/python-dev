#!/usr/bin/env python
#coding:utf8

__author__ = 'LUODI'


class ClassMethod(object):
    name = 'LUODI'

    def __init__(self):
        self.Names = 'LUODI'

    @classmethod
    def RunClassMethod(self):
        print "this is a class method"
        print self.name
        #print self.Names  类方法无法访问实例变量，可以访问类变量
    def ECHO(self):
        print "sdsdddd"

ClassMethod.RunClassMethod()

