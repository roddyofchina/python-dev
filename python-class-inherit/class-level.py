#!/usr/bin/env python
#coding:utf8

__author__ = 'LUODI'

class CLASSA(object):
    def RUN(self):
        print "CLASSA,RUN"

class CLASSB(CLASSA):
    def ECHO(self):
        print "CLASSB,ECHO"

class CLASSC(CLASSA):
    def ECHO(self):
        print "CLASSC,ECHO"
    def RUN(self):
        print "CLASSC,RUN"

class CLASSD(CLASSB,CLASSC):
    def ECHO(self):
        print "CLASSD,ECHO"

a=CLASSD()
a.ECHO()
a.RUN()
print CLASSD.__mro__
