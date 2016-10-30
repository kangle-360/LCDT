# -*- coding:utf-8 -*-
import redis


r=redis.Redis ( host = "127.0.0.1" , port = 6379 , db = 0 )


def setValueInRedis ( key , value ) :
    if key == None or value == None :
        return None
    elif r.set ( key,value ) :
        return 1
    else : 
        return 0

    
def getValueInRedis ( key ) :
    if key :
        value = r.get ( key )
        if value :
            return value
    return None
