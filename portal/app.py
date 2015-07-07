#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

import json
import datetime
from flask import Flask
import leancloud
from db.database import init_db
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__, static_folder='static', template_folder='templates')


def create_app():
    app.config.from_pyfile('../settings.py')

    app.static_folder = app.config.get('STATIC_FOLDER')

    app.config.update({'SITE_TIME': datetime.datetime.utcnow()})

    configure_jinja(app)

    configure_leancloud(app)

    register_routes(app)

    init_db()

    return app

def configure_jinja(app):

    def jinja_convert_filter(value, dct):
        if value in dct:
            return dct[value]
        return value

    env = app.jinja_env
    env.filters['convert'] = jinja_convert_filter

def register_routes(app):
    import main
    app.register_blueprint(main.main, url_prefix='')
    return app

def configure_leancloud(app):

    app_id = app.config.get('APP_ID')
    app_key = app.config.get('APP_KEY')
    master_key = app.config.get('MASTER_KEY')
    leancloud.init(app_id, app_key=app_key, master_key=master_key)