#coding:utf8

"""
Created on 2015-07-02

@author: junfu
@description:
         
Copyright (c) 2014 infohold inc. All rights reserved.
"""

from flask import render_template, redirect, url_for, abort, flash, request

from . import main

from app.lean.sdk import Users


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
    return render_template('index.html')

@main.route('/users', methods=['GET'])
def users():
    user = Users.get()
    #page = request.args.get('page', 1, type=int)
    return render_template('user.html', user=user)
