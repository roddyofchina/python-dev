#!/usr/bin/env python
#coding:utf8

__author__ = 'LUODI'


class FirstFather(object):

    def BODY(self):
        print "身体强壮"
    

class SecondFather(object):

    def CHARACTER(self):
        print "性格倔强"


class Son(FirstFather,SecondFather):

    def __init__(self,NAME):
        self.name = NAME

son1=Son('小明')
son1.BODY()
son1.CHARACTER()
