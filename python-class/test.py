#!/usr/bin/env python


class Echo:
    def getname(self):
        print self.name

    def setname(self,name):
        self.name = name



a=Echo()

a.setname("luodi")
a.getname()



