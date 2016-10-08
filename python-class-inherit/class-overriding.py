#!/usr/bin/env python
#coding:utf8

__author__ = 'LUODI'


class animal(object):
    def RUN(self):
        print "奔跑"


class DOG(animal):
    def __init__(self,name):
        self.name = name

    def RUN(self):
        #显式调用基类方法
        animal.RUN(self)
        #使用super进行调用方法
        super(DOG,self).RUN()
        print self.name,"在奔跑"

d1=DOG('张小狗')
d1.RUN()

d2=DOG('罗小狗')
d2.RUN()
#调用一个未绑定的基类方法
animal.RUN(d2)



