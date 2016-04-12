#!/usr/bin/env python
#coding:utf-8
#descripthon: python程序执行python代码，获取状态
__author__ = 'luodi'


import os

pipe = os.popen('python test01.py') #默认为'r' 对stdout进行读操作

pipe.read()

print(pipe.close()) #
