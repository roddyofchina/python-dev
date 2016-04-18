#!/usr/bin/env python
#coding:utf8

__author__ = 'Luodi'

import os,sys

def dirscan(dir_name_path):
    for file in os.listdir(dir_name_path):
        path = os.path.join(dir_name_path,file)
        if not os.path.isdir(path):
            print(path)
        else:
            dirscan(path)

if __name__ == '__main__':
    dirscan(sys.argv[1])

