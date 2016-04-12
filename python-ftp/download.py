#!/usr/bin/env python
#coding:utf-8
#author:luodi date:2014/11/17
#descrption:this module is get files from remote ftp server
#version:v1.0

import sys,os,ftplib
from ftplib import FTP
import argparse


ftp=FTP()
#Define Ftp server infomations to connect
ftp.connect('x.x.x.x','21')
ftp.login('username','passwd')

def Input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pull", help="从FTP下载文件")
    parser.add_argument("--push", help="上传文件到FTP指定目录")
    parser.add_argument("--remotepath", help="指定FTP目录")
    args = parser.parse_args()
    return args

def pusll_file(sourcefile,remotepath):
    try:
        bufsize = 1024
        fp = open(sourcefile,'rb')
        remotepath=os.path.join(remotepath,os.path.basename(sourcefile))
        roback=ftp.storbinary('STOR '+ remotepath ,fp,bufsize)
        if 'complete' in roback: print "\033[32m上传成功!!\033[0m"
        ftp.set_debuglevel(0)
        fp.close()
    except IOError,e:
        print e
    except ftplib.error_perm:
        print "\033[31mError:目录不存在\033[0m"

def download_files(filename):
    try:
        Localpath = '/data/upload/' + filename
        Getlist=ftp.nlst('/update/*')

        filepaths=[]
        for dirs in Getlist:
            filelist=ftp.nlst(dirs)
            for files in filelist:
                filepaths.append(files) 
        for lines in filepaths:
            if filename in lines:
                Getfilepath=lines
                break
            else:
                Getfilepath=0

        if Getfilepath == 0 : 
            print "ERROR:文件不存在!!!!"
            sys.exit(1)

        dirname=os.path.dirname(Getfilepath)
        ftp.cwd(dirname)
        ftp.size(filename) 
              
        #If localdir does not exist,make it
        if not os.path.isdir(os.path.dirname(Localpath)):
            os.mkdir(os.path.dirname(Localpath))
        ftp.retrbinary('RETR %s' % os.path.basename(filename),open(Localpath,'wb').write)
        ftp.quit()
        return "0",Localpath
    except ftplib.error_perm,e:
        print e
        print "\033[31mFile does not exist!!\033[0m"
        return "1",Localpath
        sys.exit(1)



if __name__ == '__main__':
    Getinput=Input_args()
    if Getinput.pull:
        code,Localpath = download_files(Getinput.pull)
        if code == "0":
            print "\033[32mDownload file is successful!! Filename is:\033[0m" + Localpath
    if Getinput.push and Getinput.remotepath:
         pusll_file(Getinput.push,Getinput.remotepath)
