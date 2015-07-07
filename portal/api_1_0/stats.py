#coding:utf8

"""
Created on 2015-07-06

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""
import time, leancloud, simplejson


class Stat(object):

    TODAY = time.strftime("%Y%m%d")

    @classmethod
    def current(cls, metrics):
        res = cls._statistics(cls.TODAY, cls.TODAY, metrics)
        # dct = dict()
        # if res.get("metrics") == metrics:
        #     dct = res.get("data")
        #
        # return dct.get(time.strftime("%Y-%m-%d"))
        return res

    def get(self):
        pass

    @classmethod
    def _statistics(cls, start, end, metrics):
        res = leancloud.client.get('/stats/appmetrics',
                                   params={"start": start,
                                           "end": end,
                                           "metrics": metrics,
                                           "X-AVOSCloud-Application-Id:": "mqoay5ghtispkaxpeo4eety4t07pmn3kpahecoa7frg981v6"}
                                   )
        return simplejson.loads(res.content)