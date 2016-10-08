#!/usr/bin/env python
#coding:utf8

__author__ = 'LUODI'


class INIT(object):
    def __init__(self):
        self.initname = 'roddypy.com'
        self.city = 'CD'
    def __str__(self):
        return "this is a test str!!!"
    def __repr__(self):
        return "%s" %self.initname
vs=INIT()
print vs
print repr(vs)
