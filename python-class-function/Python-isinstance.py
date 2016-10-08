#!/usr/bin/env python
#coding:utf8

__author__ = 'LUODI'

class A(object):
    def ANAME(self):
        print "sdsdd"

class B(A):
    def CC(self):
        pass
class C(object):
    def ss(self):
        pass
a=C()
b=A()
print isinstance(a,A)
print isinstance(b,A)
print isinstance(b,B)
