#coding:utf8

"""
Created on 2015-07-06

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)