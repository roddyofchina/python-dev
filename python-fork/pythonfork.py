#!/usr/bin/env python

__author__ = 'Luodi'

import os

def child():
    print("hello from child", os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print("hello from parent",os.getpid(),newpid)

        if raw_input() == 'q':
            break
        else:
            continue
parent()
