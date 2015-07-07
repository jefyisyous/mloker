#coding:utf8

"""
Created on 2015-07-07

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

from . import redisClient
from portal.api_1_0.stats import Stat

class PrepareStat(redisClient):

    METRICS = "accumulate_user, new_user, active_user, session, " \
              "new_user_hour, active_user_hour, session_hour, wau, " \
              "mau, push_session, push_direct, active_user_locations, " \
              "new_user_locations, device_os, device_model"

    def set_metrics(self):
        res = Stat.current(self.METRICS)
        self._setall(params=res)

    def _setall(self, params):
        for param in params:
            self._inter(param)

    def _inter(self, param):
        key1 = None
        key2 = None
        value = None

        for k, v in param.iteritems():
            if k == 'metrics':
                key1 = v
            elif k == 'data':
                for k1, v2 in v.iteritems():
                    key2 = k1
                    value = v2
        key = key1 + '#' + key2
        self.set(key, value)
