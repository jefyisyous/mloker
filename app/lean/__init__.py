#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""
import leancloud
from config import Config

class LeanInit(object):
    leancloud.init(app_id=Config.LEAN_APP_ID,
                   app_key=Config.LEAN_APP_KEY,
                   master_key=Config.LEAN_MASTER_KEY)
