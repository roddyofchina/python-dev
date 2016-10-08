#!/usr/bin/env python
#coding:utf8


class FATHER(object):
    def __init__(self):
        self.father = 'father'
        self.job = 'IT'


class SON(FATHER):
    def __init__(self):
        self.sonname = 'luodi'
        self.age=25
        super(SON,self).__init__()
        
    def into(self):
        print self.job,self.age,self.sonname

S1=SON()
S1.into()
