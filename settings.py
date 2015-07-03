#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

import os


PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

# 是否开启调试模式
DEBUG = True

# leancloud appkey
APP_ID = 'mqoay5ghtispkaxpeo4eety4t07pmn3kpahecoa7frg981v6'

APP_KEY = '7iei7k6mg98ssp69056u35bbevpxzgplt0iyifsrpbrtj5xo'

MASTER_KEY = 'j8qpixm9lyhhvuzlc2zyihs9ba17fkhdre3bvi7z6apfjo67'

# 静态目录路径
STATIC_FOLDER = os.path.join(PROJECT_PATH, 'static')

# sqlalchemy数据库配置
#SQLALCHEMY_CONFIG = "mysql+mysqldb://duckheader:duckheader@127.0.0.1:3306/duckheader?charset=utf8"