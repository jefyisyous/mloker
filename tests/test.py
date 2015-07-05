#coding:utf8

"""
Created on 2015-07-04

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""
from portal.api_1_0.users import Users
from portal.app import configure_leancloud
import simplejson
import leancloud


#
# if __name__ == '__main__':
#     leancloud.init('mqoay5ghtispkaxpeo4eety4t07pmn3kpahecoa7frg981v6',
#                    app_key='7iei7k6mg98ssp69056u35bbevpxzgplt0iyifsrpbrtj5xo',
#                    master_key='j8qpixm9lyhhvuzlc2zyihs9ba17fkhdre3bvi7z6apfjo67')
#     user = Users.get()
#     print type(user)
#     print user
#     print user.get("results")
#     print simplejson.dumps(user.get("results"))

