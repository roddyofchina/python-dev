#!/usr/bin/env python

__author__ = 'Luodi'

import sys

def openfile(filename):
    with open(filename) as file:
       files=file.readlines()
       for line in files: print line.strip('\n')


if __name__ == '__main__':
    openfile(sys.argv[1])
