# -*- coding:utf-8 -*-
import redis

r=redis.Redis(host="127.0.0.1",port=6379,db=0)

def sent(key,value):
    if key==None or value==None:
        return None�
    elif r.set(key,value):
        return 1
    else: 
        return 0
    
def printValue(key):
    if key:
        value=r.get(key)
        if value:
            return value
    else:
        return None

if __name__=='__main__':
    while 1:
        print '**********************'
        print '1.SET key'
        print '2.GET key'
        print '0.Other key to Quit'
        print '**********************'
        choose=int(input('Please input your choose:'))
        if choose == 1:
            print '**********SET*********'
            key=raw_input("Please input the key:")
            value=raw_input("Please input the value:")
            sent(key,value)
            print '**********************'
        elif choose == 2:
            print '**********GET*********'
            key=raw_input('Please input the key:')
            print printValue(key)
            print '**********************'
        else:
            exit()
