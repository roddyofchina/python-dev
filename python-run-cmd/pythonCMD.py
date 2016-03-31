#!/usr/bin/env python
#coding:utf-8
__author__="luodi"

import sys,os
import subprocess


def RunCommand(Cmdname):
    GetCmdResult=subprocess.Popen(Cmdname,stdout=subprocess.PIPE,shell=True)

    print """\033[32m###########Command Output###############\033[0m"""

    ShowResult=GetCmdResult.communicate()[0].splitlines()
    for lines in ShowResult: print lines


if __name__ == '__main__':
    try:
        Cmd=sys.argv[1]
        RunCommand(Cmd)
    except IndexError,e:
        print "输入错误:",e



