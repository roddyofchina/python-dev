#!/usr/bin/env python
#coding:utf8
__author__ = "LUODI"

from rediscluster import StrictRedisCluster
import sys,json


'''连接redis集群节点'''
def RedisCluster():
    Redis_nodes = [ {'host': '192.168.2.76', 'port': 6380},
                {'host': '192.168.2.76', 'port': 6381},
                {'host': '192.168.2.76', 'port': 6382},
                {'host': '192.168.2.105', 'port': 7380},
                {'host': '192.168.2.105', 'port': 7381},
                {'host': '192.168.2.105', 'port': 7382},
              ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=Redis_nodes)
    except Exception,e:
        print "Connect Redis node error:",e
        sys.exit(1)
    GetKeylist = ['wechat_statistics_click_' + str(i) for i in range(1,8)]    
    return (redisconn,GetKeylist)

def StrToJson(strdata):
    JsonData=json.loads(strdata)
    return JsonData["activityLumpMap"]["100"]

if __name__ == '__main__':
    conn,Keylist = RedisCluster()
    for i in Keylist:
        if conn.get(i):
            data=conn.get(i)
            countdata = StrToJson(data)
            print countdata
        else:
            print "\033[31m获取%s失败!!\033[0m" %i

