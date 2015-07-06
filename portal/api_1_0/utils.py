#coding:utf8

"""
Created on 2015-07-06

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""
import json

class Base(object):
    def __init__(self):
        pass

    def kv(self, params):
        for k, v in params.iteritems():
            if isinstance(v, dict):
                params[k] = json.dumps(v)
        return params