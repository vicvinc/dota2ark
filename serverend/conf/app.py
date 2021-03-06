#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-08-11 17:44:47
# @Last Modified by:   Administrator
# @Last Modified time: 2015-08-12 10:12:12
import os

from handler import home
from tornado.web import StaticFileHandler

dirname = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(dirname, os.pardir))

pub = os.path.join(root, 'pub')
view = os.path.join(root, 'view')

test_path = os.path.abspath(os.path.join(dirname, os.pardir))

appConf = {
	'port': '9541',
	# 'pub': { 'path': pub },
	# 'view':  { 'path': view },
	# 'test_path': { 'path': test_path },#for test
}
setting = {
	'autoreload': True,
	'debug': True,
	'xsrf_cookies': True,
	'static_hash_cache': False,
	'cookie_secret': 'cookie_secret_code',
	'autoescape': None,
}
dbConf = {
	'host': 'localhost',
	'port': '3306',
	'dbname': 'master',
	'user': 'apache',
	'pwd': 'blue1991',
}
routes = [
	(r'/', home.HomeHandler),
	# static handler
	(r'/(favicon\.ico)', StaticFileHandler, { 'path': pub }),
	(r'/pub/(.*)', StaticFileHandler, { 'path': pub }),
]
