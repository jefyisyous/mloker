#coding:utf8

"""
Created on 2015-07-07

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""
import redis


class redisDb(object):

    __pool = None

    __conn_args = {
        'host': 'localhost',
        'port': 6379,
        'timeout': 10,
        'max_connections': 50,
    }

    def exists(self, name):
        pass

    def get(self, name):
        pass

    def set(self, name, value, expire_time=None):
        pass

    def delete(self, name):
        pass


class redisClient(redisDb):

    def __init__(self):

        self.redis_cli = redis.Redis(connection_pool=self.get_pool())

    def exists(self, name):
        return self.redis_cli.exists(name)

    def get(self, name):
        redis_type = self.redis_cli.type(name)
        if redis_type == 'none':
            return None
        elif redis_type == 'hash':
            return self.redis_cli.hgetall(name)
        else:
            return self.redis_cli.get(name)

    def set(self, name, value, expire_time=None):
        pipe = self.redis_cli.pipeline()
        if isinstance(value, dict):
            pipe.hmset(name, value)
        else:
            pipe.set(name, str(value))
        if expire_time is not None:
            pipe.expire(name, expire_time)
        pipe.execute()

    def delete(self, name):
        self.redis_cli.delete(name)

    @classmethod
    def set_conn_config(cls, conn_dict):
        for k in cls.__conn_args:
            if conn_dict.has_key(k):
                cls.__conn_args[k] = conn_dict[k]

    @classmethod
    def get_pool(cls):
        if cls.__pool is None:
            cls.__pool = redis.BlockingConnectionPool(**cls.__conn_args)
        return cls.__pool