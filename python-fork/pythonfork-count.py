#!/usr/bin/env python

__author__ = 'Luodi'

import os,time

def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(),i))
    

for i in range(5):
    pid = os.fork()
    print pid
    if pid != 0 :
        print('Process %d spawned' %pid)

    else:
        counter(5)
        os._exit(0)


print('Main process exiting.')
