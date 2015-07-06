#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

import leancloud
import simplejson
import time

class Users(object):

    @classmethod
    def get(cls):
        res = leancloud.client.get('/users', params={})
        return simplejson.loads(res.content)