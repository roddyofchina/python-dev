#!/usr/bin/env python
#coding:utf8

__author__ = 'LUODI'


class CLASSInherit(object):
    '''Hello i am father'''
    def __init__(self):
        self.name = 'LUODI'
        self.age = 25
    def RUN(self):
        print "我是父类的方法"

class CLASSON(CLASSInherit):
    '''Hello i am son'''
    def ECHO(self):
        print "我是子类"

class CLASSOVERRIDING(CLASSInherit):
    def RUN(self):
        print "对父类的RUN方法进行重写"

#实例话对象
S=CLASSON()
S.ECHO()
S.RUN()
print S.name #继承了父类的方法

#重写父类方法
N=CLASSOVERRIDING()
N.RUN()
