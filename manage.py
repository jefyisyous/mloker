#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

from app.app import configure_app

def main():
    app = configure_app()

    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()