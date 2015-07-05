#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

from portal.app import create_app

def main():
    app = create_app()

    app.run(host='127.0.0.1', port=9088)


if __name__ == '__main__':
    main()