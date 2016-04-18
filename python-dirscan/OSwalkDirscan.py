#!/usr/bin/env python
#coding:utf8

__author__ = 'Luodi'

import os,sys

def dirscan(dir_name_path):
    dirfiles=[]
    for (dirname,Subdirectory,filename) in os.walk(dir_name_path):
        for fname in filename:
            path = os.path.join(dirname,fname)
            dirfiles.append(path)
    return dirfiles


if __name__ == '__main__':
    filepath=dirscan(sys.argv[1])
    print filepath

