#!/usr/bin/env python
#coding:utf8
__author__ = 'LUODI'


class DRIVE(object):
    #前进方法
    def GOING(self):
        print self.cartype,"正在前进,请保持车速!!"
    
    #倒车方法
    def ASTERN(self):
        print self.cartype,"正在倒车,请注意!!"

    #转弯方法
    def TURN(self):
        print self.cartype,"车辆正在转弯!!"

    #爬坡方法
    def CLIMBING(self):
        print self.cartype,"车辆爬坡!!"

class CAR(DRIVE):
    
    def __init__(self,cartype):
        self.cartype = cartype


bmw = CAR('宝马')
bmw.GOING()

bus = CAR('大巴车')
bus.ASTERN()

fire = CAR('消防车')
fire.TURN()

print CAR.__bases__
print bmw.__class__
    

