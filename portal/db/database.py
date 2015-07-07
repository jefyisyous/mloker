#coding:utf8

"""
Created on 2015-07-06

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:////file/mloker.db', convert_unicode=True)

metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
def init_db():
    metadata.create_all(bind=engine)