#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""
from flask import jsonify


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response