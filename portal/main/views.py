#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

from flask import render_template, redirect, url_for, abort, flash, request

from . import main

from portal.api_1_0.users import Users
from portal.api_1_0.stats import Stat
import simplejson


# @main.route('/user/<username>')
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     page = request.args.get('page', 1, type=int)
#     pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
#         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#         error_out=False)
#     posts = pagination.items
#     return render_template('user.html', user=user, posts=posts,
#                            pagination=pagination)


@main.route('/', methods=['GET'])
def index():
    user = Users.get()
    #page = request.args.get('page', 1, type=int)
    return render_template('main.html')

@main.route('/main', methods=['GET'])
def front():
    accumulate_user = Stat.current("accumulate_user")
    return render_template('main.html', accumulate_user=accumulate_user )


@main.route('/users', methods=['GET'])
def users():
    users = Users.get()["results"]
    #page = request.args.get('page', 1, type=int)
    return render_template('user.html', users=simplejson.dumps(users), posts=10, pagination=10)
