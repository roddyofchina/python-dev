#!/usr/bin/env python
#coding:utf8

class ClassVariable(object):
    #类属性
    name = 'Luodi'
    age = 25
    
    #类方法
    def PRINTNAME(self):
        print self.name

#实例化对象
EchoVariable = ClassVariable()

#实例属性
print EchoVariable.name
print EchoVariable.age
#实例方法
EchoVariable.PRINTNAME()
